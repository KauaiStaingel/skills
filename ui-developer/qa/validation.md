# Functional, responsive, and accessibility validation

Validation depth follows risk, reach, and change size. A local color correction and a new checkout flow do not need the same test matrix.

## Functional validation

Verify applicable cases:

- primary and secondary flows complete successfully;
- navigation, deep links, browser history, and refresh behavior;
- forms, constraints, validation timing, submission, retry, and data preservation;
- loading, empty, partial, success, warning, error, offline, and permission states;
- destructive actions, confirmation, cancellation, undo, and recovery;
- sorting, filtering, searching, pagination, selection, and bulk actions;
- console errors, failed requests, broken assets, and hydration warnings;
- neighboring screens that share changed tokens or components.

## Responsive and device matrix

Test representative extremes and at least one intermediate width:

- narrow mobile;
- wider mobile or small tablet when relevant;
- compact laptop;
- target desktop;
- unusually wide layouts when the product supports them.

Also test text expansion, zoom, orientation, pointer versus touch, hover absence, and on-screen keyboard effects where relevant. Breakpoints should survive content, not only empty fixtures.

## Accessibility gate

### Semantics

- on the web, page language, landmarks, heading order, lists, tables, and form structure are meaningful;
- on native platforms, screen titles, groups, control roles, values, hints, and traversal order are exposed through the platform accessibility API;
- controls use native elements or fully implement expected semantics;
- names, descriptions, status, and errors are programmatically connected;
- icons and images have correct text alternatives or are marked decorative.

### Keyboard and focus

- all actions are operable without a pointer;
- focus order follows the task and visible reading order;
- focus is clearly visible and not hidden by sticky content;
- overlays place, contain when appropriate, and return focus correctly;
- no keyboard traps exist;
- shortcuts do not conflict or activate unexpectedly.

### Perception and adaptation

- text and non-text contrast meet the project's applicable standard;
- meaning is not conveyed by color, position, shape, sound, or motion alone;
- content reflows and remains usable at increased text size and zoom;
- targets are large and separated enough for the context;
- reduced motion is respected;
- error, success, and live status feedback is perceivable without becoming noisy.

### Assistive technology

Use automated scans to catch detectable violations, then manually verify keyboard, focus, names, reading order, dynamic announcements, and critical flows. When risk or audience warrants it, test with screen readers and users with disabilities.

## Test automation

Use the project's existing tools. Suitable coverage may include:

- component render stories for relevant states;
- interaction tests that query by role and accessible name;
- end-to-end tests for critical user journeys;
- automated accessibility scans;
- visual regression for stable, high-value surfaces;
- performance budgets or monitoring.

Do not update snapshots blindly. Inspect the difference and confirm it matches the intended change.

## Evidence

Record commands run, viewports or devices checked, flows tested, and material gaps. A tool passing is evidence for what it measured, not proof of complete usability.
