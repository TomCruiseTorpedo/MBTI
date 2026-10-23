# Research notes: platform persona surfaces

> **Status:** raw desk research from a delegated research agent, 2026-10-23. Not yet independently verified. All URLs accessed 2026-10-23. "(snip)" = page returned 403/404 and only a search snippet was seen. Meta and xAI help pages were read through a summarizing fetcher, so wording is paraphrase. This landscape changed several times in the 90 days before this note; re-check before relying on it.

## Product identity

- **Muse (Meta)**, HIGH. A brand family: models (Muse Spark, Wonder, Glimmer, Image); a consumer agent launched 2026-09-08, US only, running on Muse Spark in a per-user "Muse Secure VM", reached through iOS/Android, muse.ai and WhatsApp (https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/); the Meta Model API (public preview); and Muse Code, a CLI coding agent. Muse Wonder paid-tier pricing is CNBC-reported only (MEDIUM; https://www.cnbc.com/2026/10/12/meta-muse-wonder-ai-model-agent.html).
- **Grok Bot**, HIGH. Official name is singular, "Grok Bot". Each persistent Bot runs on a cloud computer with a browser, filesystem and terminal (https://docs.x.ai/grok-bot/overview). Access via Cursor paid plans, SuperGrok or Grok Business.
- **SpaceX / xAI**, MEDIUM, secondary sources only: SpaceX acquired xAI in an all-stock deal reported closed 2026-02-02 (Reuters via https://www.nst.com.my/amp/business/corporate/2026/02/1370202/spacex-acquires-xai-musk-moves-unite-ai-space-ambitions); xAI rebranded "SpaceXAI" around 2026-07-06 (https://dataconomy.com/2026/07/07/elon-musk-rebrands-merged-xai-and-spacex-as-spacexai/). Reports on a SpaceX purchase of Cursor and a further "SpaceXSI" rename conflict (LOW, unreconciled).

## Per-platform surfaces

| Surface | Format / limit | How a user imports it | Source | Conf. |
|---|---|---|---|---|
| **Muse: Soul.md / Identity.md / Memory.md** | Markdown; no size limits stated | Assistant icon > Identity > Soul, then edit or clear. No upload or paste procedure documented | https://www.meta.com/help/superintelligence/2225571704857152/ | HIGH exists; MEDIUM mechanics |
| **Muse: chat customization** | Natural language: name, tone, style, avatar, tagline; persists across chats; revert by asking | Tell Muse in chat | https://www.meta.com/help/superintelligence/995796179982326/ | HIGH |
| **Muse: import memory** | .zip chat export from a previous assistant | Settings > Data Controls > Import memory | same page | HIGH |
| **Muse: skills** | Only Meta-built skills documented; no user skills or SKILL.md | n/a | https://www.meta.com/help/superintelligence/2797651547267109/ | HIGH |
| **Muse: Model API** | OpenAI Chat Completions/Responses and Anthropic Messages compatible at `api.meta.ai/v1`; model `muse-spark-1.1`; prefer a `developer` message over `system`; 1M-token context | Persona as a developer message | https://dev.meta.ai/resources/blog/build-with-muse-spark | HIGH |
| **Muse Code (CLI)** | Reads `AGENTS.md`, `CLAUDE.md`, `.agents/AGENTS.md`, `.claude/CLAUDE.md`; `.agents/skills/<id>/SKILL.md` and `~/.claude/skills`; MCP via stdio or streamable HTTP | `muse skills install ./path`; project rules ignored until the workspace is trusted | https://dev.meta.ai/docs/muse-code/configuration.md · https://dev.meta.ai/docs/muse-code/extending.md | HIGH |
| **Meta AI Studio** | Creating or editing AI characters ended (update dated 2026-08-10); existing characters remain | Dead end | https://about.fb.com/news/2024/07/create-your-own-custom-ai-with-ai-studio/ | HIGH |
| **Grok Bot: role by conversation** | Free text; first message sets job, sources and approval limits, then "remember". No instruction file or char limit documented | Paste into the first message | https://docs.x.ai/grok-bot/bots | HIGH |
| **Grok Bot: Team Bot setup** | Description ≤140 chars; files `.txt/.md/.markdown/.csv/.json/.yaml/.yml`, ≤256,000 chars each; ≤25 secrets | Publish a personal Bot to the team, or the Bot's Setup section | https://docs.x.ai/grok-bot/team-bots | HIGH |
| **Grok Bot: templates** | Share > Create template (public link or team-only); carries identity, description, skills, routines; file format unpublished | Recipient opens the preview, "Add to Grok Bot", or Marketplace > Import Bot | https://docs.x.ai/grok-bot/bots | HIGH; format UNVERIFIED |
| **Grok Bot: attachments** | ≤6 per message; documents, images, audio ≤25 MB; video ≤200 MB; `.md` not named | Attach in the composer | https://docs.x.ai/grok-bot/files-and-results | HIGH; `.md` unconfirmed |
| **xAI API** | `system`, `user`, `assistant` roles; `grok-4.7` 500k context | System prompt via API | https://docs.x.ai/developers/models | HIGH |
| **Grok consumer custom instructions / custom agents** | Limit reported as 4,000 or 12,000 chars; sources conflict | Settings > Customize | https://www.uniflow.kr/en/grok-custom-instructions-setup-guide-workspaces-agents/ | UNVERIFIED |
| **ChatGPT: Custom GPTs** | Being retired 2026-12-11, replaced by plugins (skills and/or MCP); migration converts GPT instructions into a skill | Plugin creation instead of a new GPT | https://help.openai.com/en/articles/20001519 (snip) · https://virtualizationreview.com/articles/2026/09/28/openai-to-retire-custom-gpts-replace-them-with-plugins.aspx | MEDIUM-HIGH |
| **ChatGPT: custom instructions / personality presets** | Limit reported raised from 1,500 to 5,000 chars (paid) on 2026-07-15; Free and Go 1,500 | Settings > Personalization | https://cryptobriefing.com/openai-chatgpt-custom-instructions-5000-characters/ | LOW |
| **Claude: Skills** | Zip with `SKILL.md`; `name` ≤64 chars, lowercase/digits/hyphens, no "anthropic" or "claude"; `description` ≤1,024 chars | claude.ai settings, upload zip; Claude Code reads `~/.claude/skills` or `.claude/skills` | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | HIGH |
| **Claude: styles / projects** | Preset and custom styles; project instructions plus knowledge; no official char limits found | In-app | https://support.anthropic.com/en/articles/10185698-configuring-and-using-styles (snip) | MEDIUM |
| **Gemini: Gems → skills** | Skills (SKILL.md, invoked with `/`) roll out in the Gemini app from 2026-10-13; personal Gems become draft skills from November 2026 | Gem manager now, skills going forward | https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills · https://support.google.com/gemini/answer/15146780 | HIGH (dates) |

## Open formats

| Format | Fields | Open spec? | Source | Conf. |
|---|---|---|---|---|
| **AGENTS.md** | Plain Markdown, no required fields; nearest file wins; user chat overrides | Stewarded by the Agentic AI Foundation (Linux Foundation); licence not stated | https://agents.md | HIGH |
| **Agent Skills `SKILL.md`** | Required `name` (≤64, matches directory) and `description` (≤1,024); optional `license`, `compatibility`, `metadata`, `allowed-tools`; free body, under 500 lines recommended; optional `scripts/`, `references/`, `assets/` | Public spec with a validator (`skills-ref`) | https://agentskills.io/specification | HIGH |
| **OpenClaw bootstrap files** | `SOUL.md` (persona, tone, boundaries), `IDENTITY.md` (name, vibe, emoji), `AGENTS.md`, `USER.md`, `TOOLS.md`, `BOOTSTRAP.md`; truncated at 20,000 chars per file, 60,000 total | Markdown conventions, no formal spec | https://docs.openclaw.ai/concepts/agent-workspace | HIGH |
| **Character Card V2** | JSON `spec:"chara_card_v2"`, `data`: name, description, personality, scenario, first_mes, mes_example, system_prompt, tags, creator, … | Public GitHub spec | https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md | HIGH |
| **Character Card V3** | `chara_card_v3`; adds assets, nickname, multilingual creator notes, dates; JSON, PNG `ccv3` chunk, `.charx` zip | Public GitHub spec | https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md | HIGH |
| **ElizaOS character** | TypeScript `Character`: name, bio, messageExamples, topics, adjectives, style, system, plugins, … | Framework schema | https://docs.elizaos.ai/agents/character-interface | HIGH |

## Terms of service

- **Anthropic AUP**, HIGH (https://www.anthropic.com/legal/aup): no impersonating real people to mislead; no fake personas or bots that claim to be human; consumer chatbots disclose AI; clearly disclosed fiction or parody allowed.
- **Meta Model API AUP**, HIGH (https://dev.meta.ai/legal/acceptable-use-policy): no impersonation without consent; no presenting AI output as human-made; agents may not hide their automated nature where disclosure is required. Consumer Muse terms not retrieved (UNVERIFIED).
- **xAI AUP**, UNVERIFIED (403). Archived 2026-06-26 version snippet lists deceptive impersonation of a real person (https://x.ai/legal/acceptable-use-policy/previous-2026-06-26).
- **OpenAI usage policies**, UNVERIFIED (403). Secondary summaries: named personas allowed; denying being an AI when sincerely asked is not.

## Can Muse and Grok Bot find and read the repo themselves?

| Question | Muse (consumer agent) | Grok Bot |
|---|---|---|
| Fetch a URL or GitHub on its own | Has a browser on its VM; whether it fetches arbitrary URLs is not stated. GitHub connector UNVERIFIED. MEDIUM at best | Browser, filesystem, terminal; egress allow-all unless an Enterprise admin restricts it; "work with links they can access"; GitHub connector exists. Cloning a repo not documented. HIGH |
| Install skills, tools, MCP | Builds "custom connectors" on request (https://www.meta.com/help/superintelligence/1687253048996149/, HIGH); MCP not mentioned; user-authored SKILL.md not documented | Installs apps and packaged skills; saved skills invoked with `/`; remote MCP referenced on the security page. SKILL.md compatibility UNVERIFIED |
| Hand it a persona | Tell it in chat (persists); edit Soul.md / Identity.md / Memory.md; upload documents in chat (types and limits undocumented) | Paste into the first message and say "remember"; attach ≤6 files; Team Bot files ≤256,000 chars; template links in an unpublished format |
| Discovery conventions | Muse Code honours AGENTS.md and `.agents/skills`; consumer agent unknown | Grok Build (not Grok Bot) lists AGENTS.md; Grok Bot unknown |

`dev.meta.ai/llms.txt` exists; docs.x.ai has `llms.txt` (MEDIUM). Whether either consumer agent honours `llms.txt`, AGENTS.md or GitHub topics: UNVERIFIED.

## Researcher's design implications

- One canonical persona source in a SKILL.md-compatible folder, with optional `persona.json` for structured fields.
- Short, standard and full tiers, sized for roughly 1,500 / 4,000 / 20,000 chars.
- Adapters as thin renderers: Muse Soul.md + Identity.md blocks; Grok Bot first-message block and Team Bot file; OpenClaw SOUL.md + IDENTITY.md; API developer/system message; optionally Character Card V3 and AGENTS.md snippets.
- Skip dying targets: Custom GPTs (retiring 2026-12-11) and Meta AI Studio character creation (ended).
- A plain-text "paste this to your agent" block that works even if the agent can't browse.
- A disclosure rule in every persona: never deny being an AI when sincerely asked; fictional archetype names only.
- Test each claim on a real Muse and Grok Bot (Soul.md paste, `.md` upload, URL fetch) before documenting it as supported.
