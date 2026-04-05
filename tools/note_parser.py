#!/usr/bin/env python3
"""
个人笔记解析器

支持格式：
  - Obsidian vault（递归扫描 .md 文件）
  - Notion 导出（Markdown zip 解压后）
  - 单个 Markdown 文件

用法：
  python3 note_parser.py --input <目录或文件> [--max-files 200]
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def extract_frontmatter(content: str) -> dict[str, str]:
    """提取 Markdown frontmatter（YAML 格式）"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def extract_headings(content: str) -> list[str]:
    return re.findall(r"^#{1,3}\s+(.+)$", content, re.MULTILINE)


def parse_note(filepath: str) -> dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    fm = extract_frontmatter(content)
    headings = extract_headings(content)
    return {
        "path": filepath,
        "title": fm.get("title") or headings[0] if headings else os.path.basename(filepath),
        "tags": fm.get("tags", "").split(",") if fm.get("tags") else [],
        "headings": headings,
        "char_count": len(content),
        "content": content,
    }


def scan_directory(directory: str, max_files: int = 200) -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
    for md_file in sorted(Path(directory).rglob("*.md")):
        if len(notes) >= max_files:
            break
        if any(part.startswith(".") for part in md_file.parts):
            continue
        notes.append(parse_note(str(md_file)))
    return notes


def main():
    parser = argparse.ArgumentParser(description="个人笔记解析")
    parser.add_argument("--input", required=True, help="Obsidian vault 目录或 Markdown 文件")
    parser.add_argument("--max-files", type=int, default=200)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    if os.path.isdir(args.input):
        notes = scan_directory(args.input, args.max_files)
    elif os.path.isfile(args.input):
        notes = [parse_note(args.input)]
    else:
        print(f"路径不存在：{args.input}", file=sys.stderr)
        sys.exit(1)

    result = {
        "source": "notes",
        "parsed_at": datetime.now().isoformat(),
        "total_notes": len(notes),
        "notes": notes,
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"已解析 {len(notes)} 篇笔记 → {args.output}")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
