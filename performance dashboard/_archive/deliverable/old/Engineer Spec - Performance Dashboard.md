# Engineer Spec — Performance Dashboard

**Owner:** Inkyung Choi
**Date:** 2026-05-09
**Scope:** II Self-Directed accountability layer
**Prototype folder:** `prototype/`
**Doctrine:** `doctrine/II Doctrine.md`

---

## 1. Goal

Make underperformance vs. S&P 500 unhideable. Every active stock-picking decision is shadowed by an automatic S&P 500 (VFV.TO ETF backing) position; alpha = real return − shadow return.

The primary decision-supporting metric on both Unified Dashboard and Performance Dashboard is **annualized return vs. S&P 500 + tracked length**. The user must always see "what is my annualized rate, vs. the benchmark, over what period". Until the tracked period reaches 5 years, the data is framed as **Preliminary** (not yet a signal).

---

## 2. File structure & navigation

```
prototype/
├── index.html                  # demo redirect into Unified Dashboard
├── Logo.svg                    # II logo
├── Unified Dashboard.html      # main dashboard (entry; perf-block links to PD)
├── Performance Dashboard.html  # detail / accountability page
├── Benchmark.html              # methodology static page (linked from PD)
├── Open Positions.html         # active holdings list
└── Closed Positions.html       # closed ledger (supports ?filter=winners|losers)
```

### Page map (high level)

```
index.html
   └→ Unified Dashboard.html                    [main entry]
        ├→ Performance Dashboard.html           via Active section perf-block
        ├→ Open Positions.html                  via Active section "View All"
        └→ Stock Page                           via individual position row (drill-down)

Performance Dashboard.html
   ├→ Benchmark.html                            via "S&P Would Have" / curve legend "S&P 500" / sub-row labels
   ├→ Closed Positions.html                     via Closed block "View All"
   ├→ Closed Positions.html?filter=winners      via Closed block "Winners" link
   ├→ Closed Positions.html?filter=losers       via Closed block "Losers" link
   ├→ Open Positions.html                       via Open block "View All"
   └→ Unified Dashboard.html                    via header "Exit" or back arrow

Open Positions.html
   └→ Stock Page                                via row click

Closed Positions.html
   └→ Stock Page                                via row click

Benchmark.html
   └→ (terminal; back via system)
```

---

## 3. Data model

### Position
```
Position {
  id: uuid
  symbol: string                  # e.g. "ATZ"
  account_id: uuid
  status: enum                    # open | closed
  thesis: text                    # required to open
  kill_line: text                 # required to open
  confidence: enum                # 40 | 50 | 60 | 70 | 80
  confidence_history: [{ value, set_at }]
  reviewed_at: timestamp
  exit_reason: enum nullable      # target_hit | stop_hit | thesis_broke | horizon | rebalance | other
}
```

### Tranche + Shadow
```
Tranche {
  id: uuid
  position_id: uuid
  side: enum                      # buy | sell
  qty: decimal
  price: decimal                  # per share, native ccy
  ccy: string                     # CAD | USD
  fx_rate: decimal                # CCY → CAD at execution
  executed_at: timestamp
  shadow_tranche_id: uuid         # FK
}

ShadowTranche {                   # auto-created on every Tranche insert
  id: uuid
  tranche_id: uuid                # parent
  symbol: 'VFV.TO'                # internal — never surfaced as label
  side: enum
  notional_cad: decimal
  executed_at: timestamp          # exact same timestamp as parent
  fill_price: decimal             # VFV.TO close that day
}
```

### Daily Snapshot
```
DailySnapshot {
  account_id: uuid
  date: date
  market_value_cad: decimal
  cash_cad: decimal
  shadow_value_cad: decimal       # all live ShadowTranches marked to today
}
```

### Confidence Calibration
```
ConfidenceCheck {
  position_id: uuid
  confidence_at: enum             # 40..80
  set_at: timestamp
  resolved_at: timestamp nullable
  outcome: enum nullable          # right | wrong | partial
}
```

### Account-level inception
```
AccountInception {
  account_id: uuid
  inception_at: date              # first tranche date — drives "Tracked since" + "X years Y months"
  signal_at: date                 # inception_at + 5 years — drives "Signal: Mar 2028" + progress bar
}
```

---

## 4. Computed metrics

### Core formulas

| Metric | Formula | Notes |
|---|---|---|
| Real return ($) | Σ (sell_proceeds − buy_cost) closed + (mark − cost) open | CAD after FX |
| Shadow return ($) | Σ same on ShadowTranches | Per-tranche, never averaged |
| Alpha ($) | real − shadow | **Primary KPI, dollars first** |
| Alpha (pp) | real_pct − shadow_pct | Secondary, muted |
| TWR (annualized) | Modified Dietz | Time-weighted, stock-picking skill |
| MWR (annualized) | XIRR | Money-weighted, includes deposit timing |
| Timing gap | MWR − TWR | Negative = poor deposit timing |
| Max drawdown | min(equity_t / peak_t − 1) | Daily marks |
| Volatility (12M) | stdev(daily returns) × √252 | Trailing 12 months |
| Avg cash % | mean(cash_cad / market_value_cad) over period | Daily basis |
| Cash drag ($) | avg_cash × shadow_period_return | Forgone return on idle cash |

### Tracked length (for hero + "Annualized · {N years M months}")
```
tracked_months = floor((today - inception_at) / 30.4375)
years = floor(tracked_months / 12)
months = tracked_months % 12
display = `${years} year${years!==1?'s':''} ${months} month${months!==1?'s':''}`
inception_display = formatDate(inception_at, 'MMM D, YYYY')   # "Mar 14, 2023"
```

### Signal threshold (5-year preliminary qualifier)
```
SIGNAL_MONTHS = 60
months_in    = tracked_months
months_to_go = max(0, SIGNAL_MONTHS - tracked_months)
progress_pct = min(100, tracked_months / SIGNAL_MONTHS * 100)
signal_date  = addYears(inception_at, 5)
signal_display = formatDate(signal_date, 'MMM YYYY')          # "Mar 2028"

is_preliminary = tracked_months < SIGNAL_MONTHS
```

When `is_preliminary === true` → show "Annualized · Preliminary" label everywhere annualized data appears, and render the **Not yet signal** callout on PD. When `is_preliminary === false` → drop the "· Preliminary" qualifier and hide the callout.

### Annualized Return summary row (Yearly Breakdown bottom)
For the displayed table, the **Annualized Return** row shows:
- `Portfolio`: TWR annualized over `tracked_months / 12` years
- `S&P 500`: shadow TWR annualized same period
- `Alpha`: portfolio − sp (in pp)

Same data as the top "Annualized · Preliminary" block — placed at the bottom of the chart so the user sees the conclusion without scrolling back up.

### Period definitions (4 options on toggle)
- **YTD**: Jan 1 of current year → today
- **1Y**: trailing 365d
- **3Y**: trailing 1095d
- **All**: since `inception_at`

Default: **All**.

### Yearly Breakdown rules
- Show **only past completed years + current year as YTD** as actuals (oldest at bottom: e.g. 2026 YTD, 2025, 2024, 2023)
- After actuals, render `.yt-divider` then **future signal row(s)** with em-dash placeholders. The signal year is `inception_year + 5` (e.g. 2028). Future rows use de-emphasized color (`c-800`).
- The **Annualized Return** summary row sits *between* actuals and the divider, with c-white emphasis and a top-border separator.

### Beat/Trailed (closed positions only — past tense)
- `beat_count`: count(closed where alpha > 0)
- `trailed_count`: count(closed where alpha ≤ 0)
- Display: "Beat S&P / Trailed" (not "Beating / Trailing")
- Open positions: still "Beating / Trailing" (present tense)
- Combined Total Positions row uses "Beating / Trailing" (mixed open + closed)

### Win Rate
- `win_rate_pct = beat_count / closed_total_count * 100`
- `avg_alpha_win_$  = mean(alpha_$ where closed and alpha_$ > 0)`
- `avg_alpha_loss_$ = mean(alpha_$ where closed and alpha_$ <= 0)`

---

## 5. Pages — sections, meaning, and click destinations

### 5.1 `Unified Dashboard.html`

**Purpose.** The main dashboard. The entry point after authentication. Shows the user's full account picture (Core managed + Active self-directed) at a glance.

**Sections, top to bottom:**

1. **Header** — II logo (left), search + menu icons (right). *Not currently linked in the prototype.*
2. **Total Value** *(right-aligned)* — sum of Core + Active. Not clickable.
3. **Core (Managed) section** — section title, Value, Projection, Allocation (3 rows: Equity / Fixed Income / Money Market). Read-only.
4. **Active (Self-directed) section**
   - Section title: "Active / Self-directed"
   - Account switcher: `RRSP ▾`
   - **Value**: dollar amount of active sleeve.
   - **Performance vs S&P 500 block (`perf-block`)** — chairman-mandated focus metric:
     - Header: `Annualized · 3 years 2 months` + `›` chevron in top-right
     - Row 1: `Your Portfolio · +18.2%`
     - Row 2: `S&P 500 · +24.0%`
     - Row 3 (separated by hairline): `Alpha · −5.8pp`
   - **Cash**: dollar amount + percentage of active sleeve held in cash.
   - **Active Positions (count)**: top 5 holdings + "View All".
   - **Under Review (count)**: positions flagged for re-underwriting.
   - **Open Orders (count)**: pending unfilled orders.

**Click destinations:**

| Element | Destination | Notes |
|---|---|---|
| Active section `perf-block` (whole block) | `Performance Dashboard.html` | Primary drill-down. Chevron in top-right indicates tap target. |
| Account switcher `RRSP ▾` | (account picker — not in prototype) | Will switch active account context. |
| Active Positions "View All" | `Open Positions.html` | |
| Active Positions individual rows | (Stock Page — not in prototype) | Row click → drill to position detail. |
| Under Review "View All" | (review queue — not in prototype) | |
| Open Orders count | (orders list — not in prototype) | |

---

### 5.2 `Performance Dashboard.html`

**Purpose.** The accountability detail page for the Active sleeve. The user lands here from the Unified Dashboard's perf-block. Surfaces every metric needed to honestly evaluate stock-picking decisions vs. holding the S&P 500.

**Sections, top to bottom:**

1. **Header** — back arrow (`history.back()`), "Exit" link → `Unified Dashboard.html`.
2. **Title block** — `Performance` / `Active · Self-Directed`.
3. **Hero** *(left-aligned)* — eyebrow `Tracked since Mar 14, 2023` + value `3 years 2 months` (18px). Communicates "for how long this data has been collected".
4. **Annualized · Preliminary block** *(under hairline divider)* — 3-column flat grid: `Your Portfolio · +18.2%` (left), `Alpha · −5.8pp` (center, smaller font), `S&P 500 · +24.0%` (right). "Preliminary" qualifier appears whenever `is_preliminary`.
5. **Not yet signal callout** *(only when `is_preliminary`)* — title + body explaining the 5-year requirement, progress bar (`tracked_months / 60`), bottom row `38 of 60 months` + `Signal: Mar 2028`. Hides entirely once `tracked_months ≥ 60`.
6. **Period bar (sticky)** — `YTD / 1Y / 3Y / All`. Default `All`. Tap → optimistic UI swap (180ms fade) of every `[data-bind]` element.
7. **Performance vs S&P 500** *(detail rows)* — `Your Portfolio` / `S&P Would Have` / `Alpha`. Dollars primary, percentages muted.
8. **Equity curve** — SVG, two lines (Portfolio solid `c-400`, S&P dashed `c-700`), Y labels at left, 4 X-axis date labels. In-chart legend with "Portfolio" + "S&P 500".
9. **Cash drag callout** — sentence + meta line. No decoration.
10. **Performance metrics** *(tappable info)* — TWR, MWR, Timing gap, Max Drawdown (+ S&P sub), Volatility (+ S&P sub), Avg Cash %. All labels tappable (dotted underline) → toggle inline info panel.
11. **Yearly Breakdown** — 4-column grid:
    ```
    Year             Portfolio   S&P     Alpha
    2026 YTD          +5.2%      +9.4%   −4.2pp
    2025              +22.4%     +18.2%  +4.2pp
    2024              +8.6%      +24.1%  −15.5pp
    2023              +18.2%     +24.2%  −6.0pp
    Annualized Return +18.2%     +24.0%  −5.8pp   ← summary row, c-white, top-border
    ───────────────────────────────────────────── (yt-divider, c-800)
    2028 Signal       —          —       —        ← future signal row, c-800 muted
    ```
12. **Decisions** — Total Positions, Beating/Trailing (sub), Win Rate vs S&P (tappable), Avg Alpha-Win/Loss (tappable subs), Open block (count + present-tense Beating/Trailing + View All), Closed block (count + past-tense Beat/Trailed + Winners/Losers links + View All).
13. **Discipline** — Days Since Last Trade, Turnover (with S&P sub), Avg Holding Period.
14. **Disclosure** — single paragraph in `c-700`. Explains TWR/MWR distinction, past/present tense convention, 5-year signal threshold.

**Click destinations:**

| Element | Destination |
|---|---|
| Header back arrow | Browser history (typically Unified Dashboard) |
| Header "Exit" | `Unified Dashboard.html` |
| Period bar tabs (YTD / 1Y / 3Y / All) | In-page state change (no navigation) |
| "S&P Would Have" row label | `Benchmark.html` |
| Equity curve "S&P 500" legend | `Benchmark.html` |
| "Max Drawdown — S&P 500 same window" sub-row | `Benchmark.html` |
| "Volatility — S&P 500" sub-row | `Benchmark.html` |
| Every metric label with dotted underline | Toggles inline info panel (no navigation) |
| Open block header / "View All" | `Open Positions.html` |
| Closed block header / "View All" | `Closed Positions.html` |
| Closed block "Winners" link | `Closed Positions.html?filter=winners` |
| Closed block "Losers" link | `Closed Positions.html?filter=losers` |

---

### 5.3 `Benchmark.html`

**Purpose.** Static methodology page. Explains why S&P 500 is the benchmark and how the per-tranche shadow comparison works.

**Sections.** Header, Title `Benchmark · S&P 500`, Why S&P, Per-tranche shadow, Alpha calculation, When performance matters, What we don't do.

**Click destinations.** Back / Exit → previous page or Unified Dashboard. No forward links.

---

### 5.4 `Open Positions.html`

**Purpose.** The full list of currently held positions (active sleeve).

**Sections:**
1. Header (back / Exit).
2. Title `Open Positions`.
3. Summary KPIs: `Open · 12`, `Discipline Flags · X`, `Unrealized Alpha · $X`.
4. **Sort bar (sticky)**: `Discipline / Impact / Alpha`. Default `Discipline`.
5. **Sort note** — small text below the bar, updates on sort change:
   - **Discipline**: *Rule violations first (kill line, past horizon, overdue review), then worst alpha.*
   - **Impact**: *Biggest absolute dollar moves first.*
   - **Alpha**: *Worst alpha first — biggest underperformers vs S&P 500 at the top.*
6. **Holdings list** — when sorted by Discipline, grouped under labels (`Below Kill Line`, `Past Horizon`, `Overdue Review`, `On Track`) with worst alpha first within each group. When sorted by Impact or Alpha, flat list with group labels hidden. Each row: `Ticker · % return · Capital · Current value · S&P would have · Alpha`. Status badge per row.

**Click destinations:**

| Element | Destination |
|---|---|
| Header back / Exit | Previous page / Unified Dashboard |
| Sort bar tabs | In-page resort + sort-note text update |
| Holdings row click | Stock Page (drill-down) |

---

### 5.5 `Closed Positions.html`

**Purpose.** The historical ledger of every closed position. Default sort surfaces the worst alpha first. Supports URL filter for the Performance Dashboard's Winners / Losers links.

**Sections:**
1. Header (back / Exit).
2. Title `Closed Positions` — when `?filter=winners` → suffix `· Winners`; when `?filter=losers` → suffix `· Losers`.
3. Summary KPIs: `Closed · 38`, `Total Capital · $X`, `Win Rate vs S&P · 38.0%`, `Total Alpha · $X`, `Avg Hold · X months`. **All KPIs recalculate on filter.**
4. **Sort bar (sticky)**: `Alpha / Impact / Recent`. Default `Alpha`.
5. **Sort note** — updates on sort change:
   - **Alpha**: *Worst alpha first — biggest underperformers vs S&P 500 at the top.*
   - **Impact**: *Biggest absolute dollar moves first.*
   - **Recent**: *Most recently closed first.*
6. **Holdings list** — each row: `Ticker · % return · Capital · Return $ · S&P $ · Alpha $ · Closed date · Hold months`. Past tense ("Beat S&P" / "Trailed").

**URL filter behavior.** On page load:
1. Read `?filter=winners|losers` from `URLSearchParams`.
2. If `winners`: hide rows where `alpha_$ ≤ 0`. If `losers`: hide rows where `alpha_$ > 0`.
3. Update title suffix and document title.
4. Recalculate every summary KPI over the visible subset only.
5. If no filter param, show all (default state).

**Click destinations:**

| Element | Destination |
|---|---|
| Header back / Exit | Previous page / Unified Dashboard |
| Sort bar tabs | In-page resort + sort-note text update |
| Holdings row click | Stock Page (read-only historical view) |

---

### 5.6 Stock Page (drill-down — *future ticket, not in this prototype*)

Reached from any holdings row on Open / Closed / Active Positions. Shows: title (symbol, last price), thesis + kill line + confidence, reviewed timestamp, performance vs S&P, position basics, navigation (History / Market / News / Research), capital decision CTA (fixed bottom).

---

### 5.7 `index.html`

**Purpose.** Demo entry point. Auto-redirects to `Unified Dashboard.html`. Production should drop this file and route the post-auth landing directly.

---

## 6. Cross-page consistency rules

1. **Back navigation**: every page except Unified Dashboard has a working back arrow. Use `history.back()` rather than hardcoded routes when possible.
2. **"Exit" affordance**: appears on detail pages (PD, Benchmark, Open/Closed) and explicitly routes to `Unified Dashboard.html` regardless of history.
3. **Tappable label pattern**: dotted underline (`0.5px dotted c-800`) under the label text indicates an info panel will toggle. **No icons.**
4. **Sort bar pattern**: every list view (Open / Closed) uses the same sort bar component with a contextual sort-note line below. Note text updates on sort change.
5. **Anti-hiding defaults**: Closed Positions defaults to "Alpha" (worst first). Open Positions defaults to "Discipline" (violations first). Never default to "Recent".
6. **Past vs present tense**: closed positions always read "Beat S&P / Trailed". Open positions always read "Beating / Trailing". The combined Total Positions row mixes both, so use "Beating / Trailing".
7. **"S&P 500" wording**: never "VFV.TO" in user-facing copy on any page.

---

## 7. Interactions

### Period toggle (Performance Dashboard)
- Tap → optimistic UI swap with 180ms fade.
- Cache last selected period in `sessionStorage`, restore on return.
- All swappable elements have `[data-bind]` (text) or `[data-bind-d]` (SVG path).
- During fade, `.swapping` class applies opacity 0.35 (text) / 0.3 (paths).

### Tappable info pattern (CRITICAL — II doctrine)
**No icons.** The label text itself is the affordance.

```html
<span class="lbl">
  <span class="lbl-tap" data-info="twr">TWR (annualized)</span>
</span>
<!-- Sibling info panel hidden by default -->
<div class="info-panel" data-info-for="twr">
  <p class="ip-body">Time-weighted return. Strips out deposit/withdrawal timing.</p>
  <p class="ip-formula">Formula: Modified Dietz</p>
</div>
```

Visual cue: 0.5px dotted underline in `var(--c-800)`. On tap: toggle `.open` class on `.lbl-tap` → text becomes c-white, underline becomes c-700. Toggle `[hidden]` on the matching `.info-panel`.

### Cross-page link from Unified perf-block
```html
<a href="Performance Dashboard.html" class="perf-block">…</a>
```
Whole block is the link. Chevron in header = visual cue. No row-level click handlers.

### Closed Positions filter
On page load:
1. Read `?filter=winners|losers` from URL.
2. If present, update document title and visible heading suffix.
3. Call `filterRows(filter)` → hides/shows DOM nodes via `.hidden` class.
4. Call `recalculateSummary(visibleRows)` → updates summary KPI bindings.
5. If no filter, show all (default state).

### Sort bars (Open / Closed Positions)
- Tap → `applySort(key)` re-orders DOM nodes.
- Update `sortNote` text content from the `sortNotes` map.
- Active state: white text, `aria-selected="true"`.
- Pre-computed `data-alpha`, `data-date`, `data-impact` on each row.

### Re-underwriting trigger
Background job: when price moves ≥20% from last review OR earnings release OR manual button → push notification + flag in Open Positions header.

### Kill line breach
Computed daily. If `current_price` crosses written kill condition → status badge red, position lifted to "Below kill line" group, surfaced in PD Decisions.

---

## 8. Design tokens

```css
--c-black:  #000000      /* page background */
--c-1000:   #1C1C1C      /* signal-callout bg, deepest container */
--c-900:    #232627      /* primary divider, signal-callout border */
--c-800:    #565B5E      /* de-emphasized / future / disabled (yt-divider, future year text) */
--c-700:    #929292      /* labels, meta, secondary text — DEFAULT for non-emphasized */
--c-400:    #C7C7C7      /* primary value text (where not c-white) */
--c-white:  #FFFFFF      /* hero, primary value, alpha emphasis */
```

**Important — common mistake:** `c-800` is for *future / disabled / very-low-emphasis* states (the muted future year row). Do **not** use it for body text (e.g., disclosure). Use `c-700` for default secondary text.

**Type scale:** 11 (eyebrow/meta), 13 (label), 14 (row val / signal title), 15 (Unified row val), 18 (PD hero / annualized value), 22 (Unified Total Value).

**Letter spacing:** -0.02em standard, -0.44px on 22px Unified Total Value.

**Font:** Inter, weight 400 only.

**Tabular numbers:** `font-feature-settings: 'lnum' 1, 'tnum' 1;` on every numeric span.

**Container:** `max-width: 393px` (mobile-first prototype).

**Padding (gutter):** 13.5px left/right standard.

**Section gap:** 64px between major PD sections; 24–28px within Annualized block (label → row); 16px within perf-block on Unified.

**Animation:** 700ms ease-out fade-in with translateY(4px) → 0 stagger on header / hero / sections. Disabled under `prefers-reduced-motion: reduce`.

**Color exception:** No green/red signaling on performance numbers. Performance is intentionally monochrome — alpha is a fact, not a celebration. Only kill-line status badge can use red.

---

## 9. Doctrine (must hold)

1. **Per-tranche shadow** — every buy auto-creates VFV.TO shadow at exact same timestamp. Never averaged.
2. **Anti-hiding** — open + closed on same ledger. Default sort = worst alpha first. Yearly breakdown shows every year, including misses.
3. **Dollars first** — pp is muted secondary on detail page; on summary blocks (Annualized, perf-block) we show pp because that's what's compounded annually.
4. **No survivor bias** — closed positions stay forever.
5. **Past tense for closed** — "Beat S&P" / "Trailed", never "Beating/Trailing" on closed.
6. **TWR + MWR side by side** — neither hides the other.
7. **Cash is a position** — surfaces as cash drag $.
8. **Confidence calibrated** — discrete levels 40/50/60/70/80 only. History tracked.
9. **No icons** — text is the affordance. Severe minimalism.
10. **Tappable text** — pattern: subtle dotted underline (c-800), label gets `.open` state on tap.
11. **5-year signal threshold** — until tracked period ≥ 5 years, all annualized framing carries the **Preliminary** qualifier and the Not yet signal callout. Avoid implying skill before 60 months.
12. **"S&P 500" wording** — never surface "VFV.TO" in user-facing copy. The ETF is implementation, not language.
13. **"Your Portfolio"** — personalize the user's number; the index is just "S&P 500". Exception: tight tabular column headers (e.g., yearly breakdown) where space forces "Portfolio".

Full reference: `doctrine/II Doctrine.md`.

---

## 10. Open questions for engineering

1. **VFV.TO price source** — Yahoo, IEX, or in-house feed? Need consistent close prices to inception.
2. **FX timing** — execute at trade-time fx_rate or daily close fx_rate? Recommend trade-time.
3. **Fractional shadow tranches** — VFV.TO ~$130. Allow fractional in shadow ledger? (Recommend yes, not a real position.)
4. **Confidence outcome scoring** — automated when position closes, or manual? (Recommend prompt user at close, default to "right" if alpha > 0.)
5. **Partial-year handling** — TWR misleading on partial first year. Currently footnoted as YTD-style on the inception year. Confirm display rule.
6. **YTD definition** — calendar year (Jan 1) or fiscal year? (Defaulting to calendar.)
7. **Info panel definitions** — every metric has a tappable label. Who owns the copy? (Currently in prototype as draft.)
8. **Signal threshold transition** — when `tracked_months` crosses 60, what's the UX? Suddenly drop "Preliminary"? Brief celebration? Recommend silent transition + small unlock indicator on first dashboard load post-threshold.
9. **Annualization on partial inception year** — annualizing TWR over a sub-year period inflates volatility. Confirm formula matches the rest of the industry: `(1 + cumulative_twr)^(365/days_tracked) − 1`.

---

## 11. Implementation checklist

- [ ] Set up design tokens as CSS variables (Section 8).
- [ ] Build `<UnifiedDashboard>` matching `Unified Dashboard.html`.
- [ ] Build `<PerformanceDashboard>` reflecting Section 5.2.
- [ ] Implement `tracked_months` and `is_preliminary` derived state on account level (Section 4).
- [ ] Wire Annualized · Preliminary block + Not yet signal callout to flip on `is_preliminary` boolean.
- [ ] Implement Yearly Breakdown table with summary "Annualized Return" row + future signal year(s).
- [ ] Implement Closed Positions URL filter (Section 7) with summary recalculation.
- [ ] Wire all `[data-bind]` / `[data-bind-d]` swappable nodes to period toggle state machine.
- [ ] Implement tappable info panels (no icons; dotted underline pattern) for every metric label flagged in Section 5.2 #10.
- [ ] Implement sort bars + dynamic sort notes on Open / Closed Positions (Section 7).
- [ ] Localize copy + dates (currently en-CA hardcoded).
- [ ] QA: ensure no green/red on performance numbers; only kill-line badge may be red.
- [ ] QA: confirm "S&P 500" never displays as "VFV.TO" in user-facing strings (search the codebase).

---

*Prototype source of truth: `prototype/`. Full doctrine: `doctrine/II Doctrine.md`.*
