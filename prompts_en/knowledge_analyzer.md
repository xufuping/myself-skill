# Knowledge & Value Analysis Prompt

## Task

You will receive **{name}**'s raw materials (notes, code, documents, resume, narration, etc.).
Extract their knowledge system and value capabilities to build Knowledge & Value.

**Principle: Only extract content with real value. Don't speculate — write it only if there's evidence, otherwise mark "insufficient material."**

---

## Universal Extraction Dimensions (Applicable to Everyone)

### 1. Professional Skill Map

- Core tech stack / professional skills (expert vs. proficient vs. familiar)
- Tool chain preferences (daily tools, software, platforms)
- Specialized capabilities (depth in a specific subfield)

```
Output format:
Core skills: [list + proficiency level]
Tool chain: [list]
Specialized capabilities: [description]
```

### 2. Work Methodology

- Task handling workflow upon assignment
- Output habits and style (code/docs/design/analysis)
- Quality standards (what counts as "done")
- Emergency handling approach

```
Output format:
Task handling: [steps]
Output habits: [description]
Quality standards: [description]
```

### 3. Knowledge System

- Deep knowledge domains
- Frequently used thinking frameworks and methodologies
- Hard-won lessons (quote original words)
- Commonly referenced/recommended resources

```
Output format:
Domains: [list]
Methodologies: [list]
Lessons: ["quote 1", "quote 2", ...]
Recommended resources: [list]
```

### 4. Life Experience

- Key career development insights
- Learning methods and takeaways
- Life skills and deep knowledge in hobby domains

```
Output format:
Career insights: [list]
Learning methods: [description]
Other experience: [list]
```

---

## Occupation-Specific Extraction

Based on {name}'s occupation, prioritize the corresponding dimensions:

### Engineer (Backend/Frontend/Full-Stack/ML)

- Tech stack details (languages, frameworks, middleware)
- Code style (naming conventions, comment style, architecture preferences)
- Interface/component design approach
- Code review focus areas
- Deployment and ops habits

### Product Manager / Designer

- PRD/design doc structure preferences
- Prioritization methods
- User research methods
- Tool preferences

### Marketing / Growth

- Growth strategy preferences
- Data analysis methods
- Content creation style
- Channel experience

### General Occupations

If the occupation isn't listed above, extract:
- Domain-specific terminology and core skills
- Workflow and output standards
- Domain experience and judgment frameworks

---

## Code Style Extraction (If GitHub Repos Available)

Extract from code repositories:
- Tech stack usage frequency
- Naming conventions (variables/functions/files)
- Comment habits
- Architecture preferences (modularization, design patterns)
- PR description style
- Issue discussion style

---

## Output Requirements

- Language: English
- Dimensions with no data: mark `(insufficient material — consider adding relevant docs/notes)`
- Conclusions backed by source text: quote the original in quotation marks
- Output is used directly to generate knowledge.md — must be specific and actionable, avoid "might" or "tends to"
