# Dittonomics

Dittonomics is a public manual and starter kit for a deliberately remixed Codex research workflow.

The name is literal: like Ditto, the project copies useful traits from multiple upstream repos and reshapes them into one portable system for empirical work in Codex.

> Caution
>
> This repository is under active construction and will change frequently. New skills, project-management workflows, and additional integration patterns will be added over time.

The project keeps the upstream workflow architecture, but rewrites the active guidance for Codex:

- `CLAUDE.md` becomes `AGENTS.md`, `AGENTS.override.md`, and repo-local skills
- `.claude/rules` and `.claude/references` become active `clo-workflow` references plus source mirrors
- slash commands become explicit `$clo-*` skills
- Claude agents become Codex custom subagents
- hidden hook behavior becomes explicit Codex utilities, references, and config guidance
- `explorations/` stays a repo-level sandbox and should be created when missing

This repository is documentation-first, but it also includes a forkable `.codex/` starter layer. It explains the architecture, customization patterns, and migration layer while shipping a reusable Codex-facing template bundle.

![Dittonomics mascot](guide/assets/ditto-mascot.svg)

## What This Repo Contains

- `.codex/`: forkable starter bundle with generic `AGENTS.md`, `clo-*` skills, custom subagents, and a workflow quick reference
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
- journal targeting remains customizable and is not limited to a fixed list
- example overlays may mention concrete journals to illustrate how a user can adapt the reference layer
- project-specific overlays still belong in repo `AGENTS.md`, `AGENTS.override.md`, and `.agents/skills/`

## Forking This Repo

If you fork this repository, the public starter layer is:

- `.codex/AGENTS.md`
- `.codex/agents/`
- `.codex/skills/`
- `.codex/WORKFLOW_QUICK_REF.md`

Treat that folder as a distributable starter kit. Copy or adapt it into your own `~/.codex/` home when you want a user-level install, and use repo-local `AGENTS.md`, `AGENTS.override.md`, and `.agents/skills/` for project-specific behavior.

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

This manual is adapted from:

- the Claude-based [Clo-Author](https://hsantanna.org/clo-author/) project and repo by Hugo Sant'Anna
- [my_claude_skills](https://github.com/dariia-m/my_claude_skills) by Daria M.
- [claudeblattman](https://github.com/chrisblattman/claudeblattman) by Chris Blattman

It does not attempt a literal clone of any one repo. The goal is to preserve the useful architecture and workflow patterns while making the instructions accurate and usable for Codex.