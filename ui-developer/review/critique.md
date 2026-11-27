# Design critique and anti-default audit

Critique the work as a fresh reviewer after implementation is functional. Separate defects, risks, and preferences.

## Review order

1. Product fit and task completion.
2. Information architecture and hierarchy.
3. Interaction, feedback, error prevention, and recovery.
4. Accessibility and responsive behavior.
5. Visual system and craft.
6. Distinctiveness and generated-UI tells.
7. Performance and implementation durability.

Do not let a striking aesthetic hide a weak task flow, or let functional correctness excuse poor hierarchy.

## Classify findings

- **Blocker:** prevents task completion, creates serious exclusion, data loss, or a broken layout.
- **Major:** materially harms comprehension, efficiency, consistency, or product fit.
- **Moderate:** visible craft or state gap with limited task impact.
- **Minor:** polish issue or preference with low impact.

For each finding, state the location, evidence, consequence, and smallest durable correction. Avoid vague feedback such as “make it pop.”

For screenshot review, a compact severity vocabulary is acceptable: `critical` for broken or unusable, `high` for a major task, accessibility, hierarchy, or unmistakable template failure, `medium` for a bounded craft gap, and `nit` for low-impact polish. Correct critical and high findings and re-capture when implementation is authorized.

## Heuristic questions

- Is system status visible and timely?
- Does language match the user's mental model?
- Can users cancel, undo, escape, or recover where needed?
- Are conventions consistent within the product and platform?
- Are errors prevented before being explained?
- Is recognition favored over memory?
- Are frequent users efficient without excluding new users?
- Does every visible unit compete for attention, and can any be removed?
- Do errors identify cause and recovery?
- Is help contextual and task-focused?

## Anti-default audit

Read [tells-catalog.md](tells-catalog.md) for the complete taxonomy. Record evidence by catalog ID so source findings, screenshots, and corrections can be compared.

Judge the stack, not one isolated choice:

- category-template structure;
- generic or fabricated content;
- unmodified library look;
- repeated card, icon-tile, radius, shadow, or gradient treatment;
- decorative labels, numbers, arrows, grids, glows, blobs, and motion;
- one aesthetic applied regardless of artifact type;
- second-order trend clusters used as automatic escape;
- missing edge states and mobile craft;
- visually polished UI that does not reveal the product's real subject.

When a flagged choice is grounded in the brief or existing system, keep it. Document the rationale only when future reviewers may otherwise “correct” it back to a default.

For each tell finding, record:

```text
ID · location · evidence type (code/render/inferred) · confidence
Why it is generic in this context
Product or user consequence
Replace / keep with rationale
```

Do not convert tell strength into user-impact severity mechanically. A weak-looking pattern can hide a critical accessibility defect, while a strong visual tell can be harmless when the brand explicitly requires it.

## Final correction pass

- Remove one unnecessary decorative layer.
- Strengthen the weakest hierarchy transition.
- Fix repeated one-off values at their system source.
- Recheck the primary flow with real content.
- Re-run relevant validation after changes.

If the request is review-only, report findings without modifying files.
