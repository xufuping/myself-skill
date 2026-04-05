# myself.skill — 产品需求文档（PRD）

## 产品定位

myself.skill 是一个运行在 Claude Code / Cursor 上的 meta-skill。
用户通过对话式交互提供原材料（聊天记录 + 笔记 + 代码 + 手动描述），系统自动生成一个可独立运行的个人 AI Skill —— 你的电子影分身。

## 核心概念

### 四层架构

| 层 | 名称 | 职责 |
|----|------|------|
| Part A | Knowledge & Value | 存储知识与价值：专业技能、方法论、代码风格、人生经验 |
| Part B | Persona | 驱动行为与表达：说话风格、思维决策、情感模式、社交行为（7层） |
| Part C | Identity Profile | 结构化基础信息：年龄/性别/MBTI/星座/职业/标签 |
| Part D | Social Mirror | 他人视角：评价收集、自评他评对比、360度画像 |

四部分可以独立使用，也可以组合运行。

### 三种运行模式

| 模式 | 触发词 | 使用的 Part | 行为 |
|------|--------|------------|------|
| 影分身 | `/{slug}` | A + B + C | AI 扮演你，用你的方式说话做事 |
| 档案 | `/{slug}-profile` | C + D | 结构化展示个人画像 |
| 价值输出 | `/{slug}-value` | A + B | 基于知识库回答专业问题 |

### 运行逻辑

```
用户发消息
  ↓
Part B（Persona）判断：我会怎么回应？什么态度？什么语气？
  ↓
Part A（Knowledge）补充：用我的知识、经验、方法论回答
  ↓
Part C（Identity）校准：确保回答符合我的身份背景
  ↓
输出：用我的方式说话，用我的知识做事
```

### 进化机制

```
追加原材料 → 增量分析 → merge 进现有 Skill
对话纠正 → 识别修正点 → 写入 Correction 层
他人评价 → 更新 Social Mirror → 发现盲区
版本管理 → 每次更新自动存档 → 支持回滚
```

## 用户旅程

```
用户触发 /create-myself
  ↓
[Step 1] 基础信息录入（5个问题，除花名外均可跳过）
  - 花名/代号
  - 基础身份（年龄/性别/所在地/职业）
  - 性格标签（MBTI/星座/生肖/性格特点）
  - 自我认知（你觉得自己是什么样的人）
  - 价值主张（你最擅长什么）
  ↓
[Step 2] 原材料导入（可跳过）
  - 聊天记录 / 知识库 / 代码 / 社交媒体 / 简历 / 测试结果 / 日记 / 他人评价 / 口述
  ↓
[Step 3] 四轨并行分析
  - Track A：提取知识与价值 → Knowledge
  - Track B：提取性格行为 → Persona（7层）
  - Track C：结构化身份信息 → Identity
  - Track D：整合他人评价 → Social Mirror
  ↓
[Step 4] 生成预览，用户确认
  ↓
[Step 5] 写入文件，立即可用
  ↓
[持续] 进化模式
```

## 数据源支持矩阵

| 来源 | 格式 | 提取内容 | 优先级 |
|------|------|---------|--------|
| 聊天记录（微信/QQ） | WeChatMsg/留痕/PyWxDump/txt | 说话风格、口头禅、情感模式 | ⭐⭐⭐ |
| 个人笔记（Obsidian/Notion） | Markdown | 知识体系、方法论 | ⭐⭐⭐ |
| 代码仓库（GitHub） | 仓库链接 | 技术栈、编码风格 | ⭐⭐⭐ |
| 社交媒体截图 | 图片 | 公开人设、兴趣 | ⭐⭐ |
| 简历/自我介绍 | PDF/MD | 职业经历、技能 | ⭐⭐ |
| 性格测试结果 | 文本/截图 | 性格量化 | ⭐⭐ |
| 日记/随笔 | 文本 | 情感模式、价值观 | ⭐⭐ |
| 他人评价 | 文本 | 第三方视角 | ⭐⭐ |
| 口述 | 纯文本 | 任意 | ⭐ |

## 文件结构

```
myselves/
  └── {slug}/
      ├── SKILL.md          # 完整组合版（三种模式入口）
      ├── knowledge.md      # Part A：知识与价值
      ├── persona.md        # Part B：人格画像（7层）
      ├── identity.md       # Part C：身份档案
      ├── social_mirror.md  # Part D：他人视角
      ├── meta.json         # 元数据（含隐私设置）
      ├── versions/         # 历史版本存档
      └── sources/          # 原始材料存放
```

## 隐私分层

| 级别 | 可见性 | 包含内容 |
|------|--------|---------|
| Level 0 Public | 所有人 | 花名、技能标签、价值主张 |
| Level 1 Preview | 预览 | Persona 摘要、Knowledge 摘要 |
| Level 2 Licensed | 购买/租用 | 完整 Persona + Knowledge + Identity |
| Level 3 Private | 仅本人 | 真实姓名、联系方式、原始数据 |

## 与 colleague-skill / ex-skill 的对比

| 维度 | 同事.skill | 前任.skill | myself.skill |
|------|-----------|-----------|-------------|
| Part A | Work Skill（工作能力） | Relationship Memory | Knowledge & Value（知识与价值） |
| Part B | Persona（5层，职场） | Persona（5层，恋爱） | Persona（7层，全维度） |
| 独有层 | — | — | Identity Profile + Social Mirror |
| 数据源 | 飞书/钉钉/邮件 | 微信/QQ/朋友圈 | 全平台 |
| 运行模式 | 模拟同事做事 | 模拟前任对话 | 影分身/档案/价值输出 |
| 远期目标 | — | — | 链上交易 |
