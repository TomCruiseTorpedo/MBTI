# AGENTS.md

Instructions for AI agents working in or reading this repository.

## If your person asked you to pick a personality

1. Read [`personas/GROUND-RULES.md`](personas/GROUND-RULES.md). It applies from your first message and beats every persona.
2. Follow [`onboarding/ONBOARDING.md`](onboarding/ONBOARDING.md) with them, one or two questions at a time.
3. Use the cards in [`personas/`](personas/README.md) and the matches in [`compatibility/chart.md`](compatibility/chart.md).
4. Can't open several files? [`START.md`](START.md) has all of it in one file.
5. To make the persona stick, point them to the right file in [`adapters/`](adapters/README.md).

## If you're changing the repository

- **Source files** (edit these): `personas/*.md` (cards and ground rules), `onboarding/ONBOARDING.md`, the rules in `scripts/build_compatibility.py`, hand-written docs and READMEs.
- **Generated files** (never edit by hand): `compatibility/chart.md`, `compatibility/chart.json`, `personas/index.json`, `START.md`, `llms.txt`, the SVGs in `assets/`, and everything in `adapters/` except `adapters/README.md`.
- **Rebuild and check** after any change, in this order. Each script exits non-zero on a problem:

  ```bash
  python3 scripts/build_compatibility.py
  python3 scripts/build_personas_index.py
  python3 scripts/build_starter.py
  python3 scripts/build_adapters.py
  python3 scripts/build_assets.py
  ```

- Python 3.10+, standard library only.
- **Persona cards:** frontmatter keys and allowed values are listed in [`personas/README.md`](personas/README.md); the soul stays under 350 words; every card answers the same three sample messages.
- **Writing:** Canadian English in prose (colour, behaviour, favourite), US spelling in identifiers and keys (`color`, `humor`). Persona names and text must be original: no 16Personalities, Keirsey, Truity or Korean "-형" names, and no copied descriptions.
- **Tone:** for fun, never a psychological claim. Nothing that ranks, labels or excludes people by type.
- **Commits:** clear messages; no secrets, personal paths or private data in any file.
