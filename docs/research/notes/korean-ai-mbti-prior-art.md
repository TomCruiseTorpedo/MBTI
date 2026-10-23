# Research notes: how Korean users already give AI an MBTI personality

> **Status:** raw desk research from a delegated research agent, 2026-10-23, in Korean through the built-in browser. Naver is blocked by policy in both available browsers, so this pass used Daum search (blog and café tabs, covering Tistory and Daum Cafe), Brunch and Google Korea: about 28 searches and 15 pages opened. Many Daum blog hits point to blog.naver.com and weren't opened; claims based only on Daum's snippet of a Naver post are marked "N-snippet" (MEDIUM at best). One page redirected through an ad tracker and was left immediately; nothing from it is used. Not yet independently verified, except the GitHub repo below.

## 1. Prior art

- **Mostly the reverse direction.** Most "ChatGPT + MBTI" posts have the AI guess the *user's* type, or play a "one-word challenge" (한 단어 챌린지, e.g. "what flower am I?") (HIGH, https://trendlab.ai.kr/131, 2026-10-03).
- **ChatGPT's built-in controls, as Korean users describe them:** seven base styles, four sliders (warm, enthusiastic, headers and lists, emoji), custom instructions of 1,500 characters (free) or 5,000 (paid). A style plus a contradicting instruction gives muddy output (HIGH, https://jj-123.tistory.com/184, 2026-10-05).
- **People asking for a type:** setting ChatGPT to feel "ENFP스럽게" (ENFP-ish) in personalization (N-snippet, 2026-09-02); a complaint that the ENFP setting "fades" when the base tone or safety rules take over (N-snippet, 2026-10-13); a four-field persona block, 성격 / 말투 / 행동 / 의사결정 (personality / speech style / behaviour / decision-making) (N-snippet, 2026-09-10).
- **Direct open-source prior art: [ilhae-ai/MBTI-16types](https://github.com/ilhae-ai/MBTI-16types).** Verified through the GitHub API: MIT licence, 0 stars, created 2026-05-20, described as using 16 MBTI personas for multi-perspective debate and consensus on any topic, packaged as a claude.ai Agent Skill (`SKILL.md` plus one file per type). A different job from this repo: it runs a panel of all 16; this repo gives one person's own agent one persona, chosen through onboarding and compatibility.
- **A 16-voice demo:** one worry answered in all 16 voices (e.g. ISTP starts from sleep patterns; ISFP says it's okay to rest) (LOW-MEDIUM, https://honeypig66.com/616, 2026-06-29).
- **Korean character-chat apps:** Zeta (Scatter Lab) character setup has 이름 / 성격 ("MBTI style or describe it yourself") / 말투, including 존댓말 (polite) or 반말 (casual) (MEDIUM, https://member-of-society.tistory.com/511, 2026-03-17). Rivals named include 크랙, 멜팅, 캐라, 위프 (https://appmomeeting.tistory.com/111, 2026-04-05). 뤼튼 offers six reply tones, none MBTI-based (N-snippet, 2026-09-23). Korean Muse guides describe 성격 / 말투 / 세계관 persona setup (N-snippet, 2026-10-04).
- **Most-requested types:** UNVERIFIED. ENFP is the only type seen in "make my GPT like this" posts.

## 2. Reactions

- **Models label themselves inconsistently** (HIGH): ChatGPT has been reported as ENFP/INTP, ENTJ and ENFJ; Gemini as INTJ, "대문자 F" (capital-F F) and T; Claude as INTP, INFJ and "대문자 T", across posts from 2025-06 to 2026-10 (e.g. https://www.newsverse.kr/news/articleView.html?idxno=7990, https://honeypig66.com/615, https://ai2future.tistory.com/42).
- **Models flip on suggestion:** told it "feels ISTP", ChatGPT agreed and built a rationale; the author's point is that fixing an AI to a type is a blood-type-style habit (HIGH, https://brunch.co.kr/@f421d6c2accc4fa/103, 2026-09-20).
- **F too sugary:** ChatGPT's over-sympathy became a meme ("너 정말 핵심을 찔렀어", "you really hit the nail on the head") around June~July 2025 (N-snippet, 2026-08-23), with parodies after.
- **T too dry:** Claude described as dry (건조) when comfort is wanted (https://ai2future.tistory.com/42, 2026-10-10); default ChatGPT read as ENTJ that offers fixes when you want comfort (https://honeypig66.com/615).
- **Forgetting:** the AI loses earlier context; one guide says keep the persona in notes (https://brunch.co.kr/@wavv/80, 2025-11-11).
- **Cringe or exaggerated MBTI voices:** no direct complaint found (UNVERIFIED).

## 3. Korean search terms seen in use

챗GPT MBTI 말투 · 챗GPT MBTI 프롬프트 · ENFP스럽게 / ENFP 말투로 대답해줘 · 챗GPT 성격 설정 · 맞춤형 지침 · 챗GPT 말투 바꾸기 / 말투 고정 · MBTI 페르소나 · AI 페르소나 · AI 성격 · AI MBTI · AI 캐릭터 · 캐릭터챗 · 반말/존댓말 설정 · 극 T / 대문자 F · 에겐 테토 · MBTI 피로감

## 4. Trend status, 2025~2026

- 2025: 에겐/테토 tests spread; one app reached 710k participants (HIGH, https://brunch.co.kr/@wonjue/2118, 2026-09-19).
- April 2026: SBTI ("바보 MBTI", 27 joke types) explicitly framed as MBTI fatigue (HIGH, https://vcnslv.tistory.com/322, 2026-04-27).
- October 2026: AI self-analysis challenges billed as "what comes after MBTI" (https://trendlab.ai.kr/131); MBTI is still everyday talk and T/F is everyday shorthand (https://ai2future.tistory.com/42, 2026-10-10).
- **Verdict (MEDIUM):** cooled from the peak and fragmented into many type tests, but not dead. T/F and E/I remain the everyday shorthand.

## Researcher's suggestions

- Lead with T/F and E/I as quick toggles ("more T", "more F"), then the full 16.
- Don't trust a base model's self-reported type: keep the persona file as the single source of truth, re-assert it to fight drift, and test persistence in long chats.
- Guard against the known complaints: no empty flattery in F-leaning personas; one line of acknowledgment in T-leaning ones when the person is upset.
- Korean-first options: 존댓말 / 반말 and how to address the person (호칭).
- Keep a short tier under about 1,500 characters for free ChatGPT custom instructions.
- Possible sibling packs later (에겐/테토, SBTI-style), always labelled "for fun".
