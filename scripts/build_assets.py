#!/usr/bin/env python3
"""Draw the README graphics as SVG: logo, chat demo and persona gallery.

The gallery reads personas/index.json, so run build_personas_index.py
first. Light and dark versions are written for the README's <picture> tags.
"""

import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', Helvetica, Arial, sans-serif"

COLORS = {"Red": "#E5484D", "Yellow": "#F5B700", "Green": "#30A46C", "Blue": "#0090FF"}
THEMES = {
    "light": {"bg": "#FFFFFF", "card": "#F6F8FA", "border": "#D0D7DE", "text": "#1F2328", "muted": "#59636E",
              "me": "#0090FF", "me_text": "#FFFFFF"},
    "dark": {"bg": "#0D1117", "card": "#161B22", "border": "#30363D", "text": "#E6EDF3", "muted": "#9198A1",
             "me": "#1F6FEB", "me_text": "#FFFFFF"},
}


def svg(width: int, height: int, body: list[str], bg: str | None = None) -> str:
    rect = [f'<rect width="{width}" height="{height}" rx="20" fill="{bg}"/>'] if bg else []
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'font-family="{FONT}">',
        *rect,
        *body,
        "</svg>",
        "",
    ])


def logo() -> str:
    """Four colour quadrants arranged as a speech bubble."""
    s, g, o = 92, 10, 14  # tile size, gap, outer margin
    tiles = [("Red", 0, 0), ("Yellow", 1, 0), ("Blue", 0, 1), ("Green", 1, 1)]
    body = [
        f'<rect x="{o + c * (s + g)}" y="{o + r * (s + g)}" width="{s}" height="{s}" rx="24" fill="{COLORS[k]}"/>'
        for k, c, r in tiles
    ]
    tail_y = o + 2 * s + g
    body.append(f'<path d="M{o + 18} {tail_y - 30} L{o + 6} {tail_y + 26} L{o + 58} {tail_y - 8} Z" '
                f'fill="{COLORS["Blue"]}"/>')
    size = 2 * o + 2 * s + g
    return svg(size, size + 28, body)


def gallery(personas: list[dict], theme: dict) -> str:
    cols, w, h, gap, pad = 4, 214, 104, 16, 24
    rows = (len(personas) + cols - 1) // cols
    width, height = pad * 2 + cols * w + (cols - 1) * gap, pad * 2 + rows * h + (rows - 1) * gap
    body = []
    for i, p in enumerate(personas):
        x, y = pad + (i % cols) * (w + gap), pad + (i // cols) * (h + gap)
        colour = COLORS[p["color"]]
        body += [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{theme["card"]}" stroke="{theme["border"]}"/>',
            f'<rect x="{x}" y="{y + 14}" width="5" height="{h - 28}" rx="2.5" fill="{colour}"/>',
            f'<text x="{x + 20}" y="{y + 50}" font-size="30">{escape(p["emoji"])}</text>',
            f'<text x="{x + 64}" y="{y + 38}" font-size="16" font-weight="600" fill="{theme["text"]}">'
            f'{escape(p["name"])}</text>',
            f'<text x="{x + 64}" y="{y + 61}" font-size="13" fill="{theme["muted"]}">'
            f'{p["code"]} · {escape(p["hangul"])}</text>',
            f'<circle cx="{x + 69}" cy="{y + 79}" r="4.5" fill="{colour}"/>',
            f'<text x="{x + 80}" y="{y + 84}" font-size="12.5" fill="{theme["muted"]}">{p["color"]}</text>',
        ]
    return svg(width, height, body, theme["bg"])


# The demo conversation: (speaker, lines). "agent" bubbles sit left, "me" right, "note" is centred.
DEMO = [
    ("agent", ["Quick one. A friend texts you:", "“I was sad, so I bought bread.”",
               "A) “What kind of bread?”   B) “Why were you sad?”"]),
    ("me", ["B, obviously. Who cares about the bread 😅"]),
    ("agent", ["Classic F 🫶 In Korea, that's the famous T/F test.", "Next: “I crashed my car.” Your first question?"]),
    ("me", ["Are you okay?!"]),
    ("note", ["… ten questions and a taste test later …"]),
    ("agent", ["You're an ENFP (엔프피) · Yellow 🟡", "You picked the reply from 🧭 The Compass (INFJ):",
               "your perfect pair. Switching now. Ready?"]),
]


def demo(theme: dict) -> str:
    width, pad, line_h, char_w = 760, 28, 23, 8.1
    body = [
        f'<circle cx="{pad + 4}" cy="26" r="6" fill="{COLORS["Red"]}"/>',
        f'<circle cx="{pad + 24}" cy="26" r="6" fill="{COLORS["Yellow"]}"/>',
        f'<circle cx="{pad + 44}" cy="26" r="6" fill="{COLORS["Green"]}"/>',
        f'<text x="{width / 2}" y="31" font-size="13" text-anchor="middle" fill="{theme["muted"]}">'
        "your agent · persona onboarding</text>",
    ]
    y = 58
    for who, lines in DEMO:
        if who == "note":
            body.append(f'<text x="{width / 2}" y="{y + 16}" font-size="13" font-style="italic" text-anchor="middle" '
                        f'fill="{theme["muted"]}">{escape(lines[0])}</text>')
            y += 38
            continue
        bw = min(width - 2 * pad - 80, int(max(len(t) for t in lines) * char_w) + 36)
        bh = 22 + line_h * len(lines)
        bx = pad if who == "agent" else width - pad - bw
        fill = theme["card"] if who == "agent" else theme["me"]
        text_fill = theme["text"] if who == "agent" else theme["me_text"]
        stroke = f' stroke="{theme["border"]}"' if who == "agent" else ""
        body.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="16" fill="{fill}"{stroke}/>')
        for j, t in enumerate(lines):
            body.append(f'<text x="{bx + 18}" y="{y + 28 + j * line_h}" font-size="15" fill="{text_fill}">'
                        f'{escape(t)}</text>')
        y += bh + 14
    return svg(width, y + 14, body, theme["bg"])


def main() -> int:
    index = ROOT / "personas" / "index.json"
    if not index.exists():
        print("personas/index.json missing: run scripts/build_personas_index.py first", file=sys.stderr)
        return 1
    personas = json.loads(index.read_text(encoding="utf-8"))["personas"]
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "logo.svg").write_text(logo(), encoding="utf-8")
    for name, theme in THEMES.items():
        (ASSETS / f"personas-{name}.svg").write_text(gallery(personas, theme), encoding="utf-8")
        (ASSETS / f"demo-{name}.svg").write_text(demo(theme), encoding="utf-8")
    print(f"wrote 5 SVGs to assets/ ({len(personas)} personas in the gallery)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
