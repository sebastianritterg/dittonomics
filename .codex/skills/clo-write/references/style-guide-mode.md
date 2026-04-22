# Style Guide Mode

Use this reference only when the user explicitly asks for `style-guide` extraction or for `--use-style-guide`.

## Purpose

This is an optional helper layer for writing calibration. It never replaces:

1. repo-local guidance
2. `econ-intro-writing` for front-end structure
3. the active `~/voice/*.md` hierarchy
4. current-draft local calibration when explicitly requested

It sits above global examples and paper-model libraries only when explicitly enabled.

## Extraction Mode

When the task is `style-guide`:

1. Gather at least two prior papers or representative writing samples when possible.
2. Prefer introductions, abstracts, conclusions, and early body paragraphs.
3. Extract observed patterns only:
   - sentence length and cadence
   - paragraph openings and closings
   - citation density and citation style
   - diction and recurring preferred verbs
   - anti-patterns the user visibly avoids
4. Ground every pattern in actual evidence from the corpus.
5. If evidence is thin or mixed, mark the pattern as low-confidence instead of forcing a rule.

## Helper Mode

When `--use-style-guide` is explicitly enabled:

1. Read the extracted style guide only after the core voice hierarchy.
2. Use it for secondary calibration:
   - rhythm
   - sentence compression
   - preferred transitions
   - recurring lexical habits
3. Ignore it when it conflicts with repo-local conventions, front-end architecture, or the active core voice.
4. Do not let it flatten the user's recognizable style into a generic benchmark voice.

## Safety Rules

- Never let a style guide override `econ-intro-writing`.
- Never let a style guide override `~/voice/core_voice.md`.
- Never treat the style guide as permission to imitate prior text verbatim.
- Never use a single paper as the exclusive source of truth about the user's voice.
