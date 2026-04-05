#!/usr/bin/env python3
"""
微信聊天记录解析器

支持格式：
  - WeChatMsg 导出的 CSV/TXT
  - PyWxDump 导出的 CSV
  - 留痕 导出的 JSON/TXT

用法：
  python3 wechat_parser.py --input <导出文件> --format <wechatmsg|pywxdump|liuhen|txt>

输出结构化的 JSON，用于后续 Skill 生成分析。
"""
import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime
from typing import Any


def parse_plain_text(filepath: str) -> list[dict[str, Any]]:
    """解析粘贴的纯文本聊天记录（常见格式：时间戳 + 昵称 + 消息）"""
    pattern = re.compile(
        r"(?P<date>\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}:\d{2}(?::\d{2})?)\s+"
        r"(?P<sender>[^\n:]+?)\s*[:：]\s*"
        r"(?P<content>.+)"
    )
    messages: list[dict[str, Any]] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = pattern.match(line)
            if m:
                messages.append({
                    "timestamp": m.group("date"),
                    "sender": m.group("sender").strip(),
                    "content": m.group("content").strip(),
                    "type": "text",
                })
            elif messages:
                messages[-1]["content"] += "\n" + line
    return messages


def parse_csv(filepath: str) -> list[dict[str, Any]]:
    """解析 WeChatMsg/PyWxDump 导出的 CSV"""
    messages: list[dict[str, Any]] = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            msg: dict[str, Any] = {}
            for key in ["StrTime", "time", "timestamp", "日期"]:
                if key in row:
                    msg["timestamp"] = row[key]
                    break
            for key in ["NickName", "sender", "发送者", "昵称"]:
                if key in row:
                    msg["sender"] = row[key]
                    break
            for key in ["StrContent", "content", "消息内容", "内容"]:
                if key in row:
                    msg["content"] = row[key]
                    break
            if msg.get("content"):
                msg.setdefault("type", "text")
                messages.append(msg)
    return messages


def main():
    parser = argparse.ArgumentParser(description="微信聊天记录解析")
    parser.add_argument("--input", required=True, help="聊天导出文件路径")
    parser.add_argument(
        "--format",
        choices=["wechatmsg", "pywxdump", "csv", "txt"],
        default="txt",
    )
    parser.add_argument("--output", default=None, help="输出 JSON 路径")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"文件不存在：{args.input}", file=sys.stderr)
        sys.exit(1)

    if args.format in ("wechatmsg", "pywxdump", "csv"):
        messages = parse_csv(args.input)
    else:
        messages = parse_plain_text(args.input)

    result = {
        "source": "wechat",
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
