---
name: clo-analyze
description: Analyze data and implement empirical work in the Clo/Dittonomics pipeline. Use when the user asks to run analysis, clean data, construct variables, estimate regressions, make tables or figures, run robustness checks, reproduce outputs, compare implementations, or call $clo-analyze. Routes to data_engineer, coder, and coder_critic.
---

# Clo Analyze

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

## Delegation Rule

Invoking this skill through `$clo-analyze` or a natural-language analysis request counts as explicit permission to dispatch the named agents for the resolved work.

- data cleaning, construction, codebooks, and descriptive figures route to `data_engineer`
- estimation scripts, tables, robustness checks, and results summaries route to `coder`
- review of produced or touched code routes to `coder_critic`
- if subagent dispatch is unavailable, fall back to the main session only with an explicit note

## Natural-Language Routing

Resolve ordinary analysis requests before asking for clarification:

- `clean the data`, `construct variables`, `make a codebook`, `summary stats`, or `descriptive figure` -> `data_engineer`, then `coder_critic` when code is produced
- `run the analysis`, `estimate the regression`, `implement the spec`, `make table [N]`, `produce figure [N]`, `robustness check`, or `event study` -> `coder -> coder_critic`
- `reproduce tables`, `replicate results`, `rerun scripts`, or `verify outputs match paper` -> `coder` plus `verifier` or route to `clo-submit audit` when this is a submission package
- `dual language`, `cross-language`, `R and Python`, `Python and Stata`, or `two implementations` -> `--dual`
- `code check`, `review script`, or `lint this analysis` -> prefer `clo-review --code` for judgment review or `clo-research-tools lint` for mechanical lint only

## Source Workflow

# Analyze

Run end-to-end data analysis by dispatching `coder` (analysis), `data_engineer` (cleaning + figures), and `coder_critic` (code review).

**Input:** `$ARGUMENTS` - dataset path or description of analysis goal.

---

## Workflow

### Step 1: Context Gathering
1. Read ~/.codex/skills/clo-workflow/references/domain-profile.md  for field conventions
2. Read strategy memo in `quality_reports/` if it exists
3. Check the repo's root guidance files (for example README.md, AGENTS.md, or project docs) for language preference. If no repo preference is declared, default to Python first, then Stata, while still supporting R and Julia.
4. Scan existing scripts in `scripts/` for project patterns

### Step 2: Data Preparation (if needed)
If raw data is provided, dispatch `data_engineer` first:
- Clean and wrangle raw data
- Handle missing values, construct variables per strategy memo
- Generate summary statistics table
- Create publication-quality descriptive figures
- Save cleaned data, codebook, and figures

### Step 3: Main Analysis
Dispatch `coder` agent:
- Stage 0: Data loading (from cleaned data or raw)
- Stage 1: Main specification (from strategy memo or user description)
- Stage 2: Robustness checks
- Stage 3: Publication-ready output (tables to `paper/tables/`, figures to `paper/figures/`)
- Produce `results_summary.md` with all estimates, SEs, and key statistics (MANDATORY)
- Save scripts to `scripts/python/` by default, `scripts/stata/` when the repo centers Stata, and `scripts/R/` or `scripts/julia/` only when explicitly chosen

The `coder` follows these principles:
- **Script structure:** Use the Script Structure Template below
- **Default stack:** Python first (`pandas`, `statsmodels` or `linearmodels`, `matplotlib` or `seaborn`), then Stata when the repo centers Stata. R and Julia remain supported when explicitly requested.
- **Standard errors:** Cluster at appropriate level (match treatment assignment)
- **Output:** `.tex` tables for LaTeX, `.pdf` or `.png` figures, and language-appropriate serialized intermediates
- **No hardcoded paths.** All paths relative to repository root.
- **Persist reusable intermediates.** Every computed object should be saved in a language-appropriate serialized format for downstream use by the writer and other agents.

### Step 4: Code Review
Dispatch `coder_critic` agent - run the full 12-category checklist:

**Strategic (categories 1-3):**
1. **Code-strategy alignment** - Does the code implement the strategy memo faithfully? Correct dependent variable, treatment, controls, fixed effects, sample restrictions?
2. **Sanity checks** - Are summary statistics printed before regressions? Do coefficient signs match economic intuition? Are sample sizes reasonable?
3. **Robustness sufficiency** - Are required robustness checks present? Alternative specifications, placebo tests, sensitivity analysis per strategy memo?

**Code Quality (categories 4-12):**
4. **Structure** - Does the script follow the standard template? Clear section headers, logical flow from setup to export?
5. **Console hygiene** - No spurious `print()` statements polluting output. Intentional output only.
6. **Reproducibility** - `set.seed()` at top if any stochastic elements. No absolute paths. All packages loaded at top. Directory creation with `showWarnings = FALSE`.
7. **Functions** - Repeated logic extracted into functions. No copy-paste code blocks with minor variations.
8. **Figure quality** - Publication-ready: proper axis labels, titles, legends, font sizes. Consistent theme across all figures.
9. **RDS pattern** - Every computed object (models, data frames, summary stats) saved via `saveRDS()` for downstream use. Not just final outputs - intermediate objects too.
10. **Comments** - Section headers present. Non-obvious code commented. No commented-out dead code left behind.
11. **Error handling** - Graceful handling of missing files, empty data subsets, convergence failures. Informative error messages.
12. **Polish** - Consistent naming conventions. No magic numbers. Clean whitespace. Professional quality ready for replication package.

If strategy memo exists, cross-reference code against stated design.
Save report to `quality_reports/[script]_code_review.md`.

### Step 5: Fix Issues
If `coder_critic` finds Critical or Major issues:
1. Re-dispatch `coder` with specific fixes (max 3 rounds)
2. Re-run `coder_critic` to verify fixes

### Step 6: Present Results
1. **Results summary** - key estimates with SEs and interpretation (from `results_summary.md`)
2. **Scripts created** - paths and descriptions
3. **Output files** - tables in `paper/tables/`, figures in `paper/figures/`
4. **Code review score** - from `coder_critic`
5. **TODO items** - missing data, additional specifications needed

---

## Script Structure Template

Use a language-appropriate script template with the same section order:

```text
00_setup
01_data_loading
02_exploration
03_main_analysis
04_tables_figures
05_export
```

Python default:
- imports at the top
- `pathlib`-based relative paths
- deterministic seeds if needed
- reusable intermediate outputs saved in a language-appropriate serialized format

Stata default:
- one driver do-file with clear section markers
- relative paths only
- deterministic seeds where needed
- reproducible export commands for tables and figures

## Results Summary (Mandatory Artifact)

Every analysis run MUST produce `results_summary.md` containing:
- All point estimates with standard errors and significance levels
- Sample sizes for each specification
- Key summary statistics (means, medians, standard deviations of main variables)
- Robustness check results (brief table or comparison)
- Any flags or anomalies discovered during analysis

This file is the primary handoff artifact to the writer agent. Without it, the writer cannot draft the results section.

---

## Dual-Language Mode (`--dual r,python`)

When `--dual [lang1,lang2]` is provided (e.g., `--dual r,python`, `--dual r,stata`):

1. `data_engineer` runs once - language-agnostic cleaning, saves to `data/cleaned/`
2. Two `coder` agents dispatch in parallel - same strategy memo, different languages
3. `coder_critic` reviews each implementation independently (max 3 rounds each)
4. **Comparison step** - verify numerical alignment per `~/.codex/skills/clo-workflow/references/domain-profile.md ` tolerances:
   - Point estimates must match within declared tolerance
   - Standard errors must match within declared tolerance
   - Flag any divergences with exact values from both languages
5. Save comparison report to `quality_reports/cross_language_comparison.md`

### Replication Tolerance Approach

Inspired by Scott Cunningham's replication methodology: **if two independent implementations agree, neither has a bug.** This is the core rationale for dual-language mode.

**Tolerance thresholds:**
- **Floating-point differences are normal.** Minor numerical differences (e.g., 1e-10) between R and Python/Stata arise from different linear algebra backends, optimizer defaults, and floating-point arithmetic. These are expected, not bugs.
- **Point estimates:** Must agree within 1e-6 (relative) or as declared in `domain-profile.md`
- **Standard errors:** Must agree within 1e-4 (relative) - SE computation varies more across implementations due to degrees-of-freedom corrections and clustering algorithms
- **P-values:** Must agree on significance at conventional levels (0.01, 0.05, 0.10). If one language says p=0.049 and the other says p=0.051, flag for manual review but do not treat as a bug.
- **Sample sizes:** Must match exactly. Any discrepancy indicates a data handling difference that must be resolved.

**When results diverge beyond tolerance:**
1. Both `coder` agents are re-dispatched to investigate
2. Check: different default options (e.g., na.rm handling, convergence criteria)
3. Check: different variable coding or factor ordering
4. The comparison report includes a side-by-side table of all estimates
5. If divergence persists after investigation, escalate to user with exact values from both languages

---

## Principles
- **Reproduce, don't guess.** If the user specifies a regression, run exactly that.
- **Show your work.** Print summary statistics before jumping to regressions.
- **Strategy alignment.** If strategy memo exists, code MUST implement it faithfully.
- **Worker-critic pairing.** `coder` creates, `coder_critic` critiques. Never skip review.
- **saveRDS everything.** Every computed object gets saved via `saveRDS()` for downstream use - model fits, cleaned data frames, summary statistics, not just final tables.
- **Publication-ready output.** Tables and figures directly includable in the paper.
- **Cross-language convergence.** When `--dual` is used, divergence is a bug until proven otherwise.




