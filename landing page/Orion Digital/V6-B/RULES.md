# Orion Digital site rules

**These extend the II design system, they do not replace it.** Tokens, the type ladder, the
three letter-spacing values, line heights, the mono tiers, the 34px stat figure, the 0.667px
hairline and the 12-column rail are II's and are used unchanged. What follows covers the
places II's system has nothing to say, because II is one product with one voice and Orion is
one listed entity over three businesses.

Canonical II sources: `Doctrine/Style_Design.md`, `design-system/index.html`,
`Doctrine/Typography.md`, and the built reference at
`Prototype/website/Intelligent Investing/V16/shared/v11.css`.

Where a rule below was written because something measurably failed, the measurement is given.
Do not relax one of these without re-measuring.

---

## 1. Every section declares a role, and only two are composed

Each section is exactly one of:

| Role | What it does | Treatment |
|---|---|---|
| `declaration` | states what the company is | the page's strongest moment |
| `evidence` | shows figures | undesigned: type on ground, no card, no image |
| `argument` | makes the case | undesigned, and never over a photograph |
| `breath` | changes the air | one flat field, almost empty |
| `index` | resources, disclosures | plain, small, findable |

**At most two sections on a page may be composed.** Everything else recedes.

V2 gave all ten sections a device (grain, photograph, sheet, pale variant, inverted plate)
and the review was *"난잡해"*. The diagnosis at the time was size and photography; both were
wrong. The cause was that the page never said which moment mattered, because ten sections
were all speaking at once. The reference reads clearly for the opposite reason: each of its
sections does one job and only two of them are designed at all.

Current assignment: `00 declaration`, `01 evidence`, `02 declaration` (the three businesses),
`03 04 05 argument`, `06 breath`, `07 argument`, `08 declaration-lite`, `09 index`,
`10 index`. Composed: 00 and 02.

An `argument` section may hold a **picture** (03 does), but never a photographic **ground**.
The distinction is rule 4. Nothing in an argument section stands on an image, so the figures
never fight a photograph for contrast, which is the reason the original no-photograph rule
existed. The rule was too blunt: what it was protecting against was text on pictures.

## 2. RETIRED. A sheet may take the full rail

Written as "a sheet must leave at least one column of ground on each side", inset to columns
2 to 11, and **retired by decision on 2026-09-05**: 02 and 04 both run the full 12 columns,
916px.

The rule was drawn from a real failure but it named the wrong cause. V2's eight sheets were
each 916px edge to edge and did read as bands, so the inset looked like the fix. What actually
made them bands was that there were **eight of them, all the same size, one after another**,
so the eye had nothing to compare and read the whole page as stacked strips. With two full
width groups on a page of eleven sections, the same 916px reads as a deliberate measure.

What survives from it: **two sections that carry a group of three sit on the same width.** 02
and 04 share a footprint, so the page says one thing about that idea instead of two.

## 3. Two reversals per page, one each way

One light plate on a dark ground, one dark plate on a light ground. That is the budget.

- hero: cream plate on the photograph
- 04: dark plate on cream, holding the loans-to-facility pair

A third reversal turns emphasis into a pattern and the first two stop meaning anything.

## 4. A ground and a picture are different things

A **ground** sits behind content: it is darkened (`brightness(0.30)`) because text stands on
it, and everything in the contrast section below applies.

A **picture** occupies its own columns with nothing on top of it. It takes whatever exposure
makes it legible on its own, and none of the ground rules apply. Section 03's panel is lifted
(`brightness(1.34)`) rather than cut, because as shot it rendered as a near-black block on
cream and read as a hole rather than as a photograph.

Both stay greyscale, so they belong to the same page.

## 4b. A picture is only as big as the part you can see

08's bands are 916px wide and their cream plate covers columns 1 to 9, so the photograph
shows through a **233 x 223px** sliver on the right and nowhere else. Every subject in the
first two attempts sat in the middle of the frame, under the plate, and what reached the
reader was an unreadable corner: measured means of **34, 31 and 81** with no legible subject
in any of them.

Two rules come out of it.

**Pick for the sliver, not for the frame.** A photograph of a space cannot read at 233px. A
single object can. Filing drawers, line cards and shop shelving all read instantly at that
size; a room, an office or a street does not.

**Judge the crop the layout will actually make.** The check is to cut the visible sliver in
the same pipeline the browser uses, `object-fit:cover` at the band's size then the band's own
filter, and look at that. Done this way the current three measure **68, 76 and 81**, inside
the 45 to 165 window where a greyscale subject still has form. Judged as full frames, the
same three images looked fine and were wrong.

This also reversed a rejection. The Payments frame was thrown out as a tangle of cabling,
which it is, in the left two thirds that the plate covers; the sliver is ordered rows of line
cards.

## 4c. One subject, one section

Pictures on this page are chosen per operating business, so no subject may appear twice. 03's
best candidates in the library were a card index and an open filing drawer, and both were
refused because 08's Wealth band is now a grid of filing drawers. A subject used twice stops
belonging to either section and becomes the page's motif.

03 also has no single business to photograph, since it reports the consolidated result. What
it has instead is the claim in its own title, earnings and cash rather than projections, so
its picture is a figure being written down by hand: the whole company's work rather than any
one part of it.

**Exposure belongs in the file.** The frame it replaced ran at `brightness(1.62)` against
grounds at `0.30`, to rescue a picture too dark for cream. Lifting a photograph that far in
CSS crushes its shadows, and needing the lift at all means the frame is wrong for the
surface. Pictures are normalised when baked, the way 05's ground is, and the filter then
only removes colour. A linear window was not enough here on its own: the source sits at mean
67, and a straight 46 to 214 remap only reached 90. Gamma 0.65 into a 40 to 240 window lands
it at **mean 117, darks 68, lights 206**, which lifts the midtones without greying the blacks
the way a brightness multiplier would.

## 4d. Darken a ground by baking a window, not by multiplying

`brightness(0.30)` is a multiplier, so it maps 255 to 76. A ground filtered that way has no
highlight available to it at all, and a ground with no highlight has no depth no matter what
is in front of the camera. Measured across nineteen candidate hero frames at that setting,
almost every one topped out at exactly **76**: the reason the hero read flat was the
exposure, not the choice of picture, and swapping frames could never have fixed it.

The hero is baked into an explicit **4 to 112** window instead and its filter is
`grayscale(1)` alone. On screen that gives min 0, max 105, mean 35, and every tier standing
on it clears its floor on the worst pixel under it:

| tier | size | worst ratio | brightest pixel under it |
|------|------|-------------|--------------------------|
| `.hmark` | 11px | 9.44 | 70 |
| `(Statement)` `.par` | 9px | **4.95** | 112 |
| `.h1` | 54px | 7.34 | 86 |
| `.hfoot .lead` | 13px | 13.2 | 48 |

The window's top end is set by that 9px tier and nothing else. At a top of 124 it measured
**4.23**, under the 4.5 floor for text that size, because the label sits over the brightest
part of the frame. 112 was chosen to clear it with margin, and is still 47% more headroom
than the multiplier allowed.

## 4e. Muted colour, and the temperature is measured

The page was built entirely in black and white: `grayscale(1)` on eighteen declarations, and
eight of the eleven image files baked to saturation 0 as well, which put the colour beyond
recovery in CSS. That was convenience, contrast maths being easier on one channel, and it
contradicted the standard, where colour is the default and black and white is stylised. A B/W
frame had already been rejected once at CEO review and replaced with its colour equivalent, so
the page was reproducing a decision that had been made against it.

**Colour lives in the file, the mute lives in CSS.** Pictures are baked from their originals
with hue intact, applying the luminance window with **one LUT across all three channels**: hue
survives, saturation compresses in proportion to the range, and the luminance means come out
identical to the greyscale versions they replace, so every contrast guarantee measured against
those numbers still holds.

| file | luminance mean | avg saturation |
|------|----------------|----------------|
| hero-vessel | 38.7 | 18.5 |
| pic-files | 135.3 | 3.0 |
| band-1 | 96.5 | 2.2 |
| band-2 | 82.1 | 6.2 |
| band-3 | 85.6 | 9.0 |
| ground-veil | 60.5 | 25.8 |

`saturate(0.75)` is the final mute. On the hero that measures **avg saturation 13.9 at
R-B -13.5**, cool, the blue-hour temperature the standard asks for. Type contrasts moved by
hundredths, 8.45 to 8.72 and 6.29 to 6.33, because `saturate()` is a luminance-preserving
matrix.

**Warm casts are corrected, not merely muted.** 08's third band is a shop interior under
tungsten and measured **R-B +19.4**, the golden tint the standard bans outright. Desaturating
alone leaves the cast: it took 55% saturation plus a luminance-holding channel shift, R x0.96
and B x1.10, to reach R-B -0.6.

**An inverted ground needs a WARM source, and this is the only place that rule applies.**
02's ground is a negative, and inverting flips temperature: a cool frame returns warm, which
is the banned tint. Four of six candidates measured cool and were refused for that alone. The
warm one, +24.1 at the sensor, inverts to **R-B -7.3 at avg saturation 7.8**, and the section
header's contrast on it went up rather than down, 5.74 to **6.73**.

**Black and white is used deliberately in one section: 08.** Both its bands and the ground
under them. The only saturated element across the three frames is the packaging on the shop
shelving, which reads as loose colour rather than documentary, while filing drawers and line
cards are near-neutral as shot and lose nothing. `grayscale(1)` and `saturate()` are both
luminance-preserving, so the exposure and the contrast numbers are identical either way.

**Three more surfaces stay neutral because their own treatment destroys colour, not by
choice.**
Pushed through their windows, a 29-saturation source comes out at:

| surface | treatment | surviving saturation |
|---------|-----------|----------------------|
| 05 ground | window 118 to 168 | 5.7 |
| 05 texture | window 208 to 246 | 4.3 |
| 02 cell veil | contrast 0.45, opacity 0.22 | 14.7, then about 3 after the opacity |

Below perception, and at that lightness they read as pale paper rather than as black and
white. Re-sourcing them would change nothing visible.

## 4a. Photographic grounds

Filter, fixed: `grayscale(1) brightness(0.30) contrast(1.06)`.

Greyscale is a deliberate departure from the Mann Standard's "colour is the default". The
reason is that this is a **ground**, not a picture: a ground carrying colour competes with
the content standing on it. A photograph used as a picture keeps its colour.

Darkening stays on-doctrine: brightness, hard edges, no gradient masks
(`design-system/index.html#imagery`).

**Text tiers on a photographic ground**

- `--c-700` and `--c-800` are forbidden on a photograph. Measured on V2: `--c-700` meta read
  **2.42:1** and an eyebrow at `--c-800` read **3.05:1**. The same tiers are comfortable on a
  flat ground (`--c-800` on cream is 6.14, `--c-700` on black is 6.75) because a flat ground
  has one luminance and a photograph has a worst pixel.
- Small text on a dark photographic ground takes `--c-400`. Measured on the current page:
  worst case **5.85:1** at 08, **7.15:1** at the hero.
- Anything smaller than the `m9` tier does not sit on a photograph at all. It goes on a sheet,
  which is opaque and therefore predictable. This is what the reference does too: its
  annotations live on the white panels, never on the picture.

**Never measure contrast from a thumbnail.** Sample the rendered pixels of the actual filtered
image at a 2px step. A downsampled estimate once returned 7.72:1 where the real render was
3.40:1, because the specular highlight was averaged away.

## 5. The label and value pair

A figure is three lines, never one:

```
(03.1)                  m9,  muted
LTM ADJUSTED EBITDA     m11, muted
C$8.9M                  v,   full strength
```

Class `.sp`. Borrowed from the reference's `(Format)` over `Horizontal`. II sets label and
value on one line, which is right for a dashboard row and wrong for a page whose whole job is
to make three or four numbers legible from across the room.

## 6a. A tier with a floor needs a measure with a floor

`.p` is `max(17px, calc(22 * var(--u)))`, so past roughly 1440 the type stops growing while
the grid keeps widening. A paragraph set to a column span therefore gets more characters per
line the wider the window, and a set of paragraphs that lines up at 1440 comes apart at 1920.

Measured in 07: at 1440 all four paragraphs set to two lines; at 1920 the three shorter ones
collapsed to one and the 180-character one stayed at two.

**Where paragraphs have to agree with each other, cap the measure at the width where the type
stops scaling.** 07's body is `max-width: 760px`. Below 1440 the cap does not bind and the
column stays fluid.

This applies to every prose tier that carries a px floor, not only this one. Cells and panels
elsewhere on the page happen to be narrow enough that it has not bitten yet.

## 6. The spaced header

The section number sits at column 1 and the label starts at column 3. Measured gap at 1440:
**95px**. Previously the two were 20u apart, roughly 11px, which is a heading with a number in
front of it rather than an annotation on a drawing.

---

## The one type value that leaves the II ladder

`.h1`, the hero title only: `max(44px, calc(96 * var(--u)))`, over 10 columns.
V16's display is `max(40px, calc(64 * var(--u)))` over 9.

This is the only display type on either site that stands on a photograph with **no box behind
it**, so its size is its hierarchy. At 8 columns and 76u the title had a 605px measure; at 10
columns and 96u it renders 54.3px across 760px and still sets in two lines. The cream plate
moves to a second row at the right, which is closer to the reference in any case: one large
thing, then one small thing offset beneath it.

**Nothing below `h1` deviates.** Keeping the exception to a single value is what makes it
maintainable. If a second exception is ever proposed, it should be treated as evidence that
the ladder needs a new tier rather than another one-off.

---

## Guidance, not rules

**Ink budget.** Roughly 15 to 20 percent of a section's area as content reads right in this
register. V2 measured 29 percent average and felt crowded. This stays guidance and never a
hard limit, because sections carrying required compliance language will exceed it and must.

---

## What was refused from the reference, and why

Recorded so the next session does not re-propose them.

| Device | Why not |
|---|---|
| Rotated and radial text | unreadable on an issuer's page, and motion-led in the original |
| Circle and triangle cut-outs | masking unrelated to the 12-column system |
| Dashed construction guides | read as "unfinished" |
| Infinite scrolling word lists | motion-led; frozen, they are just clipped words |
| Greying out inactive attributes | on an issuer's page a grey line reads as **missing data**, not "not applicable" |
| Duotone colour treatment of photographs | colour is for emphasis, not for flooding an image |

## What was borrowed, and where it lives

| Device | Where |
|---|---|
| `(Label)` over value | `.sp`, sections 03 04 05 |
| Number at column 1, label far from it | `.eyeb`, every section |
| One large thing, one small thing offset beneath | hero |
| A near-empty field holding one small group | `.voidfield`, section 06 |
| A numbered stack pinned to one edge, the rest left to the picture | `.panel`, section 08 |
| One sheet divided by hairlines rather than detached cards | `.bsheet`, section 02 |
| A picture on one side, the text stacked top to bottom on the other | `.split`, section 03 |
| Number, labelled title, prose as three zones on one line | `.prow`, section 07 |
| A market's numbers against a business's, a rule between, nothing written across it | `.face`, section 05 |
| Equal widths, unequal insides, centre left mostly empty | section 02's three cells |

## Superseded

Section 02 as three horizontal registers, built and rejected 2026-09-05. The CSS is left in
`shared/v3.css` under a `SUPERSEDED` heading so the attempt is on the record. The ruled sheet
won.
