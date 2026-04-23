# Codex-Clo-Author Docs Repo

This repository is the source of truth for the public Codex-Clo-Author manual and Quarto site.

## Editing Rules

- Edit content under `guide/`. Treat `docs/` as generated output.
- Keep `.codex/` as a public starter kit. It should stay generic, forkable, and free of machine-specific paths.
- Keep the information architecture aligned with Clo-Author: Quick Start, User Guide, Agents, Architecture, Customization, Reference.
- Rewrite for Codex-native concepts. Do not leave Claude-only instructions in active documentation.
- Preserve the worker-critic architecture, the six pipeline phases, and the exploration sandbox model.
- Document `clo-revise` as a loop-back strategic workflow rather than a new linear pipeline phase.
- Keep the public docs generic first. If you show a concrete install or field profile, label it as an example overlay rather than a personal default.

## Render Rule

- When Quarto is available, render from `guide/` so output lands in `docs/`.
- Do not hand-edit generated HTML in `docs/` except for temporary placeholders before the first render.
