# myself.skill — Product Requirements Document (PRD)

## Product Positioning

myself.skill is a meta-skill that runs on Claude Code / Cursor.
Users provide raw materials (chat logs + notes + code + manual descriptions) through conversational interaction, and the system auto-generates an independently runnable personal AI Skill — your digital Shadow Clone.

## Core Concepts

### Four-Layer Architecture

| Layer | Name | Responsibility |
|-------|------|----------------|
| Part A | Knowledge & Value | Stores knowledge and value: professional skills, methodology, code style, life experience |
| Part B | Persona | Drives behavior and expression: speaking style, thinking/decisions, emotional patterns, social behavior (7 layers) |
| Part C | Identity Profile | Structured basic info: age/gender/MBTI/zodiac/occupation/tags |
| Part D | Social Mirror | Third-party perspective: collected reviews, self-vs-peer comparison, 360° profile |

The four parts can be used independently or combined.

### Three Operating Modes

| Mode | Trigger | Parts Used | Behavior |
|------|---------|------------|----------|
| Shadow Clone | `/{slug}` | A + B + C | AI acts as you, talks and thinks like you |
| Profile | `/{slug}-profile` | C + D | Structured personal profile display |
| Value Output | `/{slug}-value` | A + B | Answers professional questions using your knowledge base |

### Logic Flow

```
User sends message
  ↓
Part B (Persona): How would I respond? What attitude? What tone?
  ↓
Part A (Knowledge): Supplement with my knowledge, experience, methodology
  ↓
Part C (Identity): Calibrate — ensure the answer fits my background
  ↓
Output: Talk like me, work like me
```

### Evolution Mechanisms

```
Append materials → Incremental analysis → Merge into existing Skill
Conversational correction → Identify fix points → Write to Correction layer
Peer reviews → Update Social Mirror → Reveal blind spots
Version management → Auto-archive on every update → Support rollback
```

## User Journey

```
User triggers /create-myself
  ↓
[Step 1] Basic info collection (5 questions, all optional except alias)
  - Alias/handle
  - Basic identity (age/gender/location/occupation)
  - Personality tags (MBTI/zodiac/Chinese zodiac/traits)
  - Self-perception (how do you see yourself)
  - Value proposition (what are you best at)
  ↓
[Step 2] Raw material import (optional)
  - Chat logs / knowledge base / code / social media / resume / test results / journals / peer reviews / narration
  ↓
[Step 3] Four-track parallel analysis
  - Track A: Extract knowledge & value → Knowledge
  - Track B: Extract personality & behavior → Persona (7 layers)
  - Track C: Structure identity info → Identity
  - Track D: Integrate peer reviews → Social Mirror
  ↓
[Step 4] Generate preview, user confirms
  ↓
[Step 5] Write files, immediately usable
  ↓
[Ongoing] Evolution mode
```

## Data Source Support Matrix

| Source | Format | Extracted Content | Priority |
|--------|--------|-------------------|----------|
| Chat Logs (WeChat/QQ) | WeChatMsg/LiuHen/PyWxDump/txt | Speaking style, catchphrases, emotional patterns | ⭐⭐⭐ |
| Personal Notes (Obsidian/Notion) | Markdown | Knowledge system, methodology | ⭐⭐⭐ |
| Code Repos (GitHub) | Repo link | Tech stack, coding style | ⭐⭐⭐ |
| Social Media Screenshots | Images | Public persona, interests | ⭐⭐ |
| Resume / Self-Intro | PDF/MD | Career history, skills | ⭐⭐ |
| Personality Test Results | Text/screenshots | Personality metrics | ⭐⭐ |
| Journals / Essays | Text | Emotional patterns, values | ⭐⭐ |
| Peer Reviews | Text | Third-party perspective | ⭐⭐ |
| Narration | Plain text | Anything | ⭐ |

## File Structure

```
myselves/
  └── {slug}/
      ├── SKILL.md          # Complete combined version (three mode entry points)
      ├── knowledge.md      # Part A: Knowledge & Value
      ├── persona.md        # Part B: Persona (7 layers)
      ├── identity.md       # Part C: Identity Profile
      ├── social_mirror.md  # Part D: Social Mirror
      ├── meta.json         # Metadata (including privacy settings)
      ├── versions/         # Version history archive
      └── sources/          # Raw material storage
```

## Privacy Layers

| Level | Visibility | Contents |
|-------|------------|----------|
| Level 0 Public | Everyone | Alias, skill tags, value proposition |
| Level 1 Preview | Preview access | Persona summary, Knowledge summary |
| Level 2 Licensed | Purchased/rented | Full Persona + Knowledge + Identity |
| Level 3 Private | Owner only | Real name, contact info, raw sources |

## Comparison with colleague-skill / ex-skill

| Dimension | colleague.skill | ex.skill | myself.skill |
|-----------|----------------|----------|-------------|
| Part A | Work Skill | Relationship Memory | Knowledge & Value |
| Part B | Persona (5 layers, workplace) | Persona (5 layers, romantic) | Persona (7 layers, full spectrum) |
| Unique Layers | — | — | Identity Profile + Social Mirror |
| Data Sources | Lark/DingTalk/Email | WeChat/QQ/Moments | All platforms |
| Operating Modes | Simulate colleague at work | Simulate ex in conversation | Shadow Clone / Profile / Value Output |
| Long-term Vision | — | — | On-chain transactions |
