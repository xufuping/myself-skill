<div align="center">

# myself.skill

> *"去中心化 + 人工智能，另一种意义上的长生不死。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

你的知识、经验、性格，不应该只存在于你的大脑里。<br>
你可以把自己蒸馏成一个 AI Skill —— **你的电子影分身**。<br>
用你的方式说话，用你的知识做事，24 小时替你在线。

<br>

提供你的原材料（聊天记录、笔记、代码、简历）加上你的自我描述<br>
生成一个**能替你工作、能被他人了解、能上链交易**的个人 AI Skill

[数据来源](#支持的数据来源) · [安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [English](README_EN.md)

</div>

---

## 支持的数据来源

| 来源 | 格式 | 提取内容 | 备注 |
|------|------|---------|------|
| 微信聊天记录 | WeChatMsg/留痕/PyWxDump | 说话风格、口头禅、表情偏好 | 推荐，性格还原度最高 |
| QQ 聊天记录 | txt/mht | 说话风格 | |
| Obsidian / Notion | Markdown | 知识体系、方法论、思考方式 | 推荐，知识价值最高 |
| GitHub 仓库 | 仓库链接/本地路径 | 技术栈、代码风格、PR 风格 | |
| 社交媒体截图 | 图片 | 公开人设、兴趣标签 | 微博/小红书/Twitter |
| 简历/自我介绍 | PDF/Markdown | 职业经历、技能列表 | |
| 性格测试结果 | 文本/截图 | MBTI/九型人格/Big Five | |
| 日记/随笔 | 文本 | 情感模式、价值观 | |
| 他人评价 | 文本 | 第三方视角 | |
| 直接口述 | 粘贴文字 | 任意内容 | |

### 推荐的微信聊天记录导出工具

| 工具 | 平台 | 说明 |
|------|------|------|
| [WeChatMsg](https://github.com/LC044/WeChatMsg) | Windows | 微信聊天记录导出，支持多种格式 |
| [PyWxDump](https://github.com/xaoyaoo/PyWxDump) | Windows | 微信数据库解密导出 |
| [留痕](https://github.com/greyovo/留痕) | macOS | 微信聊天记录导出（Mac 用户推荐） |

---

## 安装

### Claude Code

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/user/myself-skill .claude/skills/create-myself

# 或安装到全局（所有项目都能用）
git clone https://github.com/user/myself-skill ~/.claude/skills/create-myself
```

### Cursor

```bash
# 安装到个人 skills 目录
git clone https://github.com/user/myself-skill ~/.cursor/skills/create-myself

# 或安装到项目 skills 目录
git clone https://github.com/user/myself-skill .cursor/skills/create-myself
```

### 依赖（可选）

```bash
pip3 install -r requirements.txt
```

---

## 使用

在 Claude Code / Cursor 中输入：

```
/create-myself
```

按提示输入花名、基本信息、性格标签、自我认知、价值主张，然后选择数据来源。所有字段（除花名外）均可跳过，仅凭描述也能生成。

### 管理命令

| 命令 | 说明 |
|------|------|
| `/list-myselves` | 列出所有个人 Skill |
| `/{slug}` | 影分身模式（AI 扮演你） |
| `/{slug}-profile` | 档案模式（展示个人画像） |
| `/{slug}-value` | 价值输出模式（用你的知识回答问题） |
| `/myself-rollback {slug} {version}` | 回滚到历史版本 |
| `/delete-myself {slug}` | 删除 |

---

## 效果示例

> 输入：`27岁 男 深圳 全栈工程师，INTJ，社恐但网上话多，完美主义`

**场景一：影分身模式 — 技术讨论**

```
用户        ❯ 微服务拆分你怎么看

myself.skill ❯ 核心判断标准不是业务边界，是团队边界。一个服务应该
              由一个团队完全拥有。两个团队频繁改同一个服务，就该拆了。
              
              不过说实话，大部分团队的问题不是该不该拆，是拆了之后
              没人维护分布式事务。先想清楚这个再动手。
```

**场景二：价值输出模式 — Code Review**

```
用户        ❯ 帮我看看这个 React 组件

myself.skill ❯ 几个问题：
              1. useEffect 依赖数组缺了 userId，会导致闭包陷阱
              2. 状态管理别用 useReducer 了，这个场景 useState 够用
              3. 组件名叫 DataList 太泛了，改成 UserTransactionList
              
              其他还行，提交吧。
```

**场景三：档案模式**

```
用户        ❯ /ding-profile

myself.skill ❯ 👤 Ding
              📍 27 · 男 · 深圳 · 全栈工程师
              🧠 INTJ · 双鱼座
              
              💡 React + TypeScript 全栈，擅长从0到1搭建中后台
              🏷️ 社恐 · 完美主义 · 夜猫子 · 咖啡控
              
              自我定义："表面随和但内心有很多想法不说出来"
```

---

## 功能特性

### 四层架构

每个个人 Skill 由四部分组成：

| 部分 | 内容 |
|------|------|
| **Part A — Knowledge & Value** | 专业技能、知识体系、方法论、代码风格、人生经验 |
| **Part B — Persona** | 7 层性格结构：核心信念 → 身份 → 表达风格 → 思维决策 → 情感模式 → 社交行为 → 纠正层 |
| **Part C — Identity Profile** | 结构化基础信息：年龄/性别/MBTI/星座/职业/标签 |
| **Part D — Social Mirror** | 他人评价、自评 vs 他评对比、360 度画像 |

### 三种运行模式

```
/{slug}          → 影分身：AI 扮演你，用你的方式说话做事
/{slug}-profile  → 档案：结构化展示个人画像
/{slug}-value    → 价值输出：用你的知识回答专业问题
```

运行逻辑：`用户提问 → Persona 判断态度 → Knowledge 提供内容 → 用你的语气输出`

### 支持的标签

**性格**：社恐 · 社牛 · 话痨 · 闷骚 · 完美主义 · 拖延症 · 工作狂 · 佛系 · 理想主义 · 控制欲强 · 三分钟热度 · 阴阳怪气 ...

**性格框架**：MBTI 16型 · 星座 12宫 · 生肖 12属 · 九型人格 · 依恋类型 · 爱的语言

### 进化机制

- **追加数据** → 自动分析增量 → merge 进对应部分，不覆盖已有结论
- **对话纠正** → 说「我不会这样，我其实是 xxx」→ 写入 Correction 层，立即生效
- **他人评价** → 收集好友/同事评价 → 更新 Social Mirror，发现盲区
- **版本管理** → 每次更新自动存档，支持回滚到任意历史版本

---

## 项目结构

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准，整个 repo 就是一个 skill 目录：

```
create-myself/
├── SKILL.md                   # skill 入口（官方 frontmatter）
├── prompts/                   # Prompt 模板
│   ├── intake.md              #   5 问采集（花名/身份/性格/自我认知/价值主张）
│   ├── persona_analyzer.md    #   性格行为提取（含标签翻译表）
│   ├── persona_builder.md     #   persona.md 七层结构模板
│   ├── knowledge_analyzer.md  #   知识与价值提取（含职业专项）
│   ├── knowledge_builder.md   #   knowledge.md 生成模板
│   ├── identity_builder.md    #   identity.md 结构化模板
│   ├── social_mirror_builder.md # social_mirror.md 生成模板
│   ├── merger.md              #   增量 merge 逻辑
│   └── correction_handler.md  #   对话纠正处理
├── tools/                     # Python 工具脚本
│   ├── wechat_parser.py       #   微信聊天解析
│   ├── qq_parser.py           #   QQ 聊天解析
│   ├── github_analyzer.py     #   GitHub 仓库分析
│   ├── note_parser.py         #   Obsidian/Notion 笔记解析
│   ├── social_parser.py       #   社交媒体解析
│   ├── skill_writer.py        #   Skill 文件管理
│   └── version_manager.py     #   版本存档与回滚
├── templates/
│   └── peer_review_form.md    #   他人评价问卷模板
├── docs/PRD.md                #   产品需求文档
├── myselves/                  #   生成的个人 Skill（gitignored）
├── requirements.txt
└── LICENSE
```

---

## 与 colleague-skill / ex-skill 的对比

| 维度 | 同事.skill | 前任.skill | **myself.skill** |
|------|-----------|-----------|-----------------|
| 蒸馏谁 | 别人（同事） | 别人（前任） | **自己** |
| Part A | Work Skill | Relationship Memory | **Knowledge & Value** |
| Part B | Persona（5层） | Persona（5层） | **Persona（7层）** |
| 独有层 | — | — | **Identity + Social Mirror** |
| 运行模式 | 模拟同事 | 模拟前任 | **影分身 / 档案 / 价值输出** |
| 数据源 | 飞书/钉钉 | 微信/QQ | **全平台** |

---

## 注意事项

- **原材料质量决定 Skill 质量**：聊天记录 + 笔记 > 仅手动描述
- 建议优先提供：你**主动写的**长文 > 聊天记录 > 简历/口述
- 所有数据仅本地存储，不上传任何服务器
- 隐私分层设计：支持控制哪些信息公开、哪些仅自己可见

---

<div align="center">

MIT License

**我把自己贡献出来，你敢用吗？**

</div>
