#!/usr/bin/env python3
"""
QQ 聊天记录解析器

支持格式：
  - QQ 导出的 TXT（常见格式：日期 时间 昵称(QQ号) + 消息体）
  - MHT 格式（提取文本部分）

用法：
  python3 qq_parser.py --input <导出文件> --format <txt|mht>
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from typing import Any


def parse_qq_txt(filepath: str) -> list[dict[str, Any]]:
    pattern = re.compile(
        r"(?P<date>\d{4}[-/]\d{2}[-/]\d{2}\s+\d{1,2}:\d{2}:\d{2})\s+"
        r"(?P<sender>[^\(（]+?)(?:\(|（)(?P<qq>\d+)(?:\)|）)"
    )
    messages: list[dict[str, Any]] = []
    with open(filepath, "r", encoding="utf-8") as f:
        current_msg: dict[str, Any] | None = None
        for line in f:
            line = line.rstrip("\n")
            m = pattern.match(line)
            if m:
                if current_msg:
                    messages.append(current_msg)
                current_msg = {
                    "timestamp": m.group("date"),
                    "sender": m.group("sender").strip(),
                    "qq": m.group("qq"),
                    "content": "",
                    "type": "text",
                }
            elif current_msg is not None:
                if current_msg["content"]:
                    current_msg["content"] += "\n" + line
                else:
                    current_msg["content"] = line
        if current_msg:
            messages.append(current_msg)
    return messages


def main():
    parser = argparse.ArgumentParser(description="QQ 聊天记录解析")
    parser.add_argument("--input", required=True)
    parser.add_argument("--format", choices=["txt", "mht"], default="txt")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"文件不存在：{args.input}", file=sys.stderr)
        sys.exit(1)

    messages = parse_qq_txt(args.input)

    result = {
        "source": "qq",
        "parsed_at": datetime.now().isoformat(),
        "total_messages": len(messages),
        "messages": messages,
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"已解析 {len(messages)} 条消息 → {args.output}")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
