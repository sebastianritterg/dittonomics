# Strategic Revision Playbook

This playbook upgrades revision-after-review from a flat checklist into a strategic workflow.

Use it when real editor or referee reports already exist.

## Phase 1: Atomic Parsing

Extract every distinct reviewer request as a separate task.

Rules:

- split multi-part comments into multiple tasks
- preserve a verbatim quote or faithful abbreviated quote
- write each task as an imperative action
- mark completed requests, but keep them in the map for traceability

Minimum columns:

- task id
- reviewer source
- verbatim quote
- atomic task

## Phase 2: Classification

Assign each task exactly one primary category:

- `EMPIRICAL`
- `ARGUMENTATIVE`
- `STRUCTURAL`
- `CLARIFICATION`
- `EDITORIAL`
- `DECISION`

Use `DECISION` when the task requires author judgment, strategic pushback, or a go/no-go call before execution.

## Phase 3: Dependency Mapping

Distinguish two relationship types:

- structural dependency
  `Task B` cannot be completed before `Task A`
- collateral risk
  `Task A` may change the answer, relevance, or wording of `Task B`, but does not strictly block it

Use structural dependencies in the task graph.
Keep collateral risks as informational links.

## Phase 4: Validation

Validate the graph before execution.

Minimum checks:

- no missing dependency references
- no cycles
- no invalid block order once execution blocks are assigned

Optional richer checks:

- critical path
- parallel batches
- bottleneck tasks

## Phase 5: Execution Blocks

Sequence work into blocks that can be explained to coauthors.

Recommended block logic for empirical papers:

- `A`: core empirical and data-changing tasks
- `B`: robustness, sub-analyses, alternative specifications
- `C`: theory, framing, and interpretation updates
- `D`: section rewrites, structure, and response integration
- `E`: polish, exhibits, cross-references, and final consistency

Adapt block names when the paper is not empirical, but preserve the dependency logic.

## Phase 6: Risk And Decision Points

Every roadmap should flag:

- reviewer conflicts
- disagreement candidates
- results-sensitive tasks that could change conclusions
- coauthor sync points
- explicit go/no-go moments

## Phase 7: Execution And Response

After the roadmap is approved:

- route empirical tasks to `coder` or `data_engineer`
- route clarifications and rewrites to `writer`
- route review-ready outputs back to `clo-review` when needed
- use the `response_matrix` and `decision_log` to build the final response letter

## Boundary

This workflow plans and coordinates the revision.

It does not replace:

- actual empirical execution
- manuscript rewriting
- final human judgment on disagreement
