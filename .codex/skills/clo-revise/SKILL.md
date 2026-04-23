---
name: clo-revise
description: Strategic post-submission revision orchestrator for roadmap planning, DAG validation, execution routing, and response-letter drafting.
---

# Clo Revise

Use this skill for real editor or referee revision cycles.

## Kernel References

Read the canonical workflow files first:

1. `../clo-workflow/references/pipeline-contract.md`
2. `../clo-workflow/references/artifact-contracts.md`
3. `../clo-workflow/references/agent-registry.md`
4. `../clo-workflow/references/routing-rules.md`
5. `references/strategic-revision-playbook.md`
6. `references/task-graph-schema.md`
7. `references/response-protocol.md`

Then inspect repo-local overlays, the live manuscript, outputs, and all real review documents.

## Delegation Rule

Invoking this skill counts as explicit permission to dispatch the strategic revision planner pair when roadmap work is requested.

- `roadmap` should dispatch `revision_planner -> revision_planner_critic`
- `validate` may run in the main session or through the validator script
- `execute` routes approved tasks into `writer`, `coder`, `data_engineer`, and existing review lanes
- `respond` uses the roadmap artifacts plus manuscript changes to draft the response package

If subagent dispatch is unavailable, fall back to the main session only with an explicit note to the user.

## Modes

- `roadmap [review-files] [paper]`
- `validate [revision-task-graph]`
- `execute [roadmap-or-task-graph]`
- `respond [review-files] [paper]`

If no mode is supplied, default to `roadmap`.

## Mode Normalization

Canonical modes:

- `roadmap`
- `validate`
- `execute`
- `respond`

Accepted aliases:

- `revise`, `revision`, `rr`, `r&r`, `plan revision`, `reviewer roadmap` -> `roadmap`
- `validate`, `dag`, `check graph`, `validate dependencies` -> `validate`
- `execute`, `run roadmap`, `route tasks`, `start revision work` -> `execute`
- `respond`, `response`, `response letter`, `draft response` -> `respond`

If no recognized token is present:

1. infer from the first content word and the rest of the request
2. if the user supplied real review reports or asks for a revision plan, resolve to `roadmap`
3. if the user supplied a task graph or asks for dependency checking, resolve to `validate`
4. if the user asks to start doing approved tasks, resolve to `execute`
5. if the user asks for the journal-facing letter, resolve to `respond`

Only ask the user a short question when the request is genuinely ambiguous.

## Required Inputs

Common inputs:

- editor and reviewer reports
- submitted manuscript or current revision draft
- repo-local guidance and folder layout
- latest outputs or scripts when empirical requests appear

Mode-specific:

- `validate`
  `revision_task_graph.json`
- `execute`
  approved roadmap or task graph plus any relevant outputs
- `respond`
  roadmap artifacts, decision log, and current manuscript changes

## Generated Artifacts

- `roadmap`
  `revision_task_graph`, `revision_roadmap`, `revision_decision_log`, `response_matrix`
- `validate`
  validator summary and any graph repair notes
- `execute`
  updated task statuses plus routed writing or analysis tasks
- `respond`
  `response_matrix`, `response_letter`

The parent orchestrator chooses the exact save locations using the artifact contract.

## Workflow

### `roadmap`

1. read every review file and the live manuscript
2. extract atomic reviewer tasks with traceable source ids and quotes
3. classify each task
4. map hard dependencies and collateral risks
5. assign execution blocks and coauthor sync points
6. flag disagreement, partial-concession, and go/no-go items
7. dispatch `revision_planner`
8. dispatch `revision_planner_critic`
9. save or return the task graph, roadmap, decision log, and response matrix

### `validate`

1. load the structured task graph
2. run `scripts/dag_validator.py`
3. fail on:
   - unknown task references
   - cycles
   - invalid block order when blocks are assigned
4. report:
   - task count
   - dependency count
   - parallel batches
   - critical path
   - bottlenecks when available

### `execute`

1. read the approved roadmap and decision log
2. route each approved task:
   - writing or clarification -> `writer`
   - new empirical work -> `coder` or `data_engineer`
   - high-stakes decisions -> user
3. after major outputs land, recommend or trigger `clo-review` where appropriate
4. update the task graph or tracker state

### `respond`

1. read the roadmap, decision log, response matrix, and current manuscript changes
2. draft the journal-facing response package
3. preserve reviewer traceability and manuscript location references
4. flag any still-pending analyses or unresolved decisions instead of fabricating completion

## Strategic Revision Rules

1. Atomic extraction is mandatory; do not collapse multi-part reviewer comments into one vague task.
2. Keep reviewer traceability in every artifact.
3. Distinguish hard dependencies from collateral risks.
4. Disagreement and partial concession items must be explicit in the decision log and visible to the user.
5. Do not auto-execute conclusion-changing empirical requests without user visibility.
6. Use repo-first guidance, manuscript structure, outputs, and bibliography before fallback references.
7. This workflow is a loop back into analyze, write, and review, not a standalone terminal step.
8. The response letter must never imply that a pending task is already complete.
