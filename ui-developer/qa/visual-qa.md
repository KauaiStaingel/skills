# Visual QA

Visual QA compares the rendered interface with the brief, system, and real content. Read source for cause; judge pixels for outcome.

## Capture matrix

Capture or inspect:

- each changed page at representative narrow, intermediate, and wide sizes;
- full-page composition where scrolling rhythm matters;
- critical components in default, focus, hover, active, disabled, loading, empty, and error states as applicable;
- long text, large values, missing images, dense data, and localization stress cases;
- light and dark themes when both are in scope;
- before/after or visual-regression differences when available.

Use consistent environments for baseline screenshot comparison.

When the project has no established device matrix, use `1440×900`, `768×1024`, and `390×844` as practical initial baselines, then add the widths where this product's content or components actually fail. For long pages, inspect top, middle, and end rather than only the hero. Capture the accessibility tree as well when the tooling exposes it.

## Review passes

### Pass 1: hierarchy

- Is the first reading target correct?
- Is the primary action identifiable without relying on saturated color alone?
- Do scale, weight, space, and alignment agree on importance?
- Are secondary elements actually secondary?

### Pass 2: composition

- Are alignments intentional across sections and screens?
- Does spacing express grouping and section changes?
- Is density appropriate for the task?
- Are there dead zones, accidental tangencies, or crowded edges?
- Do images and data visualizations hold the composition rather than decorate it?

### Pass 3: component craft

- Do type, icons, controls, borders, radii, and surfaces feel optically balanced?
- Are state changes clear and stable?
- Does the same role look and behave consistently?
- Are cards and containers used for meaning rather than habit?

### Pass 4: responsive behavior

- Does hierarchy survive reflow?
- Are essential content and actions preserved?
- Is wrapping graceful and touch use safe?
- Do sticky, fixed, overlay, table, and media regions behave correctly?

### Pass 5: product specificity

- Does the result reflect this product's subject, users, and content?
- Could the brand name be swapped without the interface feeling wrong?
- Has one coherent idea been executed, or several fashionable treatments accumulated?

## Diagnostic views

- **Grayscale:** exposes hierarchy that depends too heavily on hue.
- **Squint or reduced zoom:** exposes flat density and competing focal points.
- **Silhouette:** exposes template-level structure.
- **No-decoration pass:** mentally remove shadows, glows, textures, and gradients to test structural quality.
- **Content stress:** exposes layouts designed around ideal strings instead of the product.

Fix systemic causes before nudging isolated pixels. Re-capture after correction.
