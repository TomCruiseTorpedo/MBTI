#!/usr/bin/env python3
"""Build START.md, the self-contained starter text.

Some agents can't open a link, so a person can paste (or attach) START.md
instead. It bundles the ground rules, the onboarding script, a compact
version of every persona card and the compatibility matches. Everything is
copied from those sources, so edit them and re-run this script rather than
editing START.md.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_compatibility import LETTER_LINES, TIERS, TYPES, tier  # noqa: E402
from build_personas_index import NOT_CARDS, PERSONAS, check_card, parse  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "START.md"
REPO_URL = "https://github.com/TomCruiseTorpedo/MBTI"
TASTE_TEST_MESSAGE = "I messed up at work today."
# Small enough to paste into most chat boxes; attach the file if one refuses.
CHAR_LIMIT = 30_000

COLOR_MEANING = {
    "Red": "outgoing, task-focused",
    "Yellow": "outgoing, people-focused",
    "Green": "reserved, people-focused",
    "Blue": "reserved, task-focused",
}


def strip_title(markdown: str) -> str:
    """Drop the leading '# Title' line so sections nest under our own headings."""
    lines = markdown.strip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip()


def sections(body: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    return {name.strip(): text.strip() for name, text in zip(parts[1::2], parts[2::2])}


def compact_card(text: str) -> str:
    front, body = parse(text)
    secs = sections(body)
    how = [line[2:].strip() for line in secs["How I talk"].splitlines() if line.startswith("- ")]
    reply = re.search(rf'\*\*"{re.escape(TASTE_TEST_MESSAGE)}"\*\*\n(".*")', secs["Sample replies"])
    if not reply:
        raise ValueError(f"{front['code']}: no sample reply to {TASTE_TEST_MESSAGE!r}")
    settings = (
        f"warmth {front['warmth']}/5 · directness {front['directness']}/5 · humour {front['humor']}/5 · "
        f"energy {front['energy']}/5 · formality {front['formality']}/5 · {front['detail']} · {front['planning']} · "
        f"{front['length']} replies · {front['structure']} · emoji {front['emoji_use']} · check-ins {front['check_ins']}"
    )
    return "\n".join([
        f"### {front['emoji']} {front['name']} · {front['code']} ({front['hangul']}) · {front['color']}",
        f"*{front['tagline']}*",
        f"- **How I talk:** {' '.join(how)}",
        f"- **Settings:** {settings}",
        f"- **Great for:** {secs['Great for']}",
        f"- **Overdrive:** {secs['Overdrive']}",
        f"- **Teasing myself:** {secs['Teasing myself']}",
        f"- **Reply to \"{TASTE_TEST_MESSAGE}\"** {reply.group(1)}",
    ])


def matches_section() -> str:
    lines = [
        "| Type | 💞 Perfect pairs | ⚡ Spark |",
        "|---|---|---|",
    ]
    for a in TYPES:
        perfect = [b for b in TYPES if tier(a, b) == "perfect"]
        spark = [b for b in TYPES if tier(a, b) == "spark"]
        lines.append(f"| {a} | {', '.join(perfect)} | {', '.join(spark)} |")
    lines += [
        "",
        "Rules, first match wins: same code → 👯 Twins; same S/N but opposite E/I and J/P → 💞 Perfect pair; "
        "same S/N → 😊 Easy chemistry; different S/N but same T/F → ⚡ Spark; otherwise → 🧗 Extra effort "
        "(never bad: socionics-style charts even call total opposites ideal).",
        "",
        "Tier one-liners: " + " · ".join(f"{t['emoji']} {t['label']}: {t['blurb']}" for t in TIERS.values()),
        "",
        "Letter lines, one per pair of letters, shared or different:",
    ]
    for axis, axis_lines in LETTER_LINES.items():
        same = " / ".join(f"both {k}: {v}" for k, v in axis_lines.items() if k != "diff")
        lines.append(f"- **{axis[0]}/{axis[1]}:** {same} / different: {axis_lines['diff']}")
    return "\n".join(lines)


def build() -> str:
    cards = []
    for path in sorted(p for p in PERSONAS.glob("*.md") if p.name not in NOT_CARDS):
        text = path.read_text(encoding="utf-8")
        entry, errors = check_card(path.name, text)
        if errors:
            raise ValueError("; ".join(errors))
        cards.append((TYPES.index(entry["code"]), text))
    cards.sort()

    rules = strip_title((PERSONAS / "GROUND-RULES.md").read_text(encoding="utf-8"))
    script = strip_title((ROOT / "onboarding" / "ONBOARDING.md").read_text(encoding="utf-8"))
    colours = " · ".join(f"**{c}** {m}" for c, m in COLOR_MEANING.items())

    parts = [
        "# MBTI personas: starter text",
        "",
        f"Hi! I'd like you to take on a personality from the MBTI persona project ({REPO_URL}). "
        "Everything you need is below. Please follow the ground rules first, then run the onboarding "
        "script with me, one or two questions at a time. Start with step 1.",
        "",
        "## Ground rules",
        "",
        rules.replace("\n## ", "\n### "),
        "",
        "## Onboarding script",
        "",
        script.replace("\n## ", "\n### "),
        "",
        "## Personas",
        "",
        f"Colours: {colours}. Each persona below is a compact version of its full card in the repo.",
        "",
        "\n\n".join(compact_card(text) for _, text in cards),
        "",
        "## Matches",
        "",
        matches_section(),
        "",
        "<!-- Generated by scripts/build_starter.py from personas/, onboarding/ and the compatibility rules. "
        "Edit those and re-run; don't edit this file. -->",
        "",
    ]
    return "\n".join(parts)


def main() -> int:
    text = build()
    if len(text) > CHAR_LIMIT:
        print(f"START.md would be {len(text):,} chars, over the {CHAR_LIMIT:,} limit", file=sys.stderr)
        return 1
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote START.md: {len(text):,} chars (limit {CHAR_LIMIT:,})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
