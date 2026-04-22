#!/bin/bash
# Placeholder preserved from upstream provenance.
# The active Codex port uses explicit verify-edit utilities instead of automatic hooks.

set -euo pipefail

FILE="${1:-}"
[[ -z "$FILE" ]] && exit 0

case "$FILE" in
  *.py)
    command -v python3 >/dev/null 2>&1 && python3 -m py_compile "$FILE" || true
    ;;
  *.R)
    command -v Rscript >/dev/null 2>&1 && Rscript -e "parse(file = '$FILE')" >/dev/null 2>&1 || true
    ;;
  *.jl)
    command -v julia >/dev/null 2>&1 && julia -e "include(\"$FILE\")" >/dev/null 2>&1 || true
    ;;
esac
