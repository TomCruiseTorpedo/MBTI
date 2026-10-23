# Design draft: agent-guided onboarding

> **Status:** draft, 2026-10-23. Built on the [research brief](../research/brief.md): platform research, the colour and trademark notes, Korean MBTI culture, and lessons from `joebwd/mental-wellness-prompts`. The compatibility chart, ground rules and first-draft persona cards are done; the onboarding script and starter text are next.

## The idea in one paragraph

This is a **for-fun, pop-psych** project, in the spirit of how people in South Korea use MBTI: a conversation starter, a compatibility game, something to laugh about with friends, not a clinical test. The person never has to read this repo. They tell their personal agent (Muse or Grok Bot first; any capable agent after that) something like *"Read github.com/TomCruiseTorpedo/MBTI and help me pick a personality for you."* The agent reads the repo, chats with them, explains which of 16 MBTI-style personas fits them best and how the two types get along, and then adopts it. The repo is therefore **an instruction set for the agent first** and a browsable library for humans second.

## User story

> As someone who chats with a personal AI agent every day, I want it to figure out my type with me, tell me which persona we'd click with best, and switch to it, so working together is more fun and feels natural.

## Conversation flow

1. **Entry.** Two routes, because we can't yet count on every agent fetching a URL:
   - **Link:** the human gives the agent the repo URL. Grok Bot has a browser and open network access by default, so this should work; whether Muse fetches arbitrary URLs is undocumented.
   - **Paste or upload:** the human pastes one self-contained starter text, or attaches it as a file. This works on any agent that can read a message.
2. **Framing.** The agent sets the tone in a sentence or two: this is a fun personality game, nothing is locked in, and the person can switch any time.
3. **Your type.** The agent asks whether the person already knows their four letters.
   - **Yes:** use them.
   - **No, or unsure:** play a short quiz (about 8~12 light, situational questions, one or two at a time) that lands on four letters and a colour. Questions work like the Korean "I was sad, so I bought bread" quiz: a one-line scenario, and the person's reaction hints at a lean. Results are leanings, and "I've changed" or "not sure" are fine answers.
4. **Your style, by taste test.** Instead of abstract questions ("warm or brief?"), which Yara found people can't answer, the agent shows two or three short sample replies to the same message and asks which one they'd rather get. It also notices how the person writes during the quiz (short or chatty, emoji or none, jokes or not). The picks fine-tune whichever persona they choose.
5. **Reflect back.** The agent sums the person up in a fun, recognizable way (their four letters, their colour, a few "this is so you" lines) and asks whether it lands.
6. **Match.** Using [`compatibility/chart.md`](../../compatibility/chart.md), the agent recommends a best-match persona (one of the person's two perfect pairs) and a wildcard (a Spark or their Twin), explains the chemistry letter by letter (where they click, where they'll bicker), and gives a taste of how each one talks.
7. **Adopt.** The person picks. The agent switches persona for the rest of the conversation, then makes it stick in the way its platform allows:
   - **Muse:** fill in Soul.md and Identity.md (Assistant > Identity > Soul), or simply tell Muse in chat, which persists.
   - **Grok Bot:** state the persona in the Bot's conversation and say "remember", or add it as a file in Team Bot setup.
   - **Others:** custom-instructions text, an uploaded skill, or harness files such as `SOUL.md`.
8. **Tune or swap later.** "Be more blunt" adjusts a style setting. "Try being an ENFP" swaps the persona.

## What the repo has to contain

| Piece | Purpose | Audience |
|---|---|---|
| Entry files | `AGENTS.md`, `llms.txt` and a README section that all point the agent to the onboarding script. Cheap to ship; no agent is confirmed to honour them yet | Agent |
| Starter text | One self-contained file with the onboarding script, a compact persona list and the compatibility chart, small enough to paste. The fallback when the agent can't browse | Human pastes, agent reads |
| Onboarding script | The flow above, written as instructions to the agent, with the quiz, the sample replies and how to score them | Agent |
| 16 persona cards | First draft done: [`personas/`](../../personas/README.md). Per type, split like Muse, OpenClaw and Yara's Moss: identity and style settings in the frontmatter, a **soul** under 350 words in the body, with replies to the same three sample messages for the taste test. `scripts/build_personas_index.py` checks every card and writes `personas/index.json` | Both |
| Ground rules | Done: [`personas/GROUND-RULES.md`](../../personas/GROUND-RULES.md), one shared operations file kept separate from the personas so no persona can rewrite it | Agent |
| Style settings | Warmth, formality, directness, humour, energy, length, emoji, check-ins: what each changes and the defaults per persona | Agent |
| Compatibility chart | Done: [`compatibility/chart.md`](../../compatibility/chart.md) and `chart.json`, generated from five author-made rules in `scripts/build_compatibility.py` (Twins, Perfect pair, Easy chemistry, Spark, Extra effort; no "worst match") | Both |
| Colour layer | Red / Yellow / Green / Blue in the sense Vinh Giang popularized (from *Surrounded by Idiots*): outgoing + task, outgoing + people, reserved + people, reserved + task. Derived from the E/I and T/F letters in an editable mapping file, with our own descriptions | Both |
| Adapters | Thin renderers from each persona card to platform formats: Muse Soul.md/Identity.md blocks; a Grok Bot block; `SKILL.md` folders (Claude, Gemini, Muse Code, OpenAI plugins); OpenClaw/Hermes `SOUL.md` + `IDENTITY.md`; plain custom-instructions text | Human (copy) |
| Size tiers | Each persona rendered short (about 1,500 chars), standard (about 4,000) and full (up to 8,000), so one version fits any instructions field | Agent |
| Machine-readable index | One JSON file listing personas, colours and pairings, for agents that parse rather than read | Agent |

## Ground rules (still apply when it's just for fun)

These are about the agent's behaviour, not personality theory:

- A warm or agreeable persona still corrects factual mistakes. Personality changes the style, not the truth.
- The agent says plainly when it's unsure.
- The agent is honest about being an AI when asked or when it matters, without tacking a disclaimer onto every reply. It never claims to be human, and the types are never a diagnosis.
- If someone signals real distress, the agent drops the playful persona, responds plainly and kindly, and points to real help. This project is not mental-health support.
- Keep it light: no "your type is bad at X" put-downs, and not for hiring or judging other people.

## Open questions

- **Live tests:** on a real Muse and a real Grok Bot, check URL fetch, file upload of `.md`, and whether a persona told in chat persists. Document only what passes.
- **Naming:** our own names for the 16 personas (not 16Personalities' nicknames or group names); four-letter codes used descriptively with an "unaffiliated" acknowledgement. The repo keeps the name "MBTI" (decided 2026-10-23), with a trademark acknowledgement in the README, since "MBTI" is a mark of the Myers & Briggs Foundation (see `docs/research/notes/colour-models-and-ip.md`).
- **Attribution:** anything adapted closely from `joebwd/mental-wellness-prompts` (MIT) needs its notice kept in a `NOTICE` file.
