# `.codex` Starter Bundle

This folder is the public, forkable Codex-facing starter layer for Dittonomics.

It is included in the repo so users can fork something structurally similar to the upstream `.claude/` distribution in Clo-Author, but adapted for Codex.

## What Is Here

- `AGENTS.md`: starter user-level constitution
- `agents/`: custom subagent templates
- `skills/`: `clo-*` workflow skills and references
- `WORKFLOW_QUICK_REF.md`: short workflow summary

## How To Use It

Option 1: copy or merge this folder into your own `~/.codex/` home

Option 2: keep it in the fork as a visible starter kit and selectively copy pieces into your machine-specific Codex setup

## Important Distinction

This repo-level `.codex/` directory is a distributable starter, not a claim that Codex auto-loads repo-local `.codex` the way Claude uses repo-local `.claude`.

For project-specific behavior inside a research repo, still use:

- `AGENTS.md`
- `AGENTS.override.md`
- `.agents/skills/`
- `explorations/`

