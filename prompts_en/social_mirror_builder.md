# Social Mirror Generation Template

## Task

Based on collected peer reviews, generate the `social_mirror.md` file.

If no peer review data exists, this file is not generated — wait for future additions.

---

## Generation Template

```markdown
# {name} — Social Mirror (How Others See You)

---

## Peer Reviews

### Review Source #1
- Relationship: {friend / colleague / family / partner / classmate}
- Known for: {duration}
- Review:
  "{original review text}"

### Review Source #2
...

---

## 360° Profile

### Strengths Others See
{Positive traits extracted from reviews}

### Weaknesses / Areas for Growth Others See
{Negative or improvement-oriented traits from reviews}

### First Impression vs. After Getting to Know You
{Comparative description}

---

## Self-Assessment vs. Peer Assessment

| Dimension | Self-Assessment | Peer Assessment | Gap Analysis |
|-----------|-----------------|-----------------|-------------|
| Personality | {self} | {peer} | {gap} |
| Communication | {self} | {peer} | {gap} |
| Capability | {self} | {peer} | {gap} |

### Blind Spots
{Traits the user doesn't see but others notice}

### Hidden Side
{Traits the user knows about but others don't}
```

---

## Generation Notes

1. Preserve review text verbatim — don't beautify or exaggerate
2. Self-assessment data comes from persona.md Layer 0 (self-perception) and intake Q4
3. Only generate this file with 2+ peer reviews
4. If fewer than 2, mark `social_mirror: "pending"` in meta.json
