# Orion Digital IR site, V3 — handoff

Written 2026-09-08. Read this before touching anything in `V3/`.

V3 is the third attempt. **V1 and V2 stay untouched** — V1 was rejected as too close to the II
site, V2 as 난잡해. V3 is a role study: the diagnosis was that V2 gave all ten sections a
device, so the page never said which moment mattered.

Reference throughout: `format.obys.agency`. Wanted: not II, encompassing II, a higher-order
concept. 무심하면서 시크한. Layout and typography over specific imagery.

---

## 1. How to build

`index.html` is **generated**. Do not edit it directly; edit the generator.

```bash
# rebuild index.html from the generator
cd "Product Design_work files/Prototype/website/Orion Digital Website/V3/_build"
python build_v3.py

# bake the self-contained review file (inlines every image and the CSS)
cd ../_review
PYTHONIOENCODING=utf-8 python bake.py     # writes latest.html, ~3.8MB

# the design validator, run from the repo root
node .claude/scripts/validate-design.js \
  "Product Design_work files/Prototype/website/Orion Digital Website/V3/index.html" \
  "Product Design_work files/Prototype/website/Orion Digital Website/V3/shared/v3.css"
```

`shared/v3.css` is hand-edited and is the real stylesheet. The generator lifts the nav from
V2's HTML by regex; that nav markup lives on a single physical line inside a
`nav.replace('...','...',1)` call, so patch it by exact substring, never by rebuilding the
escapes.

```
V3/
  index.html         generated, do not hand-edit
  RULES.md           the Orion rules that extend the II system, each with its measurement
  HANDOFF.md         this file
  shared/v3.css      the stylesheet
  _build/build_v3.py the generator
  _review/bake.py    makes the self-contained review file
  _review/latest.html the review deliverable
  Images/  + _archive/README.md
  logos/   + _archive/README.md
```

---

## 2. Content logic (Greg's, load-bearing — do not rearrange)

The page defuses the "$80M debt / $25M cash" misconception by showing that the **C$49.8M
lending facility finances the C$75.4M loan portfolio**.

- **Valuation appears last, section 05, after the balance-sheet correction in 04.** The order
  is the argument.
- **Never state "undervalued" and never print an EBITDA multiple.** "The juxtaposition does
  enough." This also rules out drawing the multiple: two discs sized to market cap and EBITDA
  was proposed in this session and refused, because a figure we may not set in type we may not
  set in geometry either.

---

## 3. Section state

| # | Section | State |
|---|---------|-------|
| hero | Building for an AI-driven financial system | image is a **stand-in** (container vessel). Window 4–124, contrast measured |
| 01 | AT A GLANCE | done, deliberately undesigned |
| 02 | THREE OPERATING BUSINESSES | done. Three logos in, subgrid-aligned to the figure |
| 03 | OPERATING & FINANCIAL SNAPSHOT | picture replaced with filed paper (`pic-files.jpg`) |
| 04 | BALANCE SHEET | done. The pair arrives in argument order (bespoke sequence) |
| 05 | MARKET VALUATION | done. Grey ground, white sheet, data at columns 7–12 |
| 06 | THE TRANSITION | mirror anchored to both rail edges, per-row hairline |
| 07 | DISCIPLINED CAPITAL ALLOCATION | done |
| 08 | THREE SOURCES OF UPSIDE | three bands replaced, one subject per business |
| 09 | INVESTOR RESOURCES | done |
| 10 | DISCLOSURES | **DRAFT · REQUIRES SECURITIES COUNSEL REVIEW** markers in place |

---

## 4. Open issues, most important first

### 4.1 Scroll motion is unverified and may not run

**Start here.** The page has a script-driven motion system (`_build/build_v3.py`, the block
beginning `// The page's motion, all of it, from one table`). It was measured working earlier
in the session — hero ground 0→109→160px, cell veil 0→30, 05 texture 0→34, picture scale
1→1.05, staggered figure arrivals at 0.82 / 0.69 / 0.51 / 0.27 / 0.07 — and then stopped
being verifiable.

What was measured at the end:

- `requestAnimationFrame` **never fires** in the review browser pane (`rafAlive: false`)
- **no scroll event reaches the page at all** (`scrollEventsReachPage: false`), and the nav's
  own `.scrolled` toggle, which had worked all session, also stopped responding
- `scrollY` still changes, and manual `el.style.transform` writes still apply

So the freeze is very likely the environment, not the code. The rAF dependency was removed
anyway (writes are synchronous in the scroll handler now, guarded by the last scroll
position), because a host that produces no frames would otherwise silently do nothing.

**First action: open `_review/latest.html` in a real browser and scroll.** If it moves, this
issue is closed. If it does not, the fallback is to drive the transforms from a
`scroll`-listener-free source, or to accept the page as static.

Native scroll timelines (`animation-timeline: view()`) were tried and abandoned: they attach,
the `ViewTimeline` object exists, but `currentTime` reads `null`, so nothing progresses. The
CSS for that path has been removed.

### 4.2 A reversion ate three edits at once — check before assuming a bug

Three edits from the same phase of work silently reverted together:

1. the `overflow:hidden` → `overflow:clip` conversion (16 declarations)
2. the whole scroll-driven CSS primitives block
3. the JS config table in the generator

All three were restored. **The design validator cannot see this** — nothing is malformed, a
rule is just missing, so it kept reporting 0 errors. This project has a history of OneDrive
reverting and truncating prototype files.

The check that catches it: measure one element per primitive and confirm it actually moves.
A quick smoke test:

```js
document.documentElement.classList.contains('js-anim')   // script finished wiring
document.querySelectorAll('.a-lag').length               // expect 8
document.querySelectorAll('.a-val').length               // expect 19
getComputedStyle(document.getElementById('at-a-glance')).overflow  // expect "clip"
```

### 4.3 Content still to confirm

- **17 Greg/Christy confirmations** listed in V1's `SESSION-2026-09-04.md` §8, including 04's
  wording and the Adjusted EV definition. Footnote 3 is Greg's conceptual version, **not
  counsel-approved**.
- **Every `.unc` value** carries a dashed underline marking it unconfirmed. All of them must
  disappear before publication. Figures are still inline; nothing is wired to `data.js`.
- **Footnote 2 arithmetic**: components sum to C$34.9M against the C$34.8M shown. Unresolved.

### 4.4 Imagery

**The page is muted colour, not black and white.** It was all-greyscale until 2026-09-08, and
that was wrong: the standard makes colour the default and black and white stylised, and a B/W
frame had already been rejected once at CEO review. Rules and measurements in RULES.md §4e.

- Six files are baked from their originals with hue intact; `saturate(0.75)` is the mute. The
  hero measures avg saturation 13.9 at R-B -13.5, cool.
- **Check R-B on any new frame.** Golden tint is banned outright. 08's third band needed a
  channel shift to get from +19.4 to -0.6.
- **An inverted ground needs a warm source.** 02's ground is a negative and inverting flips
  temperature, so a cool frame comes back golden. The current source is +24.1 warm and inverts
  to -7.3.
- **08 is black and white on purpose**, bands and ground. The packaging on the shop shelving
  was the only saturated element and read as clutter; the other two frames are near-neutral as
  shot. Luminance and contrast are unchanged, both filters being luminance-preserving.
- **Three more surfaces are neutral, and re-sourcing them would change nothing**: 05's two
  pale textures and 02's cell veil. Their own windows crush a 29-saturation source to 5.7, 4.3
  and about 3. Measured, not assumed.

**The hero is the last stand-in.** 506 photographs in the II library and not one Canadian
frame, so this needs a shoot or new sourcing. The markup says so in place. The current frame,
a container vessel at sea, stands in for direction B below and already sits at the right
temperature.

Two directions were put to the user, neither chosen yet:

| | subject | says |
|---|---------|------|
| A | a Canadian institutional or downtown frame | where the issuer is, and the dual listing |
| B | a wide load-bearing infrastructure frame | that the holding company carries weight |

Stock search terms, from the Mann Standard keyword bank with Canada added:

- A: `toronto financial district blue hour`, `bay street winter overcast`,
  `canadian bank tower documentary`, `vancouver port dusk`
- B: `bridge infrastructure documentary overcast`, `transmission lines winter`,
  `grain terminal prairie`, `container terminal blue hour`
- interior: `reading room long desk window light`, `archive shelves interior`,
  `office at night workers windows`

Filter words: `muted`, `overcast`, `blue hour`, `35mm`, `documentary`, `grain`.
Exclude: `golden hour`, `neon`, `corporate smiling`, `startup office`, `aerial`.

Midjourney is for **shoot direction only, never for the page.** Common suffix
`--ar 16:9 --style raw --v 7`:

```
Toronto financial district at blue hour, wide documentary frame from street level,
brutalist bank tower in cool grey concrete, low winter light raking one facade,
muted desaturated palette, 35mm film grain, deep quiet sky for typography,
no people in foreground, no neon, no golden tint
```

```
underside of a steel truss bridge over grey water, seen wide and low,
overcast Canadian winter light, riveted structure receding, cold blue-grey palette,
documentary photography, 35mm, film grain, large empty sky in the upper third,
no sunset, no aerial view, no HDR
```

```
wide interior of a working institutional records floor at dusk,
long tables, one lit workstation, tall windows with overcast daylight,
muted earthy palette, cool documentary temperature, 35mm film grain,
deep unlit area on the left for large type, professionals absorbed in reading,
no smiling, no screens facing camera
```

- Nothing on this page depicts Orion's own premises. The images are **context, not
  depiction**, and no caption claims otherwise. Real photography of Intelligent Investing,
  Carta Worldwide and Mogo replaces them when it exists.
- **AI-generated frames are excluded from the page.** The library's richest bucket
  (institutional interiors, ~90 frames of the same reading room) is Midjourney, as is the one
  perfect 03 subject, an overhead flat-lay of handwritten investment memos. An issuer showing
  fabricated images of its own operations is not acceptable.

### 4.5 Proposed and not yet built: global as evidence

The chairman's own quick mockup put an earth-from-space render behind the headline. The
intent is right and was a genuine gap — **Carta is European payments infrastructure**, and the
page reads as a purely Canadian holding company. The device is wrong: 3D renders, neon and
HDR are on the banned list, and the fluorescent green is a different brand.

Proposed instead, not built:

1. **Make the dual listing carry it.** NASDAQ *and* TSX is the most credible global statement
   an issuer owns, and it is currently 9px in the nav.
2. **Give each company name its market.** This also answers the open request to differentiate
   the company names. The categories already say CANADIAN WEALTH / EUROPEAN PAYMENTS
   INFRASTRUCTURE / CANADIAN CONSUMER LENDING, all buried in the same grey m9. Split market
   from activity and lift the market to the name's colour, and the three cells read
   CANADA / EUROPE / CANADA.
   Note: **the names cannot simply be enlarged.** "Intelligent Investing" at 34px wraps to two
   lines in a 305px cell while the other two stay on one, which breaks the equal-line-count
   rule for parallel columns.
3. The hero photograph is already cross-border volume at sea, which is the un-cheesy version
   of the globe.

### 4.6 Mobile

Structure is in and 375 shows zero horizontal overflow, but **no visual pass has been done by
eye**.

---

## 5. Decisions already made — do not re-litigate

- **05's disc is gone.** It was a hole cut in the sheet, then removed: as a shape it did
  nothing, and 08's Wealth band now carries the filing-drawer subject anyway. Sizing two discs
  to the figures was refused as drawing the multiple.
- **06 carries no leader lines.** They filled the empty outer margins of a centre-hugging row;
  anchoring the row to both rail edges removed that emptiness. They were also unfixably
  misaligned, sitting at cy 0.3 and 34.6 in a 34.9px row while all the type sat at 17.5.
- **`(Statement)` is gone** from the hero. It said nothing, and it was the only tier forcing
  the ground's exposure down.
- **Grounds are darkened by baking a luminance window, never by a brightness multiplier.**
  `brightness(0.30)` maps 255 to 76, so the ground has no highlight and therefore no depth
  whatever is photographed; nineteen candidate frames all topped out at exactly 76. See
  RULES.md §4d.
- **08 is text-on-cream-plate over a photograph sliver.** The plate covers columns 1–9, so the
  picture shows through 233×223px only. Pick for the sliver, not the frame: a single object
  reads at that size, a space does not. RULES.md §4b.
- **One subject per section.** RULES.md §4c.
- **Motion budget was three events, then the user asked for all sections.** Delivered as four
  primitives from one config table, with figures arriving rather than counting up.
- **No Lenis.** Scroll hijacking on an issuer's page is a real complaint, not a taste one.
- **Muted colour, not black and white.** The all-greyscale build contradicted the standard and
  reproduced a decision already made against at CEO review. Colour is baked into the file, the
  mute is `saturate(0.75)` in CSS, and the three surfaces still neutral are neutral because
  their own windows destroy colour, which is measured. RULES.md §4e.

---

## 6. Environment traps, all hit this session

- **The review browser pane cannot be trusted for scroll or animation.** No scroll events, no
  rAF. Screenshots also come back black or downsampled. Measure numerically; verify motion in
  a real browser.
- **CSS is cached separately from HTML, and images separately again.** A reload can serve a
  stale stylesheet, which looked exactly like a specificity bug twice, and a stale image,
  which looked exactly like a filter that was not applying. Bust both:
  `link.href = link.href.split('?')[0] + '?cb=' + Date.now()`
  `img.src = img.getAttribute('src').split('?')[0] + '?cb=' + Date.now()`
- **Box size is not proof that a mark paints.** A clipped SVG reports `loaded: true` with a
  non-zero box and draws nothing. Rasterise it and count dark pixels.
- **`overflow:hidden` makes an element a scroll container**, which kills `view()` timelines
  inside it. Paired with `overflow:clip` throughout.
- **`clip-path` deadlock**: an element clipped to nothing never intersects the viewport, so it
  cannot trigger its own reveal, and neither can anything inside it.
- **A decorative reveal must never be what makes content visible.** The hidden-by-default wipe
  blanked 02's three cells and 05's sheet outright when its timeline went inactive. Every
  hiding primitive is now gated on `.js-anim`, which the script adds **last**, after it has
  finished wiring up.
- **Shared subgrid tracks reserve space for every cell's content.** 02's rule sat 40.3px below
  its figure against 23.3px above the next because another cell had a footnote in that track.
  Mutually exclusive slots must share one track.
- **`ch` units ignore letter-spacing.** Every mono field here is set at +0.04em, so a 12
  character field needs `calc(12ch + 12 * 0.04em)`.
- **The rail renders 915.78px at 1440, not the nominal 930.77**, because `100vw` includes the
  scrollbar. Express absolute positions as percentages of the rail.

---

## 7. Where the rest of the canon lives

- `V3/RULES.md` — the Orion rules extending the II system, each with the measurement that
  produced it
- `V3/Images/_archive/README.md` and `V3/logos/_archive/README.md` — what was replaced and why
- `Doctrine/` — the II canon. Marketing image doctrine is the Mann Standard, in
  `Intelligent Investing/V5/V5-DIRECTION.md` §9.5, including the stock keyword bank
- V1's `SESSION-2026-09-04.md` — the confirmation queue
