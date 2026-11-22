#!/usr/bin/env python3
"""Advisory research-code lint for Dittonomics.

This is intentionally lightweight and portable. It catches grep-able research
workflow hazards before a human or critic agent spends attention on them.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


EXTENSIONS = {".r", ".py", ".jl", ".do"}


@dataclass
class Rule:
    language: str
    severity: str
    pattern: re.Pattern[str]
    message: str


RULES = [
    Rule("all", "HIGH", re.compile(r"([A-Za-z]:\\|/Users/|/home/|/Volumes/)"), "hardcoded absolute path"),
    Rule("r", "HIGH", re.compile(r"\bsetwd\s*\("), "setwd() makes scripts machine-specific"),
    Rule("py", "HIGH", re.compile(r"\bos\.chdir\s*\("), "os.chdir() makes scripts machine-specific"),
    Rule("jl", "HIGH", re.compile(r"^\s*cd\s*\(", re.I), "cd() makes scripts machine-specific"),
    Rule("stata", "HIGH", re.compile(r"^\s*cd\s+['\"]?[A-Za-z]:", re.I), "Stata cd to an absolute path"),
    Rule("all", "HIGH", re.compile(r"\b(install\.packages|pip install|Pkg\.add|ssc install)\b", re.I), "package installation inside analysis code"),
    Rule("r", "MEDIUM", re.compile(r"rm\s*\(\s*list\s*=\s*ls\s*\(\s*\)\s*\)"), "rm(list = ls()) hides state assumptions"),
    Rule("r", "MEDIUM", re.compile(r"(?<![A-Za-z0-9_.])([TF])(?![A-Za-z0-9_.])"), "use TRUE/FALSE, not T/F"),
    Rule("r", "MEDIUM", re.compile(r"\bsapply\s*\("), "sapply() can simplify unpredictably"),
    Rule("r", "MEDIUM", re.compile(r"\battach\s*\(|\bdetach\s*\("), "attach()/detach() obscures variable scope"),
    Rule("r", "MEDIUM", re.compile(r"<<-"), "global assignment with <<-"),
    Rule("r", "LOW", re.compile(r"\b1\s*:\s*[A-Za-z_]"), "1:n patterns fail when n = 0; prefer seq_len()"),
    Rule("py", "MEDIUM", re.compile(r"from\s+\S+\s+import\s+\*"), "wildcard import"),
    Rule("py", "MEDIUM", re.compile(r"^\s*except\s*:"), "bare except catches too much"),
    Rule("py", "MEDIUM", re.compile(r"\beval\s*\("), "eval() in analysis code"),
    Rule("jl", "MEDIUM", re.compile(r"@eval|\beval\s*\("), "runtime eval in Julia code"),
    Rule("stata", "MEDIUM", re.compile(r"^\s*clear\s+all\b", re.I), "clear all may hide workspace assumptions"),
    Rule("stata", "LOW", re.compile(r"^\s*set\s+more\s+off\b", re.I), "set more off is usually fine but should be in the header"),
]


def language_for(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".r":
        return "r"
    if ext == ".py":
        return "py"
    if ext == ".jl":
        return "jl"
    if ext == ".do":
        return "stata"
    return "all"


def iter_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in EXTENSIONS else []
    if target.is_dir():
        return sorted(p for p in target.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONS)
    return []


def lint_file(path: Path) -> list[tuple[int, Rule, str]]:
    lang = language_for(path)
    findings: list[tuple[int, Rule, str]] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        print(f"WARN: could not read {path}: {exc}")
        return findings

    for line_no, line in enumerate(lines, start=1):
        for rule in RULES:
            if rule.language not in {"all", lang}:
                continue
            if rule.pattern.search(line):
                findings.append((line_no, rule, line.strip()))

    text = "\n".join(lines)
    if lang in {"r", "py", "jl"} and re.search(r"\b(sample|runif|rnorm|np\.random|random\.|rand\()", text) and not re.search(r"\b(set\.seed|np\.random\.seed|random\.seed|Random\.seed!)", text):
        findings.append((1, Rule(lang, "HIGH", re.compile("$^"), "stochastic code without an obvious seed"), ""))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Advisory lint for research code.")
    parser.add_argument("target", nargs="?", default=".", help="file or directory to lint")
    parser.add_argument("--strict", action="store_true", help="exit non-zero when findings are present")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    files = iter_files(target)
    if not files:
        print(f"No R/Python/Julia/Stata files found under {target}")
        return 0

    total = 0
    for file in files:
        findings = lint_file(file)
        if not findings:
            continue
        print(f"\n{file}")
        for line_no, rule, excerpt in findings:
            total += 1
            suffix = f" :: {excerpt}" if excerpt else ""
            print(f"  L{line_no} [{rule.severity}] {rule.message}{suffix}")

    if total == 0:
        print(f"PASS: no advisory lint findings in {len(files)} files.")
        return 0

    print(f"\nADVISORY: {total} findings across {len(files)} files.")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
