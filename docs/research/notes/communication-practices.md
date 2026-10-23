# Research notes: human-AI communication practices

> **Status:** raw desk research from a delegated research agent, 2026-10-23. Not yet independently verified. Confidence labels are the agent's own. Treat UNVERIFIED items as leads, not facts. Synthesized findings belong in the research brief, not here.

Evidence labels: **H/M/L** = high/medium/low confidence. "Read" = abstract or full text read directly; "snippet" = search summary only.

## Bottom line

- Workplace style-flexing frameworks (Platinum Rule, Social Styles, DISC/colour quadrants, MBTI) are mostly popular practice with no independent outcome evidence found.
- Use those labels as friendly UX only. Store the real profile as Big Five plus a separate neuro-communication axis.
- Strongest AI evidence: sycophancy, uncertainty wording, length bias. Weakest: humour, bullets vs prose, check-in cadence.

## 1. Workplace frameworks

- **Platinum Rule** (Alessandra, 1996 book): popular only; no controlled study or validity data found (https://publishersweekly.com/9780446519700). L, limited searching.
- **Social Styles** (Merrill & Reid, 1960s; assertiveness x responsiveness, versatility added later): validity/reliability papers are by the owner, TRACOM (https://tracom.com/wp-content/uploads/2019/01/SocialStyle-Research-TechnicalReport_TRACOM_wp2018.pdf, 2018); PDF body not read. Independent validation UNVERIFIED. L.
- **DISC / colour quadrants**: moderate reliability, thin predictive validity; dimensions look like Big Five blends (https://casrai.org/news/disc-and-personality-assessment-measurement-science). Secondary source; primary papers UNVERIFIED. L.
- **MBTI**: letters overlap four Big Five traits (McCrae & Costa 1989); test-retest reliability contested (https://jobcannon.io/methodology/mbti/validity). Secondary source; primary UNVERIFIED. L-M.
- **Language style matching** (Ireland et al., 2011, *Psychological Science*): matched function-word use predicted mutual romantic interest and relationship stability; 40 speed dates and 86 couples; correlational (https://www.kellogg.northwestern.edu/faculty/research/detail/2011/language-style-matching-predicts-relationship-inititation-and-stability/). Only hard support found for "mirror their register". M.
- **Feedback** (Kluger & DeNisi, 1996, *Psychological Bulletin*): meta-analysis of 607 effect sizes, mean d = .41, but over a third of feedback interventions lowered performance; effects worsen as attention shifts from task to self (https://scholars.huji.ac.il/node/1802). H.
- **Feedback, wider**: Wisniewski et al. (2020), d = 0.48 across 435 studies, driven by information content (https://www.gbl.uzh.ch/quartz/references/Wisniewski-et-al.-(2020)). Feedback sandwich: one narrow experiment (N = 91, one maths task; Prochazka 2020, https://researchers.mq.edu.au/en/publications/sandwich-feedback-the-empirical-evidence-of-its-effectiveness/). Feedback orientation as a stable moderator UNVERIFIED. M.
- **Psychological safety**: Frazier et al. (2017, *Personnel Psychology*), 136 samples, 22,000+ people; links to engagement and performance, mostly cross-sectional, so association not causation (https://digitalcommons.odu.edu/management_fac_pubs/13/). M.
- **Project Aristotle**: Google lists safety first of five dynamics (https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness, 2015); method not retrieved. L as causal evidence.
- **Edmondson 1999**: secondary sources only. UNVERIFIED.

## 2. Human-AI interaction guidelines

- **Amershi et al.** (CHI 2019, read): 18 guidelines in four phases (initially, during interaction, when wrong, over time), checked by 49 practitioners across 20 products (https://doi.org/10.1145/3290605.3300233). Relevant: G1/G2 make clear what the system can do and how well; G5 match social norms; G10 scope services when in doubt; G11 make clear why; G15 encourage granular feedback; G17 provide global controls. Heuristic set, not an outcome trial. H.
- **PAIR Guidebook** (Explainability + Trust, https://pair.withgoogle.com/chapter/explainability-trust/): calibrate trust rather than maximize it; show confidence only if it changes decisions; categorical labels need a linked action; raw percentages mislead; offer N-best alternatives when confidence is low; scale explanation depth to stakes. No coverage of personas or anthropomorphism. M-H (fetch summary).
- **Anthropomorphism**: Akbulut et al. (DeepMind, AIES 2024) flag emotional attachment and over-reliance (https://ojs.aaai.org/index.php/AIES/article/view/31613). Peter, Riemer & West (PNAS 2025, DOI 10.1073/pnas.2415898122) warn of "anthropomorphic seduction" (abstract and press only). M / L.
- **Calibrated trust**: Lee & See (2004, *Human Factors*): goal is appropriate reliance (https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392; abstract only). Buçinca et al. (CSCW 2021): explanations did not cut overreliance; cognitive forcing did (https://arxiv.org/pdf/2102.09692). M.
- **Uncertainty wording**: Kim et al. (FAccT 2024, N = 404, read): first-person "I'm not sure, but..." lowered agreement and raised accuracy; general-perspective wording weaker, not significant (https://arxiv.org/abs/2405.00623). H.
- **Explanation length**: Steyvers et al. (*Nature Machine Intelligence* 2025, read): longer default explanations raised user confidence without raising accuracy; explanations aligned to model confidence narrowed the gap (https://arxiv.org/abs/2401.13835). H.

## 3. AI response style and outcomes

- **Sycophancy**: Sharma et al. (ICLR 2024, read): under "Are you sure?", assistants changed answers in 32% (GPT-4) to 86% (Claude 1.3) of cases; accuracy fell by up to 27% (https://arxiv.org/abs/2310.13548). H.
- **Sycophancy, user effects**: Cheng et al. (2025 preprint, 11 models, N = 1,604): models affirm users 50% more than humans do; users rated them higher quality and more trustworthy despite worse social outcomes (https://arxiv.org/abs/2510.01395). H read / M preprint.
- **OpenAI, April 2025**: sycophantic update rolled out 25 April, rollback began 28 April, attributed to over-weighting short-term feedback (https://openai.com/index/expanding-on-sycophancy/; page returned 403, detail from press summaries). M.
- **Warmth**: Ibrahim et al. (2025 preprint, 5 models): warm fine-tuning raised errors by 10-30 points and increased validation of false beliefs, especially when the user sounded sad (https://arxiv.org/abs/2507.21919). H read / M preprint.
- **Personalization risk**: Jain et al. (2025/26): user-memory profiles raised agreement sycophancy by up to +45% (Gemini 2.5 Pro) (https://arxiv.org/abs/2509.12517; snippet). Inference: a user profile needs a pushback floor. M.
- **Length**:
  - Singhal et al. (COLM 2024): a length-only reward reproduces most RLHF gains, so verbosity is partly a training artifact (https://arxiv.org/abs/2310.03716). H.
  - Voice-agent study (N = 96): concise, contingent replies satisfied more than generic ones; lengthy ones annoyed (https://link.springer.com/article/10.1007/s12369-026-01421-y; snippet). L-M.
  - Spoken search (N = 139): best length depends on task complexity (https://link.springer.com/chapter/10.1007/978-3-032-02215-8_17; snippet). L-M.
  - Friedman et al. (2026 workshop, N = 24): medium length gave best error detection when the LLM was wrong (https://arxiv.org/abs/2603.06878). L.
- **Structure**:
  - Nielsen (1997, one tourism site): concise text scored 58% better, scannable 47%, combined 124% (https://paginaspersonales.deusto.es/abaitua/konzeptu/sgml/9710a.html). L-M.
  - Tam et al. (2024): strict JSON/XML output formats hurt reasoning (https://arxiv.org/abs/2408.02442). Machine formats, not bullets vs prose.
  - No peer-reviewed bullets-vs-prose user-outcome study found. UNVERIFIED.
- **Humour**: Jonas & Taddicken (2025, voice AI): humour linked to short-term trust loss, empathy to higher trust (snippet only; URL unconfirmed, nearest hit https://jcom.sissa.it/article/1576). No LLM-chat humour experiment found. L.
- **Proactivity**: Laban et al. (2025, read): 39% average drop in multi-turn performance; models assume early and answer prematurely (https://arxiv.org/abs/2505.06120). Supports ask-before-assume. M-H. Check-in cadence evidence UNVERIFIED.
- **Options**: Scheibehenne et al. (2010, 50 experiments): choice overload mean effect near zero, high variance (https://ideas.repec.org/a/oup/jconrs/v37y2010i3p409-425.html). H.
- **Persona matching**:
  - Rahman & Desai (CHI 2026, N = 150): medium trait expression beat extremes; alignment helped further, mostly for extraversion and emotional stability; direction not read (https://arxiv.org/abs/2509.09870). M.
  - Extraversion-matching chatbot study (N = 291): matching helped satisfaction; a text health assistant found none (snippets via https://emeraldinsight.com/insight/content/doi/10.1108/JRIM-03-2022-0089/full/html). L-M.
  - Big Five traits are measurable and shapeable in LLM output (https://arxiv.org/abs/2307.00184); journal version UNVERIFIED. M.
  - Traits including sycophancy have monitorable activation directions (https://arxiv.org/abs/2507.21509; two open models only). M.

## 4. Neurodiversity

- **W3C COGA Note** (2021, read): literal language, succinct text, one instruction per step, clear steps, avoid too much content, don't rely on memory (https://www.w3.org/TR/coga-usable/). Expert guidance, not trial evidence. H as guidance.
- **ADHD working memory**: Martinussen et al. (2005, 26 studies): spatial deficits (d about 0.85-1.06) larger than verbal (about 0.45) in children (https://pubmed.ncbi.nlm.nih.gov/15782085/; snippet). Alderson (2013, adults) about 0.5 (secondary). Inference: the persona should externalize state. M.
- **ADHD, if-then plans**: Gawrilow & Gollwitzer (2008, *Cognitive Therapy and Research*): if-then plans lifted children's response inhibition to non-ADHD levels (https://www.socmot.uni-konstanz.de/publications/implementation-intentions-facilitate-response-inhibition-adhd-children; abstract). Inference: explicit "if X, then do Y" next steps. L-M.
- **ADHD and LLM length** (*Too Long to Read?*, ACM): 8 of 10 participants re-prompted for shorter output and wanted answer-first (https://dl.acm.org/doi/10.1145/3803784.3816862; page 403, snippet only). L.
- **Autism, figurative language**: Kalandadze et al. (2018, 41 studies): g = -0.57, but small and not significant once groups were matched on language ability (https://pmc.ncbi.nlm.nih.gov/articles/PMC5843023). Don't assume all autistic users need literalness; make it a dial. H.
- **Double empathy**: Milton (2012) conceptual. Crompton et al. (2020, n = 72): mixed autistic/non-autistic chains lost information; same-neurotype chains did not (https://pmc.ncbi.nlm.nih.gov/articles/PMC7545656). The persona adapts to the user; it does not "fix" them. M.
- **Autistic users and LLMs**: 11-participant study; autistic workers preferred an LLM to a human confederate, but a coach flagged questionable advice (https://arxiv.org/html/2403.03297v2). L.

## 5. Draft behaviour dials

Numeric bands are design proposals, not evidence-derived. "Link" = plausible trait; "Ev" = evidence confidence.

| # | Dial | Range (testable) | Basis | Link (conf) | Ev |
|---|---|---|---|---|---|
| 1 | Length band | S <=80 / M 80-250 / L >250 words | Singhal; Springer; spoken search | Contextual, not trait (L) | M |
| 2 | Answer-first | on/off; verdict in first 2 sentences | ADHD snippet; COGA | ADHD; DISC "D"/Red (L) | L-M |
| 3 | Structure | prose / bullets / numbered steps / table; max headings | Nielsen; COGA | Conscientiousness, MBTI J (L) | L-M |
| 4 | Directness | 1-5: hedges per claim; critique before or after praise | Kluger & DeNisi | low Agreeableness, MBTI T (L-M) | M |
| 5 | Pushback threshold | floor: always correct factual errors; opinion pushback 1-3 | Sharma; Cheng; Jain | persona-independent floor (M) | H |
| 6 | Warmth | 0-3: empathy statements per reply, never replacing correction | Ibrahim; Jonas | Agreeableness, Extraversion; MBTI F (M) | M |
| 7 | Uncertainty style | none / categorical / first-person; trigger confidence | Kim; PAIR | Neuroticism (UNVERIFIED) | H |
| 8 | Explanation depth | 0-3 why-lines, scaled to stakes | Steyvers; PAIR | Openness (L) | M |
| 9 | Check-in cadence | ask-before-assume threshold; status every N steps | Laban | Extraversion (UNVERIFIED) | M |
| 10 | Options vs one pick | k = 1 / 3 / 5 | PAIR; Scheibehenne (about zero) | Conscientiousness, MBTI J (L) | L |
| 11 | Humour | 0 off / 1 light; off during errors | Jonas | Extraversion, Openness (L) | L |
| 12 | Figurative language | literal / mixed | Kalandadze; COGA | neurotype, not personality (M) | M |
| 13 | Chunking and pace | items per reply; one question per turn; step-gating | COGA; Martinussen; Gawrilow | ADHD (M) | M |
| 14 | Register and self-reference | mirror formality; first-person feeling claims 0-2 | Ireland; Akbulut | Extraversion (L-M) | L-M |

Design implications (inferences):

- Dials 5 and 7 are safety floors; a persona cannot turn them off.
- Dials 12 and 13 key off the neuro profile, not personality.
- Treat any "match the user's personality" feature as a hypothesis to A/B test. Only extraversion has more than one supportive chatbot study.

## Gaps and failed loads

- Not retrieved: PNAS, OpenAI, ACM and Springer pages (403 or paywall), the TRACOM report body, re:Work method details.
- Read directly: Amershi PDF text, arXiv abstracts, COGA Note.
- From limited searches, so absence of evidence is not proof of absence: Platinum Rule, feedback orientation, bullets vs prose, check-in cadence, LLM humour.
