---
name: clo-submit
description: Prepare submission work for a Clo/Dittonomics project. Use when the user asks for journal targeting, submission strategy, replication package, AEA package, final verification, submission checklist, cover letter, replication audit, or calls $clo-submit. Routes to verifier and coder where needed.
---

# Clo Submit

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

## Natural-Language Routing

Resolve ordinary submission requests before asking for clarification:

- `where should I submit`, `journal target`, `rank journals`, `fit for [journal]`, or `submission strategy` -> `target`
- `build replication package`, `AEA package`, `prepare replication files`, `make README`, or `package the code/data` -> `package`
- `audit replication`, `check package`, `verify reproducibility`, `does the package run`, or `submission audit` -> `audit`
- `final submission`, `submission gate`, `ready to submit`, `cover letter`, `checklist`, or `final verification` -> `final`

When the request says `check before submitting` without a narrower object, resolve to `final`.

## Source Workflow

# Submit

Submission pipeline with four modes covering journal selection through final verification.

**Input:** `$ARGUMENTS` - mode keyword, optionally followed by journal name.

---

## Modes

### `$clo-submit target` - Journal Targeting
Get ranked journal recommendations.

**Agent:** Orchestrator (journal selection function)

Considers: contribution fit, methodology fit, audience fit, recent publications, desk rejection risk. Consults ~/.codex/skills/clo-workflow/references/domain-profile.md  for journal tiers.

Output: Ranked list of 3 target journals with rationale.
Save to `quality_reports/journal_recommendations_[date].md`

### `$clo-submit package` - Build Replication Package
Assemble AEA-compliant replication package.

**Agents:** `coder` + `verifier`

Produces:
- Master script that runs all analyses end-to-end
- README with data sources, computational requirements, instructions
- Data documentation and codebook
- Organized file structure per AEA standards
Save to `Replication/`

### `$clo-submit audit` - Audit Replication Package
Verify replication package completeness.

**Agent:** `verifier` (submission mode - 10 checks)

Checks:
1. Master script exists and runs
2. All tables reproduce
3. All figures reproduce
4. README complete
5. Data documentation present
6. Numbered script order
7. Dependencies listed
8. Runtime documented
9. Output paths match paper references
10. No hardcoded paths

### `$clo-submit final [journal]` - Final Submission Gate
Full verification + score enforcement + submission checklist.

Workflow:
1. Run comprehensive review if not done recently
2. Run replication audit
3. Check score gate: aggregate >= 95, all components >= 80
4. If PASS: generate cover letter draft + submission checklist
5. If FAIL: list blocking issues and stop

---

## Principles
- **Score >= 95 + all components >= 80. No exceptions.**
- **Don't skip verification.** Even if reports exist, check they're recent.
- **If it fails, stop.** Don't generate materials for a failing paper.
- **Cover letter is a draft.** User must review before sending.




