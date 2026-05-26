# Stock Page — Developer Handoff

**Audience:** Engineering team building the II Stock Page experience.
**Status:** MVP. AI-driven monitoring and longitudinal calibration are post-MVP.
**Last updated:** May 22, 2026

---

## 1. Page Map

| Page | File | Purpose |
|---|---|---|
| **Stock Page — Returning user** | `Stock Page v6d.html` | Main page. User holds position, has sealed memo. Default state. |
| **Stock Page — First-time user** | `Stock Page First.html` | No position, no memo yet. Entry to memo creation flow. |
| **The Memo (Full)** | `ATZ Memo.html` | Full memo detail page. Drill-in from Stock Page memo footer. |
| **The Memo — Lifecycle Variants** | `ATZ Memo Variants.html` | Reference: all 5 memo states side-by-side (Draft / Live / Triggered / Stale / Closed). |
| **AI Research & Analysis** | `ATZ AI Research v2.html` | 11-step research protocol page (pre-memo). 4 phases. Each step: prompt + output hint + Copy Prompt. |
| **Fiscal AI · ATZ** | `ATZ Fiscal.html` | Dedicated workspace landing — Live Fundamentals, Valuation, Filings, Transcripts, Peer Comps. Bloomberg-style density. |
| **Notes** | `ATZ Notes.html` | User-authored observations on this ticker. |
| **Performance Detail** | `ATZ Performance Detail.html` | Performance drill-in (annualized, equity curve, yearly). |
| **Market / News / History** | `ATZ Market.html` / `News.html` / `History.html` | Secondary source pages. |
| **Pressure Test Drawer** | _(planned)_ | Bottom drawer at Memo Review step. 4 prompt options. Copy Prompt + Memo bundle. Optional fail-safe before Seal. |

---

## 2. Stock Page (v6d) — Section by Section

The Stock Page is a single scrollable view. Top to bottom:

### 2.1 Header (`.header`)
**Elements:** Back arrow (←) · Star (☆) · Exit
**Behavior:** Standard nav. Back returns to dashboard. Star toggles watchlist (persistent). Exit closes view.
**Height:** 71px, hairline border-bottom.

### 2.2 Compliance Strip (`.compliance-strip`)
**Content:** `Self-Authored · No Suitability Review · Not Advice`
**Style:** 9px, c-800, left-aligned, persistent across every memo/stock view.
**Purpose:** Regulatory disclosure as system metadata, not consumer warning. Compliance defense delivered as institutional aesthetic.
**Behavior:** Static. No interaction. Renders on every page in the memo/stock family.

### 2.3 Title Block (`.title-block`)
**Content:**
- Line 1: `{Company Name} · {Ticker}` (e.g. `Aritzia Inc · ATZ`)
- Line 2: `Last Price {price} {currency} · {return}% vs entry`

**Data:**
- `Company Name`, `Ticker` — from securities master.
- `price` — latest market quote, refreshed on view load.
- `return %` — `(currentPrice - entryPrice) / entryPrice × 100`, rounded to 1 decimal. Positive shown without `+`, negative with `−`.
- `vs entry` label is fixed text.

### 2.4 Alert Mirror (`.oq-list`)
**Visibility:** Only when a triggering event exists. Dismissible.
**Content example:** `● Q4 earnings posted 14d ago` + `Open Memo ›`
**Trigger sources (MVP):**
- Earnings posted within last 30 days
- Position held for one full quarter since last review
- Manual trigger from dashboard

**Dot color logic:**
| Severity | Color | Trigger |
|---|---|---|
| `warning` | `#FDAD00` | Re-underwrite due, earnings posted |
| `urgent` | `#FF3533` | Reserved for true emergencies (post-MVP) |
| `review` | `#FBC308` | Reserved (post-MVP) |

**Dismiss behavior:** Click `×` → fade out 220ms → remove from DOM. Persistent across reload via local state (post-MVP: server-side dismissal tracking).
**Note:** Even when dismissed, the persistent Re-underwrite CTA remains in the memo footer.

### 2.5 Memo Block (`.memo-block`) — Hero Unit

The only boxed section. Designed as a screenshot-shareable artifact.

#### 2.5.1 Status Bar (`.memo-status-bar`)
**Content:** `The Memo · {Classify} · ● {state}` (left) + `v{version}` (right)
**Example:** `The Memo · Compounder · ● Live` + `v3`
**Fields:**
- `Classify` — one of: `Compounder` / `Emerging Compounder` / `Situational Mispricing` / `Speculative`. Set during memo creation step 1/9.
- `state` — see [Section 4 · Memo Lifecycle](#4-memo-lifecycle-state-machine).
- `version` — integer. Increments when memo is edited and re-locked.

#### 2.5.2 Thesis (01)
**Content:** Prose. Single paragraph in v6d preview (full memo splits into "Why wrong" + "Why now").
**Source:** Memo creation step 3/9.
**Max length:** No hard cap, but truncate after ~200 chars in preview if needed (full memo shows complete text).

#### 2.5.3 Kill Criteria (02)
**Content:** Numbered list of kill conditions with leading `·` bullet, plus a Response line.
**Source:** Memo creation step 4/9. User defines kill conditions during memo creation.
**Schema:**
```json
{
  "killCriteria": [
    "Same-store sales go negative for two consecutive quarters",
    "US expansion stalls below 8 new stores per year",
    "Operating margin contracts below 12% TTM"
  ],
  "killAction": "Exit position",
  "killResponse": "Exit on trigger, not on narrative. Exit position."
}
```
**Max conditions:** 5 (post-MVP). MVP shows all provided.
**MVP note:** No automated monitoring. Trigger detection is manual / user-initiated.

#### 2.5.4 Metric Grid — IV / MoS / Probability
**Layout:** 3 equal columns, hairline above + below.

| Metric | Source | Calculation |
|---|---|---|
| **Intrinsic Value** | Memo step 5/9 | User-set per-share value. Display: `{value} CAD/sh`. |
| **Margin of Safety** | Derived | `(IV − currentPrice) / IV × 100`. Display as integer %. Round down (conservative). |
| **Thesis Probability** | Memo step 6/9 | User-set 10–90% in 10% increments. |

**Assumption trails (small text below each metric):**
- IV: `{method} · {key params}` e.g. `SOTP · 10% WACC / 12% CAGR`
- MoS: `Buffer to IV / {raw}% raw` (raw = unrounded calculation)
- Probability: `Self-set / {horizon} horizon`

These transform numbers from "delivered verdicts" into "worked calculations" — compliance + epistemic honesty.

#### 2.5.5 Footer (`.memo-footer`)
**Content:** `Reviewed {date} · {Nd ago}` (left) + `→ Re-underwrite` (right)
**`Reviewed`:** Date of last memo lock or re-confirmation. `Nd ago` is delta from today.
**`Re-underwrite`:** Always present. Click → Full Memo page (`ATZ Memo.html`) in edit mode.

---

### 2.6 Position (`.pos-section`)
**Pattern:** Label-left, value-right rows.

| Row | Calculation |
|---|---|
| **Market Value** | `shares × currentPrice` |
| **Portfolio Weight** | `{entered %} → {current %}` — entered is from initial buy, current is `marketValue / portfolioValue × 100`. Both shown to expose sizing discipline. |
| **Unrealized P/L** | `(currentPrice − avgEntryPrice) × shares` |
| **Held** | `{years}y {months}m` from initial buy date. |

**Drill-in:** `View Position Detail ›` → `Holdings.html` (in `/Holdings_Position/`).

### 2.7 Performance vs S&P 500 (`.perf-vs-sp`)
**Time scope:** Cumulative · matches `Held` duration.

| Row | Calculation |
|---|---|
| **ATZ** (or ticker) | Total return % since entry |
| **S&P 500** | SPY total return % over same period |
| **Alpha** | `ATZ return − SPY return`, displayed in percentage points (`pp`). White color emphasis. |

**Doctrine:** Always show vs SPY. Underperformance must be visible — humility is the brand.
**Drill-in:** `View Performance Detail ›` → `ATZ Performance Detail.html`.

### 2.8 Fiscal AI (Primary Source)
**Container:** Dark filled box (`background: #0A0A0A`), hairline border. Distinct from other nav rows.
**Purpose:** Elevated "primary source" — Fiscal AI is a partner workspace for financial data (filings, transcripts, comps).
**Behavior:** Opens external Fiscal AI workspace (deep-linked to the ticker).

### 2.9 More Sources (`.nav-rows`)
**Rows:** Market · News · History — hairline-separated.
**Each row:** Title + meta + chevron (›).
**Targets:** `ATZ Market.html` / `ATZ News.html` / `ATZ History.html`.

### 2.10 Capital Decision CTA (`.capital-decision`)
**Position:** Fixed at bottom with gradient fade.
**Label:** `→ Capital Decision`
**Behavior:** Opens bottom sheet for Buy/Sell/Hold action commitment.
**Doctrine note:** This is the only commit action that physically moves capital. All other CTAs (Re-underwrite, Open Memo) are navigational or revision actions.

---

## 3. The Memo (Full) — `ATZ Memo.html`

Drill-in from Stock Page memo footer. The complete memo document.

### Sections (matches 9-step creation flow)
| # | Section | Source | Notes |
|---|---|---|---|
| 01 | Classify | step 1/9 | Compounder / Emerging / Situational / Speculative |
| 02 | Size | step 2/9 | Core / High Conviction / Starter / Speculative |
| 03 | Thesis | step 3/9 | Two sub-fields: "Why the market is wrong" + "Why now" |
| 04 | Kill Criteria | step 4/9 | Conditions list + Response + Floor |
| 05 | Intrinsic Value | step 5/9 | Fair value + Method + Margin of Safety (embedded) |
| 06 | Exceptional Compounding | step 6/9 | Hurdle + Horizon + Calibration |
| 07 | Source | step 7/9 | Where the idea came from |
| 08 | Note | step 8/9 | User free-text reflection |

Step 9/9 = Review screen (commit / hold-to-seal).

### Memo data schema (proposed)
```json
{
  "memoId": "memo_014",
  "ticker": "ATZ",
  "version": 3,
  "state": "live",
  "createdAt": "2024-02-14T...",
  "lockedAt": "2026-04-12T...",
  "lastReviewedAt": "2026-04-12T...",

  "classify": "compounder",
  "size": "starter",

  "thesis": {
    "whyWrong": "Aritzia is undervalued by ~40% on a SOTP basis...",
    "whyNow": "Q4 earnings confirmed US comp growth at 32%..."
  },
  "killLine": {
    "conditions": ["...", "...", "..."],
    "response": "Exit on trigger, not on narrative. Exit position.",
    "floor": "Brand equity remains tier-one..."
  },
  "valuation": {
    "intrinsicValue": 120.00,
    "currency": "CAD",
    "method": "SOTP",
    "methodDetail": "22× FY26 earnings on retail + 15× online, blended, 12% execution risk discount",
    "marginOfSafety": { "atEntry": 28, "today": 25 }
  },
  "compounding": {
    "hurdle": 20,
    "horizonYears": 3,
    "calibration": 70
  },
  "source": "own-analysis",
  "note": "..."
}
```

---

## 4. Memo Lifecycle State Machine

Memo states flow: **Draft → Live → (Triggered ↔ Live) → Closed**. Stale can fire from Live.

| State | Dot | Color | Pulse | Meaning |
|---|---|---|---|---|
| **Draft** | `●` | `c-800` (dim) | none | In progress. Not locked. Kill criteria not armed. |
| **Live** | `●` | `c-live` `#30D158` (green) | gentle (1 ↔ 0.6 opacity, 2.4s) | Default. Locked memo. Currently held position. |
| **Triggered** | `●` | `c-warning` `#FDAD00` (amber) | dramatic (1 ↔ 0.32 opacity, 2.4s) | Kill condition fired. User must review. |
| **Stale** | `●` | `c-800` (dim) | none | Not reviewed within review window (e.g., 6+ months). |
| **Closed** | `●` | `c-800` (dim) | none | Position exited. Archived. |

**Transitions:**
- `Draft → Live` — user locks the memo (Hold to seal)
- `Live → Triggered` — system detects kill condition fired (MVP: manual flag; post-MVP: automated)
- `Triggered → Live` — user re-confirms thesis (creates new version)
- `Triggered → Closed` — user exits position
- `Live → Stale` — review window expires
- `Stale → Live` — user re-reviews
- `Live → Closed` — user exits position without kill trigger

**Visual reference:** See `ATZ Memo Variants.html` for all 5 states side-by-side.

---

## 5. Design System Tokens

### Color
```css
--c-black:    #000000;  /* Page background */
--c-1000:     #1C1C1C;  /* Hairlines inside boxes */
--c-900:      #232627;  /* Hairlines outside boxes, primary borders */
--c-800:      #565B5E;  /* Compliance text, assumption trails, dim labels */
--c-700:      #929292;  /* Secondary labels (Position keys, Performance keys) */
--c-400:      #C7C7C7;  /* Body text, values */
--c-white:    #FFFFFF;  /* Numbers, emphasis */

/* Severity (use sparingly — only for active signals) */
--c-warning:  #FDAD00;  /* Triggered, Q4 earnings alert */
--c-urgent:   #FF3533;  /* Reserved — true emergencies */
--c-review:   #FBC308;  /* Reserved */

/* Lifecycle (NEW category) */
--c-live:     #30D158;  /* Live state — actively monitored thesis */
```

### Typography
- Family: `Inter`, weights 300 / 400 / 500
- Body: 13–15px, letter-spacing `-0.02em`
- Small labels: 10–11px, letter-spacing `-0.02em`
- Tracked metadata (assumption trails, K-num): use `+0.02em` letter-spacing
- All numbers use `font-feature-settings: 'tnum' 1` for tabular alignment

### Spacing
- Section gap: **48px** (doctrine standard)
- Inside-box padding: **16px** all sides
- Section header padding-bottom: **14px** + hairline
- Between hairline-divided elements: **16px** top, 16px bottom

### Borders
- All borders: **0.5px**
- Inside box: `var(--c-1000)`
- Outside box / between sections: `var(--c-900)`
- No `border-radius` (except dots — 50%)

### Symbol Grammar
| Symbol | Use |
|---|---|
| `›` | Navigation drill-in (View Memo, View Position Detail) |
| `→` | Commit action (Capital Decision, Re-underwrite, File Memo) |
| `·` | Separator (between labels, between metadata) |

---

## 6. Reusable Components

### Compliance Strip
```html
<div class="compliance-strip" aria-label="Disclosure">
  Self-Authored · No Suitability Review · Not Advice
</div>
```
Persistent across all memo/stock pages.

### Status Bar (memo header)
```html
<div class="memo-status-bar">
  <span class="memo-status-left">
    <span>The Memo · Compounder</span>
    <span class="memo-state live">
      <span class="state-dot"></span>Live
    </span>
  </span>
  <span class="memo-status-right">v3</span>
</div>
```

### Kill List
```html
<ul class="kill-list">
  <li><span class="k-num">·</span>{condition 1}</li>
  <li><span class="k-num">·</span>{condition 2}</li>
  <li><span class="k-num">·</span>{condition 3}</li>
</ul>
<p class="mc-sub"><span class="kc-label">Response:</span> {response text}</p>
```

### Metric Cell (3-cell grid)
```html
<div class="memo-metric">
  <span class="metric-label">Intrinsic Value</span>
  <span class="metric-value">120.00<span class="metric-unit">CAD/sh</span></span>
  <span class="metric-trail">SOTP · 10% WACC<br>12% CAGR</span>
</div>
```
**Trail rule:** max 2 lines per cell. Manual `<br>` at semantic boundary. Each line ≤ ~25 chars.

### Section Pattern (Position, Performance)
```html
<section class="section">
  <div class="section-header">
    <span class="section-title">{Section Name}</span>
    <span class="section-meta">{optional meta}</span>
  </div>
  <!-- row data -->
  <a href="..." class="view-link">View {detail} <span class="chev">›</span></a>
</section>
```

---

## 7. Animations

| Element | Animation | Duration | Easing |
|---|---|---|---|
| **Live dot pulse** | `opacity: 1 ↔ 0.6` | 2.4s | `cubic-bezier(0.45, 0, 0.55, 1)` |
| **Triggered dot pulse** | `opacity: 1 ↔ 0.32` | 2.4s | same |
| **Alert dismiss** | `opacity → 0` + collapse | 220ms | `ease-out` |
| **Tap feedback** | `opacity: 1 → 0.5` | 80ms | `ease` |

**All animations respect `prefers-reduced-motion: reduce`** — disable on user preference.

---

## 8. MVP Scope & Out-of-Scope

### In MVP
- All UI shown in `Stock Page v6d.html`
- Memo creation 9-step flow
- States: Draft, Live, Closed
- Manual Re-underwrite trigger
- Alert mirror (event-based, manual)

### Post-MVP (do not build now)
- Automated kill condition monitoring
- Triggered / Stale state auto-detection
- Historical accuracy display (Source step calibration data)
- AI-generated insights in Research section
- Per-source track record (Edge Analysis)

---

## 9. Edge Cases

| Scenario | Behavior |
|---|---|
| **No memo yet (first-time user)** | Show `Stock Page First.html` layout. Memo box absent. Draft Memo CTA in About section. |
| **Position closed** | State badge `● Closed` (dim). Capital Decision CTA hidden or replaced. Memo remains read-only. |
| **No active alert** | Hide `.oq-list` entirely. Memo footer Re-underwrite still present. |
| **Long thesis text (>200 chars in preview)** | Truncate with line clamp 3. Full text accessible via memo footer. |
| **MoS negative (Price > IV)** | Display `−{value}%`. Consider red accent — but doctrine reserves color, decide with design. |
| **Memo locked but Alert active** | Status badge stays `Live`. Alert mirror at top signals review. Both visible — they serve different roles. |

---

## 10. Loading & Error States

### Loading
While the Stock Page is fetching data, render the **layout shell** (header, compliance strip, title block, section headers) but show dim placeholders for dynamic values:

| Element | Loading state |
|---|---|
| `Last Price` | `— CAD` (em-dash, c-800) |
| `vs entry %` | `—% vs entry` (em-dash, c-800) |
| `Memo state badge` | Hide dot + label until loaded |
| `IV / MoS / Probability values` | `—` (em-dash, c-800) |
| `Position rows (values)` | `—` (em-dash, c-800) |
| `Performance rows` | `—` (em-dash, c-800) |
| `Alert mirror` | Hide entirely until determined |

**No skeleton loaders or shimmer animations.** Em-dash placeholders match II doctrine — the layout never moves, only values populate.

### Error
For API failures, replace dynamic values with `—` and surface a compact error indicator inside the affected section:

```html
<span class="data-val" style="color: var(--c-800);">—</span>
<span class="error-note">Data unavailable. <a>Retry</a></span>
```

Style `.error-note` as 11px c-700 with the retry link in c-400. No red banners — failures are stated, not screamed.

**Critical failure (entire page can't load):**
- Show header + compliance strip
- Single message in main area: `Unable to load this stock. Try again ›`
- Memo box and other sections hidden

---

## 11. Mock Data — Full Stock Page Payload

Example JSON the Stock Page can render against (matches the ATZ mockup):

```json
{
  "ticker": "ATZ",
  "company": "Aritzia Inc",
  "currency": "CAD",
  "lastPrice": 87.60,
  "asOf": "2026-05-22T16:00:00-04:00",

  "position": {
    "shares": 216,
    "avgEntryPrice": 61.43,
    "entryDate": "2023-02-14",
    "marketValue": 18921.60,
    "portfolioValueAtEntry": 6.1,
    "portfolioWeightCurrent": 12.2,
    "unrealizedPL": 5652.72,
    "unrealizedPLPct": 42.6,
    "heldDuration": { "years": 3, "months": 2 }
  },

  "performance": {
    "timeScope": "cumulative",
    "tickerReturn": 42.6,
    "benchmark": { "name": "S&P 500", "ticker": "SPY", "return": 14.2 },
    "alpha": 28.4
  },

  "memo": {
    "memoId": "memo_014",
    "version": 3,
    "state": "live",
    "classify": "compounder",
    "size": "starter",
    "createdAt": "2024-02-14T...",
    "lockedAt": "2026-04-12T...",
    "lastReviewedAt": "2026-04-12T...",
    "priorVersionCount": 2,

    "thesis": {
      "whyWrong": "Aritzia is undervalued by ~40% on a SOTP basis. Brand momentum, US store rollout, and operating leverage drive multi-year compounding.",
      "whyNow": "Q4 earnings confirmed US comp growth at 32%, store rollout pace at 18 net-new locations YoY, and gross margin expansion of 220bps."
    },

    "killLine": {
      "conditions": [
        "Same-store sales go negative for two consecutive quarters",
        "US expansion stalls below 8 new stores per year",
        "Operating margin contracts below 12% TTM"
      ],
      "response": "Exit on trigger, not on narrative. Exit position.",
      "floor": "Brand equity remains tier-one even in same-store softening; US store base profitable at current trajectory; cash-rich balance sheet ($142M) supports re-allocation without forced sale."
    },

    "valuation": {
      "intrinsicValue": 120.00,
      "currency": "CAD",
      "unit": "per_share",
      "method": "SOTP",
      "methodParams": ["10% WACC", "12% CAGR"],
      "methodDetail": "22× FY26 earnings on retail + 15× online, blended, 12% execution risk discount",
      "marginOfSafety": {
        "current": 25,
        "raw": 27,
        "atEntry": 28,
        "rationale": "Buffer to IV"
      }
    },

    "compounding": {
      "hurdle": 20,
      "horizonYears": 3,
      "calibration": 70,
      "calibrationSource": "self-set"
    },

    "source": "own-analysis",
    "note": "..."
  },

  "alerts": [
    {
      "id": "alert_q4_2026",
      "severity": "warning",
      "event": "Q4 earnings posted",
      "daysAgo": 14,
      "action": { "label": "Open Memo", "target": "memo" },
      "dismissable": true
    }
  ]
}
```

### Field-to-UI Mapping

| UI element | JSON path |
|---|---|
| Title block company + ticker | `company`, `ticker` |
| Last Price | `lastPrice`, `currency` |
| vs entry % | `position.unrealizedPLPct` |
| Alert mirror | `alerts[].severity` + `alerts[].event` + `alerts[].daysAgo` |
| Memo status bar | `memo.classify`, `memo.state`, `memo.version` |
| Reviewed | `memo.lastReviewedAt` (delta from now) |
| Thesis preview | `memo.thesis.whyWrong` (truncated to ~2 lines in v6d preview) |
| Kill list | `memo.killLine.conditions[]` |
| Response | `memo.killLine.response` |
| IV cell | `memo.valuation.intrinsicValue` + `memo.valuation.currency` + `methodParams` for trail |
| MoS cell | `memo.valuation.marginOfSafety.current` + `.raw` for trail |
| Probability cell | `memo.compounding.calibration` + `horizonYears` for trail |
| Position rows | `position.*` |
| Performance rows | `performance.*` |

---

## 12. Open Questions for Engineering

1. **Memo number scheme** — sequential per-user, or global? (Spec proposes per-user `memo_014` style.)
2. **Compliance copy ownership** — confirm with legal team. Current copy: `Self-Authored · No Suitability Review · Not Advice`.
3. **Review window for Stale** — proposal: 6 months from last lock/review. Confirm with product.
4. **Server-side dismissal tracking for Alert** — MVP: local only? Post-MVP: server state?
5. **Currency display** — multi-currency support timeline? Current spec assumes single ticker currency per memo.
6. **Retry behavior** — exponential backoff? User-triggered only? (Currently spec assumes user-triggered.)
7. **Stale data threshold** — how old before showing "as of {time}" indicator on price?
