# Routing Rules

This file standardizes how `clo-*` skills route work and resolve paths.

## Precedence Order

1. repo-local guidance
   `AGENTS.md`, `AGENTS.override.md`, repo-local skills, section READMEs, active manuscript structure
2. active project artifacts
   bibliography, existing manuscript files, current outputs, quality reports
3. phase-specific skill references
4. global workflow defaults

## Mode Resolution

Skills should resolve intent in this order:

1. exact canonical mode
2. recognized flag alias such as `--lit`, `--pap`, `--target`
3. recognized natural-language alias such as `literature`, `pre-analysis plan`, or `journal targeting`
4. inference from the first content word plus the rest of the request
5. one short clarification question only if the intent is still ambiguous

Natural-language routing is part of the contract, not a convenience feature.

## Path Resolution Policy

The skill, not the agent, resolves working paths first.

Each phase should resolve at least:

- manuscript root
- output root
- quality-report root
- code root
- talk root when relevant
- replication root when relevant
- exploration root when relevant

If a path is not obvious:

1. inspect the repo layout
2. inspect repo-local overlays
3. use the closest established convention in the repo
4. only then fall back to a generic default

## Bibliography Policy

When literature or writing quality depends on exemplars:

1. inspect the active bibliography and closest cited papers already in the repo
2. inspect any skill-specific references
3. use the global library only as fallback

This rule applies at minimum to `writer`, `librarian`, `strategist`, `domain_referee`, and `methods_referee`.
Apply the same repo-first policy to `ideator` and `ideator_critic` when they inspect closest papers, notes, or examples.

## Persistence Policy

- skills decide where artifacts live
- creator agents write only to named target locations in the task packet
- critics, referees, editor, and verifier return reports to the parent orchestrator
- the parent orchestrator saves reports, renames files, and promotes outputs unless explicit delegation says otherwise

## Dispatch Invariant

When a phase skill names a creator/critic or referee pairing, that routing is normative.

- invoking the skill counts as explicit permission to dispatch the named agents for the resolved mode
- paired creator/critic workflows should dispatch both roles unless the user explicitly asks for a lighter pass
- if subagent dispatch is unavailable, the main session may fall back, but it must state that fallback explicitly

## Skill Routing Summary

- `clo-ideate`
  routes to `ideator` and `ideator_critic` for pre-discovery idea generation and screening
- `clo-discover`
  routes to `librarian` and `explorer` families or runs interview directly; legacy ideation requests should redirect to `clo-ideate`
- `clo-strategize`
  routes to `strategist` and `strategist_critic`
- `clo-analyze`
  routes to `data_engineer`, `coder`, and `coder_critic`
- `clo-write`
  routes to `writer`, preserving `econ-intro-writing` for front-end work
- `clo-review`
  routes to the appropriate critic, referee, editor, or verifier workflow
- `clo-submit`
  orchestrates final checks and packaging, calling verifier or coder where needed
- `clo-talk`
  routes to `storyteller` and `storyteller_critic`
- `clo-revise`
  routes comments into writer or coder tasks while leaving decisions with the user
- `clo-new-project`
  schedules the phase graph; it does not redefine phase internals
- `clo-research-tools`
  is a utility toolbox and not a phase
