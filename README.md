# MBTI: personalities for your AI agents

Plug-and-play, MBTI-style personas for personal AI agents such as **Meta Muse** and **Grok Bot**, plus any agent that can read a link or a pasted prompt (ChatGPT, Claude, Gemini, OpenClaw and more).

Point your agent at this repo and let it do the rest. It chats with you to work out your four-letter type and your colour, tells you which of 16 personas you'd click with best (and which one would be a fun wildcard), then switches to it. No forms, no reading required.

This is a **for-fun, pop-psych** project, borrowing the way South Korea plays with MBTI: as an icebreaker, a compatibility game (궁합) and an endless source of "are you a T?" jokes. Each persona even comes with the shorthand Koreans use when they say the type out loud. It is not a psychological assessment.

## Try it

- **If your agent can open links:** tell it *"Read github.com/TomCruiseTorpedo/MBTI and follow onboarding/ONBOARDING.md with me."*
- **If it can't:** paste the whole of [START.md](START.md) into a chat with your agent, or attach it as a file. It contains everything: ground rules, the onboarding script, all 16 personas and the matches.

Not yet tested on a real Muse or Grok Bot; reports welcome.

## Status

First draft, untested on real agents.

- Onboarding script (quiz, taste test, match, adopt): [onboarding/ONBOARDING.md](onboarding/ONBOARDING.md)
- Paste-in starter text, generated from the files below: [START.md](START.md)
- 16 persona cards (first draft) and the ground rules every persona follows: [personas/](personas/README.md)
- Compatibility chart (done, for fun): [compatibility/chart.md](compatibility/chart.md)
- Design: [docs/design/agent-guided-onboarding.md](docs/design/agent-guided-onboarding.md)
- Research brief: [docs/research/brief.md](docs/research/brief.md), with raw notes in [docs/research/notes/](docs/research/notes/)

## How it works

1. Your agent asks if you know your four letters, or plays a quick quiz with you ("I was sad, so I bought bread." Do you ask *why* or *what bread*?).
2. It tells you your type, your colour, and how your type is said out loud in Korea.
3. It shows you three replies to the same message, unlabelled, and asks which one you'd rather get.
4. It reveals who wrote each, explains the chemistry with your pick, and switches to that persona.
5. It tells you how to make the persona stick on your platform, and offers to sum you up in one word.

## Trademarks

MBTI, Myers-Briggs and Myers-Briggs Type Indicator are trademarks or registered trademarks of The Myers & Briggs Foundation, Inc. This project is not affiliated with, sponsored by or endorsed by The Myers & Briggs Foundation or The Myers-Briggs Company. It does not include or reproduce the MBTI® assessment; four-letter type codes such as INTJ are used descriptively.

Other names mentioned in this repo (including 16Personalities, DiSC, Insights Discovery, Lumina Spark and True Colors) belong to their respective owners and are referenced for identification only. Persona names and descriptions in this project are original.

## Licence

[Apache-2.0](LICENSE).
