# Platform adaptation

Share product identity across platforms without forcing identical anatomy or interaction. Platform familiarity is part of usability.

## Web sites and web apps

- Preserve URL, link, history, refresh, selection, copy/paste, and browser zoom behavior.
- Use semantic HTML, responsive layout, and progressively enhanced controls.
- Verify server/client rendering boundaries, hydration, loading, and error behavior when applicable.
- Test keyboard, multiple pointer types, screen readers, high zoom, and reduced motion.
- Protect loading speed, interaction responsiveness, and layout stability with field metrics when available.

Marketing sites may be more expressive, but still require clear information order, truthful content, accessible navigation, and performance. Operational web apps usually need greater density, persistent context, and efficient keyboard behavior.

## Native mobile apps

- Follow platform navigation, control, gesture, permission, feedback, and system-back expectations unless the product has strong evidence for a custom pattern.
- Respect safe areas, dynamic type or font scaling, orientation policy, display cutouts, and on-screen keyboards.
- Do not depend on hover. Make gestures discoverable and provide accessible alternatives.
- Use native accessibility roles, labels, values, hints, focus or traversal order, and announcements.
- Test touch targets, reachability, interruption, offline or degraded networks, and lifecycle transitions.
- Use haptics and motion as feedback, not ornament; respect system accessibility settings.

## Desktop apps

- Support resizing, minimum window sizes, high-density screens, and multiple display configurations.
- Treat keyboard navigation, shortcuts, menus, context menus, focus, drag-and-drop, and file operations as first-class when relevant.
- Match platform conventions for title bars, dialogs, destructive actions, preferences, and window lifecycle.
- Favor efficient density while preserving target size, contrast, and clear focus.

## Cross-platform products

Keep shared:

- product vocabulary and information model;
- brand roles and core tokens where technically appropriate;
- action hierarchy and state meaning;
- accessibility intent;
- content and data rules.

Adapt per platform:

- navigation anatomy;
- control implementation;
- spacing and density;
- input methods and shortcuts;
- motion, feedback, and system surfaces;
- typography metrics and safe areas.

Do not copy a mobile tab bar into desktop or a desktop table into mobile solely for visual consistency. Consistency means preserving meaning and behavior while respecting each platform.
