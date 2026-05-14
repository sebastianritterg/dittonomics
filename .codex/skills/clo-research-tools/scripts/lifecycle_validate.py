#!/usr/bin/env python3
"""Minimal lifecycle validation helper for Dittonomics handoffs."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRES = {
    "discover": [],
    "strategize": ["quality_reports/*research_spec*.md", "quality_reports/*lit*.md"],
    "analyze": ["quality_reports/*strategy*.md"],
    "write": ["quality_reports/*strategy*.md"],
    "submit": ["quality_reports/*review*.md"],
}


def has_match(root: Path, pattern: str) -> bool:
    return any(root.glob(pattern))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate minimal lifecycle inputs for a Dittonomics phase.")
    parser.add_argument("phase", choices=sorted(REQUIRES))
    parser.add_argument("--root", default=".", help="project root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    missing = [pattern for pattern in REQUIRES[args.phase] if not has_match(root, pattern)]
    if missing:
        print(f"Cannot dispatch phase '{args.phase}': missing expected artifact(s).")
        for pattern in missing:
            print(f"  - {pattern}")
        if args.phase == "analyze":
            print("Recommended next step: run $clo-strategize to produce a strategy memo.")
        return 1

    print(f"PASS: lifecycle inputs available for '{args.phase}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
