# V7 — Direction

> Started 2026-07-28. V7 is a clean fork of V6 at the end of the mobile sweep. **V6 is frozen** — it keeps the 4K masters and the full unused image library; V7 carries only what the nine live pages reference.
>
> Read this before touching V7. Tokens and hard rules still come from `../../../../Doctrine/Style_Design.md`, `Doctrine/Typography.md`, and the `ii-design-guard` skill. `V5-DIRECTION.md` (carried over) still governs the visual system; this file governs what V7 changes.

---

## 1. Why V7 exists

Team feedback on the V6 mobile build, two items:

1. **"글자가 너무 많다"** — too much text on mobile.
2. **Stills read as a downgrade** — the team wants the hero/section motion on mobile, not the frozen frames V6 shipped.

Item 2 is done (see §4). Item 1 is the whole point of V7.

---

## 2. The density problem, measured

All three measured in the same pane at **390 × 844**, counting rendered visible words per 844px screen band.

| | Wealthsimple | Robinhood | **II (Self-Directed, V6)** |
|---|---|---|---|
| Total screens | ~10 | 9 | **14** |
| Total words | ~120 | 369 | **1,377** |
| **Words per screen** | **~12** | **41** | **98** |
| Heaviest screen | — | 86 | **139** |
| Body | — | 16px / 400 | 15px / 400 |
| Display | — | 28–50px / **400** | 27px / **500** |

Per-section on Self-Directed:

```
NO.01 THE RECORD      260 words   ← 1.5x the next heaviest
NO.04 CALIBRATION     176
NO.06 RESEARCH        148
NO.08 ACCOUNT TYPES   143
NO.05 DEVELOPMENT     138
NO.02 THE BENCHMARK   110
NO.03 THE REVIEW      107
NO.07 WHAT IT REFUSES  92
HERO                   59
```

The feedback is quantitatively correct: **2.4× Robinhood's per-screen density, 8× Wealthsimple's.**

---

## 3. The constraint that shapes every fix

**We cannot cut copy.**

- Web copy is Dave's pressure-tested canon. Flag candidates, never rewrite.
- Self-Directed and Managed body content is the compliance submission. No deletions, no additions, no rewording.

So density has to come down **structurally**. Every V7 move below changes layout, disclosure, or pacing — never wording.

---

## 4. Reference read (Wealthsimple / Robinhood, 2026-07-28)

Both are background-video sites, so motion on mobile is not the differentiator. The differentiator is **distribution of text**.

### What Wealthsimple actually does

1. **One idea per screen.** Eyebrow (`Wealthsimple Portfolios`) → headline → one arrow → one object. ~11 words, then nothing.
2. **No separate description paragraph.** The subhead is folded into the headline as short clauses:
   > The Summit portfolio.
   > Private markets, long-term growth, zero maintenance.

   We always ship **title + separate description block**. They ship **one block**.
3. **Prose is concentrated, not spread.** Exactly one paragraph on the entire homepage (~60 words at 19px) plus an 11px footnote. Everywhere else is headline + image. They do not thin copy evenly — they **designate a reading section** and empty the rest.
4. **Text occupies the top ~30% of the screen; the lower ~70% is a single object** on plain or gradient ground. Mountain, pie, coin, card. One subject, not a detailed photograph. (Extends the existing "imagery: ordered, not cluttered" rule.)
5. **Identical rhythm repeated 8+ screens.** They have *more* screens than us and still feel calm. Repetition is the calm.
6. **Directory pattern** for the product index: huge title + **6–9 word** description + arrow + hairline. Same structure as our `.acct3` / `.sys .mode`, but our descriptions run 30–40 words.
7. **Manual pause control** (bottom-right `⏸`) for the background motion.

### Adopt

- **A. Designate reading sections.** One or two sections carry prose; every other section becomes eyebrow + headline + one object. The displaced paragraphs *move*, they do not shrink. Needs Dave's sign-off on placement only, not wording.
- **B. Progressive disclosure on the heavy sections.** The `+` pattern already shipped on No.05b `.suit5`. Title + first line visible, remainder behind `+`. Content stays in the DOM, so compliance is satisfied.
- **C. Swipe for parallel content.** The horizontal snap strip already shipped on the homepage changelog. Apply to sections that stack siblings (No.07 refuses, No.08 account types, Managed portfolios): one card visible instead of three stacked.
- **D. Manual pause control** for hero/section video. We honour `prefers-reduced-motion` but give no manual control — a real accessibility gap.
- **E. Lighter display weight.** Robinhood runs 28–50px at 400. Ours is 27/500. Same word count reads less dense. Test as its own change; it touches `Doctrine/Typography.md`'s weight rule (see §6).

### Do not adopt (canon conflict — flagged, not applied)

- **Arrow-only CTA.** Our CTA canon is a typed-CAPS text link plus SVG arrow, and a box CTA with no arrow. A bare circular arrow replaces the label.
- **Two serif/sans display registers.** We are Inter + IBM Plex Mono. No serif.
- **Colour grounds and gradients.** Product surface is monochrome. (Marketing creative is not — different rule.)

---

## 5. What V7 inherited from the V6 mobile sweep

Already in place, do not re-derive:

- Mobile ladder **8 / 16 / 24 / 32 / 40 / 48 / 64**, section padding 72/72, screen edge 20.
- Type tiers: masthead 27/500, stream heading 22/500, item title 17/500, body 15/400 lh 1.4, small 13, mono 12–13.
- Group canon: blocks **16**, before a link **24**, label→title **8**.
- Stat patterns — short value: `64px + 1fr` grid (`.dstats .cell`); long sentence: full-width stack, hairline → value 8 → prose 16 (`.gap2 .g2stat`).
- Numbered steps: everything flush to the 20px gutter, no number column (`.loop3 .step`).
- Burger menu 27/500; the X nudged to `right:16.2px` so its rotated ink lands on the same 20px gutter as the logo.
- `.mlink` icon gap floored at 6px; table cell padding floored at 16/20px.

### Video (item 2 of the feedback, resolved)

Mobile plays the clips again. Neither tier uses the 4K masters any more.

| clip | master (V6) | `video desktop/` | `video mobile/` |
|---|---|---|---|
| hero 1 NYSE | 157 MB | 7.9 MB | 3.2 MB |
| hero 2 refinery | 157 MB | 7.0 MB | 3.0 MB |
| hero 3 port | 27 MB | 5.8 MB | 1.8 MB |
| No.04 rail yard | 15 MB | 3.6 MB | 1.4 MB |
| Self-Directed hero | 27 MB | 6.1 MB | 2.5 MB |
| Managed hero | 20 MB | 3.9 MB | 1.3 MB |

- Desktop = 1920 × 1080, CRF 26. The three homepage hero clips are trimmed to 20s because `HOLD=20` in the rotation script means nothing past 20s is ever seen.
- Mobile = 900px tall, CRF 30, same 20s trim.
- Mechanism: `<video src="…desktop…" data-m="…mobile…">`. One script per page swaps `src` to `data-m` below 900px. The extracted stills are now `poster` — instant first frame, and the fallback if autoplay is blocked.
- Only hero clip 1 is `preload="auto"` on mobile; clips 2–3 are fetched by `advance()` when their turn comes. First-load cost ≈ 3.2 MB.
- **4K masters stay in V6 only** (`V6/Images/v5 images/video from dave/`). Re-encode from there, never ship them.

---

## 6. Open, needs a decision

- ~~Validator vs 27px~~ — **resolved 2026-07-28**: 27 and 32 added to the validator's allowed set, `Doctrine/Typography.md`, and `ii-design-guard`.
- ~~Display weight 400 (§4E)~~ — **resolved 2026-07-28**: weight stays 500 (the "≥24 = 500" rule holds); hierarchy came from size instead. Hero `.hbar` mobile is now **32/500** (`clamp(26px, 8.2vw, 40px)`) on all three pages — 2.13× body vs the old 1.8×. 34 was rejected: it orphans the hero copy (`not.`, `week,`). Section h2 stays 27. Managed's first hero line needed a mobile-only `<br class="mbr">` to break as "The market," / "every week,".
- **Which sections become reading sections (§4A).** NO.01 at 260 words is the one true outlier and the obvious candidate to either become *the* reading section or be disclosed.
- **Wealthsimple could not be measured** — `wealthsimple.com` is blocked by browsing policy. Its numbers above are read off screenshots, so treat `~12 words/screen` as approximate. Robinhood and II were measured live.

---

## 6b. For Dave — NO.03 copy overlap (2026-07-28)

On mobile the loop steps are now swipe cards, which makes two of the section's paragraphs double-speak:

- **p3 ("Before the order…", 57w) ↔ step 01 Record** — phrase-level overlap (classified/role/size/probability/written case). p3's unique content is only: *"…carries the date it was written, not the date of the order"* and *"The system does not invent a history you did not create."*
- **"Every active decision begins with a record…" (18w) ↔ step 03 Review** — same idea, two phrasings ("case can change / history cannot" ≈ "new version dated / previous remains").

Interim state shipped: p3+p2 fold behind a hairline `+` under p1 (mobile only, nothing removed from the DOM). Decision needed from Dave: trim/relocate the overlapping paragraphs, or keep the fold.

## 7. Content still owed

Carried over from V6, unchanged:

- June/July changelog copy — Aiden & Ewen.
- FIG.02 canonical memo screen — Leo / Figma.
- `More interest in what was true…` 68-char line — awaiting Dave.

---

## 8. Files

```
V7/
  index-H.html
  II Site V2 - Self-Directed.html   Managed.html      Pricing.html
                Manifesto.html      Newsroom.html
                Press Release.html  Changelog Entry.html   GetTheApp.html
  grid-overlay.js      Logo.svg      appstore-badge.png
  DESIGN-RULES.md      V5-DIRECTION.md      V7-DIRECTION.md
  Images/v5 images/                  13 referenced stills and plates
                   video desktop/    6 clips, 34.3 MB
                   video mobile/     6 clips, 13.4 MB
```

39 files, 82 MB. Every `src` / `href` / `poster` / `data-m` reference resolves inside V7, and every page validates at 0 errors.

**Left behind in V6:** `_bible.html`, `_latest-section-states.html`, `ceo-content-source.html`, `design-system-web-v5.html`, `archive/`, `_experiments/`, the empty `newsroom content/`, the 4K masters, and ~347 unreferenced images (~1.57 GB).
