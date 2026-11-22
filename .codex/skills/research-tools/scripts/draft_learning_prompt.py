from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a reusable learnings prompt for the current repo.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--output", default="session_learning_prompt.md", help="Output markdown path.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()
    content = f"""# Session Learnings Prompt

Review recent work in `{root}` and decide whether any reusable insight belongs in project memory.

Checklist:
- Did this session reveal a recurring workflow or failure mode?
- Did it establish a stable naming, documentation, or verification pattern?
- Is the learning generic enough for shared memory, or only local to this machine/project?
- If the insight is machine-specific, keep it in local notes rather than repo-shared guidance.
"""
    output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()




