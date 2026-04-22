# Maintenance Operations

Dittonomics preserves official Clo-Author hook files as provenance in `references/source-hooks/`, but the active Codex port uses explicit utilities instead of hidden automation.

## Mapping From Upstream Hook Ideas To Dittonomics Utilities

| Upstream idea | Dittonomics utility |
|---|---|
| `pre-compact.py` | `$clo-research-tools checkpoint` |
| `post-compact-restore.py` | `$clo-research-tools resume-context` |
| `post-edit-lint.sh` + `lint-scripts.sh` | `$clo-research-tools verify-edit` |
| `protect-files.sh` | repo-local `AGENTS.md` guidance plus explicit path checks |

## Default Local State Folder

Dittonomics writes local operational state to:

```text
.codex-state/
```

Recommended contents:

```text
.codex-state/
  checkpoints/
    2026-04-22T18-30-00Z_end-of-day.json
    2026-04-22T18-30-00Z_end-of-day.md
  latest.json
  latest.md
  resume-context.md
```

Recommended practice:

- keep `.codex-state/` local to the repo
- add it to `.gitignore` in working research repos unless you explicitly want to share checkpoints
- treat it as operational memory, not canonical research output

## Checkpoint

Use when you want an intentional snapshot before:

- ending the workday
- compacting context
- switching branches or tasks
- handing work to a coauthor or future session

Recommended captured fields:

- current goal
- summary of work completed
- blockers
- open questions
- important files
- best next step
- git branch and recent commits
- key directories and artifacts

Bundled helper:

```text
scripts/checkpoint_context.py
```

## Resume Context

Use when re-entering a repo and you want a fast reconstruction of:

- what the last checkpoint said
- what changed since then
- the current git state
- likely next action

Bundled helper:

```text
scripts/resume_context.py
```

## Verify Edit

Use when you want a manual, explicit post-edit safety pass.

Typical checks:

- lint a touched R, Python, or Julia file
- verify the edited path still resolves
- run a lightweight compile or syntax check when appropriate
- report issues advisory-first

## Porting Rule

Do not introduce hidden automation into the active Codex port unless the user explicitly asks for it and the environment supports it cleanly.
