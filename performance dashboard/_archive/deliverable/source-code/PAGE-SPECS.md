# Per-Page Specs

What each prototype page does, what's interactive, and what the dev needs to know to wire it up.

For navigation between pages see [FLOW.md](./FLOW.md) or open [flow.html](./flow.html). For shared design tokens see [TOKENS.md](./TOKENS.md).

---

## 1. `index.html` — Preview hub (dev-only)

**Purpose:** A flat list of every prototype screen, used by reviewers to open any page directly. **Not a production screen** — would not ship.

**Contents:** Five `<a class="page-link">` rows, each linking to one of the five real screens with a one-line description.

**Interactive elements:** Five page links. No state.

**Data:** None. All hardcoded.

**Notes:** Title shows "Prototype / Performance Dashboard". Footer reads "Mobile prototype · Built for II Self-Directed loop · Per-tranche shadow benchmarking · Anti-hiding by design."

---

## 2. `unified-dashboard.html` — Main app screen

**Purpose:** The user's single entry point. Shows total portfolio value, then splits into two parallel sections — **Managed (Core)** and **Self-Directed (Active)** — with symmetric information structure.

**Sections:**
- **Total Value** (hero — `173,249.00 CAD`)
- **Managed / Core**: Value, Projection, Allocation (Equity / Fixed Income / Money Market percentages)
- **Self-Directed / Active**: Value, Projection, Composition (top holdings + Cash), Performance (Portfolio vs Benchmark vs Alpha), Positions (Active / Under Review / Open Orders counts)

**Interactive elements:**

| Element | Action | Destination |
|---|---|---|
| Header search icon | (placeholder, no handler) | — |
| Header menu icon | (placeholder, no handler) | — |
| Self-Directed performance block | Navigate | `performance-dashboard.html` |
| RRSP chip (with chevron) | Account-type dropdown | Not wired |

**Data flagged as placeholder:**
- All dollar values (`173,249.00`, `126,471.77`, `46,777.23`, etc.) — sample data
- Projection figures (`1.68M`, `0.61M`) — derived from "11% long-term S&P average" assumption, 20-year horizon
- Allocation percentages — sample
- Composition holdings (`ORIO.TO`, `BWEN`, `OSCR`, `Cash`) — sample

**Doctrine constraints applied:**
- Right-spine alignment: all numeric data on the right edge, labels on the left
- Information symmetry between Managed and Self-Directed sections
- No false precision: round numbers should later be displayed without `.00`
- Opacity ladder used for hierarchy (t1 → t4); no accent color
- 8px grid spacing, intentional whitespace

**Note on data attributes:** Most numeric values carry `data-final="..."` and `data-r="..."` attributes (used for entry animation in the prototype). Engineering can ignore these or use them as the data-binding spec.

---

## 3. `performance-dashboard.html` — Self-Directed performance detail

**Purpose:** Drill-down into the user's active (self-directed) portfolio performance vs the S&P 500. This is the **richest screen** — equity curve, period toggle, alpha calculation, behavioral metrics ("Decisions", "Discipline").

**Key sections (top to bottom):**
1. **Hero — Tracked duration** (`Tracked since Mar 14, 2023 — 3 years 2 months`)
2. **Annualized · Preliminary** (3-column: Your Portfolio / Alpha / S&P 500)
3. **"Not Yet Signal" callout** with progress bar (38 of 60 months, signal at Mar 2028 — confidence threshold)
4. **Time period toggle** (YTD / 1Y / 3Y / All) — `<span data-period="...">`
5. **Performance vs S&P 500** table (Your Portfolio / S&P Would Have / Alpha)
6. **Equity Curve** (SVG, period-aware)
7. **Cash Drag**, **Performance metrics**, **Decisions**, **Discipline** sections (see HTML for full list)

**Interactive elements:**

| Element | Action | Destination |
|---|---|---|
| Back button (top-left) | `javascript:history.back()` | Previous page |
| Exit button (top-right) | Navigate | `unified-dashboard.html` |
| Period toggle (YTD/1Y/3Y/All) | Re-render numbers and curve | (handled by `performance-dashboard.js`) |
| "S&P Would Have" label | Navigate | `benchmark.html` |
| S&P 500 SVG text | Navigate | `benchmark.html` |
| "S&P 500 same window" label | Navigate | `benchmark.html` |
| "View All" (open positions) | Navigate | `open-positions.html` |
| "Beat S&P (Winners)" label | Navigate w/ filter | `closed-positions.html?filter=winners` |
| "Trailed (Losers)" label | Navigate w/ filter | `closed-positions.html?filter=losers` |
| "View All" (closed positions) | Navigate | `closed-positions.html` |

**Data binding:** Many values are `<span data-bind="...">` for the period toggle. The JS swaps text content based on selected period. See `performance-dashboard.js` for the data structure.

**Doctrine constraints:**
- Hero is *duration* not return — the doctrine is that performance numbers under 5 years are "not yet signal"
- Alpha is shown in **percentage points (pp)** for percent comparisons, **dollars** for dollar comparisons — never mixed
- Equity curve is SVG, hand-drawn paths (no chart library) — keeps the visual minimal

---

## 4. `benchmark.html` — S&P 500 comparison view

**Purpose:** Educational / contextual screen explaining what the S&P 500 benchmark is and how it's calculated. Linked from multiple places on `performance-dashboard.html`.

**Sections:**
1. **Hero statement** — "The baseline most active investors fail to beat."
2. **Same Period comparison** (Your Portfolio / S&P 500 / Alpha)
3. **Methodology** (Return Type: Time-Weighted, Dividends: Reinvested, Cost Basis: Matched per position, Period: All Time · Fixed, Currency: CAD)
4. **"When does performance matter"** — three time horizons (1–3 Years: Mostly Noise / 5 Years: Early Signal But Fragile / 10+ Years: Meaningful Signal)

**Interactive elements:**
- Back button, Exit button only (no inline interactivity)

**Data:**
- Comparison numbers (`+2,353.46`, `+5,476.91`, `−3,123.45`) are hardcoded — needs to match whatever performance window/account the user came from. The current prototype doesn't pass context.

**Doctrine constraints:**
- Cold/Clinical tone in the explanatory copy ("Mostly Noise", "Early Signal But Fragile", "Meaningful Signal")
- Three time horizons are the brand's official stance on when active vs. passive comparisons are meaningful

**Engineering note:** This page is the same regardless of which link the user came from (`performance-dashboard.html` has three different links pointing here). Decide whether to pass context (which metric, which period) via query string.

---

## 5. `open-positions.html` — Active positions list

**Purpose:** Full list of currently held positions in the self-directed portfolio, grouped by discipline status.

**Top summary:**
- Total Open: `12`
- Discipline Flags: `7`
- Beating S&P / Trailing: `5 / 7`
- Capital Deployed: `125,000.00`
- Current Value: `131,820.00`
- Unrealized Alpha: `−1,375.25`
- Avg Hold: `1y 1m`

**Position groups:**
1. **Below Kill Line** (rule violations — top priority)
2. **Needs Review** (past horizon / approaching target / earnings due)
3. **Normal** holdings

Each row shows: symbol, return %, capital, current value, S&P shadow return, alpha, hold duration, weight, status badge.

**Interactive elements:**

| Element | Action |
|---|---|
| Back button, Exit button | Standard nav |
| Sort tabs: Discipline / Impact / Alpha | Re-sort the list (`open-positions.js`) |
| Position rows | Currently non-interactive in prototype |

**Default sort:** Discipline — "Rule violations first (kill line, past horizon, overdue review), then worst alpha."

**Data:** All position data is hardcoded in the HTML with `data-alpha` and `data-discipline` attributes that drive the JS sorting. Engineering can use these as the data model spec.

**Doctrine constraints:**
- "Anti-hiding by design" — rule violations and worst performers are surfaced first
- No color-coded green/red on positive/negative numbers — opacity and grouping do the work

---

## 6. `closed-positions.html` — Closed trades list

**Purpose:** Full history of closed trades with capital, return, S&P shadow, and alpha. Supports filtering via query string.

**Top summary:**
- Total Closed: `38`
- Win Rate vs S&P: `36.8%`
- Capital Deployed: `273,500.00`
- Total Return: `+4,727.50`
- S&P Would Have: `+33,914.00`
- Alpha: `−29,186.50`
- Avg Hold: `14m`

**Filter via URL:**
- `closed-positions.html` — no filter, all 38 shown
- `closed-positions.html?filter=winners` — only positions that beat S&P
- `closed-positions.html?filter=losers` — only positions that trailed S&P

The filter is read in `closed-positions.js` on page load via `URLSearchParams`.

**Interactive elements:**

| Element | Action |
|---|---|
| Back button, Exit button | Standard nav |
| Sort tabs: Alpha / Impact / Recent | Re-sort list |
| Position rows | Currently non-interactive |

**Default sort:** Alpha (ascending — worst first). Note text: "Worst alpha first — biggest underperformers vs S&P 500 at the top."

**Data:** Position rows are hardcoded with `data-alpha` etc. for sorting.

**Doctrine constraints:**
- Same anti-hiding principle: defaults to worst-first
- Win rate (`36.8%`) shown plainly — no euphemism

---

## Cross-page concerns for engineering

1. **No state shared across pages.** Every page renders standalone from hardcoded data. The production version will need:
   - A portfolio data layer (positions, performance, allocations)
   - A user/account selector (the RRSP chip on Unified Dashboard implies multi-account)
   - A live S&P 500 data source for the benchmark comparisons

2. **All money values are CAD.** Confirm currency handling at the API layer; the display layer should strip `.00` from round numbers (false-precision rule).

3. **Animation/entry data attributes.** `data-final="..."` and `data-r="..."` on Unified Dashboard are for the entry animation. Strip or implement at the dev's discretion — they're not load-critical.

4. **No accent color.** If the dev's component library defaults to a brand color on links/buttons, those need to be overridden per the doctrine.

5. **Tabular numerals.** `font-feature-settings: 'lnum' 1, 'tnum' 1;` is required on any element showing aligned numbers. This is already baked into the body styles.

6. **Mobile viewport target:** `max-width: 393px`. The current prototypes do not have a responsive desktop variant — confirm whether the production version is mobile-only.
