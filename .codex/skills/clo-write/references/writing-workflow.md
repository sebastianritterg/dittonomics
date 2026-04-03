# Writing Workflow

Use this sequence for default drafting unless the user explicitly asks for a lighter pass.

1. Identify the section, design, target journal, and target file.
2. Read the section contract in `section-contracts.md`.
3. Load the active style hierarchy:
   - always read `~/voice/core_voice.md`, `~/voice/voice_examples.md`, `~/voice/econ_paper_register.md`, and `~/voice/style_hierarchy.md` when the user has them
   - read `~/voice/collaboration_register.md` only in joint-paper mode
   - read `~/voice/journal_tightening_register.md` only in journal-tightening mode
   - read nearby manuscript sections only in current-draft mode
4. Gather manuscript context, repo overlays, bibliography, quality reports, and outputs.
5. Inspect the active bibliography and closest cited papers in the repo before consulting any global examples.
6. Load the governing specialist skill when required.
7. Produce a section outline.
8. Produce a paragraph plan.
9. Draft the section.
10. Run a local finish check:
   - paragraph architecture is `claim -> support -> implication`
   - causal language matches design strength
   - estimates and citations are not fabricated
   - placeholders are explicit
   - current-draft calibration did not import weak local habits
   - optional overlays did not flatten the user's core voice
11. Run `humanizer`.
12. If manuscript polish is requested, hand off to `$clo-review --proofread`.

## Output Bundle

Default delivery order:

1. Outline
2. Paragraph plan
3. Draft text
4. Humanized draft

## Overlay Semantics

- `--joint-paper`
  Load the collaboration register as a secondary overlay for pacing, synthesis, and selective compression.
- `--journal-tightening`
  Load the journal-tightening register as a secondary overlay for restraint, paragraph economy, and compact contribution framing.
- `--current-draft`
  Read nearby manuscript text and align to the current manuscript state for local consistency only.