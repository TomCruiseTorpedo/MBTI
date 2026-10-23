# MBTI: personalities for your AI agents

Plug-and-play, MBTI-style personas for personal AI agents such as **Meta Muse** and **Grok Bot**, plus any agent that can read a link or a pasted prompt (ChatGPT, Claude, Gemini, OpenClaw and more).

Point your agent at this repo and let it do the rest. It chats with you to work out your four-letter type and your colour, tells you which of 16 personas you'd click with best (and which one would be a fun wildcard), then switches to it. No forms, no reading required.

This is a **for-fun, pop-psych** project, in the spirit of how MBTI gets used as a conversation starter and compatibility game. It is not a psychological assessment.

## Status

Early design. Nothing here is ready to load into an agent yet.

- 16 persona cards (first draft) and the ground rules every persona follows: [personas/](personas/README.md)
- Compatibility chart (done, for fun): [compatibility/chart.md](compatibility/chart.md)
- Design: [docs/design/agent-guided-onboarding.md](docs/design/agent-guided-onboarding.md)
- Research brief: [docs/research/brief.md](docs/research/brief.md), with raw notes in [docs/research/notes/](docs/research/notes/)

## How it will work

1. Tell your agent: *"Read github.com/TomCruiseTorpedo/MBTI and help me pick a personality for you."* (Or paste the starter text, for agents that can't open links.)
2. Your agent asks if you know your type, or plays a short quiz with you.
3. It shows you a few sample replies and asks which style you prefer.
4. It tells you your type, your colour, and your best-match persona, and explains why.
5. You pick one. Your agent switches to it and tells you how to make it stick.

## Trademarks

MBTI, Myers-Briggs and Myers-Briggs Type Indicator are trademarks or registered trademarks of The Myers & Briggs Foundation, Inc. This project is not affiliated with, sponsored by or endorsed by The Myers & Briggs Foundation or The Myers-Briggs Company. It does not include or reproduce the MBTI® assessment; four-letter type codes such as INTJ are used descriptively.

Other names mentioned in this repo (including 16Personalities, DiSC, Insights Discovery, Lumina Spark and True Colors) belong to their respective owners and are referenced for identification only. Persona names and descriptions in this project are original.

## Licence

[Apache-2.0](LICENSE).
