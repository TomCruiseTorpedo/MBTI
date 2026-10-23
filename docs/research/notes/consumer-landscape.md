# Research notes: consumer agent landscape and harnesses

> **Status:** raw desk research from a delegated research agent, 2026-10-23. Not yet independently verified. Usage metrics mix weekly and monthly, China-only and global, web and app, so the ranking is approximate.

## Consumer ranking (rough)

| # | Product (maker) | Best usage evidence | Source | Conf. |
|---|---|---|---|---|
| 1 | ChatGPT (OpenAI) | 1.2B weekly users (OpenAI, early Oct 2026) | https://momenticmarketing.com/blog/top-ai-chatbots · https://openai.com/index/new-chatgpt-ads-format-and-measurement/ (403) | M |
| 2 | Gemini (Google) | 950M MAU, 2026-07-22 | https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/ | H |
| 3 | Muse / Meta AI (Meta) | Muse launched 2026-09-08; about 3M weekly users early October. Meta AI "1B MAU" is a stale May 2025 figure | https://thenextweb.com/news/meta-muse-3-million-weekly-users-information | L |
| 4 | Doubao (ByteDance) | 382M MAU, China, May 2026 | https://technode.com/2026/07/14/questmobile-chinas-ai-native-apps-reach-499-million-monthly-active-users/ | M |
| 5 | Qwen (Alibaba) | 167M MAU, China, May 2026 | same | M |
| 6 | DeepSeek | 130M MAU, China, May 2026 | same | M |
| 7 | Grok (xAI) | About 117M MAU, March 2026, reportedly from a SpaceX IPO filing; includes X usage | https://pulse2.com/spacex-grok-reaches-117-million-users-as-ai-push-accelerates/ | L |
| 8 | Microsoft Copilot | No official consumer MAU; third-party about 110M | https://office365itpros.com/2026/07/30/fy26-q4-microsoft-results/ | L |
| 9 | Claude (Anthropic) | No company MAU; 119M web visitors, Sep 2026 (Similarweb via Momentic) | Momentic | M (web) |
| 10 | Perplexity | Third-party 34~45M core MAU | https://www.gradually.ai/en/perplexity-statistics/ | L |

Character.AI about 20M MAU (third-party, L).

## Persona surfaces outside the main targets

| Product | Surface | Limits | Conf. |
|---|---|---|---|
| Perplexity | Per-project custom instructions (Spaces renamed Projects 2026-07-30) | 8,000 chars | H (limits) |
| Microsoft Copilot | M365: custom instructions. Consumer: memory, "Real Talk" style, Mico avatar | Not stated | H (M365); consumer L |
| DeepSeek | API system prompt only; no app persona UI found | — | H (API) |
| Doubao, Qwen | User-built agents and personas removed around 2026-07-15, the day China's interim measures on anthropomorphic AI interaction took effect (link reported by analysts, UNVERIFIED) | — | H (removal) |
| Alexa+ | Four presets (Brief, Chill, Sweet, Sassy) over five dimensions; no free text | — | H (https://www.aboutamazon.com/news/devices/alexa-plus-personality-styles) |

## Harnesses (secondary)

| Harness | Persona definition | Documented? | Conf. |
|---|---|---|---|
| Instinct | Closed, invite-only consumer agent (Spear Street Technology, dba Instinct) over iMessage/WhatsApp/calls. No persona surface found. Not a harness | No | M |
| OpenClaw | `SOUL.md`, `IDENTITY.md` (`- Name/Creature/Vibe/Emoji/Avatar:` lines), `USER.md` (4,000 chars), `AGENTS.md`, `BOOTSTRAP.md`, `MEMORY.md`, `skills/`; 20,000 chars per file, 60,000 total (https://docs.openclaw.ai/concepts/agent-workspace.md) | Yes | H |
| Hermes Agent (Nous Research) | `~/.hermes/SOUL.md`; `agent.personalities` in `config.yaml` (name → prompt); `/personality <name>` (https://hermes-agent.nousresearch.com/docs/user-guide/features/personality) | Yes | H |
| ohmo / OpenHarness (HKUDS) | `soul.md`, `identity.md`, `user.md` | README only | M |
| NanoClaw | Per-group `CLAUDE.md` | Partly | M |
| ZeroClaw | `config.toml` identity with `format` "openclaw" or "aieos" | Yes | H (keys) |

## Researcher's takeaways

- A SOUL.md + IDENTITY.md (+ USER.md) set likely covers OpenClaw, Hermes Agent and ohmo at once, and mirrors Muse's Soul.md / Identity.md.
- Keep the core persona text under 8,000 chars so one block fits Perplexity and most custom-instruction fields.
- Skip Doubao and Qwen (personas removed), DeepSeek (API only), Instinct (closed). Alexa+ can only be mapped to a preset.
