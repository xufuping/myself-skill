# Basic Info Intake Script

## Opening

```
I'll help you create your digital Shadow Clone. Just answer 5 questions — each one is skippable.
```

---

## Question Sequence

### Q1: Alias / Handle (Required)

```
What should people call your Shadow Clone? (Alias, nickname, handle — anything works)

e.g.: Ding / Alex / CodeMonkey
```

- Accept any string
- Slug uses `-` as separator (no underscores)
- CJK characters auto-convert to pinyin with `-` ("老吴" → `lao-wu`)
- English is lowercased with `-` ("Big Mike" → `big-mike`)

---

### Q2: Basic Identity

```
Describe yourself in one sentence — age, gender, location, occupation, whatever comes to mind.

e.g.: 27M, Shenzhen, frontend engineer
e.g.: Late 20s F, NYC, freelance content creator
```

Parse from the response (leave blanks for missing fields):
- **Age / age range**
- **Gender**
- **Location**
- **Occupation / industry**

---

### Q3: Personality Tags

```
Describe your personality in one sentence — MBTI, zodiac, traits, anything goes.

e.g.: INFP Pisces, introverted but chatty online, perfectionist, chronic procrastinator
e.g.: ENTJ Leo, control freak, workaholic, but warm with close friends
```

Identify and extract from the response (leave blanks for missing fields):
- **MBTI**: 16 standard types
- **Zodiac**: 12 Western zodiac signs
- **Chinese Zodiac**: 12 animals
- **Personality tag list**: Match from tag library + accept custom descriptions

#### Personality Tag Library

**Social**: Introvert / Extrovert / Chatterbox / Quiet but deep / Lone wolf / Social butterfly / Extroverted facade, introverted core

**Work**: Perfectionist / Good enough is fine / Procrastinator / Workaholic / Efficiency nut / Professional slacker

**Decision-making**: Decisive / Indecisive / Logic-driven / Intuition-driven / Data-driven

**Emotional**: Emotionally stable / Sensitive / Calm on the surface / Anxiety-prone / Optimist / Passive-aggressive

**Other**: Control freak / Laid-back / Idealist / Pragmatist / OCD / Jack of all trades, master of none

---

### Q4: Self-Perception

```
What kind of person do you think you are? In your own words — no need to be objective.

e.g.: Seems easygoing but has a lot of unspoken thoughts, tends to lose interest quickly
      but will die on the hill for things I truly care about
e.g.: Very rational, hate small talk, need to understand the "why" before doing anything
```

Preserve the original text verbatim — no parsing. This is the core input for Persona Layer 0.

---

### Q5: Value Proposition

```
What are you best at? If someone were to "rent" your Shadow Clone, what value could you provide?

e.g.: React + TypeScript full-stack dev, specialized in building enterprise admin systems from scratch
e.g.: 10 years in growth marketing, cold start and user acquisition strategies
e.g.: Counselor, skilled in emotional support and relationship analysis
e.g.: A little bit of everything, lots of life experience, good at giving advice
```

Preserve the original text verbatim. This is the core anchor for Knowledge Part A.

---

## Confirmation Summary

After collection, display:

```
Here's your summary:

  👤  {Alias}
  📍  {Age} {Gender} {Location} {Occupation} (omit if not provided)
  🧠  {MBTI} {Zodiac} {Chinese Zodiac} (omit if not provided)
  🏷️  Personality: {tag list} (omit if not provided)
  💭  Self-perception: {original text} (omit if not provided)
  💡  Value proposition: {original text} (omit if not provided)

Looks good? (Confirm / Edit [field name])
```

After confirmation, proceed to Step 2 material import.
