# Revision Task Graph Schema

This file defines the machine-readable structure used by `dag_validator.py`.

## File

`revision_task_graph.json`

Accepted shapes:

```json
{
  "tasks": {
    "R1_a1": { "...": "..." }
  }
}
```

or:

```json
{
  "R1_a1": { "...": "..." }
}
```

## Required Fields Per Task

```json
{
  "reviewer_source": "R1.a1",
  "quote": "verbatim reviewer quote or faithful abbreviated quote",
  "category": "EMPIRICAL | ARGUMENTATIVE | STRUCTURAL | CLARIFICATION | EDITORIAL | DECISION",
  "description": "Short imperative task description",
  "status": "todo | approved | blocked | in_progress | done | deferred",
  "owner": "revision_planner | writer | coder | data_engineer | user | mixed",
  "depends_on": ["R1_a0"],
  "decision_flag": "none | disagree | partial_concession | escalate | go_no_go",
  "affected_sections": ["intro", "discussion"],
  "affected_outputs": ["table_3", "figure_2"]
}
```

## Optional Fields

```json
{
  "block": "A | B | C | D | E | ?",
  "collateral_risks": [
    {
      "task_id": "R2_b1",
      "risk": "If the new regressions reverse signs, this interpretation task must be rewritten."
    }
  ],
  "notes": "Free-form planning note"
}
```

## Interpretation Notes

- `depends_on` creates real DAG edges
- `collateral_risks` are informational and do not create hard edges
- `decision_flag` is mandatory for disagreement-heavy tasks; use `none` otherwise
- use `block` only after or during sequencing; validation-only runs may leave it as `?`
