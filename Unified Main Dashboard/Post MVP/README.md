# II (Intelligent Investing) — Dashboard Prototype

Post-MVP dashboard prototype for Mogo's Intelligent Investing product.

**Live:** https://ii-inkchoi.github.io/ii-prototype/

## Pages

- **`index.html`** — Auto-redirects to the main dashboard.
- **`Unified Dashboard.html`** — Main dashboard. Open Questions at top, then Core (Managed), then Active (Self-Directed).
- **`Open Questions.html`** — Dedicated Open Questions detail screen (kept for focused-view use).
- **`Performance Dashboard.html`** — Performance vs S&P 500 analysis (from `performance dashboard/v3/`).
- **`Open Positions.html`** / **`Closed Positions.html`** / **`Benchmark.html`** — Performance Dashboard sub-pages.

## Main dashboard structure (top to bottom)

1. **Header** — Mogo wedge logo (inline SVG), search + menu icons.
2. **Open Questions** — Page head + 4 categories integrated directly on the dashboard (no extra click).
   - Big Move (red dot)
   - Material Move (orange dot)
   - Thesis Review (yellow dot)
   - Memo Pending (neutral gray dot)
   - Each section: dot + title + count, items, primary action link, × dismiss.
3. **Total Value** — Hero number (static).
4. **Core / Managed** — Single clickable block. Value + All Time + Projection + Allocation.
5. **Active / Self-Directed** — Container with multiple analytical sub-blocks:
   - Value + All Time
   - Performance vs S&P (perf-block, frame + chevron, clickable → Performance Dashboard)
   - Calibration (right-aligned pos-group, clickable)
   - Concentration (slim-block + segmented bar + // AI insight, clickable)
   - Active Positions (with 5%+ price-move dots, clickable list)
   - Cash (10%) — sub-line, clickable
   - Under Review (clickable list)
   - Open Orders (with per-ticker breakdown, clickable list)
   - Paper Trades (1 logged entry, links to Leo's prototype)

## Design system

Built against the doctrine files in `ii-doctrine` repo:
- `Mogo Design Philosophy.md` — Severe brand posture, ICP, core philosophy
- `Style_Design.md` — Tokens (colors, spacing, typography), case convention, visual hierarchy tiers, clickability affordance, AI insight signal, position move marks, Open Questions structure
- `II Doctrine.md` — Part I + Part II (accountability mechanics)

## Prototype navigation

Most `<a>` links are intentionally inert until target pages are wired. A small script in the dashboard calls `preventDefault()` on every `<a>` except those marked with `data-active="true"`.

**Currently active:**
- `Performance Dashboard.html` ← from perf-block on dashboard
- `Unified%20Dashboard.html` ← from Performance Dashboard back arrow

**Currently inert (placeholder):**
- Calibration, Concentration, Cash, Active Positions, Under Review, Open Orders, Paper Trades, individual OQ items + actions.

Add `data-active="true"` to enable each link as its target page is wired.

## × Dismiss interaction (Open Questions)

Each Open Question category has a thin SVG × at the right. Click:
1. The whole section fades out (220ms ease-out)
2. Removed from DOM
3. Header count recalculates from remaining sections
4. When count hits 0, the entire Open Questions header is hidden

## Local preview

Open `index.html` in a browser. Designed for mobile (393 × 852 viewport, iPhone 16).

## Deploy

Static site — no build step. Currently deployed via GitHub Pages on `ii-inkchoi.github.io/ii-prototype/`. Push to `main` triggers auto-deploy in 1–2 minutes.

## Status

Active iteration. See `ii-doctrine` repo for design doctrine + decision log.
