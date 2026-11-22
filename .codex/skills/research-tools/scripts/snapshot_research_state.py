from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


CANDIDATE_DIRS = [
    "quality_reports",
    ".codex-state",
    "06_paper",
    "paper",
    "talks",
    "figures",
    "tables",
    "04_outputs",
    "03_code",
    "scripts",
    "01_docs",
]


def collect_directory_snapshot(root: Path, max_children: int = 10) -> list[dict[str, Any]]:
    snapshot: list[dict[str, Any]] = []
    for rel in CANDIDATE_DIRS:
        path = root / rel
        if not path.exists():
            continue
        children = sorted(p.name for p in path.iterdir())[:max_children]
        snapshot.append({"path": rel, "children": children})
    return snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Snapshot the current research-project state.")
    parser.add_argument("--root", default=".", help="Repository root to inspect.")
    parser.add_argument("--output", default="research_state_snapshot.md", help="Output markdown path.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()

    lines = ["# Research State Snapshot", "", f"- Root: `{root}`", "", "## Key Directories"]
    for item in collect_directory_snapshot(root):
        children = ", ".join(item["children"]) or "(empty)"
        lines.append(f"- `{item['path']}`: {children}")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
