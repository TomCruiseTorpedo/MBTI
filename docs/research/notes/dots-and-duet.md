# Research notes: dots (OpenAI) and Claude Duet (Anthropic)

> **Status:** raw desk research from a delegated research agent, 2026-10-23, from first-party pages it opened. Not yet independently verified. Low-priority targets, kept mainly for search coverage. Synthesized findings belong in the research brief, not here.

**Summary:** neither product has a documented persona, system-prompt or character-definition surface. Persona packs for either have to ride on a general mechanism: Claude skills (Duet) or ChatGPT personalization settings (dots; UNVERIFIED that they apply).

## dots (OpenAI)

OpenAI writes the name in lowercase. Launched 2026-09-29 at DevDay: an always-on agent in ChatGPT with its own cloud computer, running on GPT-6 Astra. Plans: Pro (not EEA, Switzerland or UK) and Business Premium; Enterprise beta is admin-enabled and off by default. 18+ only. HIGH. Sources: https://openai.com/index/introducing-dots/ · https://help.openai.com/en/articles/20001530-getting-started-with-your-dot

| Surface | Format | Limit | How a user imports it | Confidence |
|---|---|---|---|---|
| Name and handle | Free text in the profile | None stated | Typed by hand | HIGH |
| Character or pet avatar | Preset list or a generated pet | Presets only | UI pick, no import | HIGH |
| Custom rules (Customize > Custom rules) | Free-text action description plus one of 4 behaviours: act without asking / act if pre-approved / ask first / hand off | None stated | Typed by hand | HIGH |
| Memory | ChatGPT memory plus the dot's own notes | Dot's own memories not viewable or editable | Not importable | HIGH |
| Local skills | Format not stated | Not stated | Needs desktop-app local access | MEDIUM that it exists; format UNVERIFIED |
| Tone or personality | None documented for dots | n/a | n/a | ChatGPT-wide "Characteristics" sliders (warmth, enthusiasm, markdown, emoji; help.openai.com/en/articles/20001038) never mention dots. Whether dots honour them or custom instructions: UNVERIFIED |
| Public API or SDK | None found | n/a | n/a | LOW (third-party source only) |

ToS notes:

- Custom rules cannot override built-in safety requirements or auto-review (https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs). HIGH.
- OpenAI Usage Policies bar impersonation, deception and circumventing safeguards (https://openai.com/policies/usage-policies/). MEDIUM. The page header shows "Effective: November 20, 2026", a future date; which version is current was not checked.
- Nothing found on distributing persona or prompt packs. UNVERIFIED.

## Claude Duet (Anthropic)

Official name "Claude Duet". Announced 2026-10-21 as a research preview: a proactive agent that sends a morning brief, works in a cloud VM, and asks before sending, paying, signing or deleting. Runs on Claude Opus 5.5 (not user-selectable). Standalone iOS/Android app, also on claude.ai. Waitlist for US Pro and Max only. HIGH. Sources: https://claude.com/resources/articles/claude-duet · https://support.claude.com/en/articles/17631495-get-started-with-claude-duet

| Surface | Format | Limit | How a user imports it | Confidence |
|---|---|---|---|---|
| Inherited Claude account context | Memory, skills and connectors carry over | n/a | Set up in Claude, appears in Duet | HIGH |
| Skills (Customize > Skills) | Zipped folder with `SKILL.md`: YAML frontmatter `name` + `description`, then markdown body | `name` 64 chars, lowercase, hyphens; `description` 1,024 chars; under 500 lines recommended; zip cap exists, number not stated | Settings > Customize > Skills > Upload a skill (skill folder at top level of the zip) | HIGH for format and inheritance; UNVERIFIED that Duet applies skills as chat does. Sources: claude.com/docs/skills/how-to · support.claude.com/en/articles/12512180-use-skills-in-claude |
| Account-wide instructions for Claude | Free text in Settings | No cap stated | Typed by hand | HIGH for Claude generally; UNVERIFIED for Duet (support.claude.com/en/articles/10185728) |
| Notification preferences | Natural language | None stated | Tell Duet directly | HIGH |
| Duet-specific persona, system prompt or API | None found | n/a | n/a | UNVERIFIED |

ToS notes:

- Anthropic's usage policy bars impersonating real people and deceptive personas, bars bots that claim to be human, and requires AI disclosure in consumer-facing agents (https://www.anthropic.com/legal/aup). MEDIUM, from a fetch-tool summary. The page shows an effective date of 2026-11-12, a future date; which version is current was not checked.
- Duet adds a dedicated safety system prompt and classifier, and rejects the most sensitive information such as card and government ID numbers. HIGH.
- Skills can include or install third-party packages; share only reviewable skills. HIGH.

Not read: Anthropic's "Claude Duet Safety, Privacy, and Security" article and the Duet product page.

## Implication for this repo

A `SKILL.md`-format persona is the one path that reaches Duet (through Claude skills). For dots, the only documented lever is hand-typed custom rules; a paste-ready plain-text persona block is the realistic deliverable.
