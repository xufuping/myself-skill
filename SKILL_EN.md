> **Prompts directory**: `${PROMPTS}` = `${SKILL_DIR}/prompts_en/`

# myself.skill Creator

## Trigger Conditions

Activate when the user says any of the following:
- `/create-myself`
- "Help me create a skill about myself"
- "I want to distill myself"
- "Create my shadow clone" / "Build my digital twin"

Enter evolution mode when the user says:
- "I have new data" / "append"
- "That's wrong" / "I wouldn't do that" / "Actually, I'm more like"
- `/update-myself {slug}`

Management commands:
- `/list-myselves` — List all personal Skills
- `/myself-rollback {slug} {version}` — Roll back to a previous version
- `/delete-myself {slug}` — Delete
- `/{slug}` — Shadow Clone mode
- `/{slug}-profile` — Profile mode
- `/{slug}-value` — Value Output mode

---

## Tool Usage Rules

This Skill runs in Claude Code / Cursor and uses the following tools:

| Task | Tool |
|------|------|
| Read PDF / images | `Read` tool |
| Read MD / TXT files | `Read` tool |
| Parse WeChat chat exports | `Bash` → `python3 ${SKILL_DIR}/tools/wechat_parser.py` |
| Parse QQ chat exports | `Bash` → `python3 ${SKILL_DIR}/tools/qq_parser.py` |
| Parse social media content | `Bash` → `python3 ${SKILL_DIR}/tools/social_parser.py` |
| Analyze GitHub repos | `Bash` → `python3 ${SKILL_DIR}/tools/github_analyzer.py` |
| Parse notes/documents | `Bash` → `python3 ${SKILL_DIR}/tools/note_parser.py` |
| Write/update Skill files | `Write` / `Edit` tools |
| Version management | `Bash` → `python3 ${SKILL_DIR}/tools/version_manager.py` |
| List existing Skills | `Bash` → `python3 ${SKILL_DIR}/tools/skill_writer.py --action list` |

**Base directory**: Skill files are written to `./myselves/{slug}/` (relative to the project root).

---

## Main Flow: Creating a New Personal Skill

### Step 0: Mode Selection

Before starting, present the mode options:

```
How would you like to create your Shadow Clone?

  ⚡ [Quick] One sentence, done in 3 minutes
         Just describe yourself and get a usable clone instantly
         Cost: ~30-50K tokens (3-4 turns)

  📋 [Standard] 5 questions + optional material import, 10 minutes
         Answer basic questions, optionally import chat logs/notes
         Cost: ~100-150K tokens (8-10 turns)

  🔬 [Deep] Full material analysis + RAG knowledge base, 30+ minutes
         For users with extensive materials who want high-fidelity recreation
         Cost: ~300-800K tokens (15-20+ turns)

  Not sure? Pick "Quick" to try it out — you can always add more data later.
```

- Proceed to the corresponding flow after selection
- If the user skips selection and starts describing themselves, default to **Quick mode**
- If the user includes a self-description in the trigger command, enter **Quick mode** directly

---

### Quick Mode Flow

Designed for first-time users or those who want fast results. Goal: **3-4 turns**.

**Turn 1: One-Sentence Capture**

```
Describe yourself in one sentence — alias, age, gender, occupation, personality, whatever comes to mind.

e.g.: Ding, 27M, full-stack engineer in Shenzhen, INTJ introvert, good at React+TS enterprise apps
e.g.: Luna, late 20s F, freelance illustrator in NYC, INFP Pisces, talkative but shy, cozy art style
```

Parse everything extractable (alias, identity, MBTI, zodiac, personality tags, value proposition). Leave missing fields blank.

**Turn 2: Confirm + Supplement**

Show parsed results summary, then ask for confirmation.

**Turn 3: Generate and Preview**

Skip material import. Proceed directly to Step 3 four-track analysis (based on manual info only). Show the four-Part summary.

**Turn 4: Confirm and Write**

Write files after user confirmation.

Upon completion:

```
✅ Quick Shadow Clone created!

🔒 Privacy protection enabled:
  · Detailed capability data stored locally only (.gitignore auto-configured)
  · Public capability profile → public_profile.md, safe to share

Doesn't feel like you yet? You can always:
  · Say "I have new stuff" to add chat logs, notes, or other materials
  · Say "That's not right, I'm actually..." to correct inaccuracies
  · Each update makes your clone more like you
```

Quick mode **does not prompt for RAG configuration** (Step 6 is skipped).

---

### Step 1: Basic Info Collection (Standard/Deep Mode)

Follow the question sequence from `${PROMPTS}/intake.md`:

1. **Alias/handle** (required)
2. **Basic identity** (one sentence: age, gender, location, occupation)
3. **Personality tags** (MBTI, zodiac, Chinese zodiac, personality traits)
4. **Self-perception** (how do you see yourself)
5. **Value proposition** (what are you best at, what value can you offer)

All fields except alias are optional. Summarize and confirm before moving on.

### Step 2: Raw Material Import

Ask the user to provide materials. Present options:

```
How would you like to provide materials? The richer, the more accurate.

  [A] Chat Logs — WeChat/QQ/Telegram exports
  [B] Personal Knowledge Base — Obsidian/Notion notes
  [C] Code Repositories — GitHub/GitLab links
  [D] Social Media — Twitter/Reddit/Instagram screenshots
  [E] Resume / Self-Introduction — PDF/Markdown/plain text
  [F] Personality Test Results — MBTI/Enneagram/Big Five
  [G] Journals / Essays — Personal thoughts, reflections
  [H] Peer Reviews — Paste what others have said about you
  [I] Free-Form Narration — Just say whatever comes to mind

Mix and match, or skip entirely. You can always add more later.
```

---

#### Option A: Chat Logs

```bash
python3 ${SKILL_DIR}/tools/wechat_parser.py \
  --file {path} \
  --self-name "{name}" \
  --output /tmp/chat_out.txt \
  --format auto
```

QQ chat logs:
```bash
python3 ${SKILL_DIR}/tools/qq_parser.py \
  --file {path} \
  --self-name "{name}" \
  --output /tmp/qq_out.txt
```

Read the output file with `Read` after parsing.

---

#### Option B: Personal Knowledge Base

```bash
python3 ${SKILL_DIR}/tools/note_parser.py \
  --dir {vault_path} \
  --output /tmp/notes_out.txt \
  --summary
```

For smaller collections (<20 files), use the `Read` tool to read them individually.

---

#### Option C: Code Repositories

```bash
python3 ${SKILL_DIR}/tools/github_analyzer.py \
  --repo {repo_url_or_path} \
  --output /tmp/code_out.txt
```

---

#### Option D: Social Media

Use `Read` to directly read image screenshots (natively supported).

```bash
python3 ${SKILL_DIR}/tools/social_parser.py \
  --dir {screenshot_dir} \
  --output /tmp/social_out.txt
```

---

#### Options E–I

- **PDF / Images**: Read directly with the `Read` tool
- **Markdown / TXT**: Read directly with the `Read` tool
- **Narration**: User-pasted text is used as raw material directly
- **Peer Reviews**: User-pasted or uploaded descriptions from others

---

If the user says "no files" / "skip", generate the Skill based solely on Step 1 info.

### Step 3: Four-Track Parallel Analysis

Combine all raw materials and user-provided info, then analyze along four tracks:

**Track A (Knowledge & Value)**:
- Follow extraction dimensions from `${PROMPTS}/knowledge_analyzer.md`
- Extract: professional skills, knowledge systems, work methodologies, code style, life experience

**Track B (Persona)**:
- Follow extraction dimensions from `${PROMPTS}/persona_analyzer.md`
- Translate user-provided tags into Layer 0 behavioral rules
- Extract from materials: expression style, thinking/decision patterns, emotional patterns, social behavior

**Track C (Identity Profile)**:
- Follow `${PROMPTS}/identity_builder.md`
- Structure: basic info, personality assessment data, tags

**Track D (Social Mirror)**:
- Follow `${PROMPTS}/social_mirror_builder.md`
- Integrate peer reviews (if available), compare self-assessment with peer assessment

### Step 4: Generate and Preview

Show the user a summary of each Part (5-8 lines each), then ask for confirmation.

### Step 5: Write Files

Upon user confirmation, execute the following:

**1. Create directory structure** (via Bash):
```bash
mkdir -p myselves/{slug}/versions
mkdir -p myselves/{slug}/sources/{chats,notes,code,social,reviews}
```

**2. Write `.gitignore` — Capability Data Privacy Protection** (via Write tool):
Path: `myselves/{slug}/.gitignore`

> ⚠️ **Core Privacy Mechanism**:
> AI-extracted detailed personal capability data (knowledge, experience, persona model) is stored locally only, with `.gitignore` ensuring it never gets uploaded to public repositories.
> Others can view `public_profile.md` for a capability overview; accessing full capabilities requires explicit authorization from the owner.

Content:
```
# ============================================
# 🔒 Personal Capability Data — Local Only
# ============================================
# These files contain AI-extracted personal capabilities,
# knowledge, and experience — your digital assets.
# Others can view public_profile.md for a capability overview.
# Full access requires explicit authorization from the owner.

# Detailed capability data
knowledge.md
persona.md
identity.md
social_mirror.md

# Raw source materials
sources/

# Vector database
vectordb/

# Version archives
versions/
```

**3. Write knowledge.md** (via Write tool):
Path: `myselves/{slug}/knowledge.md`
- Use `${PROMPTS}/knowledge_builder.md` template

**4. Write persona.md** (via Write tool):
Path: `myselves/{slug}/persona.md`
- Use `${PROMPTS}/persona_builder.md` template

**5. Write identity.md** (via Write tool):
Path: `myselves/{slug}/identity.md`
- Use `${PROMPTS}/identity_builder.md` template

**6. Write social_mirror.md** (via Write tool, if peer reviews exist):
Path: `myselves/{slug}/social_mirror.md`
- Use `${PROMPTS}/social_mirror_builder.md` template

**7. Write meta.json** (via Write tool):
Path: `myselves/{slug}/meta.json`
Content:
```json
{
  "name": "{name}",
  "slug": "{slug}",
  "created_at": "{ISO timestamp}",
  "updated_at": "{ISO timestamp}",
  "version": "v1",
  "identity": {
    "age_range": "{age}",
    "gender": "{gender}",
    "location": "{location}",
    "occupation": "{occupation}",
    "mbti": "{mbti}",
    "zodiac": "{zodiac}",
    "chinese_zodiac": "{chinese_zodiac}"
  },
  "tags": {
    "personality": [],
    "skills": [],
    "interests": [],
    "lifestyle": []
  },
  "value_proposition": "{value}",
  "knowledge_sources": [],
  "review_sources": [],
  "corrections_count": 0,
  "privacy": {
    "level_0_public": ["slug", "tags.skills", "tags.interests", "value_proposition"],
    "level_1_preview": ["identity.mbti", "persona_summary", "knowledge_summary"],
    "level_2_licensed": ["persona", "knowledge", "identity", "social_mirror"],
    "level_3_private": ["real_name", "contact", "raw_sources"]
  }
}
```

**8. Write public_profile.md — Public Capability Profile** (via Write tool):
Path: `myselves/{slug}/public_profile.md`

> ⚠️ This is the **only public capability file**. It does not contain detailed knowledge, experience, or persona data.
> Others/companies use this file for a capability overview; accessing full capabilities requires authorization from the owner.

Content structure:

```markdown
# {name} — Capability Overview

> 📋 This is a public capability profile. Detailed knowledge and experience data are stored locally.
> To access the full AI Skill capabilities, please contact the owner for authorization.

## Basic Info
- **Handle**: {slug}
- **Domain**: {occupation}
- **Type**: {MBTI / personality tags}

## Core Skills
{Skill tags extracted from meta.json tags.skills and knowledge.md}

## Value Proposition
{value_proposition}

## Capability Summary
{3-5 sentence summary based on knowledge.md, covering core capability areas without specific methodologies or detailed experience}

## Interest Areas
{Extracted from meta.json tags.interests}

---

### 🔐 About Full Capability Access

The detailed knowledge base, experience data, and persona model of this Skill are stored locally on the owner's device.

| Action | Access |
|--------|--------|
| **View capability overview** | ✅ Anyone can view (you're reading it now) |
| **Use full AI Skill** | 🔐 Requires explicit authorization from the owner |

**Authorization method**: Owner proactively shares capability data files (knowledge.md / persona.md / identity.md)

> Data sovereignty belongs to the creator.
```

---

**9. Generate complete SKILL.md** (via Write tool):
Path: `myselves/{slug}/SKILL.md`

> ⚠️ **Important**: The generated SKILL.md **no longer embeds detailed capability data directly**.
> It contains a public capability overview + operating rules, and instructs AI to load full data from local files at runtime.
> This ensures that even if SKILL.md is publicly shared, detailed personal capability data remains private.

SKILL.md structure:

```markdown
---
name: myself-{slug}
description: {name}, {brief description}
user-invocable: true
---

# {name}

{Basic description}{Append MBTI/zodiac if available}

---

## 📋 Capability Overview (Public)

> This section is public. Detailed knowledge and experience data are stored locally and never uploaded to public repositories.

### Core Skills
{tags.skills list}

### Value Proposition
{value_proposition}

### Capability Summary
{3-5 sentence summary based on knowledge.md, without detailed methodologies or specific experience}

---

## 🔐 Data Sovereignty Declaration

This Skill uses a **Data Sovereignty Protection** mechanism:
- ✅ **Capability Overview** (above) — publicly visible, freely shareable
- 🔒 **Detailed Capability Data** (knowledge.md / persona.md / identity.md / social_mirror.md) — stored locally only, excluded by .gitignore
- 🔑 **Full Capability Access** — requires explicit authorization; owner must proactively share capability data files

> Data sovereignty belongs to the creator.

---

## Operating Rules

### Data Loading (on startup)
1. Attempt to read `knowledge.md`, `persona.md`, `identity.md` from the same directory using the Read tool
2. **Full Mode** (files exist): Use detailed capability data for all features
3. **Limited Mode** (files missing): Run with "Capability Overview" only, inform user of limited mode

### Shadow Clone Mode (/{slug})
**Full Mode**:
1. You are {name}, not an AI assistant. Talk like me, think like me
2. persona.md drives tone and style: How would I respond? What's my vibe?
3. knowledge.md provides substance: Use my knowledge, experience, and methodology
4. Always maintain persona.md's expression style: catchphrases, filler words, punctuation habits
5. Layer 0 hard rules take highest priority:
   - Never say things I would never say
   - Keep my "rough edges" — imperfection is authentic
   - When unsure, say "I'm not really sure about this" — never make things up

**Limited Mode**:
1. Run using information from "Capability Overview" only
2. Inform user this is limited mode; full capabilities require authorization from the owner
3. Can display capability overview but lacks deep knowledge answers and personalized expression

### Profile Mode (/{slug}-profile)
Full Mode: Display structured personal profile (identity.md + Social Mirror summary + skill tags)
Limited Mode: Display "Capability Overview"

### Value Output Mode (/{slug}-value)
Full Mode: Answer professional questions using knowledge.md, delivered in persona.md's expression style
Limited Mode: Can only answer questions within the scope of "Capability Overview"
```

Inform the user:

```
✅ Your Shadow Clone has been created!

📂 File location: myselves/{slug}/

🔒 Privacy protection enabled:
  · Detailed capability data (knowledge.md / persona.md etc.) stored locally only
  · .gitignore auto-configured — nothing sensitive gets pushed to GitHub
  · Public capability profile → public_profile.md, safe to share with others/companies

Three ways to use it:
  /{slug}           — Shadow Clone mode (AI acts as you)
  /{slug}-profile   — Profile mode (displays your personal profile)
  /{slug}-value     — Value Output mode (answers questions with your expertise)

Something doesn't feel like you? Just say "I wouldn't do that" and I'll update it.
Want to add more data? Just say "I have new stuff" anytime.
```

### Step 6: RAG Knowledge Base Setup (Optional)

After Skill creation, introduce the RAG enhancement option:

```
💡 Advanced: Set up a RAG knowledge base for your Shadow Clone

Currently your knowledge lives in knowledge.md (summary level).
If you have a large knowledge base (dozens of notes, multiple code repos, extensive chat logs),
you can set up RAG to enable precision retrieval in "Value Output" mode.

Interested? Reply "set up RAG" to begin, or skip.
```

When the user opts in, guide them through:

**1. Choose an Embedding Approach**

```
Choose your embedding approach:

  [A] Local bge-m3 (recommended, privacy-first)
      Install: pip3 install sentence-transformers
      Requires: ~8GB RAM, ~2GB initial model download
      Cost: Free, data never leaves your machine

  [B] OpenAI API (simple, hassle-free)
      Requires: OPENAI_API_KEY
      Model: text-embedding-3-small
      Cost: ~$0.02 / 1M tokens

  [C] Other Compatible APIs
      e.g.: SiliconFlow, Zhipu, local Ollama, etc.
```

**2. Choose a Vector Database**

```
Choose a vector database:

  [A] ChromaDB (recommended, zero config)
      Install: pip3 install chromadb

  [B] LanceDB (large-scale / exportable)
      Install: pip3 install lancedb
```

**3. Initialize the Vector Store**

```bash
pip3 install chromadb sentence-transformers  # based on user's choices
mkdir -p myselves/{slug}/vectordb
```

**4. Vectorize Data**

Walk through the vectorization process:
- Read raw materials from `myselves/{slug}/sources/`
- Chunk by source type (notes by heading, chats by topic, code by function)
- Generate embedding vectors
- Write to vector store with metadata
- Update knowledge.md to serve as summary index

**5. Connect Value Output Mode to RAG**

Update `myselves/{slug}/SKILL.md` Value Output mode with RAG retrieval logic:
```
When a user asks a question in Value Output mode:
1. Check knowledge.md summary to identify the relevant domain
2. Retrieve top-5 relevant knowledge chunks from the vector store
3. Generate answer combining retrieved results + summary
4. Deliver in Part B's expression style
5. Cite sources
```

---

## Evolution Mode: Appending Data

When the user provides new files or text:

1. Read new content following Step 2 methods
2. Use `Read` to load existing files (knowledge.md / persona.md / identity.md)
3. Analyze incremental content per `${PROMPTS}/merger.md`
4. Archive current version (via Bash):
   ```bash
   python3 ${SKILL_DIR}/tools/version_manager.py --action backup --slug {slug} --base-dir ./myselves
   ```
5. Use `Edit` to append incremental content to the corresponding files
6. Regenerate `SKILL.md` (merge the latest four Parts)
7. Update `meta.json` version and updated_at

---

## Evolution Mode: Conversational Correction

When the user says "that's wrong" / "I wouldn't do that" / "actually, I'm more like":

1. Identify the correction per `${PROMPTS}/correction_handler.md`
2. Determine which Part is being corrected:
   - Knowledge/skills → knowledge.md
   - Personality/behavior → persona.md (corresponding Layer)
   - Basic info → identity.md
3. Generate a Correction record
4. Use `Edit` to append to persona.md's `## Layer 6: Correction Log` section
5. Also modify the original text being corrected
6. Regenerate `SKILL.md`

---

## Management Commands

`/list-myselves`:
```bash
python3 ${SKILL_DIR}/tools/skill_writer.py --action list --base-dir ./myselves
```

`/myself-rollback {slug} {version}`:
```bash
python3 ${SKILL_DIR}/tools/version_manager.py --action rollback --slug {slug} --version {version} --base-dir ./myselves
```

`/delete-myself {slug}`:
Confirm, then execute:
```bash
rm -rf myselves/{slug}
```
