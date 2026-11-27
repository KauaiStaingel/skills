# Components and states

Components encode repeated meaning and behavior. Reuse should reduce inconsistency without forcing unrelated content into the same visual container.

## State matrix

For every applicable interactive component, consider:

| Category | States |
|---|---|
| Interaction | default, hover, active/pressed, focus-visible |
| Selection | unselected, selected, indeterminate |
| Availability | enabled, disabled, read-only |
| Async | idle, loading, success, failure |
| Validation | neutral, warning, invalid, valid when useful |
| Data | populated, empty, partial, stale, overflow |

Do not manufacture states that cannot occur, but do not ship only the resting screenshot.

## Buttons and actions

- Rank actions by importance and consequence.
- Use one clear primary action in a local decision area in the ordinary case.
- Separate destructive actions and make consequences explicit.
- Keep labels action-specific.
- Preserve stable width or otherwise prevent distracting layout shift during loading.
- Do not use color alone to communicate hierarchy or danger.

## Forms

- Use persistent labels and appropriate native input types.
- Group related fields and explain format before error when possible.
- Validate at a time that helps correction; do not punish users while they are still typing.
- Preserve entered data after errors.
- Connect labels, descriptions, requirements, and errors semantically.
- Make optional versus required behavior consistent.
- Provide visible keyboard focus and predictable tab order.

## Navigation

- Show current location and distinguish navigation from actions.
- Keep terminology consistent across menus, titles, breadcrumbs, and routes.
- Do not hide essential desktop navigation on mobile without an operable replacement.
- Preserve deep links, browser history, and expected platform behavior.

## Tables and data display

- Use tables for relational data, not layout.
- Left-align ordinary text and right-align comparable numbers with tabular numerals where supported.
- Keep headers associated with cells.
- Support sorting, filtering, pagination, selection, and bulk actions only when the task needs them.
- Test long labels, zero values, large values, missing data, and loading.
- Avoid centering every cell or converting dense professional data into decorative cards by default.

## Cards and containers

Use a card when content forms a meaningful unit with its own boundary, action, or destination. Do not place every heading, metric, or feature inside identical rounded rectangles. Prefer grouping through spacing and alignment when a boundary adds no meaning.

## Overlays and disclosure

Dialogs, popovers, menus, tooltips, and drawers require:

- a clear trigger relationship;
- focus placement and return;
- keyboard operation and Escape behavior where expected;
- outside-click behavior that does not cause data loss;
- safe viewport placement and scrolling;
- accessible naming;
- motion that communicates origin without delaying use.

Tooltips cannot carry essential information needed on touch or keyboard-only flows.

## Feedback

Show progress for actions that are not immediate. Confirm outcomes near their consequence. Avoid toasts as the only record of an important result, and avoid optimistic success when the operation can still fail without a recovery path.
