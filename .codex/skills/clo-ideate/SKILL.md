---
name: clo-ideate
description: Ideation-phase orchestrator for screening seed ideas, turning them into research questions, and deciding what is worth taking into discovery.
---

# Clo Ideate

Use this skill for the ideation phase only.

## Kernel References

Read the canonical workflow files first:

1. `../clo-workflow/references/pipeline-contract.md`
2. `../clo-workflow/references/artifact-contracts.md`
3. `../clo-workflow/references/agent-registry.md`
4. `../clo-workflow/references/routing-rules.md`
5. `references/ideation-playbook.md`
6. `references/evaluation-rubric.md`

Then inspect repo-local notes, the current bibliography, draft fragments, and any existing question memos.

## Delegation Rule

Invoking this skill counts as explicit permission to dispatch the ideation creator and critic pair when the resolved mode calls for them.

- `seed`, `brainstorm`, and `rq` may run with `ideator`
- `evaluate`, `decide`, and `session` should route through `ideator -> ideator_critic`
- if subagent dispatch is unavailable, fall back to the main session only with an explicit note to the user

## Modes

- `session [topic]`
- `seed [topic]`
- `brainstorm [topic]`
- `rq [topic or idea]`
- `evaluate [idea]`
- `decide [idea or shortlist]`

If no mode is supplied, default to `session`.

## Mode Normalization

Canonical modes:

- `session`
- `seed`
- `brainstorm`
- `rq`
- `evaluate`
- `decide`

Accepted aliases:

- `idea`, `ideas`, `ideate`, `full`, `full pass`, `workshop` -> `session`
- `seed`, `topic`, `premise`, `intuition`, `hunch` -> `seed`
- `brainstorm`, `diverge`, `options`, `generate`, `expand` -> `brainstorm`
- `rq`, `research question`, `question`, `questionize` -> `rq`
- `evaluate`, `screen`, `stress-test`, `score` -> `evaluate`
- `decide`, `verdict`, `go-no-go`, `choose` -> `decide`

If no recognized token is present:

1. infer from the first content word and the rest of the request
2. if the user seems to want a full early-stage pass, resolve to `session`
3. if the user clearly wants question conversion, resolve to `rq`
4. if the user clearly wants screening or go-no-go, resolve to `evaluate`
5. otherwise resolve to `seed`

Only ask the user a short question when the request is genuinely ambiguous.

Equivalent supported examples:

- `clo-ideate session [topic]`
- `clo-ideate idea [topic]`
- `clo-ideate brainstorm from this dataset`
- `clo-ideate rq from this vague idea`
- `clo-ideate evaluate this idea`
- `clo-ideate decide between these two questions`

## Agents By Mode

- `seed`
  `ideator`
- `brainstorm`
  `ideator`
- `rq`
  `ideator`
- `evaluate`
  `ideator -> ideator_critic`
- `decide`
  `ideator -> ideator_critic`
- `session`
  `ideator -> ideator_critic`

## Required Inputs

Common inputs:

- repo-local guidance and folder layout
- any existing notes, seed ideas, memos, or bibliography files
- target field, journal, or audience if known
- any constraints the user already knows: data access, time, methods, setting

Mode-specific:

- `brainstorm`
  a topic, dataset, phenomenon, or institutional setting
- `rq`
  a rough idea, dataset, or phenomenon to convert into candidate questions
- `evaluate` and `decide`
  at least one concrete idea, draft question, or shortlist

## Generated Artifacts

- `seed`
  `idea_brief`
- `brainstorm`
  `rq_shortlist`
- `rq`
  `rq_shortlist`
- `evaluate`
  `idea_screen`
- `decide`
  `idea_screen`
- `session`
  `idea_brief`, `rq_shortlist`, `idea_screen`

The parent orchestrator chooses the exact save locations using the artifact contract.

## Ideation Rules

1. Start repo-notes-first and bibliography-first before using any global examples or broad external search.
2. For empirical ideas, closest-paper threat scanning is mandatory before recommending `pursue`.
3. For empirical ideas, every serious question needs at least a provisional identification sketch and data sketch.
4. Current web or working-paper searching can supplement the ideation pass when the frontier is moving, but papers and libraries remain guidance layers rather than sole truth.
5. Include at least one fast-fail test that could kill or rescue the idea quickly.
6. Separate ideation from discovery: do not pretend this phase replaces a real literature review or data assessment.
7. Creator/critic pairing is mandatory in `session`, `evaluate`, and `decide` unless the user explicitly asks for a lighter creator-only pass.
8. `clo-discover ideate` is treated as a legacy alias; route it here rather than burying ideation inside discovery.
