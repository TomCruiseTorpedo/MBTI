# Adapters

Ready-made versions of every persona for each kind of agent. All of them are generated from the [persona cards](../personas/README.md) by `scripts/build_adapters.py`, so pick the folder for your platform and copy the file for your persona.

Not sure which persona? Let your agent pick with you first: see [START.md](../START.md) or the [onboarding script](../onboarding/ONBOARDING.md).

> **Back up first.** Before pasting anything over your agent's existing soul, identity or custom instructions, copy what's there now and keep it somewhere safe. That copy is your undo button. Personas change how your agent talks, not its name: it stays whatever you call it.

| Your agent | Use | How |
|---|---|---|
| **Muse** (Meta) | [`soul-identity/<persona>/`](soul-identity/) | Easiest: paste `SOUL.md` into a chat and ask Muse to remember it. For a permanent version, open Assistant > Identity > Soul and paste `SOUL.md`; put the lines from `IDENTITY.md` in Identity. |
| **Grok Bot** | [`grok-bot/<persona>.md`](grok-bot/) | Paste it into your Bot's chat (it starts with "Remember this persona…"), or add it as a file in the Bot's setup. |
| **ChatGPT**, **dots** | [`custom-instructions/<persona>.txt`](custom-instructions/) | Paste into Settings > Personalization > Custom instructions (dots: Customize > Custom rules). Every block is under 1,500 characters, so it fits the free plan. |
| **Claude** (and Claude Duet) | [`skills/<persona>/`](skills/) | Zip the persona's folder (the folder itself at the top of the zip) and upload it in Settings under skills. Duet picks up skills from your Claude account. |
| **Gemini**, OpenAI plugins, Muse Code | [`skills/<persona>/`](skills/) | Each folder is a standard Agent Skills `SKILL.md`. Gemini is moving Gems to skills; Muse Code reads `.agents/skills/`. |
| **Any agent, with the whole quiz** | [`skills/mbti-persona-picker/`](skills/mbti-persona-picker/) | A skill that runs the full onboarding: quiz, taste test, match, adopt. |
| **Coding agents** (Claude Code, Codex, Cursor…) | All of [`skills/`](skills/) | `npx skills add TomCruiseTorpedo/MBTI` lists all 17 skills and installs the ones you pick ([skills CLI](https://github.com/vercel-labs/skills)). |
| **OpenClaw**, Hermes Agent, ohmo | [`soul-identity/<persona>/`](soul-identity/) | Copy `SOUL.md` and `IDENTITY.md` into your agent's workspace (Hermes: `~/.hermes/SOUL.md`). |
| **Perplexity, Copilot, Grok custom instructions, anything else** | [`custom-instructions/<persona>.txt`](custom-instructions/) | Paste wherever the app lets you describe how it should respond. |

## What's in each format

- **custom-instructions**: the persona's tagline, how it talks, its overdrive, its key settings and the short version of the ground rules. Under 1,500 characters.
- **grok-bot**, **soul-identity/SOUL.md**, **skills/SKILL.md**: the full persona (who it is, how it talks, sample replies, pet peeves, overdrive) plus its settings and the full ground rules. Under 8,000 characters.
- **soul-identity/IDENTITY.md**: name, vibe and emoji, in the field style OpenClaw uses.

## Honest status

None of these has been tested on a real Muse or Grok Bot yet, and the Muse and OpenClaw formats follow their published docs as of October 2026. If something doesn't load or the persona doesn't stick, please open an issue.
