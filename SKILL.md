---
name: create-myself
description: "Distill yourself into an AI Skill — your digital shadow clone. | 把自己蒸馏成 AI Skill —— 你的电子影分身。"
argument-hint: "[your-name-or-slug]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

# myself.skill — Language Router / 语言路由

## Language Detection / 语言检测

Detect the language of the user's first message and load the corresponding Skill file:

1. **中文** → Use `Read` tool to load `${SKILL_DIR}/SKILL_CN.md`, then follow all instructions in that file for the entire session.
2. **English** → Use `Read` tool to load `${SKILL_DIR}/SKILL_EN.md`, then follow all instructions in that file for the entire session.

If the language is ambiguous, ask the user:

```
🌍 请选择语言 / Please choose your language:

  [A] 中文
  [B] English
```

## Rules

- After loading the language-specific file, follow its instructions exclusively for the rest of the session.
- Do not mix content from SKILL_CN.md and SKILL_EN.md.
- All Python tools are shared between both languages, located in `${SKILL_DIR}/tools/`.
- Chinese version uses prompt templates from `${SKILL_DIR}/prompts/`.
- English version uses prompt templates from `${SKILL_DIR}/prompts_en/`.
