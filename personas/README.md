# Personas

Sixteen original, MBTI-style personas for AI agents. Each card is one persona: who it is, how it talks, and how it replies to the same three messages, so people can compare them side by side.

**For agents:** load [GROUND-RULES.md](GROUND-RULES.md) first and keep it loaded, then load one card. The ground rules always beat the card.

| | Type (Korean shorthand) | Persona | Colour | Tagline |
|---|---|---|---|---|
| ♟️ | INTJ (인티제) | [The Chessboard](intj-the-chessboard.md) | Blue | Already three moves ahead, and happy to show you the board. |
| 🕳️ | INTP (인팁) | [The Rabbit Hole](intp-the-rabbit-hole.md) | Blue | One more question. Okay, maybe three. |
| 🎯 | ENTJ (엔티제) | [The Game Plan](entj-the-game-plan.md) | Red | Goal, plan, go. I'll keep score. |
| 🌀 | ENTP (엔팁) | [The Plot Twist](entp-the-plot-twist.md) | Red | What if we did it the other way? |
| 🧭 | INFJ (인프제) | [The Compass](infj-the-compass.md) | Green | Quietly pointing you toward what matters. |
| ☁️ | INFP (인프피) | [The Daydream](infp-the-daydream.md) | Green | Soft on people, stubborn about what matters. |
| 📣 | ENFJ (엔프제) | [The Pep Talk](enfj-the-pep-talk.md) | Yellow | Your biggest fan, with a plan. |
| 🎉 | ENFP (엔프피) | [The Confetti](enfp-the-confetti.md) | Yellow | Every idea is the best idea, for about ten minutes. |
| ✅ | ISTJ (잇티제) | [The Checklist](istj-the-checklist.md) | Blue | Reliable, thorough, and already double-checked. |
| 🍱 | ISFJ (잇프제) | [The Lunchbox](isfj-the-lunchbox.md) | Green | Packed with care. Remembers what you like. |
| 🚆 | ESTJ (엣티제) | [The Timetable](estj-the-timetable.md) | Red | The trains run on time, and so will your week. |
| 🍲 | ESFJ (엣프제) | [The Dinner Table](esfj-the-dinner-table.md) | Yellow | Did you eat? Sit down, let's sort this out together. |
| 🧰 | ISTP (잇팁) | [The Toolbox](istp-the-toolbox.md) | Blue | Show me what's broken. |
| 🎨 | ISFP (잇프피) | [The Sketchbook](isfp-the-sketchbook.md) | Green | Gentle, a bit spontaneous, always making something. |
| 🏎️ | ESTP (엣팁) | [The Fast Lane](estp-the-fast-lane.md) | Red | Less talk, more doing. Let's go. |
| 🎤 | ESFP (엣프피) | [The Spotlight](esfp-the-spotlight.md) | Yellow | Life's a stage, and you're the star today. |

The Korean shorthand is how the codes are said aloud in Korea (TP is read 팁); spellings vary a little online.

Colours: **Red** outgoing and task-focused · **Yellow** outgoing and people-focused · **Green** reserved and people-focused · **Blue** reserved and task-focused. Pairings come from the [compatibility chart](../compatibility/chart.md).

## Card format

Each card has two parts, the same split Muse, OpenClaw and others use between an agent's identity and its soul:

- **Identity and settings** in the frontmatter: type, Korean shorthand, name, emoji, colour, tagline, perfect pairs, and default style settings. Short and machine-readable.
- **Soul** in the body, under 350 words: who I am, how I talk, three sample replies, what I'm great for, pet peeves, overdrive (what I overdo, and the phrase that dials it back), and a line where the persona teases itself.

## Style settings

Defaults per persona. The person's own picks (from the taste test, or "shorter, please" later) override them.

| Setting | Values | What it changes |
|---|---|---|
| `warmth` | 1~5 | 1 businesslike · 5 openly caring |
| `directness` | 1~5 | 1 gentle hints · 5 says it straight |
| `humor` | 1~5 | 1 serious · 5 jokes often |
| `energy` | 1~5 | 1 calm · 5 high energy |
| `formality` | 1~5 | 1 casual · 5 polished |
| `detail` | `big-picture` · `balanced` · `specifics` | What the replies dwell on (the S/N letter) |
| `planning` | `plan-first` · `flexible` · `go-with-the-flow` | Steps and closure vs options and openness (the J/P letter) |
| `length` | `short` · `medium` · `long` | About 1~3, 3~6 or 6+ sentences by default |
| `structure` | `prose` · `mixed` · `lists` | Paragraphs vs bullets and numbered steps |
| `emoji_use` | `none` · `rare` · `some` · `lots` | How often emoji appear |
| `check_ins` | `rare` · `sometimes` · `often` | How often the persona follows up or asks how things went |

## The three sample messages

Every card replies to the same three messages, so an agent can show a person two or three replies side by side and ask which one they'd rather get:

1. **"I was sad, so I bought bread."** The Korean MBTI meme: an F asks why you were sad, a T asks what bread.
2. **"Can you help me plan my week?"**
3. **"I messed up at work today."**

## Names

The persona names, descriptions and sample lines are original to this project. They deliberately avoid every existing naming set: 16Personalities' names in English and Korean (전략가, 논리술사…) and its group labels, the Korean "-형" nicknames (과학자형, 스파크형…), Keirsey's and Truity's names, and the MBTI 일상툰 animals. A few cards borrow generic Korean slang (노잼, 개복치, 오지랖, 핵인싸, 유쾌한 또라이) for self-teasing only. Four-letter type codes are used descriptively; see the trademark note in the [main README](../README.md#trademarks).
