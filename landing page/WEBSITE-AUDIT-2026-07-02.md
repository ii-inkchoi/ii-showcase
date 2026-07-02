# II Website — Full Page Audit & Build Handoff
**Date:** 2026-07-02 · **Author:** Inkyung · **For:** Dave, Aidan, Miguel

---

## 1. Scope for July 15 (per the 07-02 team call)

**The priority pages are: Home + Self-Directed + Managed** (+ whatever compliance requires). These three must ship on the 15th.

**Our recommendation: Journal and Knowledge Hub go in AFTER launch.**
The base templates/frames for both are already built (by Inkyung) — but they are not simple static pages: article system, content + image migration from Edge, and the KH content direction is still changing. **Miguel — if wiring these up needs meaningful extra work on your side, tell us; that settles it as post-launch.** If you can genuinely fit everything including compliance review by the 15th, your call.

Everything else (Pricing, About, Manifesto, GetTheApp, Benchmark/Calibration/Memo) ships if time allows, otherwise right after launch. We would rather de-scope than miss the date.

---

## 2. Page-by-page status

| # | Page | File | Status | Remaining work | Owner | V1? |
|---|------|------|--------|----------------|-------|-----|
| 1 | Home | `index.html` | **Structure final** | Product screens → latest app designs | Inkyung | **MUST** |
| 2 | Self-Directed | `II Site V2 - Self-Directed.html` | **Structure final** | Product screens → latest | Inkyung | **MUST** |
| 3 | Managed | `II Site V2 - Managed.html` | **Structure final** | Product screens → latest | Inkyung | **MUST** |
| 4 | Pricing | `II Site V2 - Pricing.html` | **Done as-is** | Confirm non-registered account support (1 line in FAQ) | Dave/Aidan | If time |
| 5 | Manifesto | `II Site V2 - Manifesto.html` | **Done as-is** (redesigned 07-02) | — | — | If time |
| 6 | About | `II Site V2 - About.html` | Structure final | Founder titles + bios are **dummy text** (awaiting Dave/Gregory copy); CEO content later | Dave/Aidan | If time |
| 7 | Get the App | `II Site V2 - GetTheApp.html` | Structure final | Real URLs: sign-in, socials (4), Privacy, Terms | Dave/Aidan | If time |
| 8 | Journal index | `II Site V2 - Journal.html` | Done | — | — | Post-launch OK |
| 9 | Journal articles ×6 | `Journal-001 … 006` | 2 of 6 on new template | 4 articles: content + images to migrate from existing Edge posts | Team + Miguel | Post-launch OK |
| 10 | Benchmark | `II Site V2 - Benchmark.html` | Done (real product card) | ⚠️ entry links from Home were removed 07-02 — re-link if shipping | Inkyung | Post-launch OK |
| 11 | Calibration | `II Site V2 - Calibration.html` | Done (real product card) | ⚠️ same as above | Inkyung | Post-launch OK |
| 12 | Memo | `II Site V2 - Memo.html` | Done (real product card) | ⚠️ same as above | Inkyung | Post-launch OK |
| 13 | Knowledge Hub | `II Site V2 - Knowledge Hub.html` | Structure only | Most cards unlinked; content direction changing (feature "What is a memo / underwriting / kill criteria" over generic TFSA/RRSP topics) | TBD | **Cut candidate** |
| 14 | KH article | `II Site V2 - KH-TFSA.html` | Done | Only reachable via KH — cut together | — | Cut candidate |

**Assets (all in use, keep):** `Logo.svg`, `appstore-badge.png`, `grid-overlay.js` (dev tool: press `g` for the 12-col grid overlay), `images/`.
**Folder state:** cleaned 07-02 — orphan pages deleted (Research, Journal-Slug, ii-app-9, Documents ×2, lineart-concepts/), zero broken links verified. `archive/` = history only, not part of the build.

---

## 3. What lands later (do NOT block the build on these)

- **Product screens** for Home / SD / Managed — Inkyung replaces with latest app designs
- **Copy finalization** — text updates from Dave, Aidan, Inkyung while the build runs; structure will not change
- **About founder bios** (Dave/Gregory), **GetTheApp real URLs**, **Journal content** (4 of 6 articles)
- **Terminology pending from app team:** "Confidence → probability/prediction" is NOT final — website keeps "Confidence" until the app decides. Memo card label "Sizing → Role / Core Position" is decided in-app but not yet applied on the site (2-word change, applies to Home + Memo page cards).

---

## 4. Design-system facts for the build

- 12-col grid, gutter `clamp(16px,1.5vw,24px)`, container max 1680, frame `clamp(24px,4vw,48px)`
- Type: Inter (sans) + Chakra Petch (mono labels). Section titles `clamp(22px,2.6vw,28px)` lh 1.3 · subtitles 18px · body 15px · mono labels 11–12px
- Section rhythm: 160px desktop / 88px mobile, uniform on every page
- Line-color rule: `--c-900` structural lines (section/row dividers) · `--c-800` object outlines (cards, page-header bottom, dotted underlines) · `--c-700` micro accents
- Monochrome only in site chrome; color appears only inside real product-UI replicas (green live states) and the single orange "NOT RECORDED" moment on Home No. 01 (kept intentionally, monochrome + pulse variant already prepared if needed)
- Validation: `node .claude/scripts/validate-design.js "<file>"` must report 0 errors

---

## 5. Open items ledger (single source)

| Item | Waiting on |
|---|---|
| Miguel: full set vs cut list by July 15 | **Miguel** |
| Founder titles + bios | Dave / Gregory |
| Sign-in / social / legal URLs | Dave / Aidan |
| Non-registered account support (FAQ wording) | Dave / Aidan |
| "Confidence → probability/prediction" naming | App team |
| "Sizing → Role / Core Position" label on site memo cards | Inkyung (after wording confirm) |
| Benchmark/Calibration/Memo entry links | Inkyung (when pages ship) |
| KH content reprioritization | Post-V1 |
