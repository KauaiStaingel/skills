# Generated-UI tells catalog

Use this catalog to detect convergence, not authorship. A tell means “review the decision in context,” not “AI definitely made this” or “remove it automatically.”

## How to use the catalog

1. Establish the artifact, page intention, existing design system, and approved direction.
2. Run the source scanner for detectable signals.
3. Inspect rendered narrow, intermediate, and wide views.
4. Mark findings with evidence type: `code`, `render`, or `inferred`.
5. Judge the stack and structural fit before changing isolated styling.
6. Keep a flagged treatment when brand, content, data, platform, or interaction justifies it.
7. Correct the underlying decision. Do not merely exchange one fashionable surface for another.

Signal classes:

- **A — strong signature:** one occurrence merits deliberate review because the treatment is highly associated with generated templates. It may still be legitimate.
- **B — system convergence:** becomes meaningful when multiple categories appear together or repeat across the page.
- **C — weak signal:** never justifies a change by itself; use only as supporting evidence.
- **E — emerging extension:** current convergence patterns outside the original core set; treat according to the strength noted.
- **Q — quality defect:** not an AI tell. Fix according to user impact and applicable standards.

## A — strong signatures

### A1. Repeated eyebrow or overline

**Recognize:** small tracked text, often uppercase, directly above most headings; sometimes prefixed by a dash, dot, sparkle, or category word.

**Why it converges:** it manufactures hierarchy without improving the section title or content structure.

**Replace:** remove it, fold necessary context into the heading, breadcrumb, metadata, index, or region label.

**Keep when:** it carries real category, date, sequence, or editorial metadata and is not stamped above every section.

### A2. Gradient-clipped headline word

**Recognize:** one phrase in a title uses purple, pink, cyan, or multicolor gradient text.

**Replace:** create emphasis through wording, scale, weight, image, or a real data point.

**Keep when:** gradient is an established brand asset or encodes real data.

### A3. Arbitrary bicolor headline

**Recognize:** the last words of a headline receive the accent color without a semantic reason.

**Replace:** keep the title chromatically coherent; let content establish emphasis.

**Keep when:** the highlighted term has a real role, such as the product name under an established identity.

### A4. “Tasteful escape” serif cluster

**Recognize:** cream or beige canvas, high-contrast display serif, warm clay or olive accent, and the last words italicized.

**Why it converges:** it is a common second-order response to purple SaaS styling.

**Replace:** derive type and palette from subject matter and references; avoid the automatic italic trick.

**Keep when:** editorial context or brand history genuinely supports the family, palette, and italic semantics.

### A5. Colored side or top stripe on generic cards

**Recognize:** otherwise identical cards differentiated by a 3–4 px colored border.

**Replace:** group by structure, label the category, or use a semantic alert component.

**Keep when:** the stripe consistently communicates a real status such as warning or error.

### A6. Decorative quotation block

**Recognize:** giant quotation marks or a quote stripe around an unattributed marketing sentence.

**Replace:** return the claim to ordinary content or provide a real, attributable quotation.

**Keep when:** the quote is authentic, sourced, and contextually important.

### A7. Pulsing status chip without live state

**Recognize:** pill such as “Available,” “Live,” or “New” with a blinking green dot.

**Replace:** remove the animation and often the chip itself.

**Keep when:** status is real, current, and operationally useful, such as a live stream or system status.

### A8. Sparkle or launch pill above the hero

**Recognize:** rounded badge with sparkle, rocket, “AI-powered,” “new,” or an arrow before the headline.

**Replace:** use a concrete, dated announcement with a destination or omit it.

**Keep when:** it represents a real launch or update and links to details.

### A9. Emoji used as the icon system

**Recognize:** repeated emoji in feature tiles, navigation, buttons, or bullets.

**Replace:** coherent icons or no icons; often stronger content is enough.

**Keep when:** emoji is user content or a restrained, intentional part of an informal brand voice.

### A10. Unexamined Tailwind purple or indigo

**Recognize:** default violet/indigo utilities, familiar hex values, or purple-to-pink glow used as automatic brand expression.

**Replace:** use the documented brand color or derive color from real material and functional roles.

**Keep when:** purple is genuinely the brand; use its exact system rather than a framework sample value.

### A11. Generic three-step section

**Recognize:** three equal columns, numbers in circles, one-word titles, and generic explanations.

**Replace:** show the real process through concrete screens, actions, timing, inputs, or outcomes; remove the section if the process is obvious.

**Keep when:** the task is truly sequential and the content is specific.

### A12. Decorative glassmorphism

**Recognize:** translucent blurred cards with white hairlines over colored blobs or gradients.

**Replace:** solid surfaces, spacing, or elevation appropriate to actual layering.

**Keep when:** content genuinely overlays media or the native platform uses material effects as an established convention.

### A13. Static card pretending to be interactive

**Recognize:** hover lift, scale, pointer cursor, or stronger shadow on a container with no action.

**Replace:** remove interaction styling or make the card a real accessible link/action.

**Keep when:** never without an interaction; verify semantics, target, keyboard, and focus.

## B — system convergence

### B1. SaaS page grammar applied to every business

**Recognize:** abstract hero, two CTAs, logo strip, feature grid, three steps, testimonials, three pricing cards, FAQ, final CTA, and four-column footer regardless of domain.

**Replace:** structure around the actual domain. A bakery needs product, menu, hours, location, and ordering; a public service needs search, common services, requirements, and status.

**Keep when:** the product is actually a SaaS and each region contains necessary, verified information.

### B2. Pasteurized card grid

**Recognize:** three, four, or six equal cards with identical icon tile, title, description, radius, border, and shadow; or a bento grid whose sizes do not reflect priority.

**Replace:** lists, tables, real screenshots, editorial groupings, or deliberately unequal composition based on content.

### B3. Icon in a tinted rounded square

**Recognize:** the same line icon inside a pale accent tile on every item.

**Replace:** unboxed icon when it improves scanning, or text/media when it does not.

### B4. Absence of real media or evidence

**Recognize:** an entire public page made only from copy, icons, gradients, and cards despite a physical product, place, process, people, or working software being available.

**Replace:** real photography, product screens, data, map, menu, schedule, work sample, or explicit placeholder requesting the missing asset.

**Keep when:** a type-led direction is intentional and the subject truly does not benefit from media.

### B5. Pills and large radius everywhere

**Recognize:** buttons, inputs, filters, badges, tabs, cards, and media all share extreme rounding.

**Replace:** a small radius scale assigned by component role; reserve pill shape for content that warrants it.

### B6. Decorative gradients, blobs, and neon

**Recognize:** mesh backgrounds, radial spotlight, blurred absolute blobs, neon borders, or waves separating sections.

**Replace:** solid surfaces, real imagery, structural contrast, or data-driven color.

**Keep when:** the brand owns the treatment or the gradient represents a real scale.

### B7. Generic animation applied everywhere

**Recognize:** every section fades upward, cards scale on hover, grids stagger, stats count from zero, or logos marquee indefinitely.

**Replace:** state feedback and one signature movement with a reduced-motion equivalent.

### B8. Component library with its factory appearance

**Recognize:** untouched starter colors, radius, shadows, typography, badges, sidebar, and spacing.

**Replace:** keep accessible behavior and component APIs, then map presentation to product tokens and density.

### B9. Inorganic repeated section rhythm

**Recognize:** every section has the same max width, padding, centered heading/subtitle pair, alternating neutral surface, and identical vertical cadence.

**Replace:** let content relationship determine width, grouping, breaks, and rhythm.

### B10. Floating device mockup with fake UI debris

**Recognize:** tilted laptop or phone surrounded by invented toasts, growth metrics, pro badges, and soft shadows.

**Replace:** a large, straight, readable product screen or a focused crop with real or clearly marked fixture data.

**Keep when:** the device frame is necessary to communicate platform and the surrounding evidence is real.

### B11. Template interface copy

**Recognize:** abstract transformation headline; subtitle that repeats it; “Why choose us?”; “More X. More Y. Less Z.”; “all in one place”; generic “Get started”; unsourced social proof.

**Replace:** what the product is, who it serves, what action happens, and verified details such as time, price, location, or capability.

## C — weak supporting signals

Do not act on these alone:

| ID | Signal | Review when |
|---|---|---|
| C1 | Inter, Geist, system font, Manrope, DM Sans, or similar common sans | It appears with an otherwise untouched template and has no product rationale |
| C2 | Too many fonts or unrelated accent colors | Roles are inconsistent and hierarchy depends on novelty |
| C3 | The same soft shadow on every surface | It accompanies the equal-card system |
| C4 | Uppercase “Learn more →” repeated on every card | It accompanies eyebrow-heavy, generic content |
| C5 | Carousel dots whose active state becomes a pill | Important content is hidden or the carousel has no user need |
| C6 | Repeated checklist ticks in colored circles | The list contains vague benefits and card-template structure |
| C7 | Friction microcopy under every CTA | Claims are generic, repetitive, or not true for the flow |
| C8 | Navy near-black theme with muted gray as the entire identity | It is a generic escape rather than a product decision |
| C9 | Theme toggle in a public landing navigation | No audience, platform, or requirement calls for it |

## E — emerging extensions

| ID | Strength | Signal | Replacement or legitimate use |
|---|---|---|---|
| E1 | Strong | Atmospheric mono strip such as “TYPE · FORM · MOTION” | Replace with real metadata; keep only when the terms are factual and useful |
| E2 | Strong | Bouncing “scroll down” cue | Remove; scrolling is already a convention unless discovery is genuinely uncertain |
| E3 | Strong | Blinking cursor in static headline or fake terminal | Keep only in an actual editable field or functioning terminal |
| E4 | Strong | “Beta,” “v0.x,” or “early access” hero pill without launch relevance | Move to navigation/changelog or keep when status is real and dated |
| E5 | Strong | Live clock, weather, or city chip unrelated to the product | Keep only for place, time, weather, or travel products |
| E6 | Cluster | Decorative grid or dot background | Keep when grid belongs to the workspace or subject, not as faded wallpaper |
| E7 | Cluster | Decorative `01 / 02 / 03` on nonsequential sections | Number only actual sequences |
| E8 | Cluster | Row of oversized unsourced metrics | Use one verified metric with source and context, or remove |
| E9 | Cluster | Bounce or spring easing in routine UI | Use restrained easing; keep expressive spring for an intentionally playful brand |
| E10 | Cluster | Unmotivated light-to-dark theme flip midpage | Use a single theme; keep one contrast break for meaningful media or CTA |
| E11 | Weak | Border and diffuse shadow defining the same edge | Pick separation or elevation unless the layered treatment has a role |
| E12 | Weak | Extreme radius on small cards | Assign radius by component role and size |
| E13 | Weak/Q | Neutral gray text on saturated surface | Use surface-relative text and verify contrast |
| E14 | Weak/Q | Justified or uppercase body copy | Use readable alignment and sentence case; reserve uppercase for brief labels |

## Quality defects that outrank tells

These are not aesthetic tells. Treat them as defects according to impact:

| ID | Defect |
|---|---|
| Q1 | Focus outline removed without an equally visible replacement |
| Q2 | Click behavior placed on nonsemantic elements without equivalent keyboard and accessibility behavior |
| Q3 | Meaning conveyed only through color, motion, position, or an unlabeled icon |
| Q4 | Missing persistent labels, actionable errors, or data preservation in forms |
| Q5 | Motion ignores reduced-motion preferences or blocks interaction |
| Q6 | Content clips, becomes unreachable, or causes unintended horizontal scrolling |
| Q7 | Fabricated customer, metric, testimonial, award, status, or product capability |
| Q8 | Low contrast, obscured focus, unsafe touch target, or inaccessible reading order |
| Q9 | Image dimensions are not reserved, producing preventable layout shift |

## Do not swap one cliché for another

| Leaving | Do not automatically replace it with |
|---|---|
| Tailwind purple | Beige, olive, terracotta, and high-contrast serif |
| Inter or system sans | Playfair-style headline with italic ending |
| Gradient | Glassmorphism |
| Emoji icons | Identical line icons in tinted rounded squares |
| Uppercase eyebrow | Italic serif eyebrow |
| Soft-shadow cards | Colored-stripe cards |
| Centered hero | Split hero with a tilted device and floating fake data |
| Abstract “Transform your business” | Equally abstract “Clarity to decide better” |

The durable correction is to return to product content, real material, task structure, approved references, and a committed system.

## Finding format

```markdown
- [impact severity] A1 — Repeated eyebrow
  - Location: route, component, line, or screenshot
  - Evidence: code | render | inferred
  - Context: why it is generic here
  - Consequence: product, comprehension, trust, or craft impact
  - Decision: replace with … | keep because …
```
