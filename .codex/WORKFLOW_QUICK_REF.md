# Workflow Quick Reference

Model: you direct, Codex orchestrates through skills and custom subagents.

## Main Pipeline

```text
$ideate -> idea brief + research question screen
    ->
$discover interview -> research spec + domain profile
    ->
$discover lit -> literature synthesis
    ->
$discover data -> data assessment
    ->
$strategize -> strategy memo
    ->
$analyze -> scripts + outputs
    ->
$write -> section contracts + draft + humanizer
    ->
$review -> review score + peer review
    ->
$submit -> final submission gate
```

Enter at any stage. Use `$new-project` when you want the full pipeline.

## Entry Points

- `$new-project`
- `$discover`
- `$strategize`
- `$strategize theory` (explicit-only)
- `$analyze`
- `$write`
- `$review`
- `$revise`
- `$talk`
- `$submit`
- `$research-tools`

Useful utilities:

- `$research-tools checkpoint`
- `$research-tools resume-context`
- `$research-tools lint`
- `$research-tools dashboard`
- `$research-tools html-report`

## Kernel Rules

- the main Codex session is the orchestrator
- skills resolve paths before dispatch
- creator agents write only to named targets
- critics, referees, editor, and verifier return reports to the parent orchestrator
- the parent orchestrator owns persistence unless it explicitly delegates a named write target
- permission registry and lifecycle validation are advisory routing contracts
- Beamer is the default talk format; Quarto requires `--quarto`

## Quality Gates

- `>= 80`: commit-ready
- `>= 90`: merge-ready
- `>= 95`: submission-ready

## Exploration Mode

For prototypes and side investigations:

- work in `explorations/`
- keep rough work outside canonical outputs
- promote only after the idea stabilizes
- archive abandoned lines under `explorations/ARCHIVE/`

## Optional Voice Mode

For writing-heavy workflows:

- keep reusable prose guidance in `~/.codex/voice/`
- treat voice as a style layer, not as evidence
- use overlays only when needed
