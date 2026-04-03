---
name: clo-workflow
description: Canonical workflow kernel for the Codex adaptation of clo-author. Defines pipeline phases, artifact contracts, routing rules, agent families, path resolution, and quality gates.
---

# Clo Workflow

Use this skill as the canonical operating contract for the `clo-*` stack.

## What It Governs

- pipeline phases and their dependencies
- quality gates between phases
- artifact names, freshness expectations, and handoffs
- valid agent families and creator/critic separation
- task-packet fields passed from orchestrators to agents
- path-resolution policy and persistence ownership
- precedence rules across repo-local guidance, skill references, and global defaults

## Read Order

1. `references/pipeline-contract.md`
2. `references/artifact-contracts.md`
3. `references/agent-registry.md`
4. `references/routing-rules.md`
5. `references/domain-profile.md` only for field calibration
6. `references/journal-profiles.md` only for journal calibration
7. `references/explorations.md` only when exploratory sandbox work is needed
8. `references/translation-map.md` and `references/source-*` only when upstream provenance matters

## Global Rules

1. The main Codex session is always the orchestrator.
2. Repo-local rules, repo-local skills, `AGENTS.override.md`, and active manuscript conventions beat generic defaults.
3. Treat path conventions from upstream Clo-Author as fallbacks only.
4. Skills orchestrate. Creator agents create. Critics/referees/editors evaluate. The verifier checks mechanics.
5. The parent orchestrator owns persistence, report saving, and file promotion unless it explicitly delegates a named write target.
6. Use a shared task packet rather than ad hoc per-agent routing language.
7. Prefer the active bibliography and closest cited papers in the repo before any global reference library.
8. Hidden hooks are not ported. Use explicit skills, artifacts, and review steps instead.
