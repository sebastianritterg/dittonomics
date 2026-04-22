#!/bin/bash
# post-edit-lint.sh - PostToolUse hook that auto-lints R/Python/Julia files
# after Edit or Write operations. Advisory only (exit 0).
#
# Environment variables set by Claude Code:
#   CLAUDE_TOOL_ARG_FILE_PATH - the file that was edited or written

FILE="${CLAUDE_TOOL_ARG_FILE_PATH:-}"
[[ -z "$FILE" ]] && exit 0

case "$FILE" in
  *.R|*.py|*.jl) ;;
  *) exit 0 ;;
esac

case "$FILE" in
  */.claude/*) exit 0 ;;
esac

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/lint-scripts.sh" "$FILE" 2>/dev/null

exit 0
