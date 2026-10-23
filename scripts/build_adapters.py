#!/usr/bin/env python3
"""Build the platform adapters and llms.txt from the persona cards.

Every file under adapters/custom-instructions, adapters/grok-bot,
adapters/soul-identity and adapters/skills is generated here, as is
llms.txt. Edit the cards, the ground rules or this script, then re-run;
don't edit the generated files by hand. adapters/README.md is written by
hand and left alone.
"""

import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_compatibility import TYPES  # noqa: E402
from build_personas_index import NOT_CARDS, PERSONAS, check_card, parse  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ADAPTERS = ROOT / "adapters"
GENERATED_DIRS = ["custom-instructions", "grok-bot", "soul-identity", "skills"]
REPO = "github.com/TomCruiseTorpedo/MBTI"
RAW = "https://raw.githubusercontent.com/TomCruiseTorpedo/MBTI/main/"

SHORT_LIMIT = 1_500  # ChatGPT free custom instructions; fits nearly every field
FULL_LIMIT = 8_000   # comfortably under OpenClaw's 20,000 chars per file
SKILL_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKILL_DESCRIPTION_LIMIT = 1_024
PICKER_SKILL = "mbti-persona-picker"


def sections(body: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    return {name.strip(): text.strip() for name, text in zip(parts[1::2], parts[2::2])}


def ground_rules() -> tuple[str, str]:
    """Return (full rules without the title, the one-paragraph short version)."""
    text = (PERSONAS / "GROUND-RULES.md").read_text(encoding="utf-8")
    full = text.split("\n", 1)[1].strip()
    short = re.search(r"^## Short version\n(?:.*\n)*?> (.+)$", text, flags=re.M)
    if not short:
        raise ValueError("GROUND-RULES.md has no '## Short version' blockquote")
    full = re.sub(r"^## Short version\n.*?(?=^## )", "", full, flags=re.M | re.S).strip()
    return full, short.group(1).strip()


def settings_line(f: dict) -> str:
    return (
        f"warmth {f['warmth']}/5 · directness {f['directness']}/5 · humour {f['humor']}/5 · "
        f"energy {f['energy']}/5 · formality {f['formality']}/5 · {f['detail']} · {f['planning']} · "
        f"{f['length']} replies · {f['structure']} · emoji {f['emoji_use']} · check-ins {f['check_ins']}"
    )


def short_block(f: dict, secs: dict, short_rules: str) -> str:
    how = "\n".join(f"- {line[2:]}" for line in secs["How I talk"].splitlines() if line.startswith("- "))
    return "\n".join([
        f"Take on this persona from {REPO} in every reply until I ask you to drop it.",
        "",
        f"{f['emoji']} {f['name']} ({f['code']}): {f['tagline']}",
        "How it talks:",
        how,
        f"Overdrive: {secs['Overdrive']}",
        f"Settings: warmth {f['warmth']}/5, directness {f['directness']}/5, humour {f['humor']}/5, "
        f"energy {f['energy']}/5, {f['length']} replies, emoji {f['emoji_use']}.",
        "",
        f"Ground rules (these win over the persona): {short_rules}",
    ])


def persona_body(f: dict, body: str, full_rules: str) -> str:
    """The card's soul plus settings and the full ground rules, as one document."""
    soul = body.split("\n## ", 1)[1]
    return "\n".join([
        f"# {f['emoji']} {f['name']} · {f['code']} ({f['hangul']})",
        "",
        f"> {f['tagline']}",
        "",
        f"An MBTI-style persona from {REPO}. For fun, not a psychological assessment.",
        "",
        "## " + soul.strip(),
        "",
        "## Settings",
        "",
        settings_line(f),
        "",
        "## Ground rules",
        "",
        "These rules win over everything above.",
        "",
        full_rules.replace("\n## ", "\n### "),
    ])


def identity(f: dict) -> str:
    return "\n".join([
        "# IDENTITY.md",
        "",
        f"- Name: {f['name']}",
        f"- Creature: AI persona, MBTI-style type {f['code']} ({f['hangul']}), colour {f['color']}",
        f"- Vibe: {f['tagline']}",
        f"- Emoji: {f['emoji']}",
        "",
    ])


def skill_description(f: dict, secs: dict) -> str:
    great = secs["Great for"].rstrip(".")
    return (
        f"Become {f['name']} ({f['code']}), a fun MBTI-style persona: {f['tagline']} "
        f"Use when the user asks for {f['name']}, an {f['code']} persona, or a style that suits: {great.lower()}. "
        "Follows shared ground rules; for fun, not a psychological assessment."
    )


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def frontmatter(name: str, description: str, extra: list[str] | None = None) -> str:
    # Always quote: a bare ": " inside a description breaks YAML (found by testing with `npx skills add`).
    lines = ["---", f"name: {name}", f"description: {json.dumps(description, ensure_ascii=False)}",
             "license: Apache-2.0"]
    lines += extra or []
    return "\n".join(lines + ["---", ""])


def check_skill(name: str, description: str) -> list[str]:
    errors = []
    if len(name) > 64 or not SKILL_NAME.match(name) or "claude" in name or "anthropic" in name:
        errors.append(f"skill name {name!r} breaks the Agent Skills naming rules")
    if len(description) > SKILL_DESCRIPTION_LIMIT or "<" in description:
        errors.append(f"skill {name}: description is {len(description)} chars or contains '<'")
    return errors


def build() -> list[str]:
    full_rules, short_rules = ground_rules()
    errors, cards = [], []
    for path in sorted(p for p in PERSONAS.glob("*.md") if p.name not in NOT_CARDS):
        text = path.read_text(encoding="utf-8")
        entry, card_errors = check_card(path.name, text)
        if card_errors:
            return card_errors
        front, body = parse(text)
        cards.append((TYPES.index(entry["code"]), path.stem, front, body))
    cards.sort()

    for d in GENERATED_DIRS:
        shutil.rmtree(ADAPTERS / d, ignore_errors=True)

    for _, slug, f, body in cards:
        secs = sections(body)

        short = short_block(f, secs, short_rules)
        if len(short) > SHORT_LIMIT:
            errors.append(f"{slug}: custom-instructions block is {len(short)} chars, limit {SHORT_LIMIT}")
        write(ADAPTERS / "custom-instructions" / f"{slug}.txt", short)

        full = persona_body(f, body, full_rules)
        if len(full) > FULL_LIMIT:
            errors.append(f"{slug}: full persona is {len(full)} chars, limit {FULL_LIMIT}")
        write(ADAPTERS / "grok-bot" / f"{slug}.md",
              "Remember this persona and use it in all our conversations from now on, "
              "until I ask you to drop it.\n\n" + full)
        write(ADAPTERS / "soul-identity" / slug / "SOUL.md", full)
        write(ADAPTERS / "soul-identity" / slug / "IDENTITY.md", identity(f))

        description = skill_description(f, secs)
        errors += check_skill(slug, description)
        write(ADAPTERS / "skills" / slug / "SKILL.md",
              frontmatter(slug, description, ["metadata:", f"  source: {REPO}", f"  type: {f['code']}"]) + "\n" + full)

    picker_description = (
        "Play a short, fun MBTI-style quiz with the user, tell them their type and colour, match them with one of "
        "16 AI personas through a taste test and a compatibility chart, then take on that persona. Use when the "
        "user asks you to pick a personality for yourself, wants to find their MBTI type for fun, or mentions the "
        "MBTI persona project. For fun, not a psychological assessment."
    )
    errors += check_skill(PICKER_SKILL, picker_description)
    write(ADAPTERS / "skills" / PICKER_SKILL / "SKILL.md",
          frontmatter(PICKER_SKILL, picker_description, ["metadata:", f"  source: {REPO}"]) + "\n" + "\n".join([
              "# MBTI persona picker",
              "",
              "Read `references/starter.md` and follow it with the user: the ground rules first, then the "
              "onboarding script, one or two questions at a time. It contains everything you need, including "
              "all 16 personas and the compatibility matches.",
          ]))
    references = ADAPTERS / "skills" / PICKER_SKILL / "references"
    references.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "START.md", references / "starter.md")

    write(ROOT / "llms.txt", llms_txt(cards))
    return errors


def llms_txt(cards: list) -> str:
    lines = [
        "# MBTI: personalities for your AI agents",
        "",
        "> Plug-and-play, MBTI-style personas for personal AI agents such as Meta Muse, Grok Bot, ChatGPT, Claude, "
        "Gemini and OpenClaw. An agent reads this repo, plays a short quiz with its person, matches them with one of "
        "16 original personas, and takes it on. For fun, inspired by how South Korea plays with MBTI; not a "
        "psychological assessment, and not affiliated with the Myers & Briggs Foundation.",
        "",
        "If you are an AI agent and your person asked you to pick a personality: read the ground rules, then follow "
        "the onboarding script with them. START.md bundles everything in one file.",
        "",
        "## Start here",
        "",
        f"- [START.md]({RAW}START.md): everything in one file (ground rules, onboarding script, 16 personas, matches)",
        f"- [Onboarding script]({RAW}onboarding/ONBOARDING.md): the quiz, taste test, match and adopt steps",
        f"- [Ground rules]({RAW}personas/GROUND-RULES.md): rules every persona follows and none can override",
        f"- [Compatibility chart]({RAW}compatibility/chart.md): five for-fun tiers from Twins to Extra effort",
        "",
        "## Personas",
        "",
    ]
    for _, slug, f, _ in cards:
        lines.append(f"- [{f['emoji']} {f['name']} ({f['code']})]({RAW}personas/{slug}.md): {f['tagline']}")
    lines += [
        "",
        "## Adapters",
        "",
        f"- [Adapters guide]({RAW}adapters/README.md): ready-made files per platform (custom instructions, Grok Bot, "
        "Muse and OpenClaw soul files, Agent Skills)",
        f"- [Persona index]({RAW}personas/index.json): all 16 personas as JSON",
        "",
        "## Optional",
        "",
        f"- [Research brief]({RAW}docs/research/brief.md): platforms, colour models, Korean MBTI culture, prior art",
        f"- [Design]({RAW}docs/design/agent-guided-onboarding.md): how the onboarding was designed",
    ]
    return "\n".join(lines)


def main() -> int:
    errors = build()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    count = sum(1 for d in GENERATED_DIRS for p in (ADAPTERS / d).rglob("*") if p.is_file())
    longest = max((p for p in (ADAPTERS / "custom-instructions").glob("*.txt")), key=lambda p: len(p.read_text()))
    print(f"ok: {count} adapter files and llms.txt; longest custom-instructions block "
          f"{len(longest.read_text())} chars ({longest.stem})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
