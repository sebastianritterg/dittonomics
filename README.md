# Dittonomics

Dittonomics is a public manual and starter kit for a deliberately remixed Codex research workflow.

The name is literal: like Ditto, the project copies useful traits from multiple upstream repos and reshapes them into one portable system for empirical work in Codex.

> Caution
>
> This repository is under active construction and will keep changing as the public starter and docs catch up with the live system.

The public repo keeps the upstream workflow architecture, but rewrites the active guidance for Codex:

- `CLAUDE.md` becomes `AGENTS.md`, `AGENTS.override.md`, and repo-local skills
- `.claude/rules` and `.claude/references` become active workflow references plus source mirrors
- slash commands become explicit `$clo-*` skills
- Claude agents become Codex custom subagents
- hidden hook behavior becomes explicit utilities, references, and config guidance
- `explorations/` stays a repo-level sandbox and should be created when missing
- writing voice becomes an explicit optional layer instead of an undocumented personal habit

This repository is documentation-first, but it also includes a forkable `.codex/` starter layer. It explains the architecture, customization patterns, migration layer, optional voice setup, and ships a reusable Codex-facing template bundle.

![Dittonomics mascot](guide/assets/ditto-mascot.svg)

## What This Repo Contains

- `.codex/`: forkable starter bundle with generic `AGENTS.md`, `clo-*` skills, custom subagents, and workflow references
- `guide/`: Quarto source for the public documentation site
- `docs/`: rendered site output for GitHub Pages
- `voice/`: public templates for building your own writing-voice layer
- `.github/workflows/render-docs.yml`: render workflow that keeps `docs/` in sync

## Documentation Structure

- Quick Start
- User Guide
- Agents
- Architecture
- Customization
- Reference

## Core Defaults Reflected Here

- the main Codex session is the orchestrator
- the parent orchestrator owns persistence unless it explicitly delegates a named target
- worker-critic separation is preserved across the stack
- Python is the primary default language
- Stata is the co-default
- R and Julia remain supported
- repo-local rules beat generic defaults
- voice is optional, explicit, and layered rather than hardcoded into every workflow

## Forking This Repo

If you fork this repository, the public starter layer is:

- `.codex/AGENTS.md`
- `.codex/agents/`
- `.codex/skills/`
- `.codex/WORKFLOW_QUICK_REF.md`
- `.codex/config.example.toml`
- `voice/`

Treat that folder as a distributable starter kit. Copy or adapt it into your own `~/.codex/` home when you want a user-level install, and use repo-local `AGENTS.md`, `AGENTS.override.md`, and `.agents/skills/` for project-specific behavior.

## Local Development

If Quarto is installed:

```bash
quarto render guide
```

That renders the site into `docs/`.

## Publishing

The intended public home is:

- Repo: `https://github.com/sebastianritterg/dittonomics`
- Site: `https://sebastianritterg.github.io/dittonomics/`

GitHub Pages should be configured to serve from the `docs/` directory on `main`.

## Attribution

This manual is adapted from:

- the Claude-based [Clo-Author](https://hsantanna.org/clo-author/) project and repo by Hugo Sant'Anna
- [my_claude_skills](https://github.com/dariia-m/my_claude_skills) by Daria M.
- [claudeblattman](https://github.com/chrisblattman/claudeblattman) by Chris Blattman

It does not attempt a literal clone of any one repo. The goal is to preserve the useful architecture and workflow patterns while making the instructions accurate and usable for Codex.