# Pipeline Contract

This file is the canonical phase graph for the `clo-*` stack.

## Phase Graph

1. `ideate`
   Screens seed ideas, converts them into candidate research questions, and records whether they should be pursued, refined, parked, or dropped.
2. `discover`
   Produces the formal research specification, literature landscape, and data feasibility view for the chosen question.
3. `strategize`
   Converts the research idea into an estimand, design, assumptions, robustness plan, and falsification logic.
4. `analyze`
   Implements the approved design in code, creates analysis outputs, and produces the writer handoff artifacts.
5. `write`
   Drafts or revises manuscript sections from approved evidence and section contracts.
6. `review`
   Runs critic, referee, editor, and verifier workflows without editing source artifacts.
7. `submit`
   Performs journal targeting, replication-package preparation, and final submission checks.

Supporting workflows:

- `new-project`
  Scheduler over the phase graph. It does not redefine phase logic.
- `revise`
  Orchestrates the post-review and post-submission revision cycle. It plans the roadmap, then routes approved work back into analyze, write, and review.
- `talk`
  Builds and audits presentations from paper artifacts.
- `research-tools`
  Utility toolbox, not a pipeline phase.

## Phase Dependencies

| Phase | Minimum required upstream artifacts |
|-------|-------------------------------------|
| ideate | none |
| discover | none; `idea_brief`, `rq_shortlist`, and `idea_screen` when available |
| strategize | `research_spec`, `lit_review`; `data_assessment` when available |
| analyze | `strategy_memo` |
| write | `strategy_memo`, `results_summary` for results-based sections |
| review | target manuscript, script, or talk artifacts already exist |
| submit | recent review artifacts plus verifier-ready project structure |

## Revision Loop

`revise` is not a new terminal phase after `submit`.

It is a loop-back workflow triggered by real editor or referee feedback. Depending on the roadmap, it may send work back to:

- `analyze` for new empirical tasks
- `write` for clarification, rewriting, and response prose
- `review` for another internal quality pass before resubmission

Minimum suggested upstream inputs for `revise`:

- reviewer or editor reports
- submitted manuscript
- latest analysis outputs when empirical requests are present
- recent review artifacts when available

## Quality Gates

- `>= 80`: commit-ready
- `>= 90`: merge-ready
- `>= 95` with no weak component: submission-ready

Recommended transition gates:

- `ideate -> discover`
  the active question is selected, the main risks are named, and the ideation verdict is at least `pursue` or `refine`
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

- an `idea_screen` becomes stale if the closest-paper landscape, target question, or core data constraint changes materially
- a `revision_roadmap` becomes stale if reviewer priorities change, a major analysis result changes, or the disagreement strategy changes
- a `strategy_memo` becomes stale if the research question, main sample, or data source changes
- a `results_summary` becomes stale if the estimation script or the manuscript-ready outputs changed
- a `proofread_report` becomes stale if the reviewed section changed after the report
