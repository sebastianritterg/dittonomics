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

## Natural-Language Contract

Every `clo-*` skill must treat ordinary user phrasing as a routable command. Resolve the intended phase, mode, target, and agent route before deciding whether to ask a question.

- Generic verbs such as `check`, `look at`, `review`, `fix`, `draft`, `write`, `run`, `build`, `prepare`, `summarize`, `audit`, `validate`, `make`, and `help with` are valid intent signals when paired with a research artifact.
- Artifact words disambiguate the mode: `section`, `paragraph`, `intro`, `conclusion`, or `prose` usually mean writing or proofread; `identification`, `strategy`, `estimand`, or `assumptions` mean strategy/methods; `script`, `regression`, `table`, `figure`, or `data` mean analysis/code; `journal`, `submission`, `replication package`, or `cover letter` mean submission; `slides`, `seminar`, `talk`, or `deck` mean talk.
- If a request names a specific Clo skill and uses natural language after it, stay inside that skill and normalize the phrase to that skill's closest canonical mode.
- If no skill is named, choose the closest `clo-*` phase from the artifact and verb. Do not require slash-command syntax.
- Prefer a reasonable route over a clarification question when the target and likely artifact type are clear.
- Ask one short clarification question only when two materially different routes would cause different agents to edit or review different artifacts.

## Natural-Language Phase Matrix

| User phrasing | Canonical route |
|---|---|
| "I have a vague idea", "help me shape this topic", "is this idea worth pursuing" | `clo-ideate session` or `clo-ideate evaluate` |
| "turn this into a research question", "give me candidate questions" | `clo-ideate rq` |
| "find the literature", "map related papers", "what papers am I missing" | `clo-discover lit` |
| "find data", "what dataset could identify this", "assess data feasibility" | `clo-discover data` |
| "interview me", "help formalize the project", "build a research spec" | `clo-discover interview` |
| "design the empirical strategy", "what is the identification", "choose estimand" | `clo-strategize strategy` |
| "write a PAP", "pre-analysis plan", "registration plan" | `clo-strategize pap` |
| "formal model", "proposition", "proof", "theory section" | `clo-strategize theory` only when explicitly theory-related |
| "run the analysis", "make the table", "clean the data", "estimate this regression" | `clo-analyze` |
| "write the intro", "draft section 5", "revise the conclusion", "humanize this paragraph" | `clo-write` |
| "check section 5", "proofread this", "writing check", "polish this paragraph" | `clo-review --proofread` |
| "methods check", "audit the ID", "is the causal design valid" | `clo-review --methods` |
| "code check", "review this script", "lint the analysis" | `clo-review --code` or `clo-research-tools lint` when mechanical only |
| "referee this", "simulate peer review", "desk review for QJE" | `clo-review --peer` |
| "make slides", "build a seminar deck", "audit this talk" | `clo-talk create` or `clo-talk audit` |
| "journal target", "prepare submission", "replication package", "final gate" | `clo-submit target`, `package`, `audit`, or `final` |
| "plan the R&R", "extract reviewer tasks", "draft response letter" | `clo-revise roadmap` or `respond` |
| "checkpoint", "resume context", "compile", "dashboard", "validate bibliography" | `clo-research-tools` |

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
Apply the same repo-first policy to `revision_planner` and `revision_planner_critic` when they inspect the live manuscript, outputs, prior reviews, and bibliography.

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
  routes `roadmap` through `revision_planner` and `revision_planner_critic`, then uses `execute` to send approved work into writer, coder, or data-engineer lanes while leaving high-stakes decisions with the user
- `clo-new-project`
  schedules the phase graph; it does not redefine phase internals
- `clo-research-tools`
  is a utility toolbox and not a phase

## Review Routing Matrix

`clo-review` uses exact Codex agent type names when dispatching:

| Review mode | Agent route |
|---|---|
| `.tex` paper target | `writer_critic`, `strategist_critic`, and `verifier` in parallel |
| `.R`, `.py`, `.do`, `.jl` target or `--code` | `coder_critic` standalone |
| `.tex` talk target under a talk directory | `storyteller_critic` standalone |
| `--proofread` | `writer_critic` standalone |
| `--methods` | `strategist_critic` standalone |
| `--peer`, `--stress`, `--peer --r2` | `editor`, then `domain_referee` and `methods_referee`, then `editor` synthesis |
| `--theory` | `theorist_critic` standalone; explicit-only |
| `--replicate` | `coder`, then `coder_critic`, then comparison and verification as needed |
| `--all` or paper excellence | all resolved direct critics plus `verifier`, with an aggregate summary |

Generic manuscript-section checks are proofreads. When the user says `clo-review check section 5`, `review section 5`, `check this section`, `polish this paragraph`, or similar prose-targeted language, resolve the mode to `--proofread` and dispatch `writer_critic`. Only override this default when the user explicitly asks for methods, code, peer review, theory, or a comprehensive full-paper review.
