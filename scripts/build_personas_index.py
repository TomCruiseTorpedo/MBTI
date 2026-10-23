#!/usr/bin/env python3
"""Check the 16 persona cards and write personas/index.json.

Each card in personas/ has flat `key: value` frontmatter (identity and
style settings) and a markdown body (the soul). This script checks that
every card is complete and agrees with the compatibility rules, the
colour rule and the personas README, then writes one JSON index for
agents that parse rather than read. It exits non-zero on any problem.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_compatibility import TYPES, tier  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PERSONAS = ROOT / "personas"
NOT_CARDS = {"README.md", "GROUND-RULES.md"}

COLORS = {("E", "T"): "Red", ("E", "F"): "Yellow", ("I", "F"): "Green", ("I", "T"): "Blue"}
COLOR_MEANING = {
    "Red": "outgoing, task-focused",
    "Yellow": "outgoing, people-focused",
    "Green": "reserved, people-focused",
    "Blue": "reserved, task-focused",
}
SCALES = ["warmth", "directness", "humor", "energy", "formality"]
CHOICES = {
    "detail": ["big-picture", "balanced", "specifics"],
    "planning": ["plan-first", "flexible", "go-with-the-flow"],
    "length": ["short", "medium", "long"],
    "structure": ["prose", "mixed", "lists"],
    "emoji_use": ["none", "rare", "some", "lots"],
    "check_ins": ["rare", "sometimes", "often"],
}
IDENTITY = ["code", "hangul", "name", "emoji", "color", "tagline", "perfect_pairs"]
SECTIONS = ["Who I am", "How I talk", "Sample replies", "Great for", "Pet peeves", "Overdrive", "Teasing myself"]
SAMPLE_MESSAGES = [
    "I was sad, so I bought bread.",
    "Can you help me plan my week?",
    "I messed up at work today.",
]
SOUL_WORD_LIMIT = 350


def color_for(code: str) -> str:
    return COLORS[(code[0], code[2])]


def hangul_for(code: str) -> str:
    """Spoken Korean shorthand: ISTJ is 잇티제, ENFP is 엔프피, and TP is read 팁."""
    first = {("I", "N"): "인", ("I", "S"): "잇", ("E", "N"): "엔", ("E", "S"): "엣"}[(code[0], code[1])]
    if code[2:] == "TP":
        return first + "팁"
    return first + {"T": "티", "F": "프"}[code[2]] + {"J": "제", "P": "피"}[code[3]]


def perfect_pairs_for(code: str) -> list[str]:
    return [t for t in TYPES if tier(code, t) == "perfect"]


def parse(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise ValueError("no frontmatter")
    front = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        front[key.strip()] = value.strip()
    return front, match.group(2)


def check_card(filename: str, text: str) -> tuple[dict | None, list[str]]:
    errors = []
    try:
        front, body = parse(text)
    except ValueError as e:
        return None, [f"{filename}: {e}"]

    missing = [k for k in IDENTITY + SCALES + list(CHOICES) if not front.get(k)]
    if missing:
        return None, [f"{filename}: missing {', '.join(missing)}"]

    code = front["code"]
    if code not in TYPES:
        return None, [f"{filename}: unknown type {code}"]
    if not filename.startswith(code.lower() + "-"):
        errors.append(f"{filename}: filename should start with {code.lower()}-")

    pairs = [p.strip() for p in front["perfect_pairs"].split(",")]
    if sorted(pairs) != sorted(perfect_pairs_for(code)):
        errors.append(f"{filename}: perfect_pairs {pairs} != chart {perfect_pairs_for(code)}")
    if front["color"] != color_for(code):
        errors.append(f"{filename}: color {front['color']} != {color_for(code)}")
    if front["hangul"] != hangul_for(code):
        errors.append(f"{filename}: hangul {front['hangul']} != {hangul_for(code)}")

    settings = {}
    for key in SCALES:
        value = front[key]
        if not value.isdigit() or not 1 <= int(value) <= 5:
            errors.append(f"{filename}: {key} must be 1~5, got {value}")
        else:
            settings[key] = int(value)
    for key, allowed in CHOICES.items():
        if front[key] not in allowed:
            errors.append(f"{filename}: {key} must be one of {allowed}, got {front[key]}")
        settings[key] = front[key]

    # The body repeats identity for human readers; it must not drift.
    title = f"# {front['emoji']} {front['name']} · {code} ({front['hangul']})"
    expected_lines = [
        title,
        f"> {front['tagline']}",
        f"**Colour:** {front['color']} ({COLOR_MEANING[front['color']]}) · **Perfect pairs:** {', '.join(pairs)}",
    ]
    for line in expected_lines:
        if line not in body.splitlines():
            errors.append(f"{filename}: body is missing the line: {line}")
    for section in SECTIONS:
        if f"\n## {section}\n" not in body:
            errors.append(f"{filename}: missing section '## {section}'")
    for message in SAMPLE_MESSAGES:
        if f'**"{message}"**' not in body:
            errors.append(f"{filename}: missing sample reply to \"{message}\"")

    soul = body.split("\n## ", 1)[1] if "\n## " in body else ""
    words = len(soul.split())
    if words > SOUL_WORD_LIMIT:
        errors.append(f"{filename}: soul is {words} words, limit {SOUL_WORD_LIMIT}")

    entry = {
        "code": code,
        "hangul": front["hangul"],
        "name": front["name"],
        "emoji": front["emoji"],
        "color": front["color"],
        "tagline": front["tagline"],
        "perfect_pairs": pairs,
        "settings": settings,
        "file": f"personas/{filename}",
        "soul_words": words,
    }
    return entry, errors


def check_readme(entries: list[dict], readme: str) -> list[str]:
    errors = []
    for e in entries:
        filename = Path(e["file"]).name
        row = f"| {e['emoji']} | {e['code']} ({e['hangul']}) | [{e['name']}]({filename}) | {e['color']} | {e['tagline']} |"
        if row not in readme.splitlines():
            errors.append(f"personas/README.md: row for {e['code']} is missing or out of date")
    return errors


def main() -> int:
    entries, errors = [], []
    cards = sorted(p for p in PERSONAS.glob("*.md") if p.name not in NOT_CARDS)
    for path in cards:
        entry, card_errors = check_card(path.name, path.read_text(encoding="utf-8"))
        errors += card_errors
        if entry:
            entries.append(entry)

    codes = [e["code"] for e in entries]
    if sorted(codes) != sorted(TYPES):
        errors.append(f"expected one card per type; got {sorted(codes)}")
    errors += check_readme(entries, (PERSONAS / "README.md").read_text(encoding="utf-8"))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    entries.sort(key=lambda e: TYPES.index(e["code"]))
    index = {
        "ground_rules": "personas/GROUND-RULES.md",
        "sample_messages": SAMPLE_MESSAGES,
        "personas": entries,
    }
    (PERSONAS / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    longest = max(entries, key=lambda e: e["soul_words"])
    print(f"ok: {len(entries)} cards; longest soul {longest['soul_words']} words ({longest['code']}); wrote personas/index.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
