# Dittonomics Starter for Codex

This file is part of the public starter bundle in this repository. Copy or adapt `.codex/` into your own `~/.codex/` home if you want a user-level Dittonomics setup.

## Core Principles

- The main Codex session is the orchestrator. Custom subagents are narrow specialists.
- Preserve worker-critic separation: creators create, critics, editors, and referees review, verifier checks mechanics.
- Respect repository-local guidance before generic defaults.
- Treat paper, output, and code paths as repository-specific. Inspect the repo before assuming `paper/`, `figures/`, or `tables/`.
- Use explicit skills, artifacts, and prompts instead of hidden hooks or slash-command assumptions.
- Let the parent orchestrator own persistence unless it explicitly delegates a named write target.
- Treat paper libraries, examples, and references as guidance layers. For empirical questions, current web search may be needed because the frontier moves.

## Install Locations

- User skills live in `~/.codex/skills`.
- Custom subagents live in `~/.codex/agents`.
- Repo-local skills live under `.agents/skills` inside each workspace.
- Optional voice files live under `~/voice`.

## Active Roles

- Ideation: `ideator`, `ideator_critic`
- Discovery: `librarian`, `librarian_critic`, `explorer`, `explorer_critic`
- Strategy: `strategist`, `strategist_critic`
- Execution: `coder`, `coder_critic`, `data_engineer`
- Writing: `writer`, `writer_critic`
- Peer review: `editor`, `domain_referee`, `methods_referee`
- Presentation: `storyteller`, `storyteller_critic`
- Verification: `verifier`

## Workflow Expectations

- Ideation should screen a seed idea, convert it into ranked research questions, and record a pursue/refine/park/kill decision before discovery when the question is still fluid.
- Discovery should produce a research spec, literature map, and data assessment before strategy work.
- Strategy should define the estimand, design, assumptions, robustness plan, and falsification tests before coding.
- Analysis defaults to Python first and Stata second unless repo guidance says otherwise. R and Julia remain supported.
- Use a repo-level `explorations/` sandbox for experiments and prototypes. If exploratory work is needed and the folder is missing, create `explorations/README.md` and `explorations/ARCHIVE/` first.
- Peer review should include editor-led journal calibration when you invoke the review workflow in journal mode.
- Submission workflows should not bypass verification or replication checks.
- Writing voice is optional and should be treated as a style layer, not as a substitute for evidence or structure.

## Quality Gates

- `>= 80`: commit-ready
- `>= 90`: merge-ready
- `>= 95` with no weak component: submission-ready

## Voice Layer

If you want a reusable prose layer, create `~/voice/` with files such as:

- `core_voice.md`
- `voice_examples.md`
- `econ_paper_register.md`
- `style_hierarchy.md`
- optional overlays for collaboration or journal tightening

Keep that layer explicit, optional, and user-owned.

## Hook Adaptation

- Do not assume hidden file-protection or compaction hooks exist.
- If context continuity matters, use the explicit snapshot utilities in `$clo-research-tools`.
- Use `.codex-state/` as the default local checkpoint folder for end-of-day snapshots and resume-context files.
- Prefer `$clo-research-tools checkpoint`, `$clo-research-tools resume-context`, and `$clo-research-tools verify-edit` over hidden background automation.
- If a repository needs stricter protected-path handling, express it in repo `AGENTS.override.md` or repo-local skills.
