# Explorations

Use `explorations/` as the repo-level sandbox for experimental work, prototypes, and side investigations that are not yet part of the canonical pipeline.

## Codex Use

- If exploratory work is needed and `explorations/` does not exist, create it before starting the experiment.
- Create `explorations/README.md` plus `explorations/ARCHIVE/`.
- Give each exploration its own subfolder, for example `explorations/new-estimator/`.
- Keep lower-stakes prototypes here until they are ready to graduate into the main code, output, or paper directories.
- When an exploration becomes production work, move the relevant assets into the repo's canonical paths and leave a short note on what graduated.

## Recommended Structure

```text
explorations/
|- README.md
|- [active-project]/
|  |- README.md
|  |- scripts/
|  |- output/
|  `- notes/
`- ARCHIVE/
```

## Exploration README Template

```markdown
# [Project Name]

## Goal
[1-2 sentence description]

## Status
[IN PROGRESS / COMPLETED / ABANDONED] (started [DATE])

## Hypotheses to Test
1. [Hypothesis 1]
2. [Hypothesis 2]

## Success Criteria
- [Something you can measure]

## Findings
(Updated as work progresses)

## Timeline
- [DATE]: Started exploration
```

## Upstream Provenance

This active guidance is adapted from the upstream Clo-Author exploration sandbox. Read `references/source-explorations/README.md` and `references/source-explorations/exploration-readme.md` when exact upstream wording matters.




