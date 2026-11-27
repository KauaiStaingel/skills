# Typography and interface content

Typography carries hierarchy, personality, and usability. Content is part of the interface, not decoration added after layout.

## Separate semantics from appearance

On the web, heading levels describe document structure. On native platforms, use the equivalent platform accessibility traits and screen hierarchy. Visual roles describe presentation. Do not choose `h3` because it looks smaller, and do not use a heading merely to obtain bold text.

- Use one page-level `h1` in the ordinary web-document case.
- Use `h2` for major sections and `h3` for subdivisions inside them.
- Do not skip levels for styling convenience.
- Use headings in descending logical order.
- A component title is a heading only when it introduces a real section in the document or accessible region.

Define visual roles independently:

```text
display
page-title
section-title
component-title
body
body-compact
label
caption
metric
code
```

The same semantic heading may use a different visual role in a dashboard, marketing page, modal, or mobile layout. Native screen titles and grouped regions should expose equivalent structure through the platform accessibility API.

## Title systems

Use the fewest hierarchy levels the content requires. Create clearly distinguishable roles rather than many nearly identical sizes.

For each role, define:

- family and fallback;
- size behavior across available space;
- weight or variable-font axes;
- line height and tracking;
- maximum measure;
- spacing before and after;
- wrapping and truncation behavior.

Test actual glyphs, languages, values, and line breaks. Avoid thin weights for small text. Keep long-form line length readable for the typeface and language; roughly 60–80 characters is a useful starting range, not a universal law.

## Titles and subtitles

A subtitle is optional. Include it only when it adds scope, state, consequence, evidence, or guidance that the title cannot carry.

Good relationship:

```text
Page title
small relational gap
Useful subtitle

larger structural gap

Page content
```

Reject subtitles that repeat the title, make vague claims, or exist only to complete a template. Treat an eyebrow or overline the same way: it needs an information role such as category, context, or navigation. Do not place tracked all-caps labels above every heading by reflex.

Avoid repeating this composition across every section without need:

```text
EYEBROW
Large centered title with one accented word
Generic centered subtitle
Three equal cards
```

## Typeface selection

- Start with brand, audience, language coverage, legibility, and performance.
- One family used deliberately can be stronger than an arbitrary display/body pairing.
- When pairing, create useful contrast without fragmenting the hierarchy.
- A common typeface is acceptable when it is an explicit product decision or part of the existing system.
- Verify licensing and delivery constraints before introducing a font.

## Interface language

- Use the user's vocabulary, not internal architecture.
- Prefer concrete verbs and active voice.
- Name an action by its result: “Save changes,” not “Submit.”
- Keep the same action name through button, confirmation, status, and documentation.
- Use sentence case unless the language or brand requires otherwise.
- Avoid promotional filler inside task UI.
- Do not fabricate testimonials, metrics, customers, availability, or compliance claims.

## Errors, help, and empty states

Errors should identify the problem, preserve user input, and state the recovery action. Avoid vague apologies and raw system codes.

Empty states should explain why the space is empty when necessary and offer the next meaningful action. Do not fill every empty state with mascots or jokes.

Help should appear near the decision it supports. Placeholder text is not a substitute for a persistent label.
