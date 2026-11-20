#!/usr/bin/env python3
"""Synchronize local Agent Skills through ~/.agents/skills."""

from __future__ import annotations

import argparse
import filecmp
import os
import shutil
from pathlib import Path


DEFAULT_TARGETS = [
    "~/.codex/skills",
    "~/.claude/skills",
    "~/.cursor/skills",
    "~/.opencode/skills",
    "~/.github-copilot/skills",
    "~/.config/github-copilot/skills",
    "~/.gemini/skills",
    "~/.cline/skills",
    "~/.warp/skills",
    "~/.trae/skills",
    "~/.qoder/skills",
    "~/.kimi/skills",
]


IGNORE_NAMES = {
    ".DS_Store",
    "__pycache__",
    ".git",
    "node_modules",
}


def expand(path: str) -> Path:
    return Path(os.path.expandvars(os.path.expanduser(path))).resolve()


def skill_dirs(root: Path, include_system: bool) -> list[Path]:
    if not root.exists():
        return []
    result: list[Path] = []
    for child in sorted(root.iterdir(), key=lambda p: p.name):
        if not child.is_dir():
            continue
        if child.name.startswith(".") and not include_system:
            continue
        if (child / "SKILL.md").is_file():
            result.append(child)
    return result


def same_tree(left: Path, right: Path) -> bool:
    cmp = filecmp.dircmp(left, right, ignore=sorted(IGNORE_NAMES))
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    return all(same_tree(left / sub, right / sub) for sub in cmp.common_dirs)


def copy_skill(src: Path, dst: Path, apply: bool, overwrite: bool) -> str:
    if not dst.exists():
        if apply:
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*IGNORE_NAMES))
        return "copy"

    if same_tree(src, dst):
        return "unchanged"

    if not overwrite:
        return "conflict"

    if apply:
        shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*IGNORE_NAMES))
    return "overwrite"


def sync_many(
    source_root: Path,
    target_root: Path,
    apply: bool,
    overwrite: bool,
    include_system: bool,
) -> tuple[int, int]:
    actions = 0
    conflicts = 0
    if not source_root.exists():
        print(f"skip missing-source {source_root}")
        return actions, conflicts

    if not target_root.exists():
        print(f"skip missing-target {target_root}")
        return actions, conflicts

    for src in skill_dirs(source_root, include_system):
        dst = target_root / src.name
        status = copy_skill(src, dst, apply, overwrite)
        print(f"{status:9} {src} -> {dst}")
        if status in {"copy", "overwrite"}:
            actions += 1
        elif status == "conflict":
            conflicts += 1
    return actions, conflicts


def default_source() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return expand(str(Path(codex_home) / "skills"))
    return expand("~/.codex/skills")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync skills from the current tool to ~/.agents/skills, then to existing tool skill directories."
    )
    parser.add_argument("--source", default=str(default_source()), help="Current tool skills directory.")
    parser.add_argument("--hub", default="~/.agents/skills", help="Shared skills hub directory.")
    parser.add_argument("--targets", nargs="*", default=None, help="Target skills directories. Existing directories only.")
    parser.add_argument("--apply", action="store_true", help="Write changes. Without this, only prints a dry run.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing differing skill folders.")
    parser.add_argument("--include-system", action="store_true", help="Include hidden/system skill folders such as .system.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = expand(args.source)
    hub = expand(args.hub)
    targets = [expand(p) for p in (args.targets if args.targets is not None else DEFAULT_TARGETS)]

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"mode {mode}")
    print(f"source {source}")
    print(f"hub {hub}")

    if args.apply:
        hub.mkdir(parents=True, exist_ok=True)

    actions, conflicts = sync_many(source, hub, args.apply, args.overwrite, args.include_system)

    for target in targets:
        if target == hub or target == source:
            continue
        a, c = sync_many(hub, target, args.apply, args.overwrite, args.include_system)
        actions += a
        conflicts += c

    print(f"summary actions={actions} conflicts={conflicts}")
    if conflicts:
        print("hint rerun with --overwrite only if replacing target skill copies is intended")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
