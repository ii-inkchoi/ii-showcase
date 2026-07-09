# II Landing — Design Rules (quick reference)

> Canonical standard = the **homepage prototype** (`index.html`). Bring every other page (Self-Directed, Managed, Pricing, Manifesto) to this. Applied autonomously — no need to re-specify column counts or font sizes each time.

## Grid & columns
- 12-column grid inside `.container` (uses `--maxw`, `--frame`, `--gutter`). Press **`g`** on any page for the overlay.
- **Text column = 5 cols** (`grid-column: 1 / 6`).
- **Paired content / card = 6 cols** (`grid-column: 7 / 13`).
- **Layout archetypes** (reuse these, don't invent one-offs):
  1. Text-left (1-5) + content/card-right (7-12).
  2. Text-top + two cards side-by-side below (1-6 / 7-12).
  3. Full-width centered statement (Close).
  4. Light-mode content section (System).

## Type scale (Inter; ChakraPetch = `var(--mono)` for labels/eyebrows only)
| Role | Size |
|---|---|
| Hero headline | `clamp(30px, 4.4vw, 52px)` |
| Section title (`.statement` tier) | **32px** (`clamp(24px, 2.5vw, 32px)`) · **5 columns** wide |
| Section intro / body / descriptions | **17px**, line-height 1.7 · **5 columns** wide (same size — not a 17/15 tier) |
| Card-internal / mockup UI labels, dense-meta, fine print only | 15 / 14 / 12 |

> **Measured against the homepage prototype (2026-07-08) — this is ground truth, match every page to it:**
> Every section title renders **32px at ~5 columns**; every section body/intro/description renders **17px at ~5 columns**. `line-height:1.7` marks a body paragraph. The only deliberate exception is a hero-stat title (like Evidence's) that spans ~8–9 columns. Do not let a title be 6 cols or a description be 15px — those are the recurring mistakes.
| Card row **label** | `var(--mono)` 12px, `--c-700` |
| Card row **value** | 14px Inter, tabular-nums |
| Eyebrow (`No. 0X` + name) | `var(--mono)` 12px, `--c-700` |
| `$` display numbers | 24 / 28 / 40 (max 40) |

Allowed font sizes only: **11 / 12 / 13 / 14 / 15 / 17 / 18 / 22 / 24 / 28 / 34 / 40**. Never invent 16 / 20 / 30, etc.

## Cards
- Background `var(--c-surface)` (#101010), border `0.5px solid var(--c-900)`, `border-radius: 4px`, **no box-shadow** (de-phoned, P1 brief — no rounded phone corners, no gloss).

## Section spacing
- Desktop `padding: 160px 0`; mobile `88px 0`. (Design-system doc says 130 but the prototype uses 160 — match the prototype.)
- Repeated rows / parallel items must render **equal line counts** (match copy length; never ship ragged).

## Color
- Product surface is **monochrome `--c-*` neutrals only**. Severity dots (the only status color): urgent `#FF3533`, warning `#FF7A00`, review `#FBC308`, live `#30D158`.
- Do **not** color simple price ±/− moves on the product surface (severity color is reserved). Exception: marketing/illustrative mockups may use accent color for life — judge by tone.
- Managed portfolio identity uses the separate `--pf-*` palette in **large areas only** (covers/images), never as small dots.

## Line colors (hairlines & borders)
- `--c-900` = structural lines (section/row dividers, card borders).
- `--c-800` = object outlines & accents (dotted underlines, vertical accent bars).
- `--c-700` = micro accents (nav caret, blockquote bar).

## Casing & copy
- Title Case typed directly in HTML. `text-transform: uppercase` is forbidden. `capitalize` only on single-word labels.
- **No em-dashes** (— / &mdash;) anywhere — use commas / periods / hyphens.

## Before finishing
- Run `node .claude/scripts/validate-design.js "<path>"` — fix all errors.
- Integrity: file ends with `</html>`, NUL byte count = 0 (OneDrive/Korean-path sync can corrupt).
- Every site page includes `<script src="grid-overlay.js"></script>` before `</body>`.
