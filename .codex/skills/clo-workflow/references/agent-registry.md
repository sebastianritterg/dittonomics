# Agent Registry

This file is the canonical role map for the installed agents.

## Families

### Ideation
- `ideator`
  Turns vague topics, hunches, or datasets into ranked research questions and discovery-ready idea packets.
- `ideator_critic`
  Stress-tests ideation outputs for novelty, empirical traction, and whether the idea should move forward.

### Discovery
- `librarian`
  Creates literature collections and structured research landscapes.
- `librarian_critic`
  Reviews literature coverage and positioning quality.
- `explorer`
  Finds and evaluates candidate datasets.
- `explorer_critic`
  Reviews data quality, feasibility, and identification fit.

### Strategy
- `strategist`
  Designs identification strategies and PAP-style plans.
- `strategist_critic`
  Reviews causal design validity and inference logic.

### Revision
- `revision_planner`
  Turns real referee or editor feedback into atomic tasks, dependency graphs, execution blocks, and a strategic revision roadmap.
- `revision_planner_critic`
  Reviews roadmap completeness, dependency logic, sequencing, and escalation choices before execution starts.

### Execution
- `data_engineer`
  Cleans data, prepares figures, and documents data assets.
- `coder`
  Implements the approved empirical design in code.
- `writer`
  Drafts or revises manuscript sections.
- `storyteller`
  Builds talk artifacts from the paper.

### Review
- `coder_critic`
  Reviews code and analysis outputs.
- `writer_critic`
  Reviews writing quality and claims-evidence alignment.
- `storyteller_critic`
  Reviews talk structure and presentation quality.
- `domain_referee`
  Peer-review simulation focused on contribution, literature, and substantive interpretation.
- `methods_referee`
  Peer-review simulation focused on methods and inference.
- `editor`
  Desk review, referee assignment, and editorial synthesis.

### Verification
- `verifier`
  Mechanical verification of compilation, execution, integrity, and replication readiness.

## Shared Task Packet

All agents should expect a parent task packet with these core fields:

- `task_type`
- `mode`
- `target_files`
- `required_artifacts`
- `optional_artifacts`
- `repo_overlays`
- `design_metadata`
- `output_expectations`
- `target_locations`
- `persistence_owner`

Agents may extend the packet for role-specific needs, but they should not redefine the shared fields.

## Separation Rules

- creators create and may write only to the resolved targets provided by the parent packet
- critics, referees, editors, and verifier do not edit source artifacts
- the parent orchestrator owns report saving, file moves, and promotion across folders unless a packet explicitly delegates a named output path
- when a repo already resolves a path, agents must use that resolved path instead of inventing a generic fallback
