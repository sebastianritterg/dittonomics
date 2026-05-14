---
name: clo-talk
description: Build and audit presentation decks. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo Talk

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

# Talk

Create, audit, or compile presentations (Beamer or Quarto RevealJS).

Dittonomics default: Beamer. Upstream Clo-Author 26.05 moved Quarto-first, but this Codex setup intentionally keeps Beamer-first by Sebastian's preference. Use Quarto RevealJS only when `--quarto` is explicit.

**Input:** `$ARGUMENTS` - mode and format/path.

---

## Modes

### `$clo-talk create [format]` - Create Beamer Talk
### `$clo-talk create [format] --quarto` - Create Quarto RevealJS Talk

Generate a presentation from the paper.

**Agents:** Storyteller (creator) -> storyteller-critic (reviewer)

#### Format Constraints

| Format | Slides | Duration | Content Scope |
|--------|--------|----------|---------------|
| job-market | 40-50 | 45-60 min | Full story, all results, mechanism, robustness |
| seminar | 25-35 | 30-45 min | Motivation, main result, 2 robustness, conclusion |
| short | 10-15 | 15 min | Question, method, key result, implication |
| lightning | 3-5 | 5 min | Hook, one result, so-what |

#### Workflow

**Step 1: Parse Arguments**

- **Format** (required): `job-market` | `seminar` | `short` | `lightning`
- **Paper path** (optional): defaults to `paper/main.tex`
- **Engine**: Beamer (default) or Quarto RevealJS (`--quarto`)
- If no format specified, ask the user.

**Step 2: Dispatch Storyteller**

Read the paper and extract: research question, identification strategy, main result, secondary results, robustness checks, key figures/tables, institutional background. Design narrative arc for the chosen format. Build the slide file with shared preamble if available.

The Storyteller follows these design principles:
- **One idea per slide** - never cram two concepts onto one frame
- **Figures over tables; tables in backup** - audiences absorb figures instantly; regression tables belong in backup slides where referees can inspect them during Q&A
- **Build tension** - motivation -> question -> method -> findings -> implications
- **Transition slides between major sections** - signal where the talk is going
- **All claims must appear in the paper** - the paper is the single source of truth; never add results or claims that are not in the manuscript

Compile with XeLaTeX (Beamer) or `quarto render` (Quarto).

Save to the repo-resolved talk folder, typically `paper/talks/[format]_talk.tex` (Beamer) or `paper/quarto/[format]_talk.qmd` (Quarto).

**Step 3: Dispatch Storyteller-Critic**

After the Storyteller returns, dispatch the storyteller-critic to review across 5 categories:

| Category | What It Checks |
|----------|---------------|
| **Narrative flow** | Does the story build properly? Is there a clear arc from motivation through results to implications? Are transitions smooth? |
| **Visual quality** | Text overflow, font readability (>= 10pt), figure sizing, consistent formatting, overfull hbox warnings |
| **Content fidelity** | Every claim traceable to the paper - no orphan results, no unsupported statements |
| **Scope for format** | Right amount of content for the duration - not cramming a seminar into a lightning talk, not padding a short talk to seminar length |
| **Compilation** | Does it compile cleanly without errors or warnings? |

Score as advisory (non-blocking). Save report to `quality_reports/[format]_talk_review.md`.

**Step 4: Fix Critical Issues**

If the storyteller-critic finds Critical issues (compilation failures, content not in paper):
1. Re-dispatch Storyteller with specific fixes (max 3 rounds per three-strikes rule)
2. Re-run storyteller-critic to verify

**Step 5: Present Results**

Report to the user:
1. Generated file path
2. Slide count and format compliance
3. Storyteller-critic score (advisory, non-blocking)
4. TODO items (missing figures, tables not yet generated)

---

### `$clo-talk audit [file]` - Visual Audit

Check existing slides for layout issues.

Run visual quality checks:
- Text overflow on any slide
- Font sizes (>= 10pt for projection)
- Table readability
- Figure sizing and labels
- Consistent formatting
- Overfull hbox warnings

---

### `$clo-talk compile [file]` - Compile Talk

3-pass XeLaTeX compilation for Beamer:
```bash
cd paper/talks && TEXINPUTS=../preambles:$TEXINPUTS xelatex -interaction=nonstopmode [file]
```

For Quarto:
```bash
cd paper/quarto && quarto render [file]
```

---

## Principles

- **Paper is authoritative.** Every claim must appear in the paper.
- **Beamer-first.** Beamer is the default; Quarto RevealJS is opt-in with `--quarto`.
- **Figures over tables.** Audiences absorb figures instantly. Put regression tables in backup slides for Q&A.
- **Less is more.** Especially for short and lightning formats - ruthlessly cut.
- **One idea per slide.** If you need a second point, make a second slide.
- **Audience calibration.** Job market = demonstrate rigor and command of the literature. Seminar = sell the interesting result. Short = method and key finding. Lightning = sell the idea in one breath.
- **Advisory scoring.** Talk scores don't block commits.
- **Worker-critic pairing.** Storyteller creates, storyteller-critic critiques. Never skip the review.




