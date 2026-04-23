---
name: clo-new-project
description: Run the full clo-author research pipeline. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo New Project

Adapt the Clo-Author workflow to Codex.

1. Start by inspecting the repo's AGENTS files, README.md, and current folder layout.
2. Use the repository's actual manuscript, output, and docs directories instead of assuming Clo-Author defaults.
3. Use the main Codex session as the orchestrator. Delegate focused work to the matching Codex subagents when that improves quality or speed.
4. Preserve worker-critic separation: creators produce artifacts, critics, editors, and referees review without editing.
5. If a repo already has paper-specific rules or skills, treat them as higher-priority than the generic Clo-Author defaults.
6. Read `references/source-skill.md` only when you need the original upstream command details or argument structure.

## Codex Notes

- Original slash commands are exposed here as explicit `$clo-*` skills.
- Hidden hooks are not ported. Use explicit verification, snapshot, upgrade, and review steps instead.
- Use the active `clo-workflow` references for domain and journal calibration: ~/.codex/skills/clo-workflow/references/domain-profile.md and ~/.codex/skills/clo-workflow/references/journal-profiles.md.
- Treat `explorations/` as the repo-level sandbox for experimental work. If exploratory work is needed and the folder is missing, scaffold it from ~/.codex/skills/clo-workflow/references/explorations.md.
- Read source mirrors only when provenance matters: ~/.codex/skills/clo-workflow/references/source-rules and ~/.codex/skills/clo-workflow/references/source-references.
- For repo-specific path conventions and field rules, prefer local `.agents/skills` and `AGENTS.override.md`.

## Source Workflow

# New Project

Launch a full research pipeline from idea to paper, orchestrated through the dependency graph.

**Input:** `$ARGUMENTS` - a research topic or `interactive` for a guided start via `$clo-discover interview`.

---

## Pipeline Overview

This skill orchestrates the full dependency graph. Each phase activates when its dependencies are met. The orchestrator manages agent dispatch, three-strikes escalation, and quality gates.

```
Phase 1: Ideation
  â””â”€â”€ $clo-ideate session -> Idea Brief + RQ Shortlist + Idea Screen

Phase 2: Discovery (depends on Phase 1 when the question is still fluid)
  â”œâ”€â”€ $clo-discover interview -> Research Spec + Domain Profile
  â”œâ”€â”€ $clo-discover lit -> Literature Synthesis + BibTeX
  â””â”€â”€ $clo-discover data -> Data Assessment

Phase 3: Strategy (depends on Phase 2)
  â””â”€â”€ $clo-strategize -> Strategy Memo + Robustness Plan

Phase 4: Execution (depends on Phase 3)
  â”œâ”€â”€ $clo-analyze -> Scripts + Tables + Figures
  â””â”€â”€ $clo-write -> Paper Sections

Phase 5: Peer Review (depends on Phase 4)
  â”œâ”€â”€ $clo-review --all -> Comprehensive Quality Score
  â””â”€â”€ $clo-review --peer -> domain-referee + methods-referee Reports

Phase 6: Submission (depends on Phase 5, score >= 95)
  â”œâ”€â”€ $clo-submit target -> Journal Recommendations
  â”œâ”€â”€ $clo-submit package -> Replication Package
  â””â”€â”€ $clo-submit final -> Final Verification
```

---

## Workflow

### Step 1: Ideation Phase

1. **If the question is still broad, uncertain, or only a hunch:**
   Run `$clo-ideate session` to produce:
   - Idea brief
   - Ranked research-question shortlist
   - Idea screen with pursue/refine/park/kill verdict

**Gate:** A question should be selected and its main risks should be named before expensive discovery work.

### Step 2: Discovery Phase

2. **If `interactive` or no research spec exists:**
   Run `$clo-discover interview` to produce:
   - Research specification (`quality_reports/research_spec_*.md`)
   - Domain profile (`~/.codex/skills/clo-workflow/references/domain-profile.md `) - if still template

3. **Run `$clo-discover lit`** with the research topic:
   - Librarian collects literature
   - librarian-critic reviews coverage
   - Output: literature synthesis + BibTeX entries

4. **Run `$clo-discover data`** to find datasets:
   - Explorer searches for data sources
   - explorer-critic assesses data quality

**Gate:** Research spec and literature review must exist before proceeding.

### Step 3: Strategy Phase

5. **Run `$clo-strategize`** to design the empirical strategy:
   - Strategist proposes identification strategy
   - strategist-critic validates the design

**Gate:** Strategy memo must pass strategist-critic review (score >= 80).

### Step 4: Execution Phase

6. **Run `$clo-analyze`** to implement the strategy:
   - Data-engineer cleans data and creates figures
   - Coder writes analysis scripts
   - coder-critic reviews code

7. **Run `$clo-write`** to draft the paper:
   - Writer drafts sections
   - Humanizer pass strips AI patterns

**Gate:** Code must pass coder-critic review. Paper sections must exist.

### Step 5: Peer Review Phase

8. **Run `$clo-review --all`** for comprehensive review:
   - strategist-critic + coder-critic + writer-critic + Verifier in parallel
   - Weighted aggregate score computed

9. **Run `$clo-review --peer`** for simulated peer review:
   - domain-referee (subject expertise) + methods-referee (econometrics)
   - Independent, blind reports
   - Orchestrator synthesizes editorial decision

**Gate:** Aggregate score >= 80 (commit-ready). Score >= 90 for submission.

### Step 6: Submission Phase (optional, user-triggered)

10. **Run `$clo-submit target`** for journal recommendations
11. **Run `$clo-submit package`** for replication package
12. **Run `$clo-submit final`** for final verification

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

- **This is always orchestrated.** Unlike other skills, `$clo-new-project` always runs through the full pipeline.
- **Dependency-driven.** Phases activate by dependency, not forced sequence.
- **Quality-gated.** Each phase transition requires passing quality checks.
- **User retains control.** Pipeline pauses at key decision points.
- **Resumable.** If interrupted, the pipeline resumes from the last completed phase.

## Exploration Sandbox

- If this repo needs a prototype sandbox and `explorations/` is missing, create it before dispatching exploratory work.
- Use `explorations/` for early tests, side calculations, or speculative branches that are not yet part of the canonical pipeline.




