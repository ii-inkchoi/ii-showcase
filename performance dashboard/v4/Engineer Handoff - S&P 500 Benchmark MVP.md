# Engineer Handoff — S&P 500 Benchmark (MVP / Phase 1)

**Owner:** Inkyung Choi
**Date:** 2026-06-02
**Status:** Design confirmed (main dashboard card + performance detail page)
**Prototype source of truth:** `v3/Unified Dashboard v2.html`, `v3/Performance Dashboard.html`
**Stack:** React + CSS variables (per prior Engineer Spec conventions)
**Supersedes:** the alpha / annualized / TWR-MWR model in the v1-era `Engineer Spec - Performance Dashboard.md`. That complexity is intentionally removed for the MVP — see §11 Out of scope.

**How to read this doc:** §4 and §5 break down *every visible element* on the two screens. Each element is explained through three lenses — **Rationale** (why it exists / why it's framed this way), **Calculation** (exactly how the number is derived), and **Engineering note** (implementation constraints). §6–§7 consolidate the data model and formulas; §4–§5 reference them but also state the calc inline so each element is self-contained.

---

## 1. Goal

Answer one question for the member, immediately and unambiguously:

> **Would I have more or less wealth today if I had simply invested in the S&P 500?**

The feature measures **outcomes, not activity**. It compares two terminal wealth amounts — the member's actual portfolio value vs. a mirrored S&P 500 portfolio fed by the same cash flows — and shows the difference in dollars and percent.

Design principle: this is **not** a performance-reporting tool. No alpha, no basis points, no annualized return, no time-/money-weighted return in the MVP. Those are later phases (§11).

---

## 2. Scope

**In (Phase 1 / this handoff):**

- Main dashboard card — replaces the old gain/alpha card with a wealth-comparison card.
- Removal of the standalone simple rate of return on the Active (Self-directed) Value block.
- Performance detail page — restructured to Summary + Contributions & Growth + Methodology.

**Out (later phases, do not build now):** position-level comparison, winners/losers attribution, XIRR, TWR, equity curve, per-deposit cash-flow table. See §11.

---

## 3. Files & navigation

```
v3/
├── Unified Dashboard v2.html      # main dashboard (entry). Active section holds the benchmark card.
└── Performance Dashboard.html     # benchmark detail page. Reached from the card.
```

```
Unified Dashboard v2.html
   └→ Performance Dashboard.html        via the "S&P 500 Benchmark · All Accounts" card (whole card is the link)

Performance Dashboard.html
   └→ Unified Dashboard v2.html         via header back arrow / "Exit"
```

---

## 4. Screen 1 — Main dashboard card (element by element)

Lives in the **Active / Self-directed** section, directly below the Value block.

```
S&P 500 Benchmark · All Accounts                    ›
Portfolio Value                              58,420.18
S&P 500 Alternative                          56,236.00
─────────────────────────────────────────────────────
Difference                       +2,184.18   +3.88%
```

Component contract (reuse existing `.perf-block` markup — no new classes):

| Component | Props | Notes |
|---|---|---|
| `BenchmarkCard` | `title`, `portfolioValue`, `spAlternative`, `differenceAmount`, `differencePct`, `href` | Whole card is one `<a>`. Difference row uses the `.perf-row.diff` modifier (top hairline). |

### 4.1 Card placement — under Active / Self-directed → Value

**Rationale.** The benchmark only belongs to the self-directed sleeve, because that is where the member makes active capital-allocation *decisions*. The Core (Managed) sleeve is delegated — there is no member decision to hold accountable, so it gets no benchmark. Sitting the card immediately under the Value figure creates the read "here is my money → here is how that money compares to the simple alternative."

**Calculation.** None (layout). Scope follows the Active sleeve and the account selector (§4.2).

**Engineering note.** Rendered as part of the Active section; inherits the section's `.mt-active` fade-in delay. Do not render it in the Core section.

### 4.2 Title — `S&P 500 Benchmark · All Accounts`

**Rationale.** Named "Benchmark," never "Performance" — the spec is explicit that this is *not* performance reporting, so the word "Performance" is off-message. `· All Accounts` exposes the account-context scope so the member knows whether they're looking at one account or the aggregate.

**Calculation.** The `· All Accounts` suffix is bound to the account switcher. "All Accounts" = aggregate across all of the member's self-directed accounts; a single-account selection narrows both the portfolio and the mirror to that account.

**Engineering note.** Recompute the mirror at the selected scope (see open question §12.4 — aggregate-of-mirrors vs. mirror-of-aggregate must be settled; they can differ once accounts have different cash-flow timing).

### 4.3 Row 1 — Portfolio Value (`58,420.18`)

**Rationale.** The card leads with a **balance (terminal wealth)**, not a gain. "How much do I have" is concrete and can't be gamed; a gain or % invites the misleading "+11%, I'm doing well" conclusion the spec warns against. This is the member's real number.

**Calculation.** `positions_value_cad + cash_cad`, marked to today. Idle cash is included on purpose.

**Engineering note.** Must include cash — cash drag is a real outcome of the member's decisions and excluding it would flatter the portfolio. Mark at the same timestamp used for the S&P 500 Alternative so the two are comparable. No currency symbol (CAD implied); tabular numerals.

### 4.4 Row 2 — S&P 500 Alternative (`56,236.00`)

**Rationale.** The counterfactual: "what your money would be worth today if you had simply bought the index with the *same* deposits, on the *same* dates." This is the heart of the feature — a **wealth counterfactual**, not an index return. It already accounts for deposit timing, so it's apples-to-apples with the member's portfolio.

**Calculation.** `Σ (MirrorLot.units × VFV_total_return_close(today))` over all live mirror lots. Each member cash flow created a mirror lot at that date's VFV close (§6).

**Engineering note.** Use a **total-return** VFV series (dividends reinvested, ETF fees reflected) — raw price closes materially understate the benchmark and would break trust. Mark to the same timestamp as Portfolio Value. Label is always "S&P 500 Alternative" — never surface "VFV" here.

### 4.5 Row 3 — Difference (`+2,184.18` / `+3.88%`)

**Rationale.** The conclusion, and the only row a hurried member needs. They should grasp "I have $2,184 more wealth than the index would have given me" with zero interpretation. Dollars come first (tangible), percent second (scale). The hairline above the row marks it visually as the verdict.

**Calculation.** `$ = Portfolio Value − S&P 500 Alternative`. `% = Difference $ ÷ S&P 500 Alternative`. (Worked: `58,420.18 − 56,236.00 = +2,184.18`; `2,184.18 ÷ 56,236.00 = +3.88%`.)

**Engineering note.** Always render the sign (`+`/`−`). **Monochrome only — no red/green** (II doctrine: performance is a fact, not a celebration). The `%` denominator is the S&P 500 Alternative, not contributions or portfolio value — keep this consistent in negative states too (§12.3).

### 4.6 Chevron `›`

**Rationale.** The single affordance cue. II design uses no buttons or icons for navigation — the chevron quietly signals the whole card is tappable and leads to the trust-building detail.

**Engineering note.** The entire card is one `<a href>`; no per-row click handlers. `:active` → opacity 0.5, 80ms.

### 4.7 Removed — simple rate of return on the Value block

**Rationale.** This is the spec's central deletion. Simple rate of return "appears useful but answers the wrong question," and becomes outright misleading under withdrawals, partial liquidations, and capital recycling. Removing it forces the benchmark card to carry the outcome narrative, instead of a standalone number the member can misread as success.

**Calculation.** N/A — deletion.

**Engineering note.** Remove the dollar gain **and** the percent (`All time +2,353.46 (+5.3%)`), leaving only the Value figure. **The Core (Managed) Value block keeps its gain line** — managed product, out of scope. Do not touch Core.

---

## 5. Screen 2 — Performance detail page (element by element)

Reached by tapping the card. Its job is to **establish trust in the calculation**, not to add advanced reporting. Three sections only.

### 5.1 Header (back arrow + Exit)

**Rationale.** Standard II detail-page chrome. Exit always returns to the dashboard regardless of history, so the member never feels trapped in a detail view.

**Engineering note.** Back arrow → `history.back()`; "Exit" → hardcoded `Unified Dashboard v2.html`.

### 5.2 Title block — `S&P 500 Benchmark` / `All Accounts`

**Rationale.** Mirrors the card's name so the member knows they tapped through to the same thing. Reinforces "Benchmark," not "Performance."

**Engineering note.** Account suffix bound to the same scope as the card (§4.2).

### 5.3 Hero — `Tracked since {date}` / `{N} months`

**Rationale.** Orientation: over what window does this comparison hold? It sets honest context — a two-month comparison is noise; a multi-year one is meaningful. Note the MVP has **no "preliminary / 5-year signal" gating** — that was v1 doctrine and is intentionally dropped. The hero is purely informational here.

**Calculation.** `inception = earliest CashFlow.occurred_on`. `tracked_months = floor((today − inception) / 30.4375)`. Date displayed `MMM D, YYYY`.

**Engineering note.** Derive inception from the first external cash flow, not account-open date (an account can exist before any money moves).

### 5.4 Section 1 — Summary

Repeats the card's three numbers as the page's lede.

```
Portfolio Value            58,420.18
S&P 500 Alternative        56,236.00
Difference        +2,184.18  +3.88%
```

**Rationale.** The detail page's purpose is trust, not new metrics. Re-stating the exact card numbers first anchors the member ("same answer I just saw") before the page shows how it was built. Repetition here is deliberate, not redundant.

**Calculation.** Identical to §4.3–§4.5. Single source of truth — these must equal the card to the cent.

**Engineering note.** Bind Summary and the card to the same computed object; never recompute independently (drift between them destroys trust).

### 5.5 Section 2 — Contributions & Growth

```
Net Contributions          50,000.00
Portfolio Growth           +8,420.18
S&P 500 Growth             +6,236.00
```

**Rationale.** This is the "show your work" section. It separates **capital the member put in** from **wealth each side generated**, so a large balance built mostly from large deposits isn't mistaken for skill. It lets the member see, at a glance: how much I invested, how much my portfolio grew, how much the index would have grown on the same money.

**Calculation.**
- **Net Contributions** = `Σ deposits + Σ transfer_in − Σ withdrawals − Σ transfer_out` (transfers booked at market value on the event date).
- **Portfolio Growth** = `Portfolio Value − Net Contributions` → `58,420.18 − 50,000.00 = +8,420.18`.
- **S&P 500 Growth** = `S&P 500 Alternative − Net Contributions` → `56,236.00 − 50,000.00 = +6,236.00`.

**Engineering note.** Cross-check: `Portfolio Growth − S&P 500 Growth` must equal the Difference $ on the card (`8,420.18 − 6,236.00 = 2,184.18`). Use this as an invariant in tests. Growth rows show the sign; Net Contributions does not.

### 5.6 Section 3 — Methodology *(collapsed, tap to expand)*

> Benchmark: Vanguard S&P 500 ETF (VFV), total return. Each deposit is mirrored into VFV at that date's close; withdrawals are mirrored out; in-kind transfers are mirrored at market value. Dividends are reinvested and ETF fees reflected. The mirrored balance becomes your S&P 500 Alternative.

**Rationale.** Methodology must be **available but secondary**: it builds trust for the skeptical member without letting mechanics upstage the conclusion. Collapsed by default. It explicitly calls out dividends / total return because excluding them would understate the benchmark — the one thing most likely to make a sophisticated member distrust the number.

**Calculation.** Describes §6–§7 in plain language; no new math.

**Engineering note.** Use the existing tappable-label pattern: dotted underline (`--c-800`), `.open` state on tap, sibling `.info-panel[hidden]` toggled. **No icon.** This is the only place "VFV" is allowed to appear in user-facing copy.

---

## 6. Data model

The mirror tracks **external cash flows only** (deposits, withdrawals, transfers). Internal buys/sells inside the account do **not** trigger a mirror event.

```
CashFlow {
  id: uuid
  account_id: uuid
  type: enum            # deposit | withdrawal | transfer_in | transfer_out
  amount_cad: decimal   # transfers booked at market value at the event date
  occurred_on: date
  mirror_id: uuid       # FK → MirrorLot, created on every CashFlow insert
}

MirrorLot {             # the VFV side of one cash flow
  id: uuid
  cash_flow_id: uuid
  side: enum            # buy | sell
  notional_cad: decimal # equals the cash flow amount
  vfv_close: decimal    # VFV total-return close on occurred_on
  units: decimal        # notional_cad / vfv_close (fractional allowed)
  occurred_on: date
}

DailySnapshot {         # see §8 — start collecting immediately
  account_id: uuid
  date: date
  portfolio_value_cad: decimal
  cash_cad: decimal
  positions_value_cad: decimal
}
```

`'VFV'` is implementation detail — never surface it as a row label. It appears only inside Methodology body copy.

---

## 7. Computed values (consolidated)

| Value | Formula | Notes |
|---|---|---|
| Net Contributions | Σ deposits + Σ transfer_in − Σ withdrawals − Σ transfer_out | Transfers at market value on event date. |
| Portfolio Value | positions_value_cad + cash_cad (today's mark) | Actual account, incl. idle cash. |
| S&P 500 Alternative | Σ MirrorLot.units × VFV_total_return_close(today) | Mark the live mirror to today. |
| Portfolio Growth | Portfolio Value − Net Contributions | |
| S&P 500 Growth | S&P 500 Alternative − Net Contributions | |
| **Difference ($)** | **Portfolio Value − S&P 500 Alternative** | Equivalently Portfolio Growth − S&P 500 Growth. **Primary KPI.** |
| **Difference (%)** | **Difference ($) ÷ S&P 500 Alternative** | Denominator is the S&P Alternative, not contributions or portfolio. |

### Tie-out (prototype example)

```
Net Contributions      50,000.00
Portfolio Value        58,420.18   →  Portfolio Growth  +8,420.18
S&P 500 Alternative    56,236.00   →  S&P 500 Growth    +6,236.00
Difference $           58,420.18 − 56,236.00 = +2,184.18
Difference %           2,184.18 ÷ 56,236.00 = +3.88%
Invariant              Portfolio Growth − S&P 500 Growth = Difference $
```

All card and detail numbers must reconcile to these formulas exactly.

---

## 8. Engineering requirement — start now

**Begin writing `DailySnapshot` rows immediately, before this ships.** Minimum fields: account_id, date, portfolio_value_cad, cash_cad, positions_value_cad.

The MVP itself only needs current marks, but Phases 4–5 (XIRR, TWR), attribution, and drawdowns all require a daily history. **Historical data not captured today cannot be reconstructed later.** This is the one backend task that cannot wait for the later phases.

---

## 9. States, edge cases & interactions

### Interactions
| Element | Behavior |
|---|---|
| Dashboard card (whole `<a>`) | Navigate to `Performance Dashboard.html`. `:active` → opacity 0.5, 80ms. |
| Methodology label | Toggle inline info panel. Label gets `.open` (text → white, underline → c-700). No icon. |
| Header back / Exit | Return to dashboard. |

### States & edge cases
- **Underperformance (negative difference):** render `−$X` and `−Y%`. **No red/green** — performance numbers are monochrome (doctrine §color). Sign alone communicates direction.
- **Withdrawals / transfers:** mirror sells/buys at the event-date VFV close; Net Contributions adjusts accordingly. Confirms the comparison stays honest under capital recycling.
- **Idle cash:** Portfolio Value includes cash; the mirror is fully invested in VFV. This is intentional (cash drag is a real outcome).
- **Insufficient history (new account, no snapshots / no VFV close on event date):** define an empty/early state — proposal: hide the card until at least one full cash flow has a mirror lot. *(Open question, §12.)*
- **Loading:** numbers fade in with the existing dashboard stagger (§10). No separate skeleton specified for the card — confirm if needed.

### Copy rules (doctrine)
- Row labels are fixed: `Portfolio Value`, `S&P 500 Alternative`, `Difference`, `Net Contributions`, `Portfolio Growth`, `S&P 500 Growth`.
- Never display `VFV` outside the Methodology body.
- No alpha / bps / annualized / TWR / MWR anywhere in the MVP.

---

## 10. Design tokens

```css
--c-black:  #000000   /* page background */
--c-900:    #232627   /* hairline dividers, the .diff top border */
--c-800:    #565B5E   /* dotted underline on tappable Methodology label */
--c-700:    #929292   /* row labels, muted % on Difference, methodology body */
--c-400:    #C7C7C7   /* card title / section labels */
--c-white:  #FFFFFF   /* values */
```

- **Type scale:** 11 (hero eyebrow), 13 (row key / muted %), 14–15 (row value / section label).
- **Font:** Inter, weight 400 only. Tabular numerals on every numeric span (`font-feature-settings: 'lnum' 1, 'tnum' 1`).
- **Container:** mobile-first, `max-width: 393px`; 13.5px side gutter; single column.
- **Card padding:** 16px vertical, top+bottom hairline. Section gap 64px on detail page.
- **Animation:** 700ms ease-out fade-in + translateY(4px)→0, staggered by section; the Active section (and its card) inherit `.mt-active` delay. Disabled under `prefers-reduced-motion: reduce`.
- **Color exception:** no green/red on performance numbers — ever.

---

## 11. Out of scope (roadmap, do not build now)

| Phase | Feature | Why deferred |
|---|---|---|
| 2 | Position-level benchmark (per-holding vs S&P during holding period) | Highest-leverage *after* portfolio benchmark; moves from outcomes to decisions. |
| 3 | Winners & losers vs benchmark (attribution) | Pattern recognition; needs Phase 2 first. |
| 4 | Money-weighted return (XIRR) | Becomes primary return metric later; requires daily snapshots (§8). |
| 5 | Time-weighted return | Sophisticated/institutional; not needed for capital-allocation decisions. |

Also removed from the prototype and **not** in MVP: equity curve chart, per-deposit external cash-flow table.

---

## 12. Open questions for engineering

1. **VFV total-return source** — which feed provides dividend-reinvested, fee-adjusted VFV closes back to account inception? Raw price closes must not be used (would understate the benchmark).
2. **Transfer valuation** — in-kind transfers mirrored at market value on the event date; confirm the pricing source for the transferred securities.
3. **Difference % denominator** — spec uses ÷ S&P 500 Alternative. Confirm this is the intended base across all states (incl. negative).
4. **Account context** — `· All Accounts` aggregates; confirm behavior when a single account is selected (recompute mirror per account, or sum of per-account mirrors? results differ with different cash-flow timing).
5. **Early / empty state** — card hidden until first mirror lot exists, or shown with placeholder? (See §9.)
6. **Rounding** — display 2 decimals; confirm internal precision and rounding rule for units and marks.

---

## 13. Implementation checklist

- [ ] Replace the dashboard `BenchmarkCard` content: `Portfolio Value` / `S&P 500 Alternative` / `Difference ($ + %)`; remove `Your Portfolio` / `S&P 500` / `Alpha`.
- [ ] Set card title to `S&P 500 Benchmark · All Accounts`; keep whole card as one link with chevron.
- [ ] Remove the all-time simple return line on the Active (Self-directed) Value block. Leave Core (Managed) untouched.
- [ ] Build the detail page: Summary → Contributions & Growth → Methodology (collapsed). Set page title to `S&P 500 Benchmark`.
- [ ] Implement `CashFlow` → `MirrorLot` creation on every external cash flow; mirror withdrawals/transfers.
- [ ] Implement the §7 computed values; unit-test against the tie-out example and the growth invariant.
- [ ] **Stand up `DailySnapshot` writes now (§8).**
- [ ] Wire Methodology tappable info panel (dotted-underline pattern, no icon).
- [ ] QA: no `VFV` in user-facing labels (only in Methodology body); no green/red on performance numbers; negative difference renders with sign only.
- [ ] QA: all displayed numbers reconcile to §7 formulas; card == Summary to the cent.

---

*Prototype source of truth: `v3/`. Numbers in this doc are the prototype's worked example and reconcile end-to-end.*
