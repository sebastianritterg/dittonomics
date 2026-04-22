---
name: clo-research-tools
description: Utility toolbox for maintenance, compilation, validation, checkpoint or resume, edit verification, upgrade, and project administration. Not a pipeline phase.
---

# Clo Research Tools

Use this skill for utilities and maintenance, not for a research phase.

## Kernel References

Read:

1. `../clo-workflow/references/routing-rules.md` when path resolution or persistence policy matters
2. `references/maintenance-operations.md` when the task involves checkpointing, recovery, edit verification, or upstream hook provenance

## Toolbox Role

This skill does not own discovery, strategy, analysis, writing, review, or submission logic.

It provides lightweight support commands such as:

- `commit [message]`
- `compile [file]`
- `validate-bib`
- `journal`
- `context`
- `checkpoint [scope(optional)]`
- `resume-context [scope(optional)]`
- `verify-edit [path(optional)]`
- `deploy`
- `learn`
- `upgrade`

## Subcommand Notes

- `checkpoint`
  creates an explicit state snapshot under `.codex-state/` and is the end-of-day or handoff command
- `resume-context`
  reconstructs working context from the latest checkpoint plus current repo state
- `verify-edit`
  runs an explicit advisory post-edit verification pass instead of hidden lint hooks
- `context`
  reports session health and likely relevant artifacts without mutating files
- `upgrade`
  updates workflow infrastructure while preserving repo content and local customizations

## File Format And Scripts

The default local state folder is:

```text
.codex-state/
  checkpoints/
    2026-04-22T18-30-00Z_end-of-day.json
    2026-04-22T18-30-00Z_end-of-day.md
  latest.json
  latest.md
  resume-context.md
```

The bundled helper scripts are:

- `scripts/checkpoint_context.py`
- `scripts/resume_context.py`
- `scripts/snapshot_research_state.py`
- `scripts/draft_learning_prompt.py`

The JSON files are the durable machine-readable layer.
The Markdown files are the human-readable layer.

### `$clo-research-tools commit [message]` - Git Commit

Stage changes, create commit, optionally create PR and merge.

- Run git status to identify changes
- Stage relevant files, never staging secrets or credentials
- Create a descriptive message
- If a quality score exists and is `>= 80`, note it in the commit body if useful

### `$clo-research-tools compile [file]` - LaTeX Compilation

3-pass XeLaTeX plus BibTeX compilation for papers or talks.

### `$clo-research-tools validate-bib` - Bibliography Validation

Cross-reference all `\cite{}` keys in paper and talk files against the active bibliography.
Report missing entries, duplicate keys, or unused entries.

### `$clo-research-tools journal` - Research Journal

Regenerate or summarize the research journal timeline from quality reports and git history.

### `$clo-research-tools context` - Context Status

Show current session health without mutating files.
Check the branch, likely relevant artifacts, and what the latest checkpoint captured.

### `$clo-research-tools checkpoint [scope]` - End-Of-Day Or Handoff Snapshot

Create an explicit checkpoint before stopping work, compacting context, or handing work to a collaborator.

Typical captured fields:

- current goal
- summary of work completed
- blockers
- open questions
- important files
- best next step
- git branch and recent commits
- key project directories

Recommended usage:

```text
Use $clo-research-tools checkpoint for this repo. Capture today's goal, what we finished, blockers, important files, and the best next step.
```

### `$clo-research-tools resume-context [scope]` - Reconstruct Working Context

Read the most recent checkpoint and combine it with current repo state so the next session starts with a clear brief.

Recommended usage:

```text
Use $clo-research-tools resume-context for this repo. Reconstruct where we left off, what matters now, and the best next action.
```

### `$clo-research-tools verify-edit [path]` - Advisory Post-Edit Check

Run a lightweight, explicit post-edit safety pass.

Typical checks:

- lint touched R, Python, or Julia files when applicable
- verify edited paths still resolve
- run lightweight compile or syntax checks when appropriate
- report issues advisory-first instead of mutating automatically

### `$clo-research-tools deploy` - Deploy Guide Site

Render the Quarto guide site and publish to GitHub Pages when the repo uses Quarto docs.

### `$clo-research-tools learn` - Extract Learnings

Draft reusable learning prompts for patterns worth saving into project or personal memory.

### `$clo-research-tools upgrade` - Upgrade Dittonomics Or Clo-Author Infrastructure

Update workflow infrastructure while preserving repo content and local customizations.

## Principles

- **Each subcommand is lightweight.** No multi-agent orchestration needed.
- **Compile stays explicit.** Build or lint only when it helps the current task.
- **validate-bib catches drift.** Run it before commits or submission.
- **Checkpoint and resume are explicit.** Do not rely on hidden automation for context continuity.
- **Upgrade preserves content.** Infrastructure changes, your paper does not.
