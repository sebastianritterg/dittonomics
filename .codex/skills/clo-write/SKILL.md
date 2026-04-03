---
name: clo-write
description: Orchestrate economics-paper drafting and revision with explicit section contracts, paragraph planning, design-aware language, and optional proofread handoff. Preserves econ-intro-writing as the governing skill for all front-end work.
---

# Clo Write

Use this skill as the writing-phase orchestrator.

## Kernel References

Read first:

1. `../clo-workflow/references/pipeline-contract.md`
2. `../clo-workflow/references/artifact-contracts.md`
3. `../clo-workflow/references/agent-registry.md`
4. `../clo-workflow/references/routing-rules.md`

Then load the local references for writing:

5. `references/section-contracts.md`
6. `references/writing-workflow.md`

## Delegation Rule

Invoking this skill counts as explicit permission to dispatch the named agents for the resolved writing mode.

- front-end work routes through `econ-intro-writing`
- non-front-end writing routes to `writer`
- optional proofread handoff routes to `clo-review --proofread`
- if subagent dispatch is unavailable, fall back to the main session only with an explicit note

## Input

Recommended invocation:

```text
$clo-write [section] [--mode draft|revise|humanize] [--design did|rdd|iv|scm|generic] [--joint-paper] [--journal-tightening] [--current-draft] [file(optional)]
```

Natural-language equivalents are also valid in the parent task packet:
- `use joint-paper mode`
- `tighten toward JDE benchmark`
- `use the current draft state as calibration`

Supported sections:

- `abstract`
- `intro`
- `context`
- `literature`
- `data`
- `strategy`
- `results`
- `mechanisms`
- `robustness`
- `policy`
- `conclusion`
- `full`
- `humanize`

Accepted aliases:

- `intro`, `introduction` -> `intro`
- `context`, `background` -> `context`
- `literature`, `lit review`, `literature review` -> `literature`
- `strategy`, `empirical strategy`, `methods` -> `strategy`
- `results`, `main results` -> `results`
- `mechanisms`, `channels` -> `mechanisms`
- `robustness`, `checks` -> `robustness`
- `conclusion`, `closing` -> `conclusion`

## Routing

- `intro`, `context`, `literature`, and opening-stack work
  route through `econ-intro-writing` as the governing skill, with repo overlays layered on top
- all other section work
  route to `writer`
- optional proofread handoff
  route to `clo-review --proofread`

## Required Inputs

Common inputs:

- repo-local overlays and path conventions
- active manuscript and section targets
- active bibliography and closest cited papers in the repo
- relevant quality reports

Section-specific inputs:

- `strategy`
  fresh `strategy_memo`
- `results`, `mechanisms`, `robustness`, `policy`
  fresh `results_summary` plus existing tables or figures
- `abstract`
  enough completed manuscript structure to state question, design, and findings

## Drafting Workflow

Unless the user explicitly asks for a lighter pass:

1. resolve the target section and target file
2. gather context from manuscript, notes, bibliography, and quality reports
3. inspect active bibliography and closest cited papers first
4. load section, method, and paper-model references only as needed
5. create outline
6. create paragraph plan
7. draft or revise
8. apply `humanizer`
9. optionally hand off to proofread

## Style Hierarchy

Load and apply prose guidance in this order:
1. `~/voice/core_voice.md`
2. `~/voice/voice_examples.md`
3. `~/voice/econ_paper_register.md`
4. `~/voice/style_hierarchy.md`

For `intro`, `context`, `literature`, and opening-stack work:
- treat this hierarchy as a style layer only
- keep `econ-intro-writing` in charge of structure, paragraph roles, and front-end logic
- if there is any conflict, preserve the intro architecture and adjust wording within it

Optional overlays:
- load `~/voice/collaboration_register.md` only in `--joint-paper` mode
- load `~/voice/journal_tightening_register.md` only in `--journal-tightening` mode
- inspect nearby manuscript sections only in `--current-draft` mode

Current-draft calibration rules:
- use the live draft only for local consistency, compression level, terminology, notation, and rhythm
- do not inherit redundancy, weak transitions, stale phrasing, or padded sentences from the live draft
- treat the live draft as a local calibration source, not a superior authority
- if the live draft conflicts with the core voice, preserve the core voice

## Global Writing Rules

- preserve `econ-intro-writing` as the authority for front-end work
- use examples and paper models as scaffolding, never as copy-paste templates
- treat co-author and JDE materials as overlays, never as replacement voices or literal templates
- never fabricate results, citations, institutional facts, or checks
- use explicit placeholders when evidence is missing
- match causal language to design strength
- use `claim -> support -> implication` paragraph architecture
- keep the parent orchestrator responsible for proofread persistence and workflow transitions
