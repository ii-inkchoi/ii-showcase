# Design Tokens

Every prototype page declares the same `:root` palette inline. This package consolidates them into `tokens.css` for engineering — wire these into the real codebase as your token source.

## Color palette

The system is monochrome on purpose (Cold/Clinical / Palantir-bar doctrine — no accent color, hierarchy via opacity).

| Token | Hex | Usage |
|---|---|---|
| `--c-black` | `#000000` | App background, primary surface |
| `--c-1000` | `#1C1C1C` | Elevated surface (cards, chips) |
| `--c-900` | `#232627` | Dividers, section rules, borders |
| `--c-800` | `#565B5E` | Tertiary text (ghost / metadata) |
| `--c-700` | `#929292` | Secondary text (labels, captions) |
| `--c-600` | `#A7A7A7` | Mid-weight text |
| `--c-400` | `#C7C7C7` | Near-primary text |
| `--c-200` | `#E3E2E2` | Soft white (used sparingly) |
| `--c-white` | `#FFFFFF` | Primary text, hero numbers |

## Opacity ladder (hierarchy)

Hierarchy is signaled by opacity on white text, not by hue.

| Token | Value | Used for |
|---|---|---|
| `--t1` | 1.00 | Hero numbers, primary text |
| `--t2` | 0.55 | Secondary metrics, supporting numbers |
| `--t3` | 0.32 | Section labels, table labels |
| `--t4` | 0.18 | Ghost tags (CAD, "Since inception") |

## Typography

- Primary face: **Inter** (Google Fonts — weights 300, 400, 500)
- Display face: **Chakra Petch** (Unified Dashboard only, used sparingly)
- Numeric features: `font-feature-settings: 'lnum' 1, 'tnum' 1;` — lining + tabular numerals so financial columns align
- Weight 600 reserved for section eyebrow labels (e.g., "MANAGED", "SELF-DIRECTED")

Type scale (px shipped in v3):

| Token | Size | Used for |
|---|---|---|
| `--fs-hero` | 52px | Total Capital, primary portfolio value |
| `--fs-h1` | 40px | Headline numbers |
| `--fs-h2` | 30px | Secondary hero (Managed value) |
| `--fs-h3` | 24px | Tertiary headlines |
| `--fs-body` | 14px | Body, table values |
| `--fs-small` | 12px | Small metadata |
| `--fs-label` | 11px | Section eyebrow labels (weight 600) |
| `--fs-ghost` | 10px | CAD currency tag, "Since inception" |

## Layout

- Mobile-first; designs target **393px** viewport (`--viewport-max`)
- 8px grid spacing (`--space-1` … `--space-8`)
- Header height: 71px (`--header-height`)
- Section inner gap: 16px; table row padding: 8px (data density)

## Brand doctrine

These tokens implement the **Cold/Clinical Design Filter** (Palantir / Serious Operator bar). Engineering notes:

1. **No accent color.** Don't add a brand green/blue. Hierarchy comes from opacity and weight only.
2. **No false precision.** Round numbers should not show `.00`. Strip trailing zeros at the display layer.
3. **Right-spine alignment** on data-heavy screens (Unified Dashboard): left = structure (labels), right = data (numbers). One vertical scan axis on the right edge.
4. **Interactivity is structural, not decorative.** No hover glows, no underlines, no accent color on links. A chevron or border-chip signals "this is a control." Drill-down rows have no trailing element — opacity contrast does the work.
5. **Tabular numerals always on** for any numeric column.
