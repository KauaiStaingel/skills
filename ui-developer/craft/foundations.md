# Visual foundations

Use foundations to create coherent decisions, not to make every interface look like a design system specimen.

## Hierarchy before decoration

Establish the reading and action order in grayscale first. Use:

- position and sequence;
- scale and weight;
- proximity and whitespace;
- alignment and repetition;
- contrast and density;
- progressive disclosure.

When every element receives equal scale, container treatment, and spacing, nothing is prioritized.

## Proximity and rhythm

Spacing communicates relationships:

- tight spacing within a semantic group;
- moderate spacing between related groups;
- generous spacing between sections or task changes.

Use a compact spacing scale, then make optical adjustments from that scale when visual weight requires it. Avoid both random spacing and one uniform gap everywhere. Repetition creates rhythm; controlled variation creates attention.

## Tokens by role

Prefer semantic roles to raw values:

```text
color.bg, color.surface, color.text, color.text-muted, color.border
color.accent, color.on-accent, color.success, color.warning, color.danger
space.*, type.*, radius.*, border.*, elevation.*, motion.*
```

Keep the number of tokens proportional to the product. A token exists when it coordinates repeated decisions or theme behavior, not merely to rename a single literal.

## Color

- Choose color for product fit and hierarchy before novelty.
- Define background, surface, foreground, muted, border, accent, and semantic states.
- Test actual foreground/background pairs; palette swatches alone do not prove contrast.
- Do not use color as the only signal for state or status.
- Use accent as punctuation. If everything is accented, nothing is.
- Treat dark mode as a designed theme with adjusted surfaces, contrast, and saturation, not a mechanical inversion.
- Avoid pure black or white only when their contrast or tone is inappropriate; do not turn near-black and off-white into universal rules.

## Surfaces, borders, radius, and elevation

Choose a consistent model:

- separation through spacing;
- separation through borders;
- elevation through surface lightness;
- shadows for actual layering or floating elements.

Do not stack border, diffuse shadow, tinted surface, and glow on every container. Use fewer container styles and distinguish hierarchy by purpose. Radius should follow component size, interaction, and visual language; one large radius on every object creates blob-like sameness.

## Iconography

- Use icons for recognizable actions, states, or objects; do not use them to fill empty space.
- Keep grid, stroke weight, optical size, joins, and fill strategy coherent.
- Pair unfamiliar icons with labels.
- Preserve accessible names for icon-only controls.
- Do not let the untouched starter icon set become the product's identity.

## Imagery and illustration

Art-direct imagery as a system:

- prefer real product, environment, process, or people when they create trust;
- define subject, crop, lighting, color treatment, texture, and aspect-ratio behavior;
- avoid generic stock scenarios and abstract blobs when concrete evidence belongs there;
- ensure alt text or decorative treatment matches the image's information role;
- reserve space to prevent layout shift.

## Motion

Motion should explain:

- what changed;
- where an element came from or went;
- whether an action succeeded;
- what currently needs attention.

Prefer transform and opacity for ordinary transitions. Keep high-frequency actions fast and unobtrusive. Avoid animating every section or card. Respect reduced-motion preferences and provide equivalent understanding without animation.
