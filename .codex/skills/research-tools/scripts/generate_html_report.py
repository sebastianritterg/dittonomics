#!/usr/bin/env python3
"""Convert quality-report markdown into a small self-contained HTML report."""

from __future__ import annotations

import argparse
import html
import re
from datetime import datetime
from pathlib import Path


TYPE_PATTERNS = {
    "peer-review": ["*referee*.md", "*editor*.md", "*review*.md"],
    "code-audit": ["*code*.md", "*audit*.md"],
    "strategy-review": ["*strategy*.md"],
    "quality-gate": ["*quality*.md", "*verification*.md"],
    "literature": ["*lit*.md", "*bibliography*.md", "*frontier*.md"],
}


def find_sources(root: Path, report_type: str, explicit: str | None) -> list[Path]:
    if explicit:
        path = (root / explicit).resolve() if not Path(explicit).is_absolute() else Path(explicit)
        return [path] if path.exists() else []
    base = root / "quality_reports"
    if not base.exists():
        return []
    files: list[Path] = []
    for pattern in TYPE_PATTERNS[report_type]:
        files.extend(base.rglob(pattern))
    return sorted(set(files), key=lambda p: p.stat().st_mtime, reverse=True)[:12]


def markdownish(text: str) -> str:
    out = []
    for raw in text.splitlines():
        line = html.escape(raw)
        if line.startswith("# "):
            out.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{line[4:]}</h3>")
        elif re.match(r"^\s*[-*]\s+", raw):
            out.append(f"<p class='bullet'>{line}</p>")
        elif line.strip():
            out.append(f"<p>{line}</p>")
        else:
            out.append("")
    return "\n".join(out)


def render(root: Path, report_type: str, sources: list[Path]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sections = []
    if not sources:
        sections.append("<section><p class='empty'>No matching source reports found.</p></section>")
    for source in sources:
        rel = html.escape(str(source.relative_to(root)) if source.is_relative_to(root) else str(source))
        body = markdownish(source.read_text(encoding="utf-8", errors="replace"))
        sections.append(f"<section><h2><code>{rel}</code></h2>{body}</section>")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dittonomics {html.escape(report_type)} report</title>
<style>
:root {{ --bg:#f6f2ea; --ink:#18221f; --muted:#6c7b77; --line:#d9d0c2; --accent:#0d6b61; }}
body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; background:var(--bg); color:var(--ink); }}
main {{ max-width:920px; margin:0 auto; padding:32px 22px 72px; }}
h1 {{ font-size:2.2rem; }}
section {{ border-top:1px solid var(--line); margin-top:28px; padding-top:20px; }}
code {{ font-family:'Cascadia Code','JetBrains Mono',monospace; font-size:.9rem; }}
.muted,.empty {{ color:var(--muted); }}
.bullet {{ padding-left:1rem; }}
@media print {{ body {{ background:white; }} }}
</style>
</head>
<body><main>
<h1>Dittonomics {html.escape(report_type)} report</h1>
<p class="muted">Generated {html.escape(now)} from <code>{html.escape(str(root))}</code>.</p>
{''.join(sections)}
</main></body></html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a local HTML report from quality_reports.")
    parser.add_argument("report_type", choices=sorted(TYPE_PATTERNS))
    parser.add_argument("source", nargs="?", help="optional source markdown file")
    parser.add_argument("--root", default=".", help="project root")
    parser.add_argument("--output", help="output HTML path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    sources = find_sources(root, args.report_type, args.source)
    output_arg = args.output or f"quality_reports/html/{args.report_type}_report.html"
    output = (root / output_arg).resolve() if not Path(output_arg).is_absolute() else Path(output_arg)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(root, args.report_type, sources), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
