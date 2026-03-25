# Codex-Clo-Author

Codex-Clo-Author is a public manual for running a Clo-Author-style empirical research workflow in Codex.

> Caution
>
> This repository is under active construction and will change frequently. New skills, project-management workflows, and additional integration patterns will be added over time.

The project keeps the upstream Clo-Author information architecture and workflow logic, but rewrites the active guidance for Codex:

- `CLAUDE.md` becomes `AGENTS.md`, `AGENTS.override.md`, and repo-local skills
- `.claude/rules` and `.claude/references` become active `clo-workflow` references plus source mirrors
- slash commands become explicit `$clo-*` skills
- Claude agents become Codex custom subagents
- hidden hook behavior becomes explicit Codex utilities, references, and config guidance
- `explorations/` stays a repo-level sandbox and should be created when missing

This repository is documentation-first. It explains the architecture, customization patterns, and migration layer. It is not a one-click installer.

## What This Repo Contains

- `guide/`: Quarto source for the public documentation site
- `docs/`: rendered site output for GitHub Pages
- `.github/workflows/render-docs.yml`: render workflow that keeps `docs/` in sync

## Documentation Structure

- Quick Start
- User Guide
- Agents
- Architecture
- Customization
- Reference

## Core Defaults Reflected Here

- Python is the primary default language
- Stata is the co-default
- R and Julia remain supported
- Journal of Development Economics appears in journal-targeting examples
- Regional Studies and Journal of Economic Geography are included as neighboring outlets

## Local Development

If Quarto is installed:

```bash
quarto render guide
```

That renders the site into `docs/`.

## Publishing

The intended public home is:

- Repo: `https://github.com/sebastianritterg/codex-clo-author`
- Site: `https://sebastianritterg.github.io/codex-clo-author/`

GitHub Pages should be configured to serve from the `docs/` directory on `main`.

## Attribution

This manual is adapted from the Claude-based [Clo-Author](https://hsantanna.org/clo-author/) project and repo by Hugo Sant'Anna.

It does not attempt a literal Claude clone. The goal is to preserve the workflow architecture while making the instructions accurate and usable for Codex.
