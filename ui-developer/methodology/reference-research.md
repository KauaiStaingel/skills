# Visual reference research

References replace an unconstrained model's average choices with observed decisions. Use them to calibrate, extract principles, and compare implementation—not to clone another brand or page.

## Start with the user and the product

Ask for:

- 2–5 sites, apps, screens, boards, or physical artifacts they admire;
- what specifically works in each reference;
- examples they do not want to resemble;
- direct competitors, for differentiation rather than imitation;
- existing photography, packaging, signage, documents, product screenshots, and brand material.

User-provided references outrank generic discovery. Do not make them reverse-engineer design jargon; ask about concrete details such as layout, type, imagery, density, color, or feeling.

For Brazilian agency, studio, production, or portfolio sites, read [references/agencias-brasileiras-portfolios.md](../references/agencias-brasileiras-portfolios.md) when Jazz Side, Agência California, or Agência We is provided as a reference, or when the work would benefit from their contrasting approaches to immersive branding, editorial art direction, and portfolio indexing.

## Search by subject, material, and format

Prefer real products and adjacent industries before design galleries. Combine:

```text
<sector or subject> + <artifact> + <specific material or task>
<visual language> + <artifact>
<section or component> + <sector>
```

Useful qualifiers include `independent`, `editorial`, `documentary`, `print-inspired`, `archive`, `catalog`, `wayfinding`, or a real domain artifact. Generic terms such as `modern`, `clean`, `sleek`, `UI kit`, and `landing page template` tend to return the same median.

## Useful catalogs

Choose sources according to the question:

- real sites from the same or neighboring sectors for proven information and business patterns;
- [SiteInspire](https://www.siteinspire.com/) for published sites by style and type;
- [Awwwards](https://www.awwwards.com/websites/) and [Godly](https://godly.website/) for expressive composition and motion, with caution around feasibility;
- [Land-book](https://land-book.com/), [Lapa Ninja](https://www.lapa.ninja/), and [One Page Love](https://onepagelove.com/) for landing-page patterns, filtered carefully to avoid SaaS convergence;
- [Dribbble](https://dribbble.com/) and [Behance](https://www.behance.net/) for visual concepts, illustration, and branding—not proof of production usability;
- [Fonts In Use](https://fontsinuse.com/) and [Typewolf](https://www.typewolf.com/) for typography in context;
- [Mobbin](https://mobbin.com/) for product-screen patterns when access is available;
- Pinterest, Savee, or Cosmos for moodboards, while verifying source, authorship, and whether images appear synthetic.

Do not sign in, accept nonessential tracking, or download assets without the user's authorization when browser work requires those actions. Verify licenses before reusing any asset.

## Filter the pool

Collect a small diverse pool, then discard references that:

- accumulate the same generated-UI tells being audited;
- have no identifiable author, product, or live implementation when that matters;
- use impossible content, illegible text, fabricated brands, or suspiciously uniform synthetic imagery;
- are visually attractive but incompatible with the task, platform, accessibility, content, or budget;
- differ only by palette while sharing the same structure.

Keep enough variety to compare genuine directions, usually 6–12 references for a substantial public-facing project and fewer for a local component.

## Make a reference card

For each retained reference, capture:

```markdown
Reference and URL:
Why it belongs:
Artifact and audience:
Layout and density:
Typography behavior:
Color source and distribution:
Imagery or data treatment:
Interaction or motion:
Memorable detail:
What not to borrow:
Production evidence or caveat:
```

This makes “I like it” actionable and exposes incompatible assumptions.

## Form directions

Group references into two or three directions. Each direction should include:

- a short product-specific name;
- two or three supporting references;
- three concrete decisions about structure, type, imagery, color, or interaction;
- required material such as photography or product data;
- feasibility and accessibility risks;
- the default pattern it deliberately avoids.

For consequential public brand work, show the directions and let the user choose, mix, or reject them. When the user explicitly delegates direction or the established system already decides it, proceed with a stated rationale.

## Extract a system before coding

From the chosen direction, extract:

- grid and alignment logic;
- type roles, scale contrast, line length, and wrapping;
- palette roles and where color originates;
- spacing rhythm, radius, borders, and elevation;
- media ratios, crops, and art direction;
- component and motion principles;
- explicit non-goals.

Implement using project tokens and primitives. Compare a screenshot of the result with the reference at an equivalent viewport, inspecting relationships rather than pixel-copying another brand. If the extracted system becomes official, record it in the project's design document.
