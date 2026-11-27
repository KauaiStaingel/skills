---
name: ui-developer
description: Create, extend, restyle, or review production UI for websites, systems, and apps when product fit, distinctive visual direction, responsive implementation, interaction states, accessibility, and rendered QA matter. Use for pages, flows, dashboards, components, design systems, and UI audits; not for backend-only work or pure marketing copy.
---

# UI Developer

Build interfaces that feel specific to their product, not assembled from fashionable defaults. Treat visual quality, usability, implementation, and validation as one continuous job.

## Core contract

- Start from the product, users, task, content, and constraints. Aesthetic direction follows strategy.
- Preserve the user's explicit choices and the project's established system. Do not redesign outside the requested scope.
- Inspect existing code, routes, tokens, components, assets, and neighboring screens before proposing changes.
- Use real or structurally realistic content and inventory available photos, product screens, data, people, places, prices, and evidence. Do not let placeholder copy determine layout or fill missing media with generic atmosphere.
- Prefer familiar interaction behavior and accessible primitives; create distinction through composition, typography, art direction, content, and a brief-specific visual idea.
- Do not ban a font, color, layout, or effect merely because it is common in generated UI. Reject unexamined defaults and unjustified stacks of them.
- Evaluate rendered pixels as well as source. A clean component tree does not prove good composition.
- Do not silently introduce dependencies, replace working architecture, or invent product requirements.

## Choose the working mode

| Request | Mode | Required modules |
|---|---|---|
| New page, app, flow, or substantial redesign | Full creation | All workflow stages relevant to the artifact |
| Extend an existing product or design system | System extension | Inspect, then craft and implementation modules that match the change |
| Small component or local visual fix | Surgical change | Existing system, component states, implementation, proportional QA |
| Review, critique, or “remove the AI look” | Audit | Review modules plus rendered QA; edit only when requested |
| Prototype or explore a risky idea | Exploration | Discovery, calibration, prototyping, then only the necessary craft modules |

Do not force a small task through every document. Load the modules whose decisions affect the current scope.

## End-to-end workflow

### 0. Establish the ground truth

1. Inspect the repository and running UI when available.
2. Locate product requirements, routes, design tokens, global styles, component libraries, fonts, icons, assets, tests, and any `DESIGN.md` or equivalent.
3. Determine the artifact type, scope, stack, supported devices, and what must remain unchanged.
4. Identify whether the user is asking for creation, implementation, review, or all three.

For intake and repository reconnaissance, read [methodology/discovery.md](methodology/discovery.md).

### 1. Define the product brief

Capture the minimum facts that materially change the solution:

- product and artifact;
- target users, context, and familiarity;
- primary job, action, and information;
- real content and data characteristics;
- positioning and desired emotional tone;
- references and what is useful in each;
- brand, platform, technical, accessibility, and delivery constraints;
- success criteria and the riskiest assumptions.

Infer from evidence first. Ask only high-signal questions that cannot be answered safely from the project. State meaningful assumptions.

For a public or persuasive page, also write what a first-time visitor must understand within roughly three seconds. Prefer a concrete product, audience, or outcome statement over an abstract promise.

### 2. Calibrate and commit to a direction

Before writing substantial UI code:

1. Translate the brief into 3–5 precise adjectives, including a useful tension when appropriate, such as “technical but not cold.”
2. Generate two or three genuinely different structural or visual directions when the brief leaves meaningful freedom.
3. Compare them against product fit, usability, feasibility, differentiation, and the existing system.
4. Select one direction and define one signature move. Spend boldness there; keep supporting decisions disciplined.
5. Review the direction against category defaults and current generated-UI clichés. Revise choices that could have been made for any similar product.

Read [methodology/calibration.md](methodology/calibration.md). When visual references are needed, read [methodology/reference-research.md](methodology/reference-research.md). For prototypes and uncertain flows, also read [methodology/prototyping.md](methodology/prototyping.md).

### 3. Form the UI system

Define only the system necessary for the scope:

- semantic color roles;
- typography roles and hierarchy;
- spacing rhythm, grid, density, and responsive behavior;
- borders, radius, elevation, and surface logic;
- component hierarchy and interaction states;
- icon and imagery direction;
- motion principles;
- content voice and terminology.

For multi-screen or continuing work, record durable decisions in the project's existing design document or a concise `DESIGN.md`; read [methodology/design-record.md](methodology/design-record.md). Do not create process artifacts for a trivial local change.

Read the relevant craft modules:

- [craft/foundations.md](craft/foundations.md) for hierarchy, tokens, color, spacing, surfaces, imagery, and motion.
- [craft/typography-content.md](craft/typography-content.md) for headings, typography, labels, interface copy, errors, and empty states.
- [craft/layout-responsive.md](craft/layout-responsive.md) for grids, composition, density, breakpoints, and adaptation.
- [craft/components-states.md](craft/components-states.md) for controls, forms, tables, navigation, overlays, and state coverage.
- [craft/distinctiveness.md](craft/distinctiveness.md) for product-specific identity and avoiding first- and second-order defaults.
- [craft/motion-composition.md](craft/motion-composition.md) only when the committed direction calls for noticeable motion or unconventional composition.

### 4. Implement in the real product

1. Reuse the project's architecture and accessible primitives where they fit.
2. Implement semantic structure before decoration.
3. Build the primary flow and information hierarchy first.
4. Add responsive behavior based on content pressure, not device names alone.
5. Complete interactive, asynchronous, empty, error, and extreme-data states.
6. Add motion only where it explains change, confirms action, or directs attention.
7. Keep tokens and component APIs coherent; avoid one-off values that conceal a missing rule.
8. Preserve functionality and verify every changed route or state.

Read [implementation/engineering.md](implementation/engineering.md) before substantial implementation. Also read [implementation/platforms.md](implementation/platforms.md) when the target includes native mobile, desktop, or multiple platforms.

### 5. Validate proportionally to risk

Run the project's relevant tests, then validate the UI in layers:

- functional behavior and data states;
- responsive and input behavior;
- semantics, keyboard, focus, contrast, zoom, reduced motion, and assistive technology;
- visual composition at target viewports;
- loading, interaction responsiveness, and layout stability;
- content clarity and consistency;
- regressions in neighboring screens.

Read [qa/validation.md](qa/validation.md) and [qa/visual-qa.md](qa/visual-qa.md). Automated accessibility checks are a first line, never the complete assessment.

### 6. Critique before handoff

Perform a separate review pass after the UI works:

1. Compare the render with the brief and committed direction.
2. Run hierarchy, silhouette, grayscale, squint, repetition, and “could this belong to any product?” checks.
3. Audit for accumulated generated-UI tells, not isolated stylistic choices.
4. Remove decoration without a content or interaction job.
5. Fix failures; do not merely list them when implementation is in scope.

Read [review/critique.md](review/critique.md), load [review/tells-catalog.md](review/tells-catalog.md) when creating or auditing for generated-UI convergence, and use [review/release-checklist.md](review/release-checklist.md) for the final gate.

For web source, run `python3 ui-developer/scripts/audit_ui.py <paths>` when the skill path is available. Treat its findings as prompts for contextual review, never as proof that a design is generic. Rendered inspection remains required.

Use [references/sources.md](references/sources.md) when standards, further reading, or visual-reference catalogs are needed.

## Non-negotiable quality gates

A UI is not ready when any applicable condition is true:

- The main user task is unclear or broken.
- Hierarchy depends on decoration instead of structure.
- The rendered result has not been inspected at representative sizes.
- Keyboard focus is missing, obscured, or illogical.
- Meaning depends on color alone.
- Components ship only in their resting state.
- Mobile is merely a shrunken desktop or content is clipped.
- Loading, empty, error, or long-content states can break the experience.
- Copy is generic, misleading, inconsistent, or fabricated as fact.
- Visual choices contradict the brief or existing design system.
- A stack of defaults makes the result interchangeable with unrelated products.
- Tests or validation relevant to the changed risk were skipped without disclosure.

## Handoff

Lead with the completed outcome. Summarize the visual and product direction, changed files or surfaces, validation performed, and any material limitations. Distinguish verified behavior from recommendations or assumptions. Avoid presenting subjective taste as an objective defect.
