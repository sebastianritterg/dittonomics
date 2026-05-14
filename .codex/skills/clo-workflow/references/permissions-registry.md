# Permission Registry

This file centralizes the advisory dispatch contract for the Dittonomics agent layer. It is adapted from Clo-Author 26.05, but translated into Codex conventions.

The registry does not replace skill activation metadata. Existing `$clo-*` skills and `agents/openai.yaml` keyword behavior remain authoritative for invocation.

## Registry Fields

- `phase`: workflow family
- `requires`: expected inputs before dispatch
- `produces`: expected outputs or report type
- `critic`: paired critic when one exists
- `escalation`: who resolves disagreement or missing information
- `quality_weight`: scoring weight when relevant
- `activation`: explicit workflow skill or direct explicit-only mode

## Roles

| Agent | Phase | Requires | Produces | Critic | Escalation | Quality | Activation |
|---|---|---|---|---|---|---|---|
| `ideator` | ideation | seed idea, topic, data hunch, or shortlist | `idea_brief`, `rq_shortlist` | `ideator_critic` | user | advisory | `$clo-ideate` |
| `ideator_critic` | ideation | ideation output | `idea_screen` | none | user | advisory | after creator pass |
| `librarian` | discovery | research idea or spec | `lit_review`, bibliography, frontier map | `librarian_critic` | user | 10% | `$clo-discover lit` |
| `explorer` | discovery | research idea/spec and variable needs | `data_assessment` | `explorer_critic` | user | 10% | `$clo-discover data` |
| `strategist` | strategy | research spec, literature, data assessment when available | `strategy_memo`, robustness plan, decision record | `strategist_critic` | user | 25% | `$clo-strategize` |
| `theorist` | strategy | explicit theory-mode request and strategy/theory target | theory memo, assumptions, propositions, proof sketch | `theorist_critic` | user | conditional | `$clo-strategize theory` |
| `data_engineer` | analysis | strategy memo or explicit data task | cleaned data, data docs, figure inputs | `coder_critic` | strategist or user | code weight | `$clo-analyze` |
| `coder` | analysis | strategy memo or explicit code target | scripts, tables, figures, results summary | `coder_critic` | strategist or user | 15% | `$clo-analyze` |
| `writer` | writing | target section, manuscript context, evidence artifacts | manuscript section or prose bundle | `writer_critic` | user | 10% | `$clo-write` |
| `revision_planner` | revision | editor/referee reports and submitted manuscript | task graph, roadmap, decision log | `revision_planner_critic` | user | advisory | `$clo-revise roadmap` |
| `editor` | review | manuscript and target journal when relevant | desk review and editorial decision | none | user | advisory | `$clo-review --peer` |
| `domain_referee` | review | manuscript and review packet | domain referee report | none | editor | 12.5% | `$clo-review --peer` |
| `methods_referee` | review | manuscript and review packet | methods referee report | none | editor | 12.5% | `$clo-review --peer` |
| `theorist_critic` | review | theory memo or formal theory section | theory review | none | user | conditional | `$clo-review --theory` |
| `storyteller` | talk | manuscript and talk format | Beamer talk by default, Quarto only with `--quarto` | `storyteller_critic` | writer or user | advisory | `$clo-talk` |
| `verifier` | submission | package or artifact to verify | verification report | none | user | 5% | `$clo-submit` |

## Dispatch Rules

- The parent Codex session resolves paths and creates the task packet before dispatch.
- Missing expected inputs should be reported before dispatch when practical.
- Critics never edit source artifacts.
- Creator agents write only to named target locations.
- Theory agents are explicit-only and never auto-activate for ordinary empirical papers.
- Beamer is the default talk output in Dittonomics even though upstream Clo-Author 26.05 moved Quarto-first.
