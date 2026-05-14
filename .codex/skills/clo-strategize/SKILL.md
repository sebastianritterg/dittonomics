---
name: clo-strategize
description: Design an identification strategy or PAP. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo Strategize

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

# Strategize

Design an identification strategy or pre-analysis plan by dispatching the **Strategist** (proposer) and **strategist-critic** (validator).

**Input:** `$ARGUMENTS` - mode keyword followed by research question or path to research spec.

---

## Modes

### `$clo-strategize [question]` or `$clo-strategize strategy [question]` - Identification Strategy
Design the causal identification strategy.

**Agents:** Strategist -> strategist-critic
**Output:** Strategy memo + robustness plan + falsification tests

Workflow:
1. Read research spec, literature review, and data assessment if they exist
2. Read ~/.codex/skills/clo-workflow/references/domain-profile.md  for common identification strategies in the field
3. Dispatch Strategist to produce:
   - Strategy memo: design choice, estimand, assumptions, comparison group
   - Pseudo-code: implementation sketch
   - Robustness plan: ordered list of checks with rationale
   - Falsification tests: what SHOULD NOT show effects
   - Referee objection anticipation: top 5 objections with responses
4. Dispatch strategist-critic to review through 4 phases:
   - Phase 1: Claim identification (design, estimand, treatment, control)
   - Phase 2: Core design validity (assumption checks, sanity checks)
   - Phase 3: Inference soundness (clustering, multiple testing)
   - Phase 4: Polish and completeness (robustness, citations)
5. If CRITICAL issues found, iterate (max 3 rounds per three-strikes)
6. Save memo to `quality_reports/strategy_memo_[topic].md`
7. Save review to `quality_reports/strategy_memo_[topic]_review.md`

### `$clo-strategize pap [spec]` - Pre-Analysis Plan
Draft a pre-analysis plan following AEA/OSF/EGAP standards.

**Input:** `$ARGUMENTS` - path to research spec file, a topic, or `interactive` for guided interview.

- If `$ARGUMENTS` includes a file path: read it (research spec from `$clo-discover interview`)
- If `$ARGUMENTS` includes `interactive`: conduct the guided PAP interview (see below)
- Otherwise: treat as topic and draft with ASSUMED placeholders marked clearly

**Agents:** Strategist (in PAP mode), optionally strategist-critic
**Output:** Pre-analysis plan document

#### Interactive PAP Interview (6-Question Guided Flow)

When invoked as `$clo-strategize pap interactive`, ask these questions one at a time before drafting:

1. **What is the research question?**
2. **What is the study design?** (RCT / natural experiment / quasi-experimental / observational)
3. **What are the primary outcome variables?** (names, measurement, data source)
4. **What is the identification strategy?** (randomization mechanism / treatment assignment / source of variation)
5. **What subgroup analyses are pre-specified?** (with justification for each)
6. **What multiple testing concerns exist?** (number of primary outcomes, family-wise error rate plan)

After all 6 answers are collected, proceed to PAP drafting.

#### PAP Sections

Dispatch Strategist in PAP mode to produce all standard sections:

1. **Study overview** - research question, design, treatment, control
2. **Outcomes** - primary, secondary, mechanism variables with measurement details
3. **Estimating equations** - with full notation protocol
4. **Subgroup analyses** - pre-specified, with justification for each
5. **Multiple testing correction** - Bonferroni / Benjamini-Hochberg / Romano-Wolf (specify which and why)
6. **Power calculations** - MDE, baseline statistics, sample size, assumptions stated explicitly with sensitivity
7. **Sample and exclusion rules** - inclusion criteria, attrition handling, outlier treatment
8. **Data and analysis** - sources, software, randomization/assignment mechanism
9. **Timeline** - data collection, analysis, registration dates
10. **Deviations log** - empty template for tracking post-registration changes

#### Platform-Specific PAP Templates

Ask the user which registry platform they plan to use (if unclear from context):

**AEA RCT Registry:**
- Most structured format. All fields required.
- Must be registered before intervention begins.
- Strict section ordering: hypotheses -> outcomes -> analysis -> power.
- Requires IRB information and funding sources.

**OSF (Open Science Framework):**
- More flexible format. Good for observational studies and natural experiments.
- Allows iterative updates with version history.
- Less rigid section structure - can adapt to study design.
- Supports pre-registration of observational/archival studies.

**EGAP (Evidence in Governance and Politics):**
- Development economics and political science focused.
- Additional governance and ethics questions required.
- Emphasizes pre-specification of heterogeneous treatment effects.
- Requires description of implementing partners and field conditions.

#### Observational Study PAP Adaptation

For observational, quasi-experimental, or natural experiment designs, adapt the PAP template:

- **Identification strategy replaces randomization** - describe the source of exogenous variation
- **Comparison group replaces control group** - define who is compared to whom and why
- **Identification assumption discussion** - explicitly state and defend each assumption
- **Placebo and falsification tests** - pre-specify what SHOULD NOT show effects
- **Robustness to specification choices** - pre-commit to bandwidth, functional form, sample restrictions
- **Treatment of endogeneity concerns** - document known threats and planned diagnostics

#### ASSUMED Placeholder Safety

**CRITICAL: Flag every ASSUMED item clearly. The researcher must review and approve before registration.**

When drafting a PAP from a topic (without a full research spec or interactive interview), many details will be assumed. For each assumed item:

- Mark it with `[ASSUMED]` in bold
- Explain what was assumed and why
- Provide the most reasonable default but flag it for review

A registered PAP with unchecked assumptions is worse than no PAP. The final section of every PAP must include:

```markdown
## Pre-Registration Checklist

**Review every [ASSUMED] item before registering this plan.**

- [ ] [ASSUMED] Item 1 - [what was assumed]
- [ ] [ASSUMED] Item 2 - [what was assumed]

**Do not register until all items are reviewed and confirmed or corrected.**
```

#### Optional strategist-critic Review

After PAP creation, optionally dispatch the strategist-critic to review:
- Are identification assumptions clearly stated and defensible?
- Is the estimator choice appropriate for the design?
- Are power calculation assumptions reasonable? Show sensitivity.
- Are pre-specified subgroups justified (not fishing)?
- Are multiple testing corrections appropriate?
- Are any [ASSUMED] items potentially problematic if left uncorrected?

Save review to `quality_reports/pre_analysis_plan_[topic]_review.md`

Save PAP to `quality_reports/pre_analysis_plan_[topic].md`

### `$clo-strategize theory [target]` - Optional Theory Support

Use this mode only when the user explicitly requests formal theory, proof support, propositions, lemmas, assumptions, or structural/theory+empirics formalization.

**Agents:** Theorist -> theorist-critic
**Output:** Theory memo or formal manuscript block, plus theory review

Workflow:
1. Confirm the request is explicitly theory-related.
2. Read the strategy memo, active manuscript section, repo bibliography, and notation conventions when available.
3. Dispatch `theorist` to produce a bounded theory memo or formal block.
4. Dispatch `theorist_critic` to review proof logic, assumptions, notation, and calibration.
5. Save outputs only to parent-resolved target paths or `quality_reports/theory/`.

Do not use this mode for standard reduced-form empirical papers unless the user explicitly asks.

### Decision Records

When `$clo-strategize` selects among plausible identification strategies, create or recommend a `decision_record` using `../clo-workflow/templates/decision-record.md`.

The record should state why the chosen design beats rejected alternatives, the key assumptions, and what evidence would change the decision.

---

## Principles

- **Strategist proposes, strategist-critic critiques.** Adversarial pairing catches design flaws early.
- **Strategy memo is the contract.** Once approved, the Coder implements it faithfully.
- **Catch problems before coding.** A flawed strategy caught now saves weeks of wasted analysis.
- **Multiple strategies are OK.** Present trade-offs and let the user choose.
- **The user decides.** If Strategist and strategist-critic disagree after 3 rounds, the user resolves it.
- **Record real design choices.** When the design choice matters, create a decision record so future reviews and R&Rs can explain why this path was chosen.
- **Pre-specification is the point.** Everything in a PAP is decided before seeing outcomes.
- **Be honest about what's exploratory.** Label subgroups and secondary outcomes clearly.
- **Power calculations require assumptions.** State every assumption. Show sensitivity.
- **A PAP is a commitment device.** Make sure the researcher understands what they're committing to.




