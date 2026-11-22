# Lifecycle Validation

Lifecycle validation is the Codex translation of Clo-Author 26.05 MAS v2 handoff checks.

It is an explicit workflow discipline, not a hidden hook.

## Pre-Dispatch Check

Before dispatching an agent, the parent orchestrator should check:

- required artifacts listed in `permissions-registry.md`
- target files or directories resolved from the actual repo layout
- required sections when the downstream task depends on them
- freshness of upstream artifacts using `pipeline-contract.md`

If a required input is missing, report:

```text
Cannot dispatch [agent]: missing [artifact or section].
Recommended next step: run [skill] to produce [artifact].
```

## Post-Completion Check

Before advancing a workflow stage, check:

- produced artifacts exist or the agent returned a complete handoff
- required sections are present when specified
- paired critic report exists when the workflow requires a creator/critic pair
- decision records or execution traces were created when the workflow involved a real choice

If output is incomplete, do not silently advance. Return the specific gap to the creator or ask the user for the missing decision.

## Practical Defaults

- Use validation strictly for phase transitions and high-stakes handoffs.
- Use validation lightly for exploratory work.
- Do not require Clo-Author directory names when a repo already has its own structure.
- Do not block writing or review merely because optional artifacts are absent; name the missing evidence and proceed only when the user explicitly accepts the limitation.
