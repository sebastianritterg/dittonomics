#!/usr/bin/env python3
"""Generate a self-contained Dittonomics project dashboard."""

from __future__ import annotations

import argparse
import html
from datetime import datetime
from pathlib import Path


SECTIONS = [
    ("overview", "Overview"),
    ("reports", "Quality Reports"),
    ("paper", "Paper"),
    ("code", "Code"),
    ("data", "Data"),
    ("state", "State"),
]


def count_files(root: Path, patterns: list[str]) -> int:
    return sum(1 for pattern in patterns for _ in root.glob(pattern))


def latest_files(root: Path, folder: str, limit: int = 8) -> list[Path]:
    base = root / folder
    if not base.exists():
        return []
    files = [p for p in base.rglob("*") if p.is_file()]
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)[:limit]


def list_items(paths: list[Path], root: Path) -> str:
    if not paths:
        return "<p class='empty'>No files found yet.</p>"
    items = []
    for path in paths:
        rel = html.escape(str(path.relative_to(root)))
        ts = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        items.append(f"<li><code>{rel}</code><span>{ts}</span></li>")
    return "<ul class='file-list'>" + "\n".join(items) + "</ul>"


def render(root: Path) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    stats = {
        "reports": count_files(root, ["quality_reports/**/*.md", "quality_reports/**/*.json"]),
        "paper": count_files(root, ["paper/**/*.tex", "06_paper/**/*.tex"]),
        "code": count_files(root, ["scripts/**/*.*", "03_code/**/*.*"]),
        "data": count_files(root, ["data/**/*.*", "02_data/**/*.*"]),
    }
    nav = "".join(f"<a href='#{sid}'>{label}</a>" for sid, label in SECTIONS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dittonomics Project Dashboard</title>
<style>
:root {{ --bg:#f6f2ea; --ink:#18221f; --muted:#6c7b77; --line:#d9d0c2; --accent:#0d6b61; --warm:#e38852; }}
body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; background:var(--bg); color:var(--ink); }}
.page {{ max-width:1100px; margin:0 auto; padding:32px 22px 64px; }}
nav {{ position:sticky; top:0; background:var(--bg); border-bottom:1px solid var(--line); padding:12px 0; display:flex; gap:16px; flex-wrap:wrap; }}
nav a {{ color:var(--accent); text-decoration:none; font-weight:700; }}
h1 {{ font-size:2.4rem; margin-bottom:4px; }}
.muted {{ color:var(--muted); }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin:24px 0; }}
.stat {{ border:1px solid var(--line); background:rgba(255,255,255,.55); padding:14px; border-radius:8px; }}
.stat strong {{ display:block; font-size:1.7rem; }}
section {{ scroll-margin-top:70px; border-top:1px solid var(--line); padding-top:26px; margin-top:26px; }}
.file-list {{ list-style:none; padding:0; }}
.file-list li {{ display:flex; justify-content:space-between; gap:18px; border-bottom:1px solid var(--line); padding:8px 0; }}
code {{ font-family:'Cascadia Code','JetBrains Mono',monospace; font-size:.9rem; }}
.empty {{ color:var(--muted); font-style:italic; }}
@media print {{ nav {{ display:none; }} }}
</style>
</head>
<body>
<div class="page">
<h1>Dittonomics Project Dashboard</h1>
<p class="muted">Generated {html.escape(now)} from <code>{html.escape(str(root))}</code>.</p>
<nav>{nav}</nav>
<section id="overview"><h2>Overview</h2><div class="stats">
<div class="stat"><strong>{stats['reports']}</strong>quality report files</div>
<div class="stat"><strong>{stats['paper']}</strong>paper tex files</div>
<div class="stat"><strong>{stats['code']}</strong>code files</div>
<div class="stat"><strong>{stats['data']}</strong>data files</div>
</div></section>
<section id="reports"><h2>Quality Reports</h2>{list_items(latest_files(root, 'quality_reports'), root)}</section>
<section id="paper"><h2>Paper</h2>{list_items(latest_files(root, 'paper') + latest_files(root, '06_paper'), root)}</section>
<section id="code"><h2>Code</h2>{list_items(latest_files(root, 'scripts') + latest_files(root, '03_code'), root)}</section>
<section id="data"><h2>Data</h2>{list_items(latest_files(root, 'data') + latest_files(root, '02_data'), root)}</section>
<section id="state"><h2>State</h2>{list_items(latest_files(root, '.codex-state'), root)}</section>
</div>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Dittonomics project dashboard.")
    parser.add_argument("--root", default=".", help="project root")
    parser.add_argument("--output", default="quality_reports/html/project_dashboard.html", help="output HTML path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = (root / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(root), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
