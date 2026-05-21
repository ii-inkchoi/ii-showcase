# II Performance Dashboard — Source Code Package

**For:** Krish / dev assigned to [IIA-2565](https://mogofintech.atlassian.net/browse/IIA-2565)
**From:** Inkyung Choi
**Date:** 2026-05-19

This is the source for the v3 prototype of the II Performance Dashboard. Use it alongside the engineering spec in the Jira ticket.

---

## ⚡ Start here: `flow.html`

**Open [`flow.html`](./flow.html) in a browser first.** It's the Figma-style overview — all 6 prototype screens laid out on one canvas with arrows showing navigation between them. Click any screen to open it full-size. This is the closest analog to opening a Figma prototype file.

## How to read this folder

The original prototypes in `/v3/*.html` are self-contained single files (inline `<style>` and `<script>`). This folder splits each one into the three standard files a developer expects, with cross-page links rewired to the new filenames:

```
source-code/
├── README.md                       ← you are here
├── flow.html                       ← interactive flow viewer (start here)
├── FLOW.md                         ← text version of the flow diagram
├── PAGE-SPECS.md                   ← per-page intent, data, and interactivity
├── TOKENS.md                       ← design tokens reference
├── tokens.css                      ← shared CSS variables (color, type, spacing)
│
├── index.html / index.css                              ← preview hub (dev-only)
├── unified-dashboard.html / .css                       ← main app screen
├── performance-dashboard.html / .css / .js             ← performance detail
├── benchmark.html / .css                               ← S&P 500 explainer
├── open-positions.html / .css / .js                    ← active positions list
├── closed-positions.html / .css / .js                  ← closed trades list
│
└── Logo.svg                        ← brand asset
```

Each `.html` references its own `.css` and (if present) `.js` by filename. Open any HTML in a browser — no build step, no server needed.

## Where to start

1. **Open `flow.html`** — see the whole prototype on one screen, click any frame to open it.
2. **Read [`PAGE-SPECS.md`](./PAGE-SPECS.md)** — every page documented (purpose, interactive elements, placeholder data, doctrine constraints).
3. **Read [`TOKENS.md`](./TOKENS.md)** + [`tokens.css`](./tokens.css) — design primitives you'll wire into your component library.
4. Open `unified-dashboard.html` directly to see the entry point, then follow the links.

## Mapping back to the original files

| Original (in `/v3`) | Source (this folder) |
|---|---|
| `index.html` | `index.html` + `index.css` |
| `Unified Dashboard.html` | `unified-dashboard.html` + `unified-dashboard.css` |
| `Performance Dashboard.html` | `performance-dashboard.html` + `performance-dashboard.css` + `performance-dashboard.js` |
| `Benchmark.html` | `benchmark.html` + `benchmark.css` |
| `Open Positions.html` | `open-positions.html` + `open-positions.css` + `open-positions.js` |
| `Closed Positions.html` | `closed-positions.html` + `closed-positions.css` + `closed-positions.js` |

Content is byte-equivalent — same DOM structure, same CSS rules, same JS. Only difference: inline blocks were extracted into separate files and cross-page links were updated to the kebab-case filenames.

## Talking to an AI tool about this code

Feed the AI the full `source-code/` folder. Good first questions:

- *"Walk me through what happens when I tap the Self-Directed performance block on the Unified Dashboard."* — uses FLOW.md + unified-dashboard.html
- *"Which values on `performance-dashboard.html` are real data vs. placeholders?"* — uses PAGE-SPECS.md + the HTML
- *"How are the design tokens organized, and which ones do I need to add to our component library?"* — uses TOKENS.md + tokens.css
- *"What's the difference between `closed-positions.html` and `closed-positions.html?filter=winners`?"* — uses PAGE-SPECS.md + closed-positions.js
- *"What doctrine constraints am I violating if I add a green/red color to gains and losses?"* — uses TOKENS.md "Brand doctrine" section

## Status of the prototype

- Visual design and information architecture: final for v3.
- Data: all hardcoded sample values. Production needs a data layer.
- Interactivity: navigation links and sort/filter/period toggles are wired. Position rows, header icons, and the RRSP account chip are not yet wired.
- Responsive: mobile-only (393px viewport). No desktop variant.
- Open questions for engineering: see §10 of the spec in IIA-2565.

## Contact

- Design intent / scope questions before kickoff → Inkyung
- During implementation when Inkyung is OOO → Dave (doctrine intent only)
