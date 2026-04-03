# Pipeline Contract

This file is the canonical phase graph for the `clo-*` stack.

## Phase Graph

1. `discover`
   Produces the initial question framing, literature landscape, and data feasibility view.
2. `strategize`
   Converts the research idea into an estimand, design, assumptions, robustness plan, and falsification logic.
3. `analyze`
   Implements the approved design in code, creates analysis outputs, and produces the writer handoff artifacts.
4. `write`
   Drafts or revises manuscript sections from approved evidence and section contracts.
5. `review`
   Runs critic, referee, editor, and verifier workflows without editing source artifacts.
6. `submit`
   Performs journal targeting, replication-package preparation, and final submission checks.

Supporting workflows:

- `new-project`
  Scheduler over the phase graph. It does not redefine phase logic.
- `revise`
  Orchestrates the response-to-reviews cycle using the same phase contracts.
- `talk`
  Builds and audits presentations from paper artifacts.
- `research-tools`
  Utility toolbox, not a pipeline phase.

## Phase Dependencies

| Phase | Minimum required upstream artifacts |
|-------|-------------------------------------|
| discover | none |
| strategize | `research_spec`, `lit_review`; `data_assessment` when available |
| analyze | `strategy_memo` |
| write | `strategy_memo`, `results_summary` for results-based sections |
| review | target manuscript, script, or talk artifacts already exist |
| submit | recent review artifacts plus verifier-ready project structure |

## Quality Gates

- `>= 80`: commit-ready
- `>= 90`: merge-ready
- `>= 95` with no weak component: submission-ready

Recommended transition gates:

- `discover -> strategize`
  `research_spec` and `lit_review` exist and are current enough for the active question.
- `strategize -> analyze`
  `strategy_memo` exists and no blocking strategist-critic issue remains.
- `analyze -> write`
  code outputs exist and `results_summary` is fresh relative to the current scripts.
- `write -> review`
  target sections exist in the active manuscript root.
- `review -> submit`
  recent review artifacts pass the submission threshold and the verifier does not fail.

## Freshness Rule

An artifact is stale when any core upstream input changed materially after the artifact was last updated. Orchestrators should check freshness before routing downstream work.

Examples:

- a `strategy_memo` becomes stale if the research question, main sample, or data source changes
- a `results_summary` becomes stale if the estimation script or the manuscript-ready outputs changed
- a `proofread_report` becomes stale if the reviewed section changed after the report
