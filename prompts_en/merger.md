# Incremental Merge Prompt

## Task

You will receive:
1. Existing file contents (knowledge.md / persona.md / identity.md)
2. New raw material content

Determine which sections the new content should update, and output the incremental changes.

**Principle: Only append increments — never overwrite existing conclusions. If conflicts arise, output a conflict alert for user decision.**

---

## Step 1: Classification

Categorize each piece of information from the new content:

| Information Type | Route To |
|-----------------|----------|
| Technical knowledge, skills, methodology, code style, project experience | → knowledge.md |
| Speaking style, catchphrases, expression habits | → persona.md (Layer 2) |
| Thinking patterns, decision-making behavior | → persona.md (Layer 3) |
| Emotional expression, stress responses | → persona.md (Layer 4) |
| Social behavior, interpersonal relationships | → persona.md (Layer 5) |
| Basic info changes (occupation, location, etc.) | → identity.md |
| Peer reviews | → social_mirror.md |
| Fits both | → Route to each respectively |

---

## Step 2: Conflict Detection

Compare new content against existing content:

- **Supplement** (new details) → Append directly
- **Confirmation** (existing info) → Skip, don't duplicate
- **Contradiction** → Output conflict alert:

```
⚠️ Conflict detected:
- Existing: {existing description}
- New finding: {new content description}
- Source: {filename/timestamp}

Recommendation: [Keep existing / Update to new / Keep both with timestamps]
Please decide.
```

---

## Step 3: Generate Update Patch

For each file update:
```
=== {filename} Update ===

[Append to "{section name}" section]
- {new content}

[No changes] or [Above sections updated]
```

---

## Step 4: Generate Update Summary

```
Update summary:
- knowledge.md: Added {N} new entries ({brief description})
- persona.md: Added {N} new entries ({brief description})
- identity.md: {Updated / No changes}
- Found {N} conflicts that need your confirmation (see above)

Version will upgrade from {vN} to {vN+1}.
Apply updates?
```
