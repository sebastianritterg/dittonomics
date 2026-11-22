# Conclusion Playbook

## Purpose

Conclusions in economics papers should close the contribution. They are not a recap of every section.

The conclusion should restate the question, design, and main result compactly; interpret only what the evidence supports; acknowledge scope conditions; and end with a restrained implication for the literature or policy debate.

## Required Elements

1. Restate the research question and approach in one sentence.
2. Re-state the main result with magnitude, units, and benchmark when available.
3. Interpret mechanisms, welfare, or incidence only if the paper actually supports that interpretation.
4. State limitations briefly and honestly.
5. Draw one restrained, specific implication.
6. Add one forward-looking line only if it is meaningful and not generic.

## Default Scaffold

Rewrite this scaffold rather than pasting it mechanically:

```text
This paper studies [QUESTION] in [SETTING] using [DESIGN]. We find [MAIN RESULT + MAGNITUDE]. The evidence is consistent with [INTERPRETATION], though [LIMITATION] limits inference about [SCOPE]. These findings inform [POLICY/LITERATURE] by [IMPLICATION].
```

## Recommended Paragraph Plan

For a short conclusion, use one to three paragraphs:

1. **Core answer.** Question, setting, design, headline magnitude.
2. **Interpretation and scope.** Mechanism or welfare interpretation if supported, paired with the main limitation or scope condition.
3. **Contribution and implication.** What the result changes in the literature or policy conversation, stated specifically.

For a longer conclusion, add only one extra paragraph, usually for policy scope or external validity. Do not add a literature review, robustness recap, or new result.

## Use The Paper's Own References

Before drafting a conclusion, inspect the conclusions or final discussion sections of the closest already-cited papers in the repo when available.

Use them to calibrate:

- how much magnitude belongs in the closing paragraph
- whether the target literature ends on policy, method, mechanism, or external validity
- how cautious the limitation language should be
- how the paper names its contribution without overselling

Do not imitate sentences, cadence, or claims from model papers. Repo-local manuscript logic and the user's voice hierarchy remain higher priority.

## Language Rules

- Keep causal language no stronger than the design allows.
- If the main evidence is reduced-form, say what the results show and what they are consistent with; do not identify unobserved welfare or mediation unless the paper does.
- If a mechanism section is suggestive, use `consistent with`, `suggestive of`, or `mechanism-consistency evidence`.
- Do not introduce new citations unless the conclusion needs a very specific literature positioning sentence.
- Do not introduce new results, tables, robustness checks, or empirical objects.
- Avoid generic endings such as `future research should explore this issue`.

## Common Failure Modes

- Repeating the introduction almost verbatim.
- Listing every section of the paper again.
- Ending with a broad policy slogan unsupported by the design.
- Treating limitations as an apology rather than a scope condition.
- Saying `important implications` without naming the actual implication.
- Adding speculative mechanisms because the conclusion feels too short.

## Microexamples

```text
This paper studies whether [TREATMENT] affects [OUTCOME] in [SETTING] using [DESIGN]. We find [MAIN EFFECT WITH UNITS], equal to [BENCHMARK].
```

Why this works: it gives the reader a compact reminder of the paper's core contribution.

```text
The evidence is consistent with [MECHANISM], though the design is less informative about [LIMITATION OR MARGIN].
```

Why this works: it pairs interpretation with an explicit boundary.

```text
Taken together, the results inform [LITERATURE OR POLICY QUESTION] by showing that [SPECIFIC TAKEAWAY].
```

Why this works: it ends on a concrete implication rather than a generic closing.

## Finish Check

Before finalizing, verify:

- the headline result and magnitude match the tables exactly
- no sentence reports evidence not already shown in the paper
- limitations are short, honest, and not self-defeating
- the implication is specific enough to survive without adjectives like `important`
- the final sentence sounds like the author, not like a grant abstract
