#!/usr/bin/env python3
"""
Skill 文件管理工具

功能：
  --action list   列出所有已生成的个人 Skill
  --action create 创建新 Skill 目录结构
"""
import argparse
import json
import os
import sys


def list_skills(base_dir: str) -> None:
    if not os.path.isdir(base_dir):
        print(f"目录不存在：{base_dir}")
        return
    slugs = [
        d for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith(".")
    ]
    if not slugs:
        print("暂无已生成的个人 Skill。")
        return
    print(f"已生成的个人 Skill（共 {len(slugs)} 个）：\n")
    for slug in sorted(slugs):
        meta_path = os.path.join(base_dir, slug, "meta.json")
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            name = meta.get("name", slug)
            version = meta.get("version", "?")
            updated = meta.get("updated_at", "?")
            value = meta.get("value_proposition", "")
            print(f"  [{slug}]  {name}  v{version}  更新于 {updated}")
            if value:
                print(f"           💡 {value}")
        else:
            print(f"  [{slug}]  （缺少 meta.json）")
    print()


def main():
    parser = argparse.ArgumentParser(description="myself.skill 文件管理")
    parser.add_argument("--action", choices=["list", "create"], required=True)
    parser.add_argument("--base-dir", default="./myselves")
    parser.add_argument("--slug", default=None)
    args = parser.parse_args()

    if args.action == "list":
        list_skills(args.base_dir)
    elif args.action == "create":
        if not args.slug:
            print("--slug 参数必填", file=sys.stderr)
            sys.exit(1)
        skill_dir = os.path.join(args.base_dir, args.slug)
        os.makedirs(os.path.join(skill_dir, "versions"), exist_ok=True)
        for sub in ["chats", "notes", "code", "social", "reviews"]:
            os.makedirs(os.path.join(skill_dir, "sources", sub), exist_ok=True)
        print(f"已创建目录结构：{skill_dir}/")


if __name__ == "__main__":
    main()
