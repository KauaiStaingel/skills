# Discovery and intake

Use discovery to remove consequential ambiguity, not to delay implementation.

## Repository reconnaissance

Inspect before asking questions:

1. Identify the framework, styling method, routing, rendering model, and test setup.
2. Find global styles, tokens, themes, fonts, icons, assets, primitives, and shared components.
3. Inspect sibling screens to learn established hierarchy, density, navigation, language, and behavior.
4. Find product documentation, acceptance criteria, analytics hints, fixtures, schemas, and real copy.
5. Run or preview the product when practical. Source alone cannot reveal every visual rule.
6. Note dirty worktree changes and preserve unrelated work.

Summarize what is already decided, what is inferred, and which gaps could change the result.

## Minimal brief

Capture these fields when relevant:

| Field | Decision it drives |
|---|---|
| Artifact | Layout grammar, density, and expected interactions |
| Audience and context | Vocabulary, familiarity, accessibility, and trust |
| Primary job | Information order and dominant action |
| Content and data | Components, hierarchy, edge cases, and density |
| Positioning | Tone, typography, color, imagery, and motion |
| Existing system | What must be reused or extended |
| References | Calibration, not cloning |
| Constraints | Platform, stack, devices, performance, compliance, scope |
| Success measure | What “better” means and what to verify |

For public-facing pages, add a **first-glance sentence**: what a new visitor must understand in roughly three seconds. It should identify the offer, subject, audience, or action concretely enough that the page does not depend on a vague headline.

## Material inventory

List the real material available before choosing a layout:

- product screenshots, data, charts, demos, and workflows;
- photography of people, place, process, product, packaging, or environment;
- prices, hours, address, availability, menu, catalog, or schedule;
- verified testimonials, customer logos, outcomes, and sources;
- brand assets, previous campaigns, editorial material, and physical artifacts.

If essential material is missing, request it or use an explicit placeholder such as `[photo of the storefront]` or `[real dashboard screenshot]`. Do not fabricate proof, and do not conceal the gap with generic icon cards, floating mockups, abstract gradients, or synthetic testimonials.

## High-signal questions

Ask only questions whose answers produce different implementations. Prefer one compact batch when the user can answer efficiently.

Useful questions include:

- Who performs the main task, and under what conditions?
- What should the user understand or do first?
- Which content is real, and what ranges or edge cases occur?
- Which existing brand or product rules are fixed?
- What specifically should be borrowed from or avoided in each reference?
- Which devices, input modes, locales, or accessibility needs are essential?
- What would make the result feel wrong even if it were usable?

Avoid asking users to choose implementation details they reasonably expect the UI developer to decide. Do not ask for information already present in the repository.

## User needs and hypotheses

Express needs around outcomes, not proposed widgets:

> When [context], the user needs to [goal], so they can [outcome].

Separate evidence from hypotheses. Examples:

- Evidence: operators use the screen continuously on 13-inch laptops.
- Hypothesis: a denser table will reduce task time.
- Test: complete the primary comparison task with realistic data at the target viewport.

Prioritize the assumptions with the highest combination of uncertainty and impact.

## Scope control

Define:

- surfaces and flows included;
- behavior that must remain unchanged;
- whether copy, assets, information architecture, or only presentation may change;
- acceptance criteria;
- proportional validation expected.

Do not infer authority to rewrite the brand, product model, or unrelated screens from a request to improve one UI.
