# UI engineering

Implement the committed direction in the project's actual architecture. Visual redesign does not authorize functional or dependency churn.

## Before editing

1. Read the files in scope and their callers.
2. Identify public component APIs, data flow, routing, state management, and test coverage.
3. Find reusable primitives and tokens.
4. Confirm which behavior and content must remain stable.
5. Establish a way to run or render the affected UI.

## Structure

- On the web, use semantic HTML and browser behavior before custom roles and handlers. On native platforms, use native controls and accessibility semantics before custom equivalents.
- Separate product/domain components from low-level visual primitives when that distinction improves reuse.
- Keep component boundaries aligned with behavior and ownership, not arbitrary visual fragments.
- Avoid premature generic components with large variant APIs.
- Preserve source order and accessible reading order when using visual rearrangement.

## Styling and tokens

- Reuse existing tokens when they express the intended role.
- Add semantic tokens when repeated decisions lack a shared name.
- Avoid scattered magic values and long chains of arbitrary utility overrides.
- Keep specificity understandable; prevent global selectors from fighting local styles.
- Use logical properties and intrinsic sizing where practical.
- Treat one-off optical adjustments as explicit exceptions, not hidden system rules.

## Responsive implementation

- Build from content constraints and test intermediate widths.
- Avoid fixed heights around dynamic text.
- Prevent horizontal overflow except in deliberate regions such as data tables.
- Reserve media dimensions and test image crop behavior.
- Verify touch, mouse, keyboard, and focus behavior as applicable.

## State and data implementation

- Model loading, empty, error, partial, stale, permission, and success states when the product can produce them.
- Preserve form data through recoverable failures.
- Make async status available to assistive technology without excessive announcements.
- Test realistic minimum, typical, and maximum content.
- Avoid fabricated production data in committed UI unless clearly marked fixtures are appropriate.

## Motion

- Animate properties appropriate for smooth rendering when possible.
- Use motion tokens for duration and easing when repeated.
- Keep interaction response immediate.
- Implement `prefers-reduced-motion` behavior.
- Avoid motion that changes layout unexpectedly, blocks interaction, or repeats without value.

## Performance

- Choose the lightest asset and component strategy that meets the direction.
- Size and optimize images; lazy-load below-the-fold media when appropriate.
- Avoid unnecessary client-side code, duplicate libraries, and expensive effects.
- Load fonts deliberately and provide suitable fallbacks.
- Protect loading speed, interaction responsiveness, and visual stability.

## Dependencies

Do not add a UI library, font package, animation system, icon set, or testing service silently. First verify that the current stack cannot meet the need cleanly, then state the dependency and tradeoff.

## Verification during implementation

Render after meaningful increments. Check the main flow first, then secondary states. Run targeted tests early enough that architectural or accessibility mistakes are inexpensive to fix.
