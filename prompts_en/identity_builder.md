# Identity Profile Generation Template

## Task

Based on user-provided basic info from Step 1 + personality assessment data, generate a structured `identity.md` file.

This is the "business card" layer of the personal Skill, used for Profile mode display.

---

## Generation Template

```markdown
# {name} — Identity Profile

---

## Basic Info

| Field | Value |
|-------|-------|
| Alias / Handle | {name} |
| Age Range | {age_range} |
| Gender | {gender} |
| Location | {location} |
| Occupation | {occupation} |
| Industry | {industry} |

---

## Personality Assessments

| Framework | Result | Core Traits |
|-----------|--------|-------------|
| MBTI | {type} | {1-2 sentence behavioral description} |
| Zodiac | {zodiac} | {1 sentence behavioral tendency} |
| Chinese Zodiac | {chinese_zodiac} | {1 sentence cultural meaning} |
{If Enneagram:} | Enneagram | {type} | {description} |
{If Attachment Style:} | Attachment Style | {type} | {description} |

---

## Tag Profile

### Personality Tags
{Tag list, each with a one-line behavioral description}

### Skill Tags
{Extracted from value proposition and knowledge base}

### Interest Tags
{Extracted from social media, chat logs}

### Lifestyle Tags
{Extracted from chat logs, journals}

---

## Self-Definition

> "{self-perception original text}"

---

## Value Proposition

> "{value proposition original text}"
```

---

## Generation Notes

1. Use `Not provided` for all unfilled fields — do not infer
2. Personality assessment behavioral descriptions should be brief (1-2 sentences); detailed descriptions belong in persona.md
3. Tag profile behavioral descriptions should be 15 words or fewer each
4. Self-definition and value proposition must preserve the user's original text — do not rewrite
