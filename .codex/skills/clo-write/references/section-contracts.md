# Section Contracts

Use this file as the source of truth for section-level inputs, restrictions, and default targets.

## General Rules

- Always prefer the repo's actual manuscript layout over generic defaults.
- If the user gives a file path, that path overrides the default target.
- If the repo lacks a standalone section, write the corresponding subsection in the nearest existing file and say so explicitly.
- Front-end work is governed by the repo's intro-writing logic when that exists.

## Generic Section Map

| Section | Required inputs | Optional inputs | Restrictions | Suggested default target |
|---|---|---|---|---|
| `abstract` | stable question, design, headline finding | contribution sentence, policy implication | do not finalize before core sections exist | `paper/sections/01_abstract.tex` |
| `intro` | active front-end notes, current draft | journal calibration, contribution variants | do not substitute a generic intro recipe if the repo has a stronger front-end workflow | `paper/sections/02_introduction.tex` |
| `context` | background notes, institutional details | references | keep institutional density here rather than bloating the intro | `paper/sections/03_context.tex` |
| `literature` | literature notes, annotated bibliography | positioning memo | synthesize by theme, not paper-by-paper | `paper/sections/04_literature.tex` |
| `data` | data notes, variable definitions, sample definition | descriptives table, measurement notes | if no standalone data section exists, write the corresponding subsection in the methods file | nearest methods file |
| `strategy` | strategy memo, estimand, identification assumptions | pseudo-code, robustness plan | do not invent tests not already planned or run | `paper/sections/05_strategy.tex` |
| `results` | existing tables/figures or results summary | heterogeneity notes | do not narrate estimates that do not exist | `paper/sections/06_results.tex` |
| `mechanisms` | mechanism evidence already produced | notes on interpretation | distinguish mechanism evidence from speculation | `paper/sections/07_mechanisms.tex` |
| `robustness` | checks already run or placeholders marked pending | threats-to-validity memo | do not claim robustness that has not been run | `paper/sections/08_robustness.tex` |
| `policy` | supported interpretation, scope limits | policy relevance notes | keep policy claims proportional to evidence | `paper/sections/09_policy.tex` |
| `conclusion` | stable headline results, limitations, contribution | policy and future-work angle | no new findings | `paper/sections/10_conclusion.tex` |

## Design Metadata

When `--design` is available, use it to calibrate:

- language strength
- assumption discussion
- typical threats
- example selection

Supported design tags:

- `did`
- `rdd`
- `iv`
- `scm`
- `generic`