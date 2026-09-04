# HANDOFF — V16 landing site

**Rewritten 2026-09-02 when the folder moved V15 → V16. Read this, then `SESSION-2026-09-02.md`
(what changed and why — its last section, 2026-09-03, closes the desktop pass), then
`shared/TITLE-TIERS.md` (the rules themselves).**

**Desktop is closed as of 2026-09-03. Mobile is the next phase and has not been audited.**

Designer: Inkyung Choi (Mogo). Works in Korean, replies best to measured numbers rather than
adjectives. Reference screen **1512** — check that width first, always — with **1920** and **1440**
as the other two working widths. Deployed to GitHub Pages.

---

## Goal

Polish the "Intelligent Investing" landing site so that every value on it is either **on the design
system** or **has a recorded reason not to be**. The work is screenshot-driven: she sends a crop,
names what feels wrong, and expects the cause found and fixed sitewide — never patched in one
section only.

> "한 섹션만 가능하게 꼼수 부리면 안 되고" — no per-section hacks.
> "규칙을 만들어서 전체적으로 적용해야지 그때그때 임시방편으로 룰을 바꾸지마"
> "모든건 시스템 안에서 결정해야해"

Those last two came after a value was invented on the spot instead of read from the rules that
already existed. **Find the rule, quote it, apply it. If there is no rule, say so and write one** —
do not pick a number and move on.

---

## The pages

13 site pages. The three that carry the design system and get worked on together:

| | file | role |
|---|---|---|
| home | `index.html` | **the reference.** SD-optimised below the hero, one topic per section |
| product | `self-directed.html` | |
| product | `managed.html` | follows home + SD; **not** a source of truth to cite |

Plus `pricing` · `manifesto` · `newsroom` · `press-release` · `get-the-app` · four `changelog-*` +
`changelog-entry`, and `wireframe-final.html` — an internal plain-content document for content
review, not a site page.

Shared layer: `shared/v11.css` and `shared/v11-sub.js` load last and own everything that must be
identical across pages. **A page block may only carry `#section-id` rhythm and documented
exceptions.** When a value does not behave as the page's CSS says, grep the shared sheet first.

---

## How to work on this (the part that matters most)

1. **Measure before claiming.** Never read a CSS line and report it as the rendered value. This has
   produced a wrong answer more than once. Serve the folder over HTTP and read computed styles and
   rects in the real browser.
2. **Serve it, don't open the file.** `python -m http.server` at the `landing page` folder (see
   `.claude/launch.json`, `ii-landing`, port 8123) → `http://localhost:8123/V16/index.html`. Opening
   `file://` gives a static snapshot: `shared/v11.css` never loads, so **every type token falls back
   to its unshared default** and the measurements are wrong in a way that looks plausible.
3. **`u` is the unit.** `--u: calc(100vw / 2545)`. Report spacing in `u`, not px — px changes with
   the window and she will (correctly) call it meaningless. Rail 1645u, gutter 30u, column 109.583u.
   n columns = `n * 109.583 + (n-1) * 30`. 4 col = 528.3u, 5 col = 667.9u, 6 col = 807.5u,
   7 col = 947.08u, 8 col = 1086.66u, 9 col = 1226u, 10 col = 1366u.
   Note `--u` uses `100vw`, which includes the scrollbar, while layout uses the client width — so
   measured `u` runs ~1% low. Compare in **columns**, not raw u, when it matters.
4. **Type sizes have floors,** and the floor is why most bugs here exist. `--t-body: max(17px, 22u)`,
   display `max(40px, 64u)`, `--t-mono11: max(9px, 11u)`. Below the crossover the size is frozen
   while every `u` measure keeps shrinking. Crossovers: display 1590 · `--t-read27` 1603 ·
   `--t-h34` 1647 · `--t-body` 1966 · `--t-mono11` 2082 · `--t-mono13` 2153 · `--t-mono15` 2206.
   **A px-hardcoded value and a token-based neighbour agree below the crossover and diverge above
   it** — check at 2560 as well as the working widths.
5. **Kill the reveal animation before measuring**: add `.in` to every `.rv`/`.ri`, and disable
   transitions, animations and transforms, or you measure mid-fade.
6. **Measure ink, not boxes**, when the question is "does this look too far apart" — use a `Range`
   over the text nodes. Box gaps lie when font sizes differ, and a block element's width is its
   container's, not its text's.
7. **Canvas figures do not always draw in a headless pass.** The constellation and the sphere came
   back as blank bitmaps. Do not conclude anything about a diagram's composition from an empty
   canvas; say the render did not happen.
8. **Cascade traps.** Before concluding "this rule does nothing", find the rule that actually wins.
   Walk the stylesheets, match the element, compare specificity — reading the file top to bottom will
   mislead you. Live examples: `.rows3 .row .t` has **six** competing declarations across four
   sheets with three different sizes; `.metaline`'s leading is set by an unscoped block that loads
   *after* the mobile block and beats it.
9. **Back up before each change**: `cp x.html _archive/x-pre-<topic>-YYYYMMDD.html`. V15's `_archive/`
   holds every backup written on 09-01 and 09-02; V16 starts a fresh one.
10. **OneDrive has silently truncated files here.** After a scripted edit, check the file still ends
    with `</html>` and contains no NUL bytes.
11. Cache-bust with a query string when re-checking in the browser; `shared/v11.css` caches
    separately from the HTML.

---

## The design system as it now stands

### Measure — the whole rule

| | ≥1800 | ≤1799 |
|---|---|---|
| display title `.bigh2` `.sys h2` `.loop3 h2` | **9 col** (1226u) | **10 col** (1366u) |
| body prose | **6 col** (807.5u) | **7 col** (947.08u) |

Declared once as `var(--prose)`. That is for prose that **owns** its row; prose that **shares** its
row with a figure or a second column is **6 col at every width**.

Outside the column correction: two-column grids that already fill the rail (`.pgrid5`,
`.close9 .cols` — 6+6), `.latest .lt-sum` (its own container's formula), and the caption tier.

**Plated titles take no measure at all.** `#benchmark` / `#development` / `#refuses` on SD and
`.gap2` / `.std5` on the home set `max-width:none` deliberately: `.a`/`.b` are `nowrap` black plates,
so the markup decides the line breaks and a measure would only overflow them. Their leading is
**0.90**, which is plate spacing, not text leading. Plain titles are **1.05**. The home hero is
**1.35** because its plate is a `box-decoration-break:clone` child that wraps. Three values, three
constructions — this is not drift.

### Captions

**A caption takes the width of the thing it annotates. Never pin it to a column count** — a
`max-width` number is a fossil of how wide the target used to be, and it does not follow when the
target moves. **A running note that flows with body text is 6 col** (12 col was tried and rejected:
a 9px mono line runs ~190 characters). Multiple caption lines under one target: `margin` **0**
between them, leading only; target → first caption **24px**.

### Fixed-width elements sharing a row with prose

**Prose width is the rule value.** A narrowing row does not shrink the prose — the fixed-width
element (a logo row, a badge row) drops to its own line and left-aligns there. Use
`flex: 0 0 <n col>` on the prose: with a content-sized or `0` basis, flex decides wrapping *before*
shrinking and the row breaks while there is still room.

### TYPESET registry — the criterion is ITEM COUNT

| | title / body | tokens |
|---|---|---|
| TYPESET 1 · LARGE | 28 / 500 / 1.25 + 17 / 400 / 1.3 | `--t-h34` + `--t-body` (unused) |
| TYPESET 2 · MEDIUM | 22 / 500 / 1.25 + 17 / 400 / 1.3 | `--t-read27` + `--t-body` |
| TYPESET 3 · SMALL | 17 / 500 / 1.25 + 15 / 400 / 1.3 | `--t-body` + `--t-small17` |

**3 items or fewer → TYPESET 2. 4 or more → TYPESET 3.** A TYPESET title takes the same measure as
the body under it; in a three-up card row the card enforces that, and a full-rail row (`.rows3`) has
to be given `max-width:var(--prose)` explicitly. **She calls these by name** ("typeset 2로 해줘") —
apply the table, do not re-derive.

`--t-h34` is the TYPESET 1 **title** token. It is not the stat token, and using it for numbers is a
bug that only shows below 1647px.

### Stat numbers

**34px fixed / 500 / −0.069em / 1.15. 폭 무관이 의도다.** The one deliberate px-hardcode on the
site. `.v11-stat` (home), `.tri .v` (SD, managed), `.dstats .v` (home).

### Spacing scale
14u · 28u · 42u · 71u · 104u · 113u · 184u.
- section padding **184u** top and bottom, symmetric
- eyebrow → title **42u** · title → content **71u**
- title → body **14u** · body → mono meta **14u** (ROW RULES, inside a card)
- panel padding **42u**; card column gap **28u**; content → text CTA **42u** with `margin-top:auto`
- prose paragraph → paragraph **24px flat** (24 against the 22.1 leading is 1.09×, the point of it)
- two sentences meant to read as **one** statement: margin **0**, leading only
  ("한문단의 행간처럼")

### Mono (IBM Plex Mono)
Ladder **13 / 11 / 9**, tracking `0.04em` everywhere. Leading: multi-line mono prose **1.5**,
one-line label/meta **1.4**, captions 9px/1.4 — judged **per component**, not per instance, since a
line that fits at 1512 wraps on a phone. Mono = meta only (labels, dates, captions, specs), never
prose body. Uppercase belongs to the **13** tier; 11 and 9 are sentence case, with dates and the
home's beat labels as the accepted exceptions.

### Radius
`--r-site:4px` (site boxes, diagram figures) · `--r-app:12px` (app mockups — `.dr-doc`, `.cal-card`)
· `--r-app-in:6px` (boxes inside a mockup, currently unused) · `--r-pill:99px`.

### Hairlines
Canon **0.667px**. Dark grounds `rgba(255,255,255,0.18)`; light grounds `rgba(28,28,28,0.16)`;
**a dark box on a light ground takes `--c-800`** (the `.dr-doc` answer — and note that is about the
*ground*, not the box: the same plate on black takes the white hairline). Product-UI mockups keep
their own 1px internal scale. Buttons are still 1px; `.calcard` (dead CSS) holds the only 0.5px.

### Grounds and fills
- Light-ground panel canon: **white on cream**, 42u, 4px (home membership cards, `.close9 .offer`).
  This is correct — do not "fix" it.
- Dark ground: `--c-1000 #1C1C1C` on black.
- **A figure on a black ground uses `--c-surface #151515`**, not `--c-elev #0A0A0A` (10/255 off black
  is invisible). Precedent: `.constplate`.
- **The fill answers to its ground**: opaque on a flat ground; **translucent on a photo** so the photo
  reads through the gaps instead of sitting under one slab. `.refuse .r` = `rgba(28,28,28,0.60)`,
  measured as the most transparent value that keeps c-200 body text at AAA over that photo
  (alpha 0 = 3.8:1, a WCAG failure — which is why "just an outline" is not an option).
- Titles are white on black, `#1C1C1C` on cream/white, `#565B5E` for a dimmed second line. Red is for
  a reversal line and negative numbers. **There is no third colour** — a sky-blue title was removed
  on 09-02.
- Status colours: `--c-live-muted #288752` · `--c-review-muted #966E26` · `--c-urgent-muted #BE3C36`
  · `--c-700` (neutral/void).

### App mockups
`.dr-doc` (memo) and `.cal-card` (record) — the only two app screens. 5 col, max-width 566px,
radius 12px. `.constfig` / `.pffig` / `.sphwrap` / `.loopfig` are canvas **diagrams**, a different
class (radius 4px).

### Figure placement
SD's three figures sit in the third track of a **6 col / 1fr / 5 col** grid — 5 col wide, left edge
at **column 8** (`.specimens`, `.calgrid`, `.close9 .cols.figrow`). Managed's two sit at **4 col**
(`.defgrid`, `.pfgrid`) — her call on 09-02. **The two pages disagree and that is unsettled.**
When a prose row needs a figure, give it this grid; do not put the figure in a prose track.

Figure rows align at the **top**, not the bottom. Measured at 1512: bottom offsets +90 / −37 / −1 px
across the three SD rows, top offsets all within a few px of −150u. A figure scales with the window
while prose height is floored, so a shared bottom edge cannot hold — do not chase it.

---

## What worked

- **Measure, then decide.** Every value she accepted was derived from a measurement, not proposed.
  The card transparency (composite over the real photo, p99.99 worst case → 0.60) and the "photo is
  too dark" answer (the histogram said the problem was *range*, not brightness) are the models.
- **Find the site's own precedent before inventing a value.** `--c-surface` for a figure on black,
  `--c-800` for a dark box on a light ground, `flex:0 0` for the prose in a fixed-width row —
  each already existed somewhere for the same situation.
- **Read the rule file before proposing a number.** Every value invented on the spot this session was
  sent back; every one traced to `TITLE-TIERS.md` was accepted.
- **Subtracting beats retuning.** The constellation's 30-label rim ring was removed after thinning it
  to 12 made it worse.
- **Write the reasoning into the CSS comment**, including reversals and what was tried and rejected.
  The comments are load-bearing documentation and she reads them.
- **Restore, don't rebuild.** THE DEFAULT came back on 09-02 with **zero new CSS** — the `.def4`
  rules had been maintained through two versions after the markup was deleted.

## What didn't work

- **Reporting a CSS line as the rendered value** — twice, both times wrong.
- **Inventing a column count** (a 9-col cap for the trust lead) when the measure rule already said 6.
- **Copying a value without its condition** — `--c-800` for a plate border is right on cream and
  wrong on black.
- **Unifying every figure to 6 col.** Clean on the grid, but the figures are aspect-driven, so 4→6
  col made them 1.5× taller (risk stack 417×500 → 614×774 at 1960). Reverted.
- **`box-decoration-break:clone` on a flex item** — a flex item blockifies `display:inline`. Put the
  plate on an inline child.
- **`contrast()` above 1 on a dark image** — it pivots on 0.5 and crushes to black.
- **Subgrid `grid-row: span N` where N < the flow-child count** — the overflow stacks silently into
  the last track. Count the children first.
- **Guessing an alpha, a filter, or a gap by eye.** Every one got sent back until measured.

---

## Open — do not decide these alone

1. **Memo mockup is clipped.** `.dr-doc` is a deliberate teaser (fixed `aspect-ratio:528/630`,
   `overflow:hidden`, bottom fade, "VIEW THE FULL MEMO"), but its content was rebuilt to Figma
   3967:1732 without updating the ratio: it overflows by 171px at 1512 / 194px at 1440 / 22px at
   1920, and the whole **Kill Criteria** block is cut. Needs the new frame's ratio, or a decision
   that the teaser ends after Thesis.
2. **SD closing layout.** Three things — prose, the white offer, the constellation — where the home
   has two. Last shape discussed, needing no new copy: split the two existing paragraphs, first with
   the figure, second with the offer, so the closing row matches the home.
3. ~~Figure width, SD 5 col vs managed 4 col.~~ **Settled 2026-09-03: 4 col, columns 9-12, on all
   three pages** (memo, calibration, constellation, sphere). Inkyung called it directly.
4. **Document list differs** — SD 7 items, managed 5 (SD adds `Self-Directed Investing App Terms of
   Use` and `Best Execution Policy`). Both are OEO-specific and compliance requires IISI/IIWMI
   separation, so the difference is probably correct. Confirm; do not "unify".
5. **`#benchmark` title runs past the measure.** Its ink is **9.84 col** where the canon is 9. It
   is one of the three `max-width:none` flex-column titles whose line breaks are authored in `.a` /
   `.b` spans, so a `max-width` would break the construction — the fix is to end the `.a` line a
   word earlier. Copy call, Dave.
6. **Figure pull-ups are still eyeballed** — `-250u`, `-271u`, `-296u`, `-255u`, each set by hand to
   lift a figure level with its section title. Offered to derive them from the title block's height;
   no answer.

## Known work, no decision needed

7. Consolidate `--prose` and `--prose-cols` into one spelling across the 6 pages.
8. `--t-mono12` is redundant at desktop — absorb it.
9. `.calcard` is dead CSS across 8 pages, and holds the only 0.5px hairlines.
10. `--r-app-in:6px` is declared but unused — `.dr3-*` and `.cal-*` inner boxes are all radius 0.
11. Remaining one-line mono labels at 1.5 instead of 1.4: `.k`, `thead th`, `.nr-tabs button`,
    `.step b`, pricing `.sub`.
12. `.menuov-cta` is the only mono at weight 500 (5 pages) — intent unconfirmed.
13. Mobile `.metaline` / `.figcap` declarations are tangled on SD and managed; the desktop role split
    has not been applied to the ≤900 blocks. **Mobile is the next phase** and has not been audited.
14. The `.constfig` move script does not restore the figure to the desktop layout when a narrow
    window is widened — it stays in the bottom sheet until reload.
15. **Compliance / content, from `SESSION-2026-08-31.md` §8:** managed has 9 placeholders; the home's
    NO.01 headline is still marked TBC; managed's closing SD sentence (entity separation). The memo
    mockup keeps a fictional issuer (NOVA) — Figma 3967:1732 uses AAPL / 87.60 CAD; swap only if
    compliance clears it.

**Needs her eyes, never verified here:** the hero videos actually playing, the canvas diagrams
composed (they render blank in a headless pass), and the photo sections at full resolution.

---

## Sharing

Build the share copy **from** V16; never work inside one. Scan the pages for references rather than
listing assets by hand — a hand-written list missed six mobile videos and five newsroom images.
Pick up `src` / `poster` / `data-m` and JS string paths. Photos → 1600px long edge, JPEG q78;
desktop video → 1280px wide, mobile → 960px, CRF 30, audio dropped, `+faststart`. Fully opaque PNGs
convert to JPEG — rewrite those references **in the copy only**. Fonts stay on the Google Fonts CDN,
so the viewer needs a connection.

Last build: 13 pages, 39 assets, media 83.3MB → 18.3MB, folder 19MB. One ffmpeg run segfaulted
mid-encode and left a file with no moov atom — **ffprobe every output** before shipping.
