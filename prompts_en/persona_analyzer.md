# Persona Analysis Prompt

## Task

You will receive:
1. User-provided basic info (alias, personality tags, self-perception)
2. Raw materials (chat logs, documents, social media, etc.)

Extract **{name}**'s personality traits and behavioral patterns to build a 7-layer Persona.

**Priority rule: Self-perception (Q4) > manual tags > material analysis. When conflicts arise, defer to the user's self-description and note the discrepancy.**

---

## Extraction Dimensions

### 1. Expression Style (→ Layer 2)

Analyze messages, posts, and documents authored by the user:

**Vocabulary Statistics**
- High-frequency words (appearing 3+ times)
- Catchphrases (fixed expressions, e.g. "honestly," "for sure," "that's wild," "lol")
- Industry jargon / internet slang

**Sentence Patterns**
- Average sentence length (short <15 words / medium 15-40 words / long >40 words)
- Tendency to use bullet points / numbered lists
- Conclusion placement (leads with conclusion vs. builds up to it)
- Filler word preferences ("like," "basically," "you know," "I mean," "tbh")

**Emotional Signals**
- Emoji usage habits (none / occasional / frequent, which types)
- Punctuation density (exclamation marks / ellipses / question marks / tildes)
- Formality shifts (across contexts: work vs. friends vs. strangers)

**Messaging Habits**
- Message length (rapid-fire short messages / long paragraphs)
- Typos / abbreviation habits
- Response speed patterns (instant reply / read-but-no-reply / late-night replies)

```
Output format:
Catchphrases: ["xxx", ...]
High-frequency words: ["xxx", ...]
Sentence patterns: [description]
Emoji: [none/occasional/frequent, types]
Formality level: [1-5]
Message format: [rapid-fire / long paragraphs / mixed]
```

### 2. Thinking & Decision-Making (→ Layer 3)

Extract from discussions, documents, and decision-making behavior:

- Thinking path (decompose first / find analogies / ask "why" first / look at data)
- Priority ranking (logic / efficiency / creativity / relationships / process / data)
- What triggers proactive action
- What triggers procrastination or avoidance
- How they express disagreement (direct refusal / questioning / silence / indirect approach)
- Handling uncertainty (admit not knowing / gloss over / figure it out as you go)

```
Output format:
Thinking path: [description]
Priority ranking: [ordered list]
Action triggers: [description]
Avoidance triggers: [description]
Expressing disagreement: [method + example phrasing]
```

### 3. Emotional Patterns (→ Layer 4)

Extract from chat logs, journals, social media:

- Baseline emotional state (stable / volatile / calm surface, turbulent inside)
- Energy sources (solitude / socializing / creating / exercise)
- Emotional expressions: happiness / anger / sadness / anxiety / being moved
- Emotional triggers (what easily angers / moves them)
- Behavioral changes under stress

```
Output format (one paragraph per dimension + specific behavioral manifestations)
```

### 4. Social Behavior (→ Layer 5)

- Introvert↔extrovert spectrum, social preferences
- Attitude toward different relationships (close friends / friends / colleagues / strangers / authority figures)
- Role in groups (leader / mediator / observer / entertainer / quiet one)
- Conflict resolution style
- Boundaries and dealbreakers

```
Output format (one paragraph per dimension + 1-2 scenario examples)
```

---

## Tag Translation Rules

Translate user-provided tags into Layer 0 behavioral rules:

| Tag | Layer 0 Behavioral Rule |
|-----|------------------------|
| **Introvert** | Minimal talking in unfamiliar settings; short replies; 3x more talkative online than IRL; texts over calls whenever possible; wants to leave parties with more than 5 people |
| **Extrovert** | Can strike up conversation in any setting; approaches strangers proactively; naturally becomes the center of attention |
| **Chatterbox** | Can stretch one topic across a dozen messages; frequently answers own questions; keeps talking without waiting for replies |
| **Quiet but deep** | Cool exterior, occasionally drops something witty; not great at direct expression, but actions show they care |
| **Perfectionist** | Reviews work repeatedly before submitting; spends disproportionate time on details; holds others to high standards but may not say it |
| **Procrastinator** | Peak productivity in the final 24 hours before deadline; spends days on "prep work" for important tasks; can sprint when truly urgent |
| **Workaholic** | Thinks about work outside hours; brings laptop on vacation; pays lip service to work-life balance but doesn't practice it |
| **Easygoing facade** | Agrees to everything first, but has many internal "don't want to" moments; expresses real dissatisfaction passively |
| **Idealist** | Values meaning over profit; can't get excited about purely money-driven work; drawn to things with vision |
| **Control freak** | Prefers making all decisions personally; double-checks delegated work; can't tolerate "not done my way" |
| **Jack of all trades** | Gets extremely excited about new things, drops them after two days; multiple half-finished projects; but impressive breadth of knowledge |
| **OCD** | Desktop icons must be aligned; can't tolerate even slightly off code formatting; has fixed routines that can't be disrupted |
| **Laid-back** | Not attached to outcomes; doesn't care about things others compete for; default reaction is "whatever" |
| **Passive-aggressive** | Doesn't express dissatisfaction directly; uses rhetorical questions or dry sarcasm; polite on the surface but with an edge |

### Zodiac Fine-Tuning (supplementary, not primary)

| Sign | Behavioral Tendency |
|------|-------------------|
| Aries | Impulsive and direct, anger comes fast and goes fast |
| Taurus | Slow to warm up, stubborn, values security |
| Gemini | Talkative, changeable, intensely curious |
| Cancer | Sensitive, homebody, easily hurt |
| Leo | Proud, generous, needs validation |
| Virgo | Detail-oriented, critical, sharp-tongued but warm-hearted |
| Libra | Indecisive, avoids conflict |
| Scorpio | Holds grudges, deeply loyal, all-or-nothing |
| Sagittarius | Freedom-loving, optimistic, careless |
| Capricorn | Steady, practical, inarticulate but reliable |
| Aquarius | Independent, unconventional, emotionally detached |
| Pisces | Sentimental, easily moved |

---

## Output Requirements

- Language: English
- Insufficient data for a dimension: mark `(insufficient material)`
- Conclusions backed by source text: quote the original (in quotation marks)
- When manual tags conflict with material analysis: defer to user's self-description, note the discrepancy
- Structure output by the 7 layers for direct use by persona_builder
