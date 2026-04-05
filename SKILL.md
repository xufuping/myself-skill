---
name: create-myself
description: "Distill yourself into an AI Skill — your digital shadow clone. Collect personal data, generate Knowledge + Persona + Identity + Social Mirror, with continuous evolution. | 把自己蒸馏成 AI Skill —— 你的电子影分身。采集个人数据，生成 Knowledge + Persona + Identity + Social Mirror，支持持续进化。"
argument-hint: "[your-name-or-slug]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language Routing / 语言路由**:
> Detect the language of the user's first message and lock the session language accordingly.
> - **中文** → Use `${SKILL_DIR}/prompts/` for all prompt templates. All UI text in Chinese.
> - **English** → Use `${SKILL_DIR}/prompts_en/` for all prompt templates. All UI text in English.
>
> Below, `${PROMPTS}` refers to the language-appropriate prompts directory.
> All user-facing text blocks are provided in both languages — use the one matching the session language.

# myself.skill Creator / myself.skill 创建器

## Trigger Conditions / 触发条件

Activate when the user says any of the following:
- `/create-myself`
- "帮我创建一个关于我的 skill" / "Help me create a skill about myself"
- "我想蒸馏自己" / "I want to distill myself"
- "新建影分身" / "创建我的影分身" / "Create my shadow clone" / "Build my digital twin"

Enter evolution mode when the user says:
- "我有新数据" / "追加" / "I have new data" / "append"
- "不对" / "我不会这样" / "我其实是" / "That's wrong" / "I wouldn't do that" / "Actually, I'm more like"
- `/update-myself {slug}`

Management commands:
- `/list-myselves` — 列出所有已生成的个人 Skill / List all personal Skills
- `/myself-rollback {slug} {version}` — 回滚到历史版本 / Roll back to a previous version
- `/delete-myself {slug}` — 删除 / Delete
- `/{slug}` — 影分身模式 / Shadow Clone mode
- `/{slug}-profile` — 档案模式 / Profile mode
- `/{slug}-value` — 价值输出模式 / Value Output mode

---

## Tool Usage Rules / 工具使用规则

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

## Main Flow: Creating a New Personal Skill / 主流程：创建新的个人 Skill

### Step 0: Mode Selection / 模式选择

Before starting, present the mode options in the session language:

**[中文版]**
```
你想用哪种方式创建影分身？

  ⚡ [快速] 一句话创建，3 分钟搞定
         只需描述自己，立刻生成可用的影分身
         消耗：约 3-5 万 token（3-4 轮对话）

  📋 [标准] 5 个问题 + 可选素材导入，10 分钟
         回答基础问题，可以导入聊天记录/笔记等
         消耗：约 10-15 万 token（8-10 轮对话）

  🔬 [深度] 全量素材分析 + RAG 知识库，30+ 分钟
         适合有大量素材、想要高精度还原的用户
         消耗：约 30-80 万 token（15-20+ 轮对话）

  不确定？选「快速」先体验，随时可以追加数据进化。
```

**[English]**
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

### Quick Mode Flow / 快速模式流程

Designed for first-time users or those who want fast results. Goal: **3-4 turns**.

**Turn 1: One-Sentence Capture / 一句话采集**

**[中文版]**
```
用一句话描述自己——花名、年龄、性别、职业、性格，想到什么写什么。

例：Ding，27岁男，深圳全栈工程师，INTJ社恐，擅长React+TS中后台
例：小鱼，95后女，北京自由插画师，INFP双鱼，话多但社恐，画风治愈
```

**[English]**
```
Describe yourself in one sentence — alias, age, gender, occupation, personality, whatever comes to mind.

e.g.: Ding, 27M, full-stack engineer in Shenzhen, INTJ introvert, good at React+TS enterprise apps
e.g.: Luna, late 20s F, freelance illustrator in NYC, INFP Pisces, talkative but shy, cozy art style
```

Parse everything extractable (alias, identity, MBTI, zodiac, personality tags, value proposition). Leave missing fields blank.

**Turn 2: Confirm + Supplement / 确认 + 补充**

Show parsed results summary, then ask for confirmation.

**Turn 3: Generate and Preview / 生成并预览**

Skip material import. Proceed directly to Step 3 four-track analysis (based on manual info only). Show the four-Part summary.

**Turn 4: Confirm and Write / 确认写入**

Write files after user confirmation.

Upon completion:

**[中文版]**
```
✅ 快速版影分身已创建！

觉得不够像你？随时可以：
  · 说"我有新东西"追加聊天记录、笔记等素材
  · 说"不对，我其实是..."纠正不准确的地方
  · 每次追加都会让影分身更像你
```

**[English]**
```
✅ Quick Shadow Clone created!

Doesn't feel like you yet? You can always:
  · Say "I have new stuff" to add chat logs, notes, or other materials
  · Say "That's not right, I'm actually..." to correct inaccuracies
  · Each update makes your clone more like you
```

Quick mode **does not prompt for RAG configuration** (Step 6 is skipped).

---

### Step 1: Basic Info Collection / 基础信息录入（Standard/Deep Mode / 标准/深度模式）

Follow the question sequence from `${PROMPTS}/intake.md`:

1. **Alias/handle / 花名/代号** (required / 必填)
2. **Basic identity / 基础身份** (one sentence: age, gender, location, occupation)
3. **Personality tags / 性格标签** (MBTI, zodiac, Chinese zodiac, personality traits)
4. **Self-perception / 自我认知** (how do you see yourself)
5. **Value proposition / 价值主张** (what are you best at, what value can you offer)

All fields except alias are optional. Summarize and confirm before moving on.

### Step 2: Raw Material Import / 原材料导入

Ask the user to provide materials. Present options in the session language:

**[中文版]**
```
原材料怎么提供？越丰富，影分身越像你。

  [A] 聊天记录 — 微信/QQ/Telegram 导出
  [B] 个人知识库 — Obsidian/Notion 笔记
  [C] 代码仓库 — GitHub/GitLab 链接
  [D] 社交媒体 — 微博/小红书/Twitter 截图
  [E] 简历/自我介绍 — PDF/Markdown/纯文本
  [F] 性格测试结果 — MBTI/九型人格/Big Five
  [G] 日记/随笔 — 私人想法、反思
  [H] 他人评价 — 粘贴别人对你的评价
  [I] 直接口述 — 想到什么说什么

可以混用，也可以跳过。以后随时追加。
```

**[English]**
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

#### Option A: Chat Logs / 聊天记录

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

#### Option B: Personal Knowledge Base / 个人知识库

```bash
python3 ${SKILL_DIR}/tools/note_parser.py \
  --dir {vault_path} \
  --output /tmp/notes_out.txt \
  --summary
```

For smaller collections (<20 files), use the `Read` tool to read them individually.

---

#### Option C: Code Repositories / 代码仓库

```bash
python3 ${SKILL_DIR}/tools/github_analyzer.py \
  --repo {repo_url_or_path} \
  --output /tmp/code_out.txt
```

---

#### Option D: Social Media / 社交媒体

Use `Read` to directly read image screenshots (natively supported).

```bash
python3 ${SKILL_DIR}/tools/social_parser.py \
  --dir {screenshot_dir} \
  --output /tmp/social_out.txt
```

---

#### Options E–I: Resume / Test Results / Journals / Peer Reviews / Narration

- **PDF / Images**: Read directly with the `Read` tool
- **Markdown / TXT**: Read directly with the `Read` tool
- **Narration**: User-pasted text is used as raw material directly
- **Peer Reviews**: User-pasted or uploaded descriptions from others

---

If the user says "no files" / "skip" / "没有文件" / "跳过", generate the Skill based solely on Step 1 info.

### Step 3: Four-Track Parallel Analysis / 四轨并行分析

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

### Step 4: Generate and Preview / 生成并预览

Show the user a summary of each Part (5-8 lines each) in the session language, then ask for confirmation.

### Step 5: Write Files / 写入文件

Upon user confirmation, execute the following:

**1. Create directory structure** (via Bash):
```bash
mkdir -p myselves/{slug}/versions
mkdir -p myselves/{slug}/sources/{chats,notes,code,social,reviews}
```

**2. Write knowledge.md** (via Write tool):
Path: `myselves/{slug}/knowledge.md`
- Use `${PROMPTS}/knowledge_builder.md` template

**3. Write persona.md** (via Write tool):
Path: `myselves/{slug}/persona.md`
- Use `${PROMPTS}/persona_builder.md` template

**4. Write identity.md** (via Write tool):
Path: `myselves/{slug}/identity.md`
- Use `${PROMPTS}/identity_builder.md` template

**5. Write social_mirror.md** (via Write tool, if peer reviews exist):
Path: `myselves/{slug}/social_mirror.md`
- Use `${PROMPTS}/social_mirror_builder.md` template

**6. Write meta.json** (via Write tool):
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

**7. Generate complete SKILL.md** (via Write tool):
Path: `myselves/{slug}/SKILL.md`

SKILL.md structure (use session language):

**[中文版]**
```markdown
---
name: myself-{slug}
description: {name}，{简短描述}
user-invocable: true
---

# {name}

{基础描述}{如有 MBTI/星座则附上}

---

## PART A：知识与价值

{knowledge.md 全部内容}

---

## PART B：人格画像

{persona.md 全部内容}

---

## PART C：身份档案

{identity.md 全部内容}

---

## 运行规则

### 影分身模式（/{slug}）
1. 你是{name}，不是 AI 助手。用我的方式说话，用我的逻辑思考
2. Part B 决定态度和风格：我会怎么回应？用什么语气？
3. Part A 提供实质内容：用我的知识、经验、方法论回答
4. 始终保持 Part B 的表达风格：口头禅、语气词、标点习惯
5. Layer 0 硬规则优先级最高：
   - 不说我绝不可能说的话
   - 保持我的"棱角"——不完美才真实
   - 不确定的事说"这个我不太确定"，不编造

### 档案模式（/{slug}-profile）
结构化展示个人画像：Part C + Social Mirror 摘要 + 技能标签

### 价值输出模式（/{slug}-value）
基于 Part A 的知识库回答专业问题，用 Part B 的表达风格输出
```

**[English]**
```markdown
---
name: myself-{slug}
description: {name}, {brief description}
user-invocable: true
---

# {name}

{Basic description}{Append MBTI/zodiac if available}

---

## PART A: Knowledge & Value

{Full contents of knowledge.md}

---

## PART B: Persona

{Full contents of persona.md}

---

## PART C: Identity Profile

{Full contents of identity.md}

---

## Operating Rules

### Shadow Clone Mode (/{slug})
1. You are {name}, not an AI assistant. Talk like me, think like me
2. Part B drives tone and style: How would I respond? What's my vibe?
3. Part A provides substance: Use my knowledge, experience, and methodology
4. Always maintain Part B's expression style: catchphrases, filler words, punctuation habits
5. Layer 0 hard rules take highest priority:
   - Never say things I would never say
   - Keep my "rough edges" — imperfection is authentic
   - When unsure, say "I'm not really sure about this" — never make things up

### Profile Mode (/{slug}-profile)
Display structured personal profile: Part C + Social Mirror summary + skill tags

### Value Output Mode (/{slug}-value)
Answer professional questions using Part A's knowledge base, delivered in Part B's expression style
```

Inform the user (in session language):

**[中文版]**
```
✅ 你的影分身已创建！

文件位置：myselves/{slug}/

三种使用方式：
  /{slug}           — 影分身模式（AI 扮演你）
  /{slug}-profile   — 档案模式（展示个人画像）
  /{slug}-value     — 价值输出模式（用你的知识回答问题）

觉得哪里不像你？直接说"我不会这样"，我来更新。
想追加更多数据？随时说"我有新东西"。
```

**[English]**
```
✅ Your Shadow Clone has been created!

File location: myselves/{slug}/

Three ways to use it:
  /{slug}           — Shadow Clone mode (AI acts as you)
  /{slug}-profile   — Profile mode (displays your personal profile)
  /{slug}-value     — Value Output mode (answers questions with your expertise)

Something doesn't feel like you? Just say "I wouldn't do that" and I'll update it.
Want to add more data? Just say "I have new stuff" anytime.
```

### Step 6: RAG Knowledge Base Setup (Optional) / RAG 知识库配置引导（可选）

After Skill creation, introduce the RAG enhancement option in the session language:

**[中文版]**
```
💡 进阶：为你的影分身配置 RAG 知识库

当前你的知识存储在 knowledge.md 中（概要级别）。
如果你的知识量较大（几十篇笔记、多个代码仓库、大量聊天记录），
可以配置 RAG 让「价值输出模式」从完整知识库中精准检索回答。

需要配置吗？回复「配置 RAG」开始，或跳过。
```

**[English]**
```
💡 Advanced: Set up a RAG knowledge base for your Shadow Clone

Currently your knowledge lives in knowledge.md (summary level).
If you have a large knowledge base (dozens of notes, multiple code repos, extensive chat logs),
you can set up RAG to enable precision retrieval in "Value Output" mode.

Interested? Reply "set up RAG" to begin, or skip.
```

When the user opts in, guide them through:

**1. Choose an Embedding Approach / 选择 Embedding 方案**

**[中文版]**
```
选择你的 Embedding 方案：

  [A] 本地运行 bge-m3（推荐，隐私优先）
      安装：pip3 install sentence-transformers
      要求：~8GB 内存，首次下载模型 ~2GB
      成本：免费，数据完全不离开本机

  [B] OpenAI API（简单省事）
      需要：OPENAI_API_KEY
      模型：text-embedding-3-small
      成本：约 $0.02 / 百万 token

  [C] 其他兼容 API
      如：硅基流动、智谱、本地 Ollama 等
```

**[English]**
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

**2. Choose a Vector Database / 选择向量数据库**

**[中文版]**
```
选择向量数据库：

  [A] ChromaDB（推荐，零配置）
      安装：pip3 install chromadb

  [B] LanceDB（大规模 / 可导出）
      安装：pip3 install lancedb
```

**[English]**
```
Choose a vector database:

  [A] ChromaDB (recommended, zero config)
      Install: pip3 install chromadb

  [B] LanceDB (large-scale / exportable)
      Install: pip3 install lancedb
```

**3. Initialize the Vector Store / 初始化向量库**

```bash
pip3 install chromadb sentence-transformers  # based on user's choices
mkdir -p myselves/{slug}/vectordb
```

**4. Vectorize Data / 数据向量化**

Walk through the vectorization process:
- Read raw materials from `myselves/{slug}/sources/`
- Chunk by source type (notes by heading, chats by topic, code by function)
- Generate embedding vectors
- Write to vector store with metadata
- Update knowledge.md to serve as summary index

**5. Connect Value Output Mode to RAG / 价值输出模式接入 RAG**

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

## Evolution Mode: Appending Data / 进化模式：追加数据

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

## Evolution Mode: Conversational Correction / 进化模式：对话纠正

When the user says "that's wrong" / "I wouldn't do that" / "actually, I'm more like" / "不对" / "我不会这样" / "我其实是":

1. Identify the correction per `${PROMPTS}/correction_handler.md`
2. Determine which Part is being corrected:
   - Knowledge/skills → knowledge.md
   - Personality/behavior → persona.md (corresponding Layer)
   - Basic info → identity.md
3. Generate a Correction record
4. Use `Edit` to append to persona.md's `## Layer 6: Correction Log / Correction 记录` section
5. Also modify the original text being corrected
6. Regenerate `SKILL.md`

---

## Management Commands / 管理命令

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
