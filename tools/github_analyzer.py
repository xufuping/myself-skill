#!/usr/bin/env python3
"""
GitHub 仓库分析工具

功能：
  - 分析本地 git 仓库的语言分布、提交风格、代码规模
  - 提取 commit message 风格和 PR 习惯

用法：
  python3 github_analyzer.py --repo <本地仓库路径> [--max-commits 500]
"""
import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


LANG_MAP = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
    ".tsx": "TypeScript React", ".jsx": "JavaScript React",
    ".java": "Java", ".go": "Go", ".rs": "Rust", ".rb": "Ruby",
    ".cpp": "C++", ".c": "C", ".cs": "C#", ".swift": "Swift",
    ".kt": "Kotlin", ".vue": "Vue", ".svelte": "Svelte",
    ".sh": "Shell", ".sql": "SQL", ".md": "Markdown",
    ".css": "CSS", ".scss": "SCSS", ".html": "HTML",
}


def run_git(repo: str, args: list[str]) -> str:
    result = subprocess.run(
        ["git", "-C", repo] + args,
        capture_output=True, text=True, timeout=30,
    )
    return result.stdout.strip()


def analyze_languages(repo: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for path in Path(repo).rglob("*"):
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        if path.is_file():
            lang = LANG_MAP.get(path.suffix.lower())
            if lang:
                counter[lang] += 1
    return dict(counter.most_common(10))


def analyze_commits(repo: str, max_commits: int = 500) -> dict[str, Any]:
    log = run_git(repo, [
        "log", f"--max-count={max_commits}",
        "--format=%H||%an||%ae||%aI||%s",
    ])
    if not log:
        return {"total": 0, "authors": {}, "samples": []}

    authors: Counter[str] = Counter()
    samples: list[str] = []
    total = 0
    for line in log.split("\n"):
        parts = line.split("||", 4)
        if len(parts) < 5:
            continue
        total += 1
        authors[parts[1]] += 1
        if len(samples) < 20:
            samples.append(parts[4])

    return {
        "total": total,
        "authors": dict(authors.most_common(5)),
        "message_samples": samples,
    }


def main():
    parser = argparse.ArgumentParser(description="GitHub 仓库分析")
    parser.add_argument("--repo", required=True, help="本地仓库路径")
    parser.add_argument("--max-commits", type=int, default=500)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    if not os.path.isdir(os.path.join(args.repo, ".git")):
        print(f"不是 git 仓库：{args.repo}", file=sys.stderr)
        sys.exit(1)

    result = {
        "source": "github",
        "repo_path": os.path.abspath(args.repo),
        "parsed_at": datetime.now().isoformat(),
        "languages": analyze_languages(args.repo),
        "commits": analyze_commits(args.repo, args.max_commits),
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"分析完成 → {args.output}")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
