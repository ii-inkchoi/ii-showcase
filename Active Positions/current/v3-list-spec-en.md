# Active Position List — v3 Spec (EN)

**Status**: Draft sketch, pending PM / Chairman review
**Source**: builds on Chairman v2 (with Held column)
**Doctrine references**: Mogo Design Philosophy §1, §6, §8, §10, §11, §13, §14, §15
**Sketch file**: `v3-list-sketch.html` (visual reference)

---

## Goal

Move the Active Position list from a **broker view** (balance + recent change) to a **decision-system view** (commitment context). The list is an orientation surface; calibration depth lives on Stock Detail.

---

## Changes from Chairman v2

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Add **account scope label** above the page title (e.g., "RRSP", "All accounts") | Across the existing 4 screens, account scope is implicit and inconsistent (Dashboard has an RRSP picker, Active Positions list shows nothing, Stock Detail shows nothing, Holdings shows "All Accounts"). Users must guess which account they are looking at, which silently breaks trust. Surfacing the scope as a small persistent label removes that guesswork. |
| 2 | "Held" column → **"Held / Horizon"** (e.g., `1.5y / 3y`) | A raw "time held" number is automatic data. What matters in II is whether the user is honoring the *commitment they made at entry*. Showing `held / horizon` reframes the column from "elapsed time" to "progress against your own commitment" — which is the doctrine §11 friction principle and §13 memo principle made visible at the list level. When `held == horizon`, that itself is a signal for re-calibration. |
| 3 | **Remove daily price and daily ±%** from the row (Chairman v2 keeps these) | Doctrine §15 is explicit: minimize intraday noise; activity correlates negatively with returns. Daily ± in the primary list trains the user to glance daily and react. The `Value` column already reflects today's price (`market value = shares × current price`), so today's impact is implicit; an explicit % invites yesterday-vs-today comparison, which is doctrine §3 Enemy (Noise + Short-termism + Impulse). The Stock Detail / Market tab is the deliberate place for daily price inspection. **Open question #6** — confirm with Chairman before ship. |
| 4 | Move **CAD currency notation from per-row to column header** ("Value CAD") | All values in the list are auto-converted to CAD (USD positions included). Repeating "CAD" on every row adds visual weight without adding information once the user understands the column. Single notation in the column header is sufficient. Doctrine §1: "Do not explain more than is necessary." |
| 5 | **Calibration data deliberately NOT in list** — confidence pair (`stated · baseline`) lives only on Stock Detail | Calibration is the heart of the system, but the Active Position list is an orientation surface (doctrine §14 logic, applied here to the list). A paired numeric like `80%·76%` requires header-level explanation to be parsable ("which is mine?"), and that explanation itself adds visual weight that contradicts doctrine §1. The Stock Detail calibration plot — a line with a dot above/below — is visually self-explanatory and is the right home for the challenge. Concentrating calibration analysis on the surface deliberately built for it is also doctrine §15 (avoid retraining the user to glance daily at a self-evaluation metric). |
| 6 | Page title stays **right-aligned**; numeric columns stay **right-aligned**; text labels are **left-aligned** | Doctrine §8 says "no centering, ever." It does not say everything must be left. The MVP system has already converged on a coherent convention: page titles right-aligned (anchor of identification), numeric columns right-aligned (functional magnitude scanning), prose and text labels left-aligned. v3 follows that system convention. (Doctrine file §8 has been updated with an Alignment Rules subsection.) |

---

## Columns (final)

```
Ticker   Weight   Held / Hor   Value (CAD)
left     right    right        right (number top, since-entry % below)
```

**4 columns total.** No Confidence column, no Daily column, no Last Price column.

### Mock data

| Ticker  | Weight | Held / Hor | Value     | Since   |
|---------|--------|-----------|-----------|---------|
| ORIO.TO | 74%    | 1d / 3y   | 513,240   | -18.3%  |
| BWEN    | 4.9%   | 2w / 5y   | 33,600    | +10.4%  |
| FND     | 3.9%   | 3w / 5y   | 26,862    | -2.5%   |
| OSCR    | 3.0%   | 6m / 3y   | 20,580    | -4.7%   |
| RELY    | 2.0%   | 1.5y / 3y | 19,456    | +26.1%  |
| GOOG    | 0.8%   | 2y / 5y   | 1.94M     | +26.1%  |

(All values CAD; column header shows "Value CAD" once.)

---

## Visual hierarchy

- **Primary** (off-white, `#EDEDED`): Ticker, Weight, Value (number)
- **Secondary** (muted, ~`#aaa`): Held / Hor, since-entry %
- **Chrome** (subtle, ~`#444`–`#777`): scope label, column headers, "CAD" unit, dividers (`#1a1a1a`–`#222`)

Rationale: Primary = the user's identity and size of position. Secondary = commitment context (Held / Hor) and historical performance (since-entry %) — present but not competing. Chrome = orientation only. Doctrine §8 calls for subtle hierarchy where labels do not compete with body.

---

## Removed from v1/v2

- **Weight bar** (visual indicator under Weight number) — Chairman v2 already removed this; v3 keeps removed. *Rationale*: decorative, adds no information beyond the percentage itself. Doctrine §8.
- **Daily ±% / Daily price** — see change #3.
- **Last Price column** — folded out. *Rationale*: last price is intraday by nature, not decision-relevant at the list level, and the user can see it on Stock Detail. Removing it gives back column width to Held/Horizon and Value.
- **Per-row "CAD" text** — moved to column header. See change #4.

---

## Where calibration data lives (and why)

**Buy / sell flow**: stated confidence + system baseline confidence both shown to the user at decision time (per current calibration design — WIP).

**Stock Detail page**: calibration plot (line + dot showing over/under). Visually self-explanatory. This is the dedicated surface for self-audit.

**Active Position list (this spec)**: NOT shown. Deliberate restraint. The list shows only what is needed to orient and to see commitment progress (Held / Horizon).

This division is doctrine-aligned: list = orientation, Stock Detail = analysis. Same principle that separates Dashboard (orientation) from Stock Detail in Mogo Design Philosophy §14.

---

## Open questions (resolve with PM / Chairman / calibration owner)

1. **Horizon source**: is `Horizon` a value the user explicitly committed to in the buy flow (calibration), or derived from a default? If derived, the column is misleading. **This blocks v3 ship.**
2. **Held expiry behavior**: when `held >= horizon`, do we (a) keep showing `3y / 3y`, (b) flag the row for re-calibration, or (c) auto-trigger re-calibration?
3. **Sort order**: currently weight desc (matches v1/v2). Acceptable as a single non-configurable order, or do we want multiple sort modes? Adding sort controls drifts toward broker-pattern.
4. **Empty state**: what does this screen look like with 0 active positions? (Should not feel encouraging — a serious investor with 0 positions has 0 positions on purpose.)
5. **Currency disclosure detail**: should USD positions show original currency on Stock Detail (so the user can see USD-native price + value), even though list is fully CAD?
6. **Daily ±% / daily price removal — Chairman buy-in**: v2 keeps these; v3 proposes removal with the rationale in change #3 above. Confirm with Chairman before Claude Design build. If Chairman insists on keeping daily, alternative C (show daily ± only when |Δ| > 3%) is a possible compromise.
7. **Calibration column omission — Chairman / calibration-owner buy-in**: confirm that confidence pair lives only on Stock Detail, not in list. (Per change #5.)

---

## Dependencies

- **Calibration page (WIP)**: must capture at minimum `confidence` and `horizon` at buy time for `Held / Horizon` to function on this list.
- **Account scope model**: a coherent decision needed across all 4 screens (Dashboard, Active Positions, Stock Detail, Holdings) — v3 alone cannot fix this; it just stops hiding the issue.
- **USD → CAD conversion** logic in the data layer (for displaying all positions in CAD).

---

## Next steps

1. Review this spec with PM (11:00 or 16:00).
2. Confirm calibration assumptions (`confidence`, `horizon`).
3. Resolve Open Questions #1, #6, #7 with Chairman.
4. Build in **Claude Design** using II Design System.
5. Share Claude Design URL back into this folder.
6. Internal test (Stage 2) with shadow data before any external rollout.

---

## Related files

- `Mogo Design Philosophy.md` — doctrine (updated with Alignment Rules)
- `references/ICP Definition V1.md`
- `references/Figma vs Prototype Decision Rule.md`
- `v3-list-sketch.html` — visual reference (this folder)
- `v3-list-spec-ko.md` — Korean version
