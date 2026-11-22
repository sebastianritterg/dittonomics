from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from snapshot_research_state import collect_directory_snapshot


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a durable end-of-day or handoff checkpoint.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--state-dir", default=".codex-state", help="Directory where checkpoint files are written.")
    parser.add_argument("--label", default="checkpoint", help="Human label for the checkpoint.")
    parser.add_argument("--scope", default="manual", help="Checkpoint scope, such as end-of-day or handoff.")
    parser.add_argument("--summary", default="", help="Short summary of work completed.")
    parser.add_argument("--goal", default="", help="Current or closing goal.")
    parser.add_argument("--next-step", default="", help="Best next step for the next session.")
    parser.add_argument("--blocker", action="append", default=[], help="Blocker to record. Can be repeated.")
    parser.add_argument("--open-question", action="append", default=[], help="Open question to record. Can be repeated.")
    parser.add_argument("--important-file", action="append", default=[], help="Important file path to record. Can be repeated.")
    parser.add_argument("--note", action="append", default=[], help="Extra note to record. Can be repeated.")
    return parser.parse_args()


def run_git(root: Path, *args: str) -> list[str]:
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def slugify(label: str) -> str:
    keep = []
    for ch in label.strip().lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in {" ", "-", "_"}:
            keep.append("-")
    slug = "".join(keep).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "checkpoint"


def normalize_files(root: Path, values: list[str]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for value in values:
        path = (root / value).resolve() if not Path(value).is_absolute() else Path(value).resolve()
        try:
            relative = path.relative_to(root)
            display = relative.as_posix()
        except ValueError:
            display = str(path)
        items.append({"path": display, "exists": path.exists()})
    return items


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Dittonomics Checkpoint",
        "",
        f"- Checkpoint ID: `{payload['checkpoint_id']}`",
        f"- Created: `{payload['created_at']}`",
        f"- Scope: `{payload['scope']}`",
        f"- Root: `{payload['root']}`",
        "",
        "## Summary",
        "",
        f"- Goal: {payload['goal'] or '(not provided)'}",
        f"- Summary: {payload['summary'] or '(not provided)'}",
        f"- Next step: {payload['next_step'] or '(not provided)'}",
        "",
        "## Blockers",
    ]
    blockers = payload["blockers"] or ["(none recorded)"]
    lines.extend([f"- {item}" for item in blockers])
    lines.extend(["", "## Open Questions"])
    questions = payload["open_questions"] or ["(none recorded)"]
    lines.extend([f"- {item}" for item in questions])
    lines.extend(["", "## Important Files"])
    important_files = payload["important_files"] or [{"path": "(none recorded)", "exists": False}]
    for item in important_files:
        suffix = "" if item["path"] == "(none recorded)" else f" (exists: {str(item['exists']).lower()})"
        lines.append(f"- `{item['path']}`{suffix}")
    lines.extend(["", "## Notes"])
    notes = payload["notes"] or ["(none recorded)"]
    lines.extend([f"- {item}" for item in notes])
    lines.extend(["", "## Git", "", f"- Branch: `{payload['git']['branch'] or '(unknown)'}`", "", "### Status"])
    status = payload["git"]["status"] or ["(clean or unavailable)"]
    lines.extend([f"- `{item}`" for item in status])
    lines.extend(["", "### Recent Commits"])
    commits = payload["git"]["recent_commits"] or ["(unavailable)"]
    lines.extend([f"- `{item}`" for item in commits])
    lines.extend(["", "## Directory Snapshot"])
    for item in payload["directories"]:
        children = ", ".join(item["children"]) if item["children"] else "(empty)"
        lines.append(f"- `{item['path']}`: {children}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    state_dir = (root / args.state_dir).resolve()
    checkpoints_dir = state_dir / "checkpoints"
    checkpoints_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    checkpoint_id = f"{timestamp}_{slugify(args.label)}"

    payload = {
        "schema_version": 1,
        "checkpoint_id": checkpoint_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "scope": args.scope,
        "goal": args.goal.strip(),
        "summary": args.summary.strip(),
        "next_step": args.next_step.strip(),
        "blockers": [item.strip() for item in args.blocker if item.strip()],
        "open_questions": [item.strip() for item in args.open_question if item.strip()],
        "important_files": normalize_files(root, args.important_file),
        "notes": [item.strip() for item in args.note if item.strip()],
        "git": {
            "branch": next(iter(run_git(root, "rev-parse", "--abbrev-ref", "HEAD")), ""),
            "status": run_git(root, "status", "--short"),
            "recent_commits": run_git(root, "log", "--oneline", "-5"),
        },
        "directories": collect_directory_snapshot(root),
    }

    json_path = checkpoints_dir / f"{checkpoint_id}.json"
    md_path = checkpoints_dir / f"{checkpoint_id}.md"
    latest_json = state_dir / "latest.json"
    latest_md = state_dir / "latest.md"

    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(payload), encoding="utf-8")
    shutil.copyfile(json_path, latest_json)
    shutil.copyfile(md_path, latest_md)

    print(md_path)


if __name__ == "__main__":
    main()
