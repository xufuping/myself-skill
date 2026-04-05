#!/usr/bin/env python3
"""
社交媒体内容解析器

支持格式：
  - 微博/小红书/Twitter 数据包导出（JSON）
  - 朋友圈文本导出
  - 手动粘贴的文字内容

用法：
  python3 social_parser.py --input <文件> --platform <weibo|xiaohongshu|twitter|generic>
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from typing import Any


def parse_generic_text(filepath: str) -> list[dict[str, Any]]:
    """按段落分割纯文本，每段作为一条 post"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    paragraphs = re.split(r"\n{2,}", content.strip())
    posts: list[dict[str, Any]] = []
    for i, para in enumerate(paragraphs):
        para = para.strip()
        if para:
            posts.append({
                "index": i + 1,
                "content": para,
                "platform": "generic",
            })
    return posts


def parse_json_export(filepath: str) -> list[dict[str, Any]]:
    """解析平台 JSON 数据包"""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ["posts", "statuses", "data", "tweets", "items"]:
            if key in data and isinstance(data[key], list):
                return data[key]
    return [data]


def main():
    parser = argparse.ArgumentParser(description="社交媒体解析")
    parser.add_argument("--input", required=True)
    parser.add_argument(
        "--platform",
        choices=["weibo", "xiaohongshu", "twitter", "generic"],
        default="generic",
    )
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"文件不存在：{args.input}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(args.input)[1].lower()
    if ext == ".json":
        posts = parse_json_export(args.input)
    else:
        posts = parse_generic_text(args.input)

    result = {
        "source": f"social_{args.platform}",
        "parsed_at": datetime.now().isoformat(),
        "total_posts": len(posts),
        "posts": posts,
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"已解析 {len(posts)} 条内容 → {args.output}")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
