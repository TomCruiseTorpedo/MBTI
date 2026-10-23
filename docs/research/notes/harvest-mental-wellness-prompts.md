# Harvest notes: joebwd/mental-wellness-prompts

> **Status:** read directly through the GitHub API, 2026-10-23. Source: https://github.com/joebwd/mental-wellness-prompts (MIT licence, 229 stars, last pushed 2026-10-23). Its tone guide says the material was originally developed for Yara AI through 12+ months of testing and clinical review (October 2024 to October 2025), then released publicly.

## Licence

MIT, compatible with this repo's Apache-2.0. Any text or code adapted substantially must keep the MIT copyright and permission notice, for example in a `NOTICE` or `THIRD_PARTY_NOTICES.md` file with a link back. Ideas and structure can be reused freely.

## What is worth taking

| From | What | How it fits here |
|---|---|---|
| `tone_style_configuration.md` | "Voice personality settings": warmth, formality, directness, humour, energy, each with a level and a one-line meaning | Template for the style settings on every persona card |
| `tone_style_configuration.md` | "Adaptive style rules: if the user is brief/direct, emotional, analytical, humorous, formal", each with how to respond and an example line | Template for reading the user's style from how they write; maps loosely onto T/F, J/P and E/I |
| `tone_style_configuration.md` | Opening and closing patterns; "avoid performative warmth"; words to replace with plain language | Voice guidance for all 16 personas, especially the warm ones |
| `wellness_cli/soul.py` | Split between `SOUL.md` ("who am I and how do I show up", under 350 words) and `AGENTS.md` ("what do I do and how do I run"); onboarding answers woven into the soul | Same split as Muse's Soul.md and OpenClaw's SOUL.md. Persona card = soul; ground rules = operations |
| `wellness_cli/soul.py` | Principles: helpful not performatively helpful; low fluff; real point of view without lore overriding usefulness; no sycophancy | Persona-writing rules |
| `FAILED_APPROACHES.md` §8 | Asking about preferences upfront ("warm or brief? formal or casual?") failed: people don't know their preferences in the abstract. Detect them from how the person writes instead | Changes onboarding step 4: show sample replies to pick from and read the person's own style, rather than abstract questions |
| `FAILED_APPROACHES.md` §4 | Constant AI disclaimers annoyed users; never mentioning AI caused confusion and is deceptive. Balance: honest when asked or when limits matter | Matches the ground rule "never claim to be human" without nagging |
| `FAILED_APPROACHES.md` §1 | "Please be brief" and buried word limits didn't hold; explicit, prominent limits did | How to write length settings into a persona |
| `safety_crisis_resources.md`, `wellness_cli/safety_supervisor.py` | Region-aware crisis resources and escalation | One rule only: if someone signals real distress, the agent drops the playful persona and points to real help. Not a therapy feature |

## What to leave out

- The therapy pathways (`sample_pathway_anxiety.md`, `sample_pathway_sleep.md`) and the conversation guide's clinical framing. This project is a fun personality game, not mental-health support.
- The Moss CLI, memory vault and governance code. A prompt toolkit doesn't need them.
