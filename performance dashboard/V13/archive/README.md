# V13 archive

Superseded working files. Kept for history, not canon. Do not cite these as current.

Active files live in the V13 root: `main dashboard.html` (latest dashboard),
`positions screens.html` (performance dashboard + open/closed/detail screens),
`main-dashboard-benchmark-variants.html` (team-review page for the S&P card),
`benchmark-entry-point-variants-recovered.html` (read-only source of the four card variants).

| File | Why archived | What replaces it |
|---|---|---|
| `main-dashboard-benchmark-variants.bak.html` | Backup of the review page while it still held the A/B/C card set (chart-forward / difference-leads / minimal-fix). | `main-dashboard-benchmark-variants.html`, rebuilt 2026-09-02 around the four entry-point variants (1 Alpha Line · 2 Instrument · 3 Headline · 4 Reveal). |
| `benchmark-section-variants-recovered.html` | Earlier recovered exploration of the same benchmark section, before the chart engine was ported. | `benchmark-entry-point-variants-recovered.html` (2026-08-28 rebuild: ports the performance dashboard's own seeded chart engine and scrub machinery instead of hand-authored polylines). |
| `deposit-line-study-recovered.html` | Standalone study of how to show the deposit / cost-basis line against account value. | Resolved and shipped: the performance dashboard's main chart carries the `Deposited` line as a third series, with its value in the scrub readout (`positions screens.html`). |
| `sort-control-comparison.html` | Five options for the sort control on the positions list, a question now settled. | The shipped sort sheet on the open/closed screens in `positions screens.html`. |
| `tracked-since-comparison.html` | Threshold options for when to show the "Tracked since" inception card. | The shipped tracked-since card in `positions screens.html` (under-5-years state, with the 5-year benchmark date). |

Archived 2026-09-02.
