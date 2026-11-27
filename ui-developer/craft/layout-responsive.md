# Layout, composition, and responsiveness

Layout organizes content and action across changing space. Do not treat responsiveness as a final pass that stacks desktop columns.

## Start with content and task

Identify:

- the primary reading and action order;
- information that must remain visible;
- content that can reflow, collapse, scroll, or move behind disclosure;
- minimum usable sizes for controls, data, and media;
- how real content expands, localizes, and fails.

Choose grid, container, and density from these pressures.

## Composition

- Use repeated alignments to establish continuity.
- Vary scale and negative space to clarify hierarchy.
- Use asymmetry when it serves emphasis or content, not as a compulsory anti-template trick.
- Center alignment suits short, singular messages; sustained task UI and dense content often benefit from stronger edge alignment.
- Avoid wrapping every section in an identical card or max-width centered column.
- A bento or tile grid is appropriate when units have genuinely different content, priority, or destinations.

## Density

Match density to usage:

- recurring professional tasks favor efficient scanning and compact controls;
- consumer onboarding may require more guidance and space;
- marketing and editorial pages can use larger compositional pauses;
- mobile needs prioritization, not simply larger gaps or hidden functionality.

Offer density modes only when user needs justify the added system complexity.

## Responsive method

1. Establish the semantic source order.
2. Find where content begins to collide, wrap badly, lose hierarchy, or create unsafe targets.
3. Introduce breakpoints at those failures.
4. Decide per region whether to resize, reflow, reorder visually without breaking semantics, disclose, scroll, or replace with a more suitable pattern.
5. Test intermediate widths, not just one phone and one desktop.

Prefer intrinsic layout, flexible grids, container-aware components, `minmax`, wrapping, and content constraints over device-specific coordinates.

## Common adaptations

- Navigation may condense, but primary destinations and current location must remain understandable.
- Tables may scroll, prioritize columns, use a responsive detail view, or change presentation; do not silently remove critical data.
- Toolbars may wrap, group, or move secondary actions into a menu while preserving the primary action.
- Sidebars may become drawers only when focus, escape, overlay, and state behavior are implemented correctly.
- Media needs stable aspect ratios and purposeful crops.
- Dialogs need safe viewport margins and scroll containment.

## Bidirectionality, zoom, and localization

Use logical CSS properties and avoid layouts that assume left-to-right reading. Test text expansion, long unbroken values, increased text size, and browser zoom. Do not rely on truncation for essential information without a way to access the full value.
