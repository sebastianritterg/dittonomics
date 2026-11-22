from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resume context from the latest Dittonomics checkpoint.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--state-dir", default=".codex-state", help="Directory where checkpoint files are stored.")
    parser.add_argument("--checkpoint", default="", help="Optional checkpoint JSON path or checkpoint ID. Defaults to latest.json.")
    parser.add_argument("--output", default="", help="Optional markdown output path. Defaults to .codex-state/resume-context.md.")
    return parser.parse_args()


def run_git(root: Path, *args: str) -> list[str]:
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def resolve_checkpoint(root: Path, state_dir: Path, checkpoint_arg: str) -> Path | None:
    if checkpoint_arg:
        candidate = Path(checkpoint_arg)
        if candidate.suffix == ".json" and candidate.exists():
            return candidate.resolve()
        candidate = state_dir / "checkpoints" / f"{checkpoint_arg}.json"
        if candidate.exists():
            return candidate.resolve()
    latest = state_dir / "latest.json"
    if latest.exists():
        return latest.resolve()
    return None


def render_markdown(root: Path, payload: dict[str, Any] | None) -> str:
    branch = next(iter(run_git(root, "rev-parse", "--abbrev-ref", "HEAD")), "")
    status = run_git(root, "status", "--short")
    commits = run_git(root, "log", "--oneline", "-5")

    lines = [
        "# Dittonomics Resume Context",
        "",
        f"- Root: `{root}`",
        f"- Current branch: `{branch or '(unknown)'}`",
        "",
    ]

    if payload is None:
        lines.extend(
            [
                "## Latest Checkpoint",
                "",
                "No prior checkpoint found.",
                "",
                "## Suggested Next Step",
                "",
                "- Create a fresh checkpoint once you establish the current goal.",
            ]
        )
    else:
        lines.extend(
            [
                "## Latest Checkpoint",
                "",
                f"- Checkpoint ID: `{payload['checkpoint_id']}`",
                f"- Created: `{payload['created_at']}`",
                f"- Scope: `{payload['scope']}`",
                "",
                "## Stored Summary",
                "",
                f"- Goal: {payload.get('goal') or '(not provided)'}",
                f"- Summary: {payload.get('summary') or '(not provided)'}",
                f"- Next step: {payload.get('next_step') or '(not provided)'}",
                "",
                "## Stored Blockers",
            ]
        )
        blockers = payload.get("blockers") or ["(none recorded)"]
        lines.extend([f"- {item}" for item in blockers])
        lines.extend(["", "## Stored Open Questions"])
        questions = payload.get("open_questions") or ["(none recorded)"]
        lines.extend([f"- {item}" for item in questions])
        lines.extend(["", "## Important Files"])
        important_files = payload.get("important_files") or [{"path": "(none recorded)", "exists": False}]
        for item in important_files:
            lines.append(f"- `{item['path']}` (exists now: {str(item.get('exists', False)).lower()})")
        lines.extend(["", "## Suggested Next Step", "", f"- Start from: {payload.get('next_step') or 'review the latest checkpoint and repo status manually.'}"])

    lines.extend(["", "## Current Git Status"])
    status_lines = status or ["(clean or unavailable)"]
    lines.extend([f"- `{item}`" for item in status_lines])
    lines.extend(["", "## Recent Commits"])
    commit_lines = commits or ["(unavailable)"]
    lines.extend([f"- `{item}`" for item in commit_lines])
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    state_dir = (root / args.state_dir).resolve()
    checkpoint_path = resolve_checkpoint(root, state_dir, args.checkpoint)

    payload: dict[str, Any] | None = None
    if checkpoint_path and checkpoint_path.exists():
        payload = json.loads(checkpoint_path.read_text(encoding="utf-8"))

    output_path = Path(args.output).resolve() if args.output else state_dir / "resume-context.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(root, payload), encoding="utf-8")

    print(output_path)


if __name__ == "__main__":
    main()
