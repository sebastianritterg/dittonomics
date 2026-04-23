# Artifact Contracts

This file standardizes the intermediate artifacts shared across the `clo-*` stack.

## Core Artifacts

### `idea_brief`
- Purpose: canonical seed memo for the pre-discovery ideation phase
- Typical producer: `clo-ideate seed` or `clo-ideate session`
- Typical consumers: `clo-ideate`, `clo-new-project`, `clo-discover`
- Suggested filename: `quality_reports/idea_brief_[topic].md`
- Minimum contents:
  - problem or phenomenon of interest
  - one-sentence nugget
  - why-now motivation
  - current constraints or comparative advantage
  - closest-paper threat notes
  - fast-fail test

### `rq_shortlist`
- Purpose: ranked candidate research questions with empirical hooks
- Typical producer: `clo-ideate brainstorm`, `clo-ideate rq`, or `clo-ideate session`
- Typical consumers: `clo-ideate evaluate`, `clo-discover interview`, `clo-discover lit`, `clo-discover data`
- Suggested filename: `quality_reports/rq_shortlist_[topic].md`
- Minimum contents:
  - 3-5 candidate research questions
  - testable hypothesis for each
  - identification sketch for each
  - data sketch for each
  - contribution or positioning hook
  - ranking rationale

### `idea_screen`
- Purpose: explicit ideation verdict before discovery work gets expensive
- Typical producer: `clo-ideate evaluate`, `clo-ideate decide`, or `clo-ideate session`
- Typical consumers: user, `clo-new-project`, `clo-discover`
- Suggested filename: `quality_reports/idea_screen_[topic].md`
- Minimum contents:
  - seven-dimension evaluation
  - pursue/refine/park/kill verdict
  - strongest objection
  - best pivot if the first version fails
  - recommended next discovery step

### `research_spec`
- Purpose: canonical research question, motivation, hypothesis, data sketch, and open issues
- Typical producer: `clo-discover interview`; `clo-ideate` may seed it when the idea is already mature
- Typical consumers: `clo-strategize`, `clo-discover lit`, `clo-discover data`
- Suggested filename: `quality_reports/research_spec_[topic].md`
- Minimum contents:
  - research question
  - motivation
  - hypothesis
  - candidate empirical strategy
  - data sketch
  - open questions

### `lit_review`
- Purpose: structured literature map and positioning base
- Producer: `clo-discover lit`
- Consumers: `clo-strategize`, `clo-write`, referees, editor
- Suggested filename: `quality_reports/lit_review_[topic].md`
- Minimum contents:
  - categorized papers
  - proximity or relevance ranking
  - key findings and methods
  - frontier gap or positioning summary

### `data_assessment`
- Purpose: ranked data-source assessment with feasibility and measurement tradeoffs
- Producer: `clo-discover data`
- Consumers: `clo-strategize`
- Suggested filename: `quality_reports/data_assessment_[topic].md`
- Minimum contents:
  - candidate datasets
  - access status
  - key variables
  - feasibility grade
  - identification compatibility notes

### `strategy_memo`
- Purpose: approved design contract for coding and methods writing
- Producer: `clo-strategize`
- Consumers: `clo-analyze`, `clo-write`, `clo-review --methods`, methods referee
- Suggested filename: `quality_reports/strategy_memo_[topic].md`
- Minimum contents:
  - estimand
  - design
  - treatment and control definition
  - assumptions
  - estimation choices
  - robustness plan
  - falsification tests

### `results_summary`
- Purpose: canonical writer handoff from analysis
- Producer: `clo-analyze`
- Consumers: `clo-write`, `clo-review`, `clo-talk`
- Suggested filename: `quality_reports/results_summary.md`
- Minimum contents:
  - point estimates with uncertainty
  - sample sizes
  - description of main tables and figures
  - robustness status
  - anomalies or interpretation flags

### `draft_section`
- Purpose: editable manuscript section produced through `clo-write`
- Producer: `clo-write`
- Consumers: `clo-review --proofread`, peer-review workflows, `clo-talk`
- Suggested location: repo-resolved manuscript section directory
- Minimum contents:
  - section text
  - any explicit placeholders
  - citations that resolve against the active bibliography

### `proofread_report`
- Purpose: manuscript polish report without editing
- Producer: `clo-review --proofread`
- Consumers: user, `clo-revise`, `clo-submit final`
- Suggested filename: `quality_reports/[section]_proofread_report.md`
- Minimum contents:
  - category scores
  - concrete findings
  - unresolved compilation or citation issues

### `revision_task_graph`
- Purpose: machine-readable graph of atomic reviewer tasks, dependencies, and risk links
- Producer: `clo-revise roadmap`
- Consumers: `clo-revise validate`, `clo-revise execute`, user
- Suggested filename: `quality_reports/revision_tasks_[journal_or_date].json`
- Minimum contents:
  - one task per reviewer request
  - reviewer source and verbatim quote
  - task category
  - owner and status
  - dependency list
  - affected manuscript sections or outputs
  - decision flag for disagreement or escalation

### `revision_roadmap`
- Purpose: human-readable strategic revision plan with execution blocks and decision points
- Producer: `clo-revise roadmap`
- Consumers: user, `clo-revise execute`
- Suggested filename: `quality_reports/revision_roadmap_[journal_or_date].md`
- Minimum contents:
  - atomic task summary
  - execution blocks
  - critical path
  - coauthor sync points
  - go/no-go decisions
  - process risks and conflict notes

### `revision_decision_log`
- Purpose: explicit record of disagree, partial concession, defer, or escalate decisions
- Producer: `clo-revise roadmap` or `clo-revise execute`
- Consumers: user, response-letter drafting, later revision rounds
- Suggested filename: `quality_reports/revision_decision_log_[journal_or_date].md`
- Minimum contents:
  - affected reviewer comment
  - chosen stance
  - rationale
  - owner
  - follow-up requirement

### `response_matrix`
- Purpose: one-to-one mapping from reviewer quotes to manuscript actions or planned responses
- Producer: `clo-revise roadmap` or `clo-revise respond`
- Consumers: `clo-revise respond`, user
- Suggested filename: `quality_reports/response_matrix_[journal_or_date].md`
- Minimum contents:
  - reviewer source
  - verbatim quote
  - linked task id
  - action taken or planned
  - manuscript location
  - response stance

### `response_letter`
- Purpose: outward-facing response letter for the journal
- Producer: `clo-revise respond`
- Consumers: user, submission workflow
- Suggested filename: `quality_reports/referee_response_[journal_or_date].tex`
- Minimum contents:
  - summary of major changes
  - point-by-point responses
  - exact reviewer references
  - manuscript section or page references

### `peer_review_bundle`
- Purpose: desk decision, referee reports, and editor synthesis
- Producer: `clo-review --peer`
- Consumers: user, `clo-revise`, `clo-submit final`
- Suggested location: repo-resolved review root, typically `quality_reports/clo-reviews/`
- Minimum contents:
  - desk review or send-out note
  - referee assignments
  - domain and methods reports
  - editorial decision

### `replication_review_bundle`
- Purpose: cross-language replica, critique, comparison, and verification status for review-time replication checks
- Producer: `clo-review --replicate`
- Consumers: user, `clo-revise`, `clo-submit final`
- Suggested location: repo-resolved review root, typically `quality_reports/clo-reviews/`
- Minimum contents:
  - source and target language identification
  - replica script or explicit replica handoff
  - `coder_critic` review of the comparison
  - numerical comparison summary with tolerance notes
  - verifier status for the replica workflow

### `aggregate_review_summary`
- Purpose: weighted synthesis of the direct critic and verifier stack for a resolved review target
- Producer: `clo-review --all` or comprehensive review mode
- Consumers: user, `clo-revise`, `clo-submit final`
- Suggested filename: `quality_reports/aggregate_review_summary_[topic_or_date].md`
- Minimum contents:
  - included reports and omitted reports
  - score by contributing reviewer
  - weighting rule used
  - overall gate outcome

### `replication_audit`
- Purpose: verification output for package completeness and reproducibility
- Producer: `clo-submit audit` or verifier in submission mode
- Consumers: `clo-submit final`, user
- Suggested filename: `quality_reports/replication_audit_[date].md`
- Minimum contents:
  - checklist results
  - pass/fail by item
  - blockers

## Artifact Freshness Expectations

- Orchestrators should compare artifact timestamps against the newest relevant upstream input.
- If freshness is unclear, rerun or explicitly mark the artifact as stale rather than assuming it is valid.
- Downstream skills should prefer a clearly fresh artifact over a richer but stale one.
