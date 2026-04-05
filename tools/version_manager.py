#!/usr/bin/env python3
"""
版本管理工具

功能：
  --action save     保存当前版本快照
  --action rollback 回滚到指定版本
  --action history  查看版本历史
"""
import argparse
import json
import os
import shutil
import sys
from datetime import datetime


def _versions_dir(base_dir: str, slug: str) -> str:
    return os.path.join(base_dir, slug, "versions")


def _skill_dir(base_dir: str, slug: str) -> str:
    return os.path.join(base_dir, slug)


VERSIONED_FILES = [
    "SKILL.md", "knowledge.md", "persona.md",
    "identity.md", "social_mirror.md", "meta.json",
]


def save_version(base_dir: str, slug: str, message: str = "") -> None:
    skill_dir = _skill_dir(base_dir, slug)
    versions_dir = _versions_dir(base_dir, slug)
    os.makedirs(versions_dir, exist_ok=True)

    existing = sorted([d for d in os.listdir(versions_dir) if d.startswith("v")])
    next_num = len(existing) + 1
    version_tag = f"v{next_num}"
    version_dir = os.path.join(versions_dir, version_tag)
    os.makedirs(version_dir)

    for fname in VERSIONED_FILES:
        src = os.path.join(skill_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, version_dir)

    manifest = {
        "version": version_tag,
        "created_at": datetime.now().isoformat(),
        "message": message,
        "files": [f for f in VERSIONED_FILES if os.path.exists(os.path.join(skill_dir, f))],
    }
    with open(os.path.join(version_dir, "_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"[{slug}] 已保存 {version_tag}：{message or '(无描述)'}")


def rollback(base_dir: str, slug: str, version: str) -> None:
    version_dir = os.path.join(_versions_dir(base_dir, slug), version)
    if not os.path.isdir(version_dir):
        print(f"版本 {version} 不存在", file=sys.stderr)
        sys.exit(1)

    save_version(base_dir, slug, message=f"rollback 前自动备份")

    skill_dir = _skill_dir(base_dir, slug)
    for fname in VERSIONED_FILES:
        src = os.path.join(version_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, skill_dir)
    print(f"[{slug}] 已回滚到 {version}")


def show_history(base_dir: str, slug: str) -> None:
    versions_dir = _versions_dir(base_dir, slug)
    if not os.path.isdir(versions_dir):
        print("暂无版本记录。")
        return
    versions = sorted([d for d in os.listdir(versions_dir) if d.startswith("v")])
    for v in versions:
        manifest_path = os.path.join(versions_dir, v, "_manifest.json")
        if os.path.exists(manifest_path):
            with open(manifest_path, "r", encoding="utf-8") as f:
                m = json.load(f)
            print(f"  {v}  {m.get('created_at', '?')}  {m.get('message', '')}")
        else:
            print(f"  {v}  (缺少 manifest)")


def main():
    parser = argparse.ArgumentParser(description="myself.skill 版本管理")
    parser.add_argument("--action", choices=["save", "rollback", "history"], required=True)
    parser.add_argument("--base-dir", default="./myselves")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--version", default=None, help="rollback 时指定版本号")
    parser.add_argument("--message", default="", help="save 时的版本描述")
    args = parser.parse_args()

    if args.action == "save":
        save_version(args.base_dir, args.slug, args.message)
    elif args.action == "rollback":
        if not args.version:
            print("--version 参数必填", file=sys.stderr)
            sys.exit(1)
        rollback(args.base_dir, args.slug, args.version)
    elif args.action == "history":
        show_history(args.base_dir, args.slug)


if __name__ == "__main__":
    main()
