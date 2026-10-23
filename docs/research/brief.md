# Research brief

> **Date:** 2026-10-23. A synthesis of the raw notes in [`notes/`](notes/). Facts here come from those notes, which carry their own sources and confidence levels; check the note before relying on a detail. Products in this space changed several times in the three months before this brief, so re-check platform facts before each release.

## What shaped the design

- **Muse and Grok Bot can both hold a persona, but differently.** Muse has editable Soul.md and Identity.md files and remembers style changes told to it in chat. Grok Bot takes its role from the conversation ("…remember") or from files added in Team Bot setup.
- **Grok Bot can probably read the repo by itself; Muse might not.** Grok Bot has a browser and open network access by default. Whether Muse fetches arbitrary URLs is undocumented. So the repo ships a paste-in starter text as well as a link route.
- **The soul / operations split is everywhere.** Muse (Soul.md + Identity.md), OpenClaw and Hermes Agent (`SOUL.md`), and Yara AI's Moss (`SOUL.md` + `AGENTS.md`) all keep "who I am" apart from "how I run". Persona cards follow the same split.
- **Don't ask people abstract style questions.** Yara AI found people can't answer "warm or brief? formal or casual?" in the abstract. Onboarding shows sample replies to choose from instead, and reads the person's own writing style.
- **Personality changes the style, never the truth.** Warm or agreeable AI is measurably more likely to agree with wrong statements, and user profiles can make it worse. A floor of correcting factual mistakes applies to every persona.
- **The colours people know come from DISC.** Vinh Giang's colour video draws on Thomas Erikson's *Surrounded by Idiots*, a Red/Yellow/Green/Blue version of DISC. That is the colour layer here.
- **Keep the name, own the content.** "MBTI" is a mark of the Myers & Briggs Foundation; the repo keeps the name with an acknowledgement, but the 16 persona names and all descriptions are original.

## 1. Where personas will live

| Platform | Priority | How a persona gets in | What we ship |
|---|---|---|---|
| **Muse (Meta)** | Top | Edit Soul.md / Identity.md (Assistant > Identity > Soul), or tell Muse in chat (persists) | Soul and Identity blocks per persona, plus a "tell Muse" paste block |
| **Grok Bot (xAI / SpaceXAI)** | Top | State the role in the Bot's conversation and say "remember"; Team Bot setup files (`.md` accepted, up to 256,000 chars) | A paste block and a Team Bot file per persona |
| ChatGPT | Reach | Custom instructions (1,500 chars on Free and Go, reported 5,000 on paid); Custom GPTs retire 2026-12-11 in favour of plugins built on skills | Short-tier text; `SKILL.md` folder |
| Gemini | Reach | Gems moving to skills (`SKILL.md`) from October 2026 | `SKILL.md` folder |
| Claude, Claude Duet | Reach / search coverage | Skills (`SKILL.md` zip upload); Duet inherits the account's skills | `SKILL.md` folder |
| dots (OpenAI) | Search coverage | Hand-typed custom rules only | Short-tier text |
| OpenClaw, Hermes Agent, ohmo | Harnesses | `SOUL.md` + `IDENTITY.md` (OpenClaw caps 20,000 chars per file) | Harness files |
| Perplexity | Optional | Per-project instructions, 8,000 chars | Standard-tier text |

Skip for now: Meta AI Studio (character creation ended), Doubao and Qwen (user-built personas removed in July 2026), DeepSeek (API only), Instinct (closed, no persona surface).

**Size tiers.** Every persona renders short (about 1,500 chars), standard (about 4,000) and full (up to 8,000), so one version fits any field.

## 2. How an agent finds and reads the repo

- **Link route:** the person gives their agent the repo URL. Expected to work on Grok Bot; untested on Muse.
- **Paste route:** a single self-contained starter text with the onboarding script, a compact persona list and the compatibility chart. Works on any agent.
- **Discovery files:** `AGENTS.md` and `llms.txt` at the root, a README section for agents, and GitHub topics. Muse Code (Meta's CLI) honours `AGENTS.md` and skills folders; whether the consumer Muse app or Grok Bot honours any of these is unknown. They are cheap, so ship them, but don't claim they work.
- **Live tests before release:** on a real Muse and a real Grok Bot, check URL fetch, `.md` file upload, and whether a persona told in chat survives a new conversation. Document only what passes.

## 3. Four letters and four colours

The four letters stay the main label, because that is what people already know and share. The colour is a friendlier second label, worked out from two of the letters:

| Colour | Means | Letters |
|---|---|---|
| Red | Outgoing, task-focused | E + T: ENTJ, ESTJ, ENTP, ESTP |
| Yellow | Outgoing, people-focused | E + F: ENFP, ENFJ, ESFP, ESFJ |
| Green | Reserved, people-focused | I + F: INFJ, INFP, ISFJ, ISFP |
| Blue | Reserved, task-focused | I + T: INTJ, INTP, ISTJ, ISTP |

- This matches the colours in Erikson's book and Vinh Giang's video, and the structure of Insights Discovery. It is convention, not research.
- True Colors uses Blue and Green almost the opposite way. The README and persona cards define our colours in plain words and claim no match with any vendor's model.
- S/N and J/P, which the colours ignore, set level of detail and planning style in each persona.
- Lumina Spark contributes two ideas, under our own names: a person can lean both ways on a trait, and a persona can show a natural, everyday and stressed side.

## 4. Style settings and ground rules

**Settings on every persona card** (adapted from Yara AI's tone template and the communication research): warmth, formality, directness, humour, energy, reply length, structure, emoji, and how often to check in. Length limits must be explicit and prominent; Yara found "please be brief" alone doesn't hold.

**Ground rules no persona can change:**

- Correct factual mistakes, however warm the persona.
- Say plainly when unsure.
- Be honest about being an AI when asked or when it matters, without a disclaimer on every reply. Never claim to be human; the types are never a diagnosis.
- If someone signals real distress, drop the playful persona and point to real help.
- Keep it light: no put-downs by type, and not for hiring or judging other people.

## 5. Compatibility

The tone to aim for is how South Korea plays with MBTI (notes: [`korean-mbti-culture.md`](notes/korean-mbti-culture.md)): an icebreaker since a 2020 TV episode, on most young people's dating profiles, in idol introductions, and in memes such as "너 T야?" ("are you a T?") and the "I was sad, so I bought bread" quiz, where an F asks why you were sad and a T asks what bread.

**The chart.** Korean compatibility (궁합) charts have no known source and contradict each other, and even a Korean test site admits its grades are just the author's rules. So ours says so up front: [`compatibility/chart.md`](../../compatibility/chart.md), generated from five rules in `scripts/build_compatibility.py`:

| Tier | Rule | Per type |
|---|---|---|
| 👯 Twins | Same code | 1 |
| 💞 Perfect pair (찰떡) | Same S/N, opposite E/I and J/P | 2 |
| 😊 Easy chemistry | Same S/N otherwise | 5 |
| ⚡ Spark | Different S/N, same T/F | 4 |
| 🧗 Extra effort | Everything else | 4 |

The perfect-pair rule reproduces all eleven best-match pairs the Korean charts most often share (ENFP–INFJ, ENFP–INTJ, INFJ–ENTP, INFP–ENFJ, ENTJ–INFP, ESTJ–ISFP, ESTJ–ISTP, and ISTJ/ISFJ with ESFP/ESTP). The pairs those charts most often call worst, S types against NF types, mostly land in Extra effort.

**How it's used and framed:**

- The agent's best-match persona is one of the person's two perfect pairs; the wildcard is a Spark (to be challenged) or their Twin (to feel understood).
- The agent explains a pairing like a chemistry (케미) card, from one line per letter: same or different E/I, S/N, T/F, J/P.
- There is no "worst match". Critics in Korea point to people excluded or rejected by type, so hard pairings are "Extra effort", never bad.
- Personas tease themselves, never the person or other types. "Are you a T?" is a joke the persona can make about itself.
- People can say "I've changed" or "not sure"; the agent treats letters as leanings, not boxes.
- Never for hiring or screening partners. Korea's hiring-by-type controversy is exactly what to avoid.

## 6. Names and trademarks

- "MBTI", "Myers-Briggs" and "Myers-Briggs Type Indicator" are marks of The Myers & Briggs Foundation, Inc. The README carries an acknowledgement; the project uses the four-letter codes descriptively and never reproduces the assessment.
- The Elite Four nicknames (Architect, Logician…) are 16Personalities' published names. They don't appear to be trademarked, but 16Personalities claims copyright on its descriptions. All 16 persona names and descriptions here are original, and its group names (Analysts, Diplomats, Sentinels, Explorers) are avoided too.
- Vendor colour names ("Fiery Red", "Sunshine Yellow", "Commanding Red") are avoided; Red, Yellow, Green and Blue are generic.
- Text adapted closely from `joebwd/mental-wellness-prompts` keeps its MIT notice in a `NOTICE` file.

## 7. What carries over from Elite Four

Elite Four, an earlier multi-agent experiment by the same author (February 2026), had an MBTI layer for its four fireteam agents.

- **Keep:** the per-type fields in `agent_mbti_configs_async.json` (communication style, feedback preference, conflict handling, decision approach, good and difficult pairings) as a starting checklist for each persona card; loading one shared primer so every agent reads the types the same way.
- **Drop:** gating abilities by type (`skill_modules.disallowed`); the 16Personalities nicknames; the generic reference prose.
- **Fix:** the lookup table lists ESFP twice.

## Not researched further

The personality-science strand was stopped once the project was set as for-fun pop-psych. The communication notes still record what the evidence says about AI response style, for anyone who wants it.
