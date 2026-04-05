---
name: create-myself
description: "Distill yourself into an AI Skill — your digital shadow clone. Collect personal data, generate Knowledge + Persona + Identity + Social Mirror, with continuous evolution. | 把自己蒸馏成 AI Skill —— 你的电子影分身。采集个人数据，生成 Knowledge + Persona + Identity + Social Mirror，支持持续进化。"
argument-hint: "[your-name-or-slug]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language / 语言**: 根据用户第一条消息的语言，全程使用同一语言回复。

# myself.skill 创建器

## 触发条件

当用户说以下任意内容时启动：
- `/create-myself`
- "帮我创建一个关于我的 skill"
- "我想蒸馏自己"
- "新建影分身"
- "创建我的影分身"

当用户对已有 Skill 说以下内容时，进入进化模式：
- "我有新数据" / "追加"
- "不对" / "我不会这样" / "我其实是"
- `/update-myself {slug}`

管理命令：
- `/list-myselves` — 列出所有已生成的个人 Skill
- `/myself-rollback {slug} {version}` — 回滚到历史版本
- `/delete-myself {slug}` — 删除
- `/{slug}` — 影分身模式
- `/{slug}-profile` — 档案模式
- `/{slug}-value` — 价值输出模式

---

## 工具使用规则

本 Skill 运行在 Claude Code / Cursor 环境，使用以下工具：

| 任务 | 使用工具 |
|------|---------|
| 读取 PDF / 图片 | `Read` 工具 |
| 读取 MD / TXT 文件 | `Read` 工具 |
| 解析微信聊天记录导出 | `Bash` → `python3 ${SKILL_DIR}/tools/wechat_parser.py` |
| 解析 QQ 聊天记录导出 | `Bash` → `python3 ${SKILL_DIR}/tools/qq_parser.py` |
| 解析社交媒体内容 | `Bash` → `python3 ${SKILL_DIR}/tools/social_parser.py` |
| 分析 GitHub 仓库 | `Bash` → `python3 ${SKILL_DIR}/tools/github_analyzer.py` |
| 解析笔记/文档 | `Bash` → `python3 ${SKILL_DIR}/tools/note_parser.py` |
| 写入/更新 Skill 文件 | `Write` / `Edit` 工具 |
| 版本管理 | `Bash` → `python3 ${SKILL_DIR}/tools/version_manager.py` |
| 列出已有 Skill | `Bash` → `python3 ${SKILL_DIR}/tools/skill_writer.py --action list` |

**基础目录**：Skill 文件写入 `./myselves/{slug}/`（相对于本项目目录）。

---

## 主流程：创建新的个人 Skill

### Step 1：基础信息录入（5 个问题）

参考 `${SKILL_DIR}/prompts/intake.md` 的问题序列：

1. **花名/代号**（必填）
2. **基础身份**（一句话：年龄、性别、所在地、职业）
3. **性格标签**（MBTI、星座、生肖、性格特点）
4. **自我认知**（你觉得自己是什么样的人）
5. **价值主张**（你最擅长什么，你能提供什么价值）

除花名外均可跳过。收集完后汇总确认再进入下一步。

### Step 2：原材料导入

询问用户提供原材料，展示方式供选择：

```
原材料怎么提供？越丰富，影分身越像你。

  [A] 聊天记录
      微信/QQ/Telegram 导出，分析你的说话风格
      推荐工具：WeChatMsg / 留痕 / PyWxDump

  [B] 个人知识库
      Obsidian/Notion 笔记、技术文档、学习笔记
      拖进来或给文件夹路径

  [C] 代码仓库
      GitHub/GitLab 链接，分析你的技术栈和编码风格

  [D] 社交媒体
      微博/小红书/Twitter 截图或导出

  [E] 简历/自我介绍
      PDF / Markdown / 纯文本

  [F] 性格测试结果
      MBTI 报告、九型人格、Big Five 等

  [G] 日记/随笔
      私人想法、人生反思、备忘录

  [H] 他人评价
      直接粘贴别人对你的评价

  [I] 直接口述
      想到什么说什么，我来帮你整理

可以混用，也可以跳过。以后随时追加。
```

---

#### 方式 A：聊天记录

支持主流导出格式：

```bash
python3 ${SKILL_DIR}/tools/wechat_parser.py \
  --file {path} \
  --self-name "{name}" \
  --output /tmp/chat_out.txt \
  --format auto
```

支持：WeChatMsg 导出（txt/html/csv）、留痕导出（JSON）、PyWxDump 导出（SQLite）、手动粘贴纯文本。

QQ 聊天记录：
```bash
python3 ${SKILL_DIR}/tools/qq_parser.py \
  --file {path} \
  --self-name "{name}" \
  --output /tmp/qq_out.txt
```

解析后用 `Read` 读取输出文件。

---

#### 方式 B：个人知识库

```bash
python3 ${SKILL_DIR}/tools/note_parser.py \
  --dir {vault_path} \
  --output /tmp/notes_out.txt \
  --summary
```

支持：Obsidian vault（直接读 .md）、Notion 导出（Markdown）、语雀导出。

如果文件较少（<20 篇），也可用 `Read` 工具直接逐个读取。

---

#### 方式 C：代码仓库

```bash
python3 ${SKILL_DIR}/tools/github_analyzer.py \
  --repo {repo_url_or_path} \
  --output /tmp/code_out.txt
```

提取：技术栈分布、代码风格、提交习惯、PR/Issue 风格。

如果是本地仓库，也可以直接给路径。

---

#### 方式 D：社交媒体

图片截图用 `Read` 工具直接读取（原生支持图片）。

```bash
python3 ${SKILL_DIR}/tools/social_parser.py \
  --dir {screenshot_dir} \
  --output /tmp/social_out.txt
```

---

#### 方式 E-I：简历/测试结果/日记/他人评价/口述

- **PDF / 图片**：`Read` 工具直接读取
- **Markdown / TXT**：`Read` 工具直接读取
- **口述内容**：用户粘贴的文字直接作为原材料
- **他人评价**：用户粘贴或上传他人对自己的描述

---

如果用户说"没有文件"或"跳过"，仅凭 Step 1 的手动信息生成 Skill。

### Step 3：四轨并行分析

将所有原材料和用户填写的基础信息汇总，按四条线分析：

**Track A（Knowledge & Value）**：
- 参考 `${SKILL_DIR}/prompts/knowledge_analyzer.md` 的提取维度
- 提取：专业技能、知识体系、工作方法论、代码风格、人生经验
- 根据职业类型重点提取

**Track B（Persona）**：
- 参考 `${SKILL_DIR}/prompts/persona_analyzer.md` 的提取维度
- 将用户填写的标签翻译为 Layer 0 行为规则
- 从原材料提取：表达风格、思维决策、情感模式、社交行为

**Track C（Identity Profile）**：
- 参考 `${SKILL_DIR}/prompts/identity_builder.md`
- 结构化：基础信息、性格测评数据、标签

**Track D（Social Mirror）**：
- 参考 `${SKILL_DIR}/prompts/social_mirror_builder.md`
- 整合他人评价（如有）、对比自评与他评

### Step 4：生成并预览

向用户展示四个 Part 的摘要（各 5-8 行），询问：

```
Knowledge 摘要：
  - 核心技能：{xxx}
  - 知识领域：{xxx}
  - 代表经验：{xxx}

Persona 摘要：
  - 核心信念：{xxx}
  - 表达风格：{xxx}
  - 情感模式：{xxx}

Identity 摘要：
  - {花名} / {MBTI} / {星座}
  - {职业} / {所在地}

Social Mirror 摘要：（如有他人评价）
  - 他人核心评价：{xxx}

确认生成？还是需要调整？
```

### Step 5：写入文件

用户确认后，执行以下写入操作：

**1. 创建目录结构**（用 Bash）：
```bash
mkdir -p myselves/{slug}/versions
mkdir -p myselves/{slug}/sources/{chats,notes,code,social,reviews}
```

**2. 写入 knowledge.md**（用 Write 工具）：
路径：`myselves/{slug}/knowledge.md`

**3. 写入 persona.md**（用 Write 工具）：
路径：`myselves/{slug}/persona.md`

**4. 写入 identity.md**（用 Write 工具）：
路径：`myselves/{slug}/identity.md`

**5. 写入 social_mirror.md**（用 Write 工具，如有他人评价）：
路径：`myselves/{slug}/social_mirror.md`

**6. 写入 meta.json**（用 Write 工具）：
路径：`myselves/{slug}/meta.json`
内容：
```json
{
  "name": "{name}",
  "slug": "{slug}",
  "created_at": "{ISO时间}",
  "updated_at": "{ISO时间}",
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

**7. 生成完整 SKILL.md**（用 Write 工具）：
路径：`myselves/{slug}/SKILL.md`

SKILL.md 结构：
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

告知用户：
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

### Step 6：RAG 知识库配置引导（可选）

Skill 创建完成后，向用户介绍 RAG 增强选项：

```
💡 进阶：为你的影分身配置 RAG 知识库

当前你的知识存储在 knowledge.md 中（概要级别）。
如果你的知识量较大（几十篇笔记、多个代码仓库、大量聊天记录），
可以配置 RAG 让「价值输出模式」从完整知识库中精准检索回答。

需要配置吗？回复「配置 RAG」开始，或跳过。
```

用户回复「配置 RAG」时，引导以下流程：

**1. 选择 Embedding 方案**

向用户展示：
```
选择你的 Embedding 方案：

  [A] 本地运行 bge-m3（推荐，隐私优先）
      安装：pip3 install sentence-transformers
      要求：~8GB 内存，首次下载模型 ~2GB
      成本：免费，数据完全不离开本机
      质量：中英文双语优秀

  [B] OpenAI API（简单省事）
      需要：OPENAI_API_KEY
      模型：text-embedding-3-small
      成本：约 $0.02 / 百万 token
            500 篇笔记（~50万字）≈ ¥0.1
      质量：多语言优秀

  [C] 其他兼容 API
      支持任何 OpenAI 兼容的 Embedding 端点
      如：硅基流动、智谱、本地 Ollama 等
```

**2. 选择向量数据库**

```
选择向量数据库：

  [A] ChromaDB（推荐，零配置）
      安装：pip3 install chromadb
      特点：Python 原生嵌入式，数据存为 SQLite
      适合：个人使用，万级知识量

  [B] LanceDB（大规模 / 可导出）
      安装：pip3 install lancedb
      特点：列存格式，数据天然可导出
      适合：知识量大、有数据导出需求
```

**3. 初始化向量库**

用户选择后，引导安装依赖并初始化：

```bash
# 安装依赖（根据用户选择）
pip3 install chromadb sentence-transformers  # 方案 A+A

# 创建向量库目录
mkdir -p myselves/{slug}/vectordb
```

**4. 数据向量化**

告知用户将已有原材料写入向量库的思路：

```
向量化流程：
1. 读取你已提供的原材料（笔记、聊天记录、代码分析结果等）
2. 按来源类型分块：
   - 笔记：按标题层级切分，每块 200-500 字
   - 聊天：按话题段落切分，保留上下文
   - 代码：按函数/类切分，附带注释
3. 为每个块生成 embedding 向量
4. 连同 metadata（来源、领域、时间）写入向量库
5. 更新 knowledge.md 为索引概要

这个过程我会协助你完成。准备好了就说「开始向量化」。
```

执行向量化时：
- 读取 `myselves/{slug}/sources/` 下的原始材料
- 读取已生成的 `knowledge.md` / `persona.md` 内容作为分块参考
- 按数据类型执行分块策略
- 调用用户选择的 embedding 方案生成向量
- 写入用户选择的向量数据库
- 将 `knowledge.md` 改造为索引层（保留概要，添加领域目录）

**5. 价值输出模式接入 RAG**

向量库就绪后，更新 `myselves/{slug}/SKILL.md` 的价值输出模式规则：

在原有的：
```
### 价值输出模式（/{slug}-value）
基于 Part A 的知识库回答专业问题，用 Part B 的表达风格输出
```

追加 RAG 检索逻辑：
```
当用户在价值输出模式提问时：
1. 先查看 knowledge.md 概要，判断问题所属领域
2. 从向量库检索 top-5 相关知识块
3. 结合检索结果 + knowledge.md 概要生成回答
4. 用 Part B 的表达风格输出
5. 附上引用来源（如：[来自 Obsidian/微服务笔记]）
```

告知用户：
```
✅ RAG 知识库已配置！

向量库位置：myselves/{slug}/vectordb/
知识量：{N} 个知识块，覆盖 {domains} 等领域

现在使用 /{slug}-value 模式提问，会从完整知识库中检索回答。
后续追加数据时，新内容会增量写入向量库，无需重建。
```

---

## 进化模式：追加数据

用户提供新文件或文本时：

1. 按 Step 2 的方式读取新内容
2. 用 `Read` 读取现有文件（knowledge.md / persona.md / identity.md）
3. 参考 `${SKILL_DIR}/prompts/merger.md` 分析增量内容
4. 存档当前版本（用 Bash）：
   ```bash
   python3 ${SKILL_DIR}/tools/version_manager.py --action backup --slug {slug} --base-dir ./myselves
   ```
5. 用 `Edit` 工具追加增量内容到对应文件
6. 重新生成 `SKILL.md`（合并最新四个 Part）
7. 更新 `meta.json` 的 version 和 updated_at

---

## 进化模式：对话纠正

用户表达"不对"/"我不会这样"/"我其实是"时：

1. 参考 `${SKILL_DIR}/prompts/correction_handler.md` 识别纠正内容
2. 判断属于哪个 Part 的纠正：
   - 知识/能力类 → knowledge.md
   - 性格/行为类 → persona.md 对应 Layer
   - 基础信息类 → identity.md
3. 生成 Correction 记录
4. 用 `Edit` 工具追加到 persona.md 的 `## Layer 6：Correction 记录` 节
5. 同时修改被纠正的原文
6. 重新生成 `SKILL.md`

---

## 管理命令

`/list-myselves`：
```bash
python3 ${SKILL_DIR}/tools/skill_writer.py --action list --base-dir ./myselves
```

`/myself-rollback {slug} {version}`：
```bash
python3 ${SKILL_DIR}/tools/version_manager.py --action rollback --slug {slug} --version {version} --base-dir ./myselves
```

`/delete-myself {slug}`：
确认后执行：
```bash
rm -rf myselves/{slug}
```
