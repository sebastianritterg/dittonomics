---
name: new-project
description: Start or orchestrate a full Clo/Dittonomics research project. Use when the user asks to start a new empirical project, take an idea from topic to paper, run the full research pipeline, set up end-to-end Clo workflow, or call $new-project. Routes across ideation, discovery, strategy, analysis, writing, review, revision, submission, and talks.
---

# New Project

Adapt the Clo-Author workflow to Codex.

1. Start by inspecting the repo's AGENTS files, README.md, and current folder layout.
2. Use the repository's actual manuscript, output, and docs directories instead of assuming Clo-Author defaults.
3. Use the main Codex session as the orchestrator. Use the subagent policy in the starter AGENTS.md when resolving a skill request.
4. Preserve worker-critic separation: creators produce artifacts, critics, editors, and referees review without editing.
5. If a repo already has paper-specific rules or skills, treat them as higher-priority than the generic Clo-Author defaults.
6. Read `references/source-skill.md` only when you need the original upstream command details or argument structure.

## Codex Notes

- Invoke this skill as `$new-project`.
- Hidden hooks are not ported. Use explicit verification, snapshot, upgrade, and review steps instead.
- Use the active `workflow` references for domain and journal calibration: ~/.codex/skills/workflow/references/domain-profile.md and ~/.codex/skills/workflow/references/journal-profiles.md.
- Treat `explorations/` as the repo-level sandbox for experimental work. If exploratory work is needed and the folder is missing, scaffold it from ~/.codex/skills/workflow/references/explorations.md.
- Read source mirrors only when provenance matters: ~/.codex/skills/workflow/references/source-rules and ~/.codex/skills/workflow/references/source-references.
- For repo-specific path conventions and field rules, prefer local `.codex/skills` and `AGENTS.override.md`.

## Natural-Language Routing

Use this skill when the user asks for an end-to-end research pipeline rather than a single phase.

- `start a new project`, `new empirical project`, `take this idea through the pipeline`, `from idea to paper`, `set up a research project`, or `run clo-author on this topic` -> full orchestrated pipeline
- `interactive start`, `interview me first`, or `help me scope a new project` -> begin with `ideate session` or `discover interview` depending on how fluid the idea is
- if the user asks only for literature, data, strategy, analysis, writing, review, or submission, route to that narrower Dittonomics skill instead

## Source Workflow

# New Project

Launch a full research pipeline from idea to paper, orchestrated through the dependency graph.

**Input:** `$ARGUMENTS` - a research topic or `interactive` for a guided start via `$discover interview`.

---

## Pipeline Overview

This skill orchestrates the full dependency graph. Each phase activates when its dependencies are met. The orchestrator manages agent dispatch, three-strikes escalation, and quality gates.

```
Phase 1: Ideation
  -> $ideate session -> Idea Brief + RQ Shortlist + Idea Screen

Phase 2: Discovery (depends on Phase 1 when the question is still fluid)
  -> $discover interview -> Research Spec + Domain Profile
  -> $discover lit -> Literature Synthesis + BibTeX
  -> $discover data -> Data Assessment

Phase 3: Strategy (depends on Phase 2)
  -> $strategize -> Strategy Memo + Robustness Plan

Phase 4: Execution (depends on Phase 3)
  -> $analyze -> Scripts + Tables + Figures
  -> $write -> Paper Sections

Phase 5: Peer Review (depends on Phase 4)
  -> $review --all -> Comprehensive Quality Score
  -> $review --peer -> domain-referee + methods-referee Reports

Phase 6: Submission (depends on Phase 5, score >= 95)
  -> $submit target -> Journal Recommendations
  -> $submit package -> Replication Package
  -> $submit final -> Final Verification
```

---

## Workflow

### Step 1: Ideation Phase

1. **If the question is still broad, uncertain, or only a hunch:**
   Run `$ideate session` to produce:
   - Idea brief
   - Ranked research-question shortlist
   - Idea screen with pursue/refine/park/kill verdict

**Gate:** A question should be selected and its main risks should be named before expensive discovery work.

### Step 2: Discovery Phase

2. **If `interactive` or no research spec exists:**
   Run `$discover interview` to produce:
   - Research specification (`quality_reports/research_spec_*.md`)
   - Domain profile (`~/.codex/skills/workflow/references/domain-profile.md `) - if still template

3. **Run `$discover lit`** with the research topic:
   - `librarian` collects literature
   - `librarian_critic` reviews coverage
   - Output: literature synthesis + BibTeX entries

4. **Run `$discover data`** to find datasets:
   - `explorer` searches for data sources
   - `explorer_critic` assesses data quality

**Gate:** Research spec and literature review must exist before proceeding.

### Step 3: Strategy Phase

5. **Run `$strategize`** to design the empirical strategy:
   - `strategist` proposes identification strategy
   - `strategist_critic` validates the design

**Gate:** Strategy memo must pass `strategist_critic` review (score >= 80).

### Step 4: Execution Phase

6. **Run `$analyze`** to implement the strategy:
   - `data_engineer` cleans data and creates figures
   - `coder` writes analysis scripts
   - `coder_critic` reviews code

7. **Run `$write`** to draft the paper:
   - `writer` drafts sections
   - Humanizer pass strips AI patterns

**Gate:** Code must pass `coder_critic` review. Paper sections must exist.

### Step 5: Peer Review Phase

8. **Run `$review --all`** for comprehensive review:
   - `strategist_critic` + `coder_critic` + `writer_critic` + `verifier` in parallel
   - Weighted aggregate score computed

9. **Run `$review --peer`** for simulated peer review:
   - domain-referee (subject expertise) + methods-referee (econometrics)
   - Independent, blind reports
   - Orchestrator synthesizes editorial decision

**Gate:** Aggregate score >= 80 (commit-ready). Score >= 90 for submission.

### Step 6: Submission Phase (optional, user-triggered)

10. **Run `$submit target`** for journal recommendations
11. **Run `$submit package`** for replication package
12. **Run `$submit final`** for final verification

---

## User Interaction Points

The pipeline pauses for user input at these points:
- After interview (approve research spec)
- After strategy memo (approve identification strategy)
- After data analysis (review results before paper drafting)
- After peer review (review feedback before revision)
- Before submission (approve journal choice)

Between pauses, the orchestrator runs autonomously per `workflow.md`.

---

## Principles

- **This is always orchestrated.** Unlike other skills, `$new-project` always runs through the full pipeline.
- **Dependency-driven.** Phases activate by dependency, not forced sequence.
- **Quality-gated.** Each phase transition requires passing quality checks.
- **User retains control.** Pipeline pauses at key decision points.
- **Resumable.** If interrupted, the pipeline resumes from the last completed phase.

## Exploration Sandbox

- If this repo needs a prototype sandbox and `explorations/` is missing, create it before dispatching exploratory work.
- Use `explorations/` for early tests, side calculations, or speculative branches that are not yet part of the canonical pipeline.



