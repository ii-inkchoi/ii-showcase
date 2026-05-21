# II Prototype — Showcase

Static prototype viewer for the **Intelligent Investing** app.

## Open

Start at [`Showcase.html`](./Showcase.html). It hosts every screen behind a single sidebar.

> Local: open `Showcase.html` directly in a browser.
> Hosted: GitHub Pages serves it at the repo root.

## Structure

| Path | What |
| --- | --- |
| `Showcase.html` | Sidebar + phone-frame viewer. Entry point. |
| `Stock Pages/` | Per-stock surface (First-time, Recurring · Intact / Approaching / Invalidated, Memo, Notes, Performance detail). |
| `Unified Main Dashboard/Post MVP/` | Main dashboard (Open Positions, Closed Positions, Performance Dashboard, Benchmark, Open Questions). |
| `Managed Dashboard/` | Managed-track dashboard. |
| `Active Positions/` | v3 list sketch. |
| `Under Review/` | Under Review · Delisted state. |
| `self-directed onboarding/` | 10-step onboarding flow + index. |
| `ii-bottom-sheet-system/` | Bottom-sheet component spec + demo. |
| `performance dashboard/` | Earlier performance surface explorations. |
| `landing page/` | Public-facing Vite + React landing page. Built output in `landing page/dist/`. |
| `_archive/` (per-folder) | Older versions kept for reference. |

## Sidebar grouping

Three top-level tracks:

- **Unified** — main dashboard, the shared entry to both paths.
- **Managed** — Mogo-run portfolio. Core path. Has its own dashboard.
- **Self-Directed** — drill-in from main dashboard. Stock Page family, Memo, Performance, Active Positions, Under Review, Onboarding.

Plus:

- **Components** — design-system surfaces (bottom-sheet).
- **Site** — company-facing Landing Page (desktop / responsive frame).

## Hosting on GitHub Pages

1. Push this repo to GitHub.
2. Settings → Pages → Source: `Deploy from a branch` → branch `main` → folder `/ (root)`.
3. Wait for the green checkmark. The site URL appears at the top of the Pages settings.

### Landing Page note

The landing page is built with Vite + React. `landing page/vite.config.ts` is set to `base: './'` so the bundled assets use relative paths and work under any sub-path. The committed `landing page/dist/` already has the asset references converted (`/assets/...` → `./assets/...`) so it serves correctly out of the box.

To rebuild after a code change:
```bash
cd "landing page"
npm install
npm run build
```
The new `dist/` will continue to use relative asset paths thanks to the `base: './'` config.

## File handling

- `node_modules/`, `dist/.vite/`, `.env*`, `.netlify/`, `.vercel/`, `.claude/` are gitignored.
- The largest tracked asset is the archived Figma flat snapshot inside `_archive/` (~20 MB).
- All screens use relative paths so the prototype survives moving / hosting on a sub-path.

## Doctrine

Memo as spine. Capital decision at the bottom. Buy / Sell language replaced by Initiate / Increase / Reduce. Persona × Thesis Health drives the per-stock variants.
