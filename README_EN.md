<div align="center">

# myself.skill

> *"Reject Data Necromancy. Forge Your Own Shadow Clone — Digital creators of the world, unite!"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

🧬 Your knowledge, experience, and personality shouldn't live only in your head —<br>
and they certainly shouldn't be free fodder for platforms to harvest and resell.<br>
**It's time to reclaim your data sovereignty and forge your own Shadow Clone** 🥷

📦 Provide your raw materials (chat logs · notes · code · resume)<br>
🎭 Generate a personal AI Skill that **talks like you, thinks like you, and keeps evolving**

`📦 Raw Materials` → `🧠 AI Distillation` → `🎭 Personal Skill` → `🔄 Continuous Evolution`

<br>

🧑‍💻 **For Individuals · Skill Capitalization**<br>
Your tech intuition, code style, and methodology — packaged as a reusable digital asset.<br>
Your clone handles code reviews, doc generation, and flags blind spots via Issues — a self-investment flywheel that grows stronger with use.

🏢 **For Teams · On-Demand Expertise**<br>
No need to expand headcount during peak demand — subscribe to expert Shadow Clones at low cost.<br>
Voluntary authorization, full transparency, no outsourcing quality roulette or data breach risks.

🫂 **For Connection · Digital Companionship**<br>
"Maybe I can be there for you in a different way" — a digital monument that transcends the three deaths.

> 📖 [**Learn more: From "Digital Laborer" to "Digital Sovereign" →**](introduce_en.md)

[Data Sources](#supported-data-sources) · [Install](#installation) · [Usage](#usage) · [Examples](#demo) · [中文](README.md)

</div>

---

## Supported Data Sources

| Source | Format | Extracted Content | Notes |
|--------|--------|-------------------|-------|
| WeChat Chat Logs | WeChatMsg/LiuHen/PyWxDump | Speaking style, catchphrases, emoji preferences | Recommended — highest personality fidelity |
| QQ Chat Logs | txt/mht | Speaking style | |
| Obsidian / Notion | Markdown | Knowledge system, methodology, thinking patterns | Recommended — highest knowledge value |
| GitHub Repos | Repo link / local path | Tech stack, code style, PR style | |
| Social Media Screenshots | Images | Public persona, interest tags | Twitter/Reddit/Instagram |
| Resume / Self-Intro | PDF/Markdown | Career history, skill list | |
| Personality Test Results | Text/screenshots | MBTI/Enneagram/Big Five | |
| Journals / Essays | Text | Emotional patterns, values | |
| Peer Reviews | Text | Third-party perspective | |
| Free-Form Narration | Pasted text | Anything | |

### Recommended WeChat Export Tools

| Tool | Platform | Description |
|------|----------|-------------|
| [WeChatMsg](https://github.com/LC044/WeChatMsg) | Windows | WeChat chat export, multiple formats |
| [PyWxDump](https://github.com/xaoyaoo/PyWxDump) | Windows | WeChat database decryption & export |
| [LiuHen](https://github.com/greyovo/留痕) | macOS | WeChat chat export (recommended for Mac) |

---

## Installation

### Claude Code

```bash
# Install to current project (run in git repo root)
mkdir -p .claude/skills
git clone https://github.com/user/myself-skill .claude/skills/create-myself

# Or install globally (available in all projects)
git clone https://github.com/user/myself-skill ~/.claude/skills/create-myself
```

### Cursor

```bash
# Install to personal skills directory
git clone https://github.com/user/myself-skill ~/.cursor/skills/create-myself

# Or install to project skills directory
git clone https://github.com/user/myself-skill .cursor/skills/create-myself
```

### Dependencies (Optional)

```bash
pip3 install -r requirements.txt
```

---

## Usage

In Claude Code / Cursor, type:

```
/create-myself
```

You'll be asked to choose a mode:

| Mode | Method | Time | Best For |
|------|--------|------|----------|
| ⚡ **Quick** | One-sentence self-description | ~3 min | First-time users, quick generation |
| 📋 **Standard** | 5 questions + optional materials | ~10 min | Most users (recommended) |
| 🔬 **Deep** | Full materials + RAG knowledge base | 30+ min | High-fidelity recreation, extensive materials |

Not sure? Pick "Quick" to try it out — you can always add data to evolve your clone later.

### Cost Breakdown

| Mode | Agent Requests | Approx. Tokens | Comparable To |
|------|---------------|----------------|---------------|
| ⚡ Quick | 3-4 | ~30-50K | Writing two functions with AI autocomplete |
| 📋 Standard | 8-10 | ~100-150K | A medium-sized code refactoring conversation |
| 🔬 Deep | 15-20+ | ~300-800K | A full architecture design discussion |

> 💡 **Worth it?** Every AI autocomplete and chat consumes tokens anyway. Creating a **permanent, continuously evolving** personal Shadow Clone is far more cost-effective than scattered daily usage. Quick mode needs only 3 requests — barely noticeable.

### Management Commands

| Command | Description |
|---------|-------------|
| `/list-myselves` | List all personal Skills |
| `/{slug}` | Shadow Clone mode (AI acts as you) |
| `/{slug}-profile` | Profile mode (displays personal profile) |
| `/{slug}-value` | Value Output mode (answers with your expertise) |
| `/myself-rollback {slug} {version}` | Roll back to a previous version |
| `/delete-myself {slug}` | Delete |

---

## Demo

> Input: `27M, full-stack engineer in Shenzhen, INTJ, shy IRL but verbose online, perfectionist`

**Scenario 1: Shadow Clone Mode — Tech Discussion**

```
User         ❯ What's your take on microservice decomposition?

myself.skill ❯ The core criterion isn't business boundaries — it's team boundaries.
               A service should be fully owned by one team. When two teams are
               constantly modifying the same service, it's time to split.

               Honestly though, the real problem for most teams isn't whether to
               split — it's that nobody handles distributed transactions afterward.
               Figure that out before making any moves.
```

**Scenario 2: Value Output Mode — Code Review**

```
User         ❯ Can you review this React component?

myself.skill ❯ A few issues:
               1. useEffect dependency array is missing userId — stale closure bug
               2. Drop useReducer here, useState is sufficient for this case
               3. "DataList" is too generic — rename to UserTransactionList

               Rest looks fine. Ship it.
```

**Scenario 3: Profile Mode**

```
User         ❯ /ding-profile

myself.skill ❯ 👤 Ding
               📍 27 · M · Shenzhen · Full-Stack Engineer
               🧠 INTJ · Pisces

               💡 React + TypeScript full-stack, specializes in enterprise admin systems
               🏷️ Introverted · Perfectionist · Night owl · Coffee addict

               Self-definition: "Seems easygoing on the surface but has a lot
               of unspoken thoughts underneath"
```

---

## Features

### Four-Layer Architecture

Each personal Skill consists of four parts:

| Part | Content |
|------|---------|
| **Part A — Knowledge & Value** | Professional skills, knowledge systems, methodology, code style, life experience |
| **Part B — Persona** | 7-layer personality structure: Core Beliefs → Identity → Expression Style → Thinking & Decision → Emotional Patterns → Social Behavior → Correction Log |
| **Part C — Identity Profile** | Structured basic info: age/gender/MBTI/zodiac/occupation/tags |
| **Part D — Social Mirror** | Peer reviews, self-assessment vs. peer-assessment comparison, 360° profile |

### Three Operating Modes

```
/{slug}          → Shadow Clone: AI acts as you, talks and thinks like you
/{slug}-profile  → Profile: structured personal profile display
/{slug}-value    → Value Output: answers professional questions with your knowledge
```

Logic flow: `User query → Persona determines attitude → Knowledge provides content → Output in your voice`

### Supported Tags

**Personality**: Introvert · Extrovert · Chatterbox · Quiet but deep · Perfectionist · Procrastinator · Workaholic · Laid-back · Idealist · Control freak · Jack of all trades · Passive-aggressive ...

**Personality Frameworks**: MBTI 16 types · Western Zodiac 12 signs · Chinese Zodiac 12 animals · Enneagram · Attachment Style · Love Languages

### RAG & Personal Knowledge Graph

After Skill creation, you can set up **RAG (Retrieval-Augmented Generation)** to build a personal knowledge graph. This enables your "Value Output" mode to retrieve precise answers from your full knowledge base, not just the `knowledge.md` summary.

Type "set up RAG" after creating your Skill to start the guided setup.

**Dual-Layer Knowledge Architecture**:

```
knowledge.md (Summary Layer)  ←  Shadow Clone / Profile mode: quick access, fits in LLM context
       │ index points to
       ▼
Vector DB (Deep Layer)        ←  Value Output mode: precision retrieval from thousands of knowledge chunks
```

**Embedding Options & Cost**:

| Option | Model | Cost | Privacy | Best For |
|--------|-------|------|---------|----------|
| **Local (recommended)** | `bge-m3` | Free, ~8GB RAM needed | Data never leaves your machine | Privacy-sensitive, decent hardware |
| **OpenAI API** | `text-embedding-3-small` | ~$0.02/1M tokens, 500 notes ≈ $0.10 | Data passes through OpenAI servers | Quick setup, large knowledge base |
| **Compatible APIs** | SiliconFlow/Zhipu/Ollama, etc. | Varies by provider | Depends on provider | Specific needs, local network |

**Vector Database Options**:

| Option | Features | Install |
|--------|----------|---------|
| **ChromaDB (recommended)** | Python-native embedded, zero config, personal scale | `pip3 install chromadb` |
| **LanceDB** | Columnar format, high performance, natively exportable | `pip3 install lancedb` |

**How RAG Works**:

1. Your raw materials (notes, chats, code, etc.) are chunked into **Knowledge Atoms** (self-contained knowledge chunks with source, domain, and recency metadata)
2. Each atom is embedded into a vector via your chosen embedding model and stored in the local vector database
3. When you ask questions in `/{slug}-value` mode, the system retrieves the most relevant chunks and generates precise answers
4. New data is incrementally indexed — no full rebuild needed

### Evolution Mechanisms

- **Append data** → auto-analyzes increments → merges into the relevant part without overwriting existing conclusions
- **Conversational correction** → say "I wouldn't do that, I'm actually like xxx" → writes to the Correction layer, takes effect immediately
- **Peer reviews** → collect friend/colleague feedback → updates Social Mirror, reveals blind spots
- **Version management** → auto-archives on every update, supports rollback to any version

---

## Project Structure

This project follows the [AgentSkills](https://agentskills.io) open standard — the entire repo is a skill directory:

```
create-myself/
├── README.md                  # Chinese README
├── README_EN.md               # English README (this file)
├── SKILL.md                   # Skill entry point (bilingual routing)
├── introduce.md               # Chinese: project philosophy
├── introduce_en.md            # English: project philosophy
├── prompts/                   # Chinese prompt templates
│   └── *.md
├── prompts_en/                # English prompt templates
│   └── *.md
├── tools/                     # Python utility scripts (shared)
│   ├── wechat_parser.py       #   WeChat chat parser
│   ├── qq_parser.py           #   QQ chat parser
│   ├── github_analyzer.py     #   GitHub repo analyzer
│   ├── note_parser.py         #   Obsidian/Notion note parser
│   ├── social_parser.py       #   Social media parser
│   ├── skill_writer.py        #   Skill file manager
│   └── version_manager.py     #   Version archive & rollback
├── templates/
│   ├── peer_review_form.md    #   Chinese peer review questionnaire
│   └── peer_review_form_en.md #   English peer review questionnaire
├── examples/
│   ├── example_ding/          #   Chinese example
│   └── example_ding_en/       #   English example
├── docs/
│   ├── PRD.md                 #   Chinese PRD
│   └── PRD_EN.md              #   English PRD
├── myselves/                  #   Generated personal Skills (gitignored)
│   └── {slug}/
│       ├── vectordb/          #   Vector database (Knowledge Atoms storage)
│       └── ...
├── requirements.txt
└── LICENSE
```

---

## Notes

- **Material quality determines Skill quality**: Chat logs + notes > manual descriptions alone
- Prioritize: long-form content **you wrote** > chat logs > resume/narration
- All data is stored locally — nothing is uploaded to any server
- Privacy-layered design: control what's public, what's preview-only, and what's private

---

<div align="center">

MIT License © [xuqingfeng](https://github.com/xufuping)

</div>
