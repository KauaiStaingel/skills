# Durable design record

Use a project design record to prevent later sessions from rediscovering the same direction and drifting back to defaults.

## When to create or update it

Create or substantially update `DESIGN.md` for:

- a new branded surface or multi-screen product;
- a redesign;
- a durable token or component-system change;
- a direction that future contributors must preserve.

Do not create it for a one-line fix or transient exploration.

## Precedence

Resolve conflicts in this order:

1. The user's current explicit instruction and approved product requirements.
2. The implemented product system and current behavior that must remain compatible.
3. The project's maintained design record.
4. This skill's defaults and external references.

When code and documentation drift, investigate which is intentional. Update the record or flag the mismatch; do not silently restyle the product.

## Compact schema

```markdown
# DESIGN.md — <product>

## Product truth
Users, context, primary jobs, supported platforms, real material, constraints, and observable success.

## Surface intentions
| Surface | Intent | Variation | Motion | Density | Primary action |

## Direction
Positioning adjectives, direction sentence, signature move, non-goals, and approved references.

## Foundations
Typography roles; semantic color roles; spacing and grid; radius, border, elevation; imagery; iconography; motion.

## Components and states
Shared patterns, exceptions, and required state coverage.

## Accessibility and performance
Applicable standards, platform requirements, budgets, and testing expectations.

## Do / do not
Project-specific examples and justified exceptions to generic audit warnings.

## Decision log
Append-only durable decisions with date, context, decision, reason, affected surfaces, and reference.
```

Keep values concrete enough to implement. A token table may include exact font families, semantic variable names, color values, type steps, spacing steps, radii, and motion durations. Do not turn the file into a catalog of every component property already encoded in source.

## Decision log entry

```markdown
### YYYY-MM-DD — <decision>
- Context:
- Decision:
- Why:
- Avoid:
- Surfaces:
- Evidence or reference:
```

Record decisions that change future choices, not routine bug fixes.
