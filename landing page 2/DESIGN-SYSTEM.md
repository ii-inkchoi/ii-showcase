# II Website — Design System Reference
**Date:** 2026-07-02 · Companion to `WEBSITE-AUDIT-2026-07-02.md`. Values below are the canonical ones used across all 18 live pages. When in doubt, `index.html` is the source of truth.

---

## 1. Color tokens

Define hex **only** in `:root`. Everywhere else use `var(--c-*)`.

| Token | Hex | Use |
|---|---|---|
| `--c-black` | `#000000` | page background |
| `--c-elev` | `#0A0A0A` | elevated card/panel background |
| `--c-surface` | `#151515` | full-bleed band background (e.g., Home No. 04) |
| `--c-1000` | `#1C1C1C` | deep surface, card-internal dividers |
| `--c-900` | `#232627` | structural hairlines (see §5) |
| `--c-800` | `#565B5E` | object outlines, dotted underlines, muted text |
| `--c-700` | `#929292` | secondary text, mono labels |
| `--c-600` | `#A7A7A7` | body text |
| `--c-400` | `#C7C7C7` | brighter body / emphasized label |
| `--c-200` | `#E3E2E2` | headings, near-white |
| `--c-white` | `#FFFFFF` | primary values, strongest text |
| `--c-live` | `#30D158` | ONLY inside real product-UI replicas (Auto-Invest chip, up-arrows) |
| `--c-urgent` | `#FF3533` | ONLY inside real product-UI replicas |
| `--c-warning` | `#FF7A00` | ONLY the single "NOT RECORDED" moment on Home No. 01 (index uses `#FF7A00`; some subpages define `#FDAD00` but do not use it in chrome) |

**Rule: the site chrome is monochrome.** Color appears only (a) inside product-UI replica cards mirroring the real app, (b) the one deliberate orange moment on Home No. 01.

## 2. Fonts

- **Sans:** `'Inter', sans-serif` — everything by default
- **Mono:** `--mono: 'Chakra Petch', ui-monospace, monospace` — numbers-as-labels, eyebrows, fig captions, sources
- Body sets `font-feature-settings: 'tnum' 1, 'lnum' 1, 'ss01' 1` and `letter-spacing: -0.01em`
- Google Fonts load: `family=Chakra+Petch:wght@400;500&family=Inter:wght@300;400;500`
- **No serif anywhere. No `text-transform: uppercase` (validator errors). No em-dashes (—) in copy.**

## 3. Type scale (by role)

| Role | Size | LH | LS | Color |
|---|---|---|---|---|
| Hero headline (Home only) | `clamp(24px, 7.4vw→, 52px)` per hero rules | 1.25 | −0.03em | c-200 |
| Page title (subpages) | `clamp(30px, 4.4vw, 40px)` | 1.25 | −0.03em | c-200 |
| Page deck / hero sub | `clamp(17px, 1.6vw, 18px)` | 1.55 | −0.015em | c-400 |
| **Section title (statement tier)** | `clamp(22px, 2.6vw, 28px)` | **1.3** | −0.025em | c-200 |
| Subtitle / card·step·list titles | **18px** | 1.3 | −0.01/−0.02em | c-200 or white |
| **Body copy** | **15px** | 1.55–1.7 | −0.01em | c-600 |
| Mono label / eyebrow | 12px | — | +0.04em | c-700 (no.) + c-400 (name) |
| Mono micro (sources, tags) | 11px | — | +0.04–0.08em | c-700 |
| Footnote / small sans | 13px | 1.5–1.6 | −0.01em | c-600/700 |
| Footer legal | 12px | 1.7 | — | c-800 |

Mobile (≤640px): statements clamp to `clamp(22px, 6.5vw, 28px)`; **`text-wrap: balance` must be disabled (`text-wrap: wrap`) on all statement-tier text** — balance causes ugly early line breaks on phones. Desktop keeps balance.

Off-scale sizes (8–10px) exist **only inside product-UI replica cards** — intentional, they mirror the real app. Do not normalize them.

## 4. Layout & spacing

- **Grid:** 12 columns · `--gutter: clamp(16px, 1.5vw, 24px)` · container `--maxw: 1680px` · frame padding `--frame: clamp(24px, 4vw, 48px)`
- Column width formula: `calc((100% + var(--gutter)) / 12 * N - var(--gutter))`
- Common spans: statement 1–7 · right content 7–13 · centered pair 3–7 | 7–11 · evidence stat cards 7–10 | 10–13
- **Section rhythm: `padding: 160px 0` desktop · `88px 0` mobile (≤900px)** — uniform on every page. Exception: `.cta-section` = `160px 0 100px` / `72px 0` mobile.
- Eyebrow → title gap: **28px**. Title → body: 22–32px. Statement-to-content column top: right column starts at eyebrow height (Fit/Evidence/Membership pattern).
- Reading measure: body text max ~660–720px. Never full-width paragraphs (except 12px footer legal).
- Dev tool: press **`g`** on any page → 12-col grid overlay (`grid-overlay.js`, keep the script tag on new pages).

## 5. Line (hairline) color rule — 3 tiers

| Token | Role | Examples |
|---|---|---|
| `--c-900` | **Structural** — quiet lines on the background | section dividers (mobile `::before` only), row dividers (lists, tables, steps, FAQ), card-internal dividers, footer top, `.cta-section` top |
| `--c-800` | **Object outlines & accents** | card/frame borders, button borders, vertical accent bars, `.page-header` bottom, dotted underlines |
| `--c-700` | **Micro accents only** | nav caret, blockquote bar |

All hairlines are `0.5px solid`. Desktop has **no** full-width dividers between sections (whitespace does that job); mobile (≤760px) gets `::before` hairlines between sections.

## 6. Breakpoints

| Width | What changes |
|---|---|
| ≥1024px | desktop nav links show, hamburger hides |
| ≤1200px | Home "The Fit" right columns stack |
| ≤900px | sections 88px padding, most 2-col layouts stack, container 24px padding |
| ≤760px | mobile section hairlines, banner stacks below hero text, page-header `104px 0 88px` |
| ≤640px | statements full-width + `text-wrap: wrap`, type clamps down |

Banner canvas on mobile: `min(84vw, 36vh)` square (Journal: `min(92vw, 40vh)`), centered, below the header text — fits in one viewport with the text.

## 7. Component grammar (quick reference)

- **Eyebrow:** `No. 0X` (mono 12 c-700) + name (mono 12 c-400), 20px gap, 28px below.
- **Product-UI replica card:** `background: var(--c-elev)`, `border: 0.5px solid var(--c-800)`, `border-radius: 4px`, **no box-shadow, no phone chrome/status bars**, bottom mask fade when content is cut: `mask-image: linear-gradient(to bottom, #000 82–90%, transparent 100%)`.
- **Fig caption:** below every product screen — `Fig. 0X · Name. One factual line.` (mono 12, c-700, 14–16px above-gap). No em-dashes.
- **Dark panel (non-replica):** `background: var(--c-elev)`, radius 4px, padding 28px, no border (used on Home No. 04 over the `--c-surface` band).
- **Link with roll arrow:** `class="link"` + arrow SVG + `.roll/.roll-in` double-span hover. Same pattern everywhere ("View Managed", closing CTAs).
- **Row lists:** rows separated by `0.5px solid var(--c-900)` bottom lines; label left / value right (`.mb-row` style) or full-width rows with title col 1–5, desc col 7–13 (Managed "No..." table style).
- **Closing CTA section:** centered one-line canon (statement tier) + roll-arrow "Get the App", `border-top: 0.5px solid var(--c-900)`.

## 8. Motion

- **Reveal:** `.ri` elements fade/rise in via IntersectionObserver (adds `.in` at ~12% visibility). `transition: opacity .9s cubic-bezier(0.4,0,0.2,1), transform .9s` from `translateY(18px)`. Stagger with inline `--d` delays (0.04s steps).
- **Hero:** `hero-rise` keyframes on load (staggered 0–0.42s).
- **node-pulse:** the Home No. 01 hollow/solid node breathes (opacity 1↔0.3, 2s ease-in-out infinite).
- **All motion wrapped in `@media (prefers-reduced-motion: no-preference)`.** Canvas banners pause off-screen via IntersectionObserver and use DPR-aware sizing (`getBoundingClientRect` at runtime).

## 9. Hard don'ts

1. No hex colors outside `:root` (validator error)
2. No `text-transform: uppercase` (validator error)
3. No em-dashes (—) in copy — commas/periods/hyphens instead
4. No serif fonts
5. No phone chrome on product screens (no status bars, no big radii, no shadows)
6. No color in site chrome (see §1)
7. No invented UI — product screens must mirror real app screens
8. Parallel rows/columns must render equal line counts — match copy length, never ship ragged

## 10. Validate before committing

```
node .claude/scripts/validate-design.js "<file or folder>"
```
0 errors required. Warnings inside replica cards (tiny fonts) are accepted.
