# Stock Page + Memo · V3 Developer Handoff

**Audience:** Engineering team building the II (Intelligent Investing) Stock Page + Memo experience.
**Status:** V3 prototype. Single-textarea memo. Research absorbed onto Stock Page. State sync via localStorage.
**Last updated:** May 26, 2026

---

## 1. Page Map

| Page | File | Purpose |
|---|---|---|
| Handoff landing | `index.html` | Engineering handoff entry. V3 direction + page list + spec links. |
| Stock Page · Returning user | `Stock Page v6d.html` | Canonical. Position held, memo sealed. Main view. |
| Stock Page · First-time user | `Stock Page First.html` | No position, no memo. Same on-page surfaces as v6d. |
| The Memo | `ATZ Memo.html` | Single textarea editor. Auto-save to draft. Seal commits draft → live. |
| The Memo · State Variants | `ATZ Memo Variants.html` | Reference for the three V3 states (Live · Draft · Sealed Empty). |
| User Flow | `User Flow.html` | V3 navigation map. |
| Fiscal AI · ATZ | `ATZ Fiscal.html` | (External) Dedicated data workspace. Linked from Stock Page. |

V2 pages removed: `ATZ AI Research v2.html`, multi-step memo creation flow, Pressure Test drawer.

---

## 2. State Model (Core)

Two `localStorage` keys are the source of truth:

| Key | Purpose | Written by |
|---|---|---|
| `atz-memo-draft` | Work-in-progress textarea content | ATZ Memo auto-save (600ms debounce) |
| `atz-memo-live` | Sealed / committed memo (the public version) | ATZ Memo `sealMemo()` only |
| `atz-memo-state` | Last-known state label (`live` / `draft`) | Both, kept in sync |
| `atz-memo-version` | Increments on every Seal | `sealMemo()` |
| `atz-memo-sealed-at` | ISO timestamp of last seal | `sealMemo()` |

Stock Page v6d reads `atz-memo-live`. ATZ Memo reads `atz-memo-draft` (textarea content) and compares to `atz-memo-live` to determine state.

### 2.1 State Variants

| State | `live` | `draft` | UI |
|---|---|---|---|
| Live | content | content (same as live) | ● Live (green pulse) · "Sealed memo. Editing replaces the live version." |
| Draft | content (old) | different content | ● Draft (static grey) · "Editing the sealed memo. Seal to update." |
| Sealed Empty | `""` (empty) | `""` | Dot hidden · "Sealed empty. Write below to start a new draft." |
| Never Sealed | `null` (or seeded) | `""` | Same as Draft, meta reads "Not yet sealed. Sealing creates the live record." |

### 2.2 State Transitions

```
[Never Sealed] --type--> [Draft] --Seal Memo--> [Live]
                                              <--edit--
                                              [Draft]
                                              
[Live] --erase all--> [Draft (empty)] --Seal--> [Sealed Empty]
[Sealed Empty] --type--> [Draft] --Seal--> [Live]
```

### 2.3 Seeding (Demo)

Both Stock Page v6d and ATZ Memo include a `seedExampleMemoIfMissing()` that runs on load. It populates the example Aritzia memo into `atz-memo-live` and `atz-memo-draft` if `live === null` (truly never seeded).

The seed check uses `!== null`, NOT a truthy check. This preserves the Sealed Empty state (`live === ""`) instead of re-seeding over it.

Stock Page First overrides: on initial session entry (controlled by `sessionStorage['first-time-initialized']`), it explicitly sets both keys to `""` to force the first-time persona.

---

## 3. Stock Page v6d — Section by Section

Single scrollable view. Top to bottom:

### 3.1 Header
Back · Star · Exit. Standard nav. 71px height, hairline border-bottom.

### 3.2 Compliance Strip
`Self-Authored · No Suitability Review · Not Advice`. 9px, c-800, left-aligned. Persistent across all pages.

### 3.3 Title Block
- Line 1: `Aritzia Inc · ATZ` — c-white, 22px
- Line 2: `Last Price 36.95 CAD · +42.6% vs entry` — c-700, 13px

### 3.4 Alert Mirror (`.oq-list`)
Surfaces decision-prompts from the dashboard. Each row:
- Dot (severity color)
- Title (`Q4 earnings posted 14d ago`)
- Action link (`Re-underwrite ›`)
- Dismiss `×` icon (animates out)

Severity colors only: `c-warning #FDAD00` (review), `c-urgent #FF3533` (action required).

### 3.5 Memo Block
Compound section. Doctrine-elevated.

**Status bar:** `The Memo · Compounder · Hurdle 20%` + state badge (right-aligned).

**Content area:**
- Preview: first paragraph of `atz-memo-live`, white-space pre-wrap
- Truncation: cut at first `\n\n` (paragraph break). Fallback: sentence boundary at 360 chars.
- Read More / Read Less toggle (dotted underline, `.mc-toggle`) — expands inline
- When `live === ""`: badge hidden, preview = "Memo cleared. Re-underwrite, or run the Research Prompt below to start again." Read More toggle hidden.

**Footer:** `Reviewed Xd ago` (relative time) + `Re-underwrite` link (right-aligned, 15px).

**Sync triggers:**
- `syncMemoFromStorage()` on initial load
- `pageshow` event (bfcache restore)
- `visibilitychange` event (tab returns to foreground)
- `storage` event (other tab updated localStorage)

### 3.6 Position
Hairline-separated rows. Holdings · Avg cost · Weight (entered → current).
Drill-in: `View Position Detail ›`.

### 3.7 Performance vs S&P
Cumulative return, alpha, drawdown, duration. Two-column rows.
Drill-in: `View Performance Detail ›`.

### 3.8 About Aritzia Inc.
Single short paragraph (3 lines). Baseline company context even when memo is empty.
Drill-in: `Read More on the Company ›`.

### 3.9 Primary Source (compound card)
Two children:
1. **Fiscal AI · ATZ** — nav-row.primary, drill-in to dedicated workspace
2. **Research Prompt · ATZ** — primary-card (3-row compound):
   - **Action row** — title + meta + SVG copy icon (`#copyPromptSymbol`). Tap copies the prompt from `<script id="researchPromptText">`. ⊕ → ✓ for 1.8s + meta text → "Copied. Paste into your AI tool."
   - **Output structure** — accordion. Default collapsed showing `Output · 9 sections · 2,500–3,500 words ›`. Click expands list of 9 numbered sections (Business Overview, Classification, Thesis + Decomposition, Why Now, Kill Criteria, Intrinsic Value, Probability, Deeper Work, Verify on Fiscal). Chevron rotates 90° on open.
   - **Footer row** — `Open in · Claude · ChatGPT · Gemini · Perplexity`. All `target="_blank"`. Hairline divider above.

### 3.10 More Sources
Nav rows: Market · News · History. Currently dead links (`href="#"`).

### 3.11 Capital Decision Footer
Fixed-bottom with fade scrim. `→ Capital Decision`. Currently dead link. Destination is the V3 Classification picker (not yet built).

---

## 4. Stock Page First — Differences from v6d

Same chrome (header, compliance, title). Differences in body sections.

### 4.1 Header
Includes Back · Star · Exit. Star meaningful (no position yet).

### 4.2 Title Block
No `Last Price · +X% vs entry`. Just `Aritzia Inc · ATZ`.

### 4.3 Memo Entry
Replaces v6d's memo block. Row pattern:
- Section header: `Memo`
- Field row: `Write your memo ›` (drill-in to ATZ Memo)
- Hint: `Tip · Run the Research Prompt below first, then paste the AI's response here.`

### 4.4 No Position / Performance Sections
Sections skipped — user has no position yet.

### 4.5 About + Primary Source + More Sources
Same as v6d.

### 4.6 Persona Reset
On initial session entry, Stock Page First explicitly clears memo localStorage:

```js
if (!sessionStorage.getItem('first-time-initialized')) {
  localStorage.setItem('atz-memo-live', '');
  localStorage.setItem('atz-memo-draft', '');
  localStorage.setItem('atz-memo-state', 'draft');
  localStorage.setItem('atz-memo-version', '0');
  localStorage.removeItem('atz-memo-sealed-at');
  sessionStorage.setItem('first-time-initialized', '1');
}
```

This preserves any subsequent edits within the same session.

---

## 5. ATZ Memo — The Editor

Single textarea. The only memo input surface.

### 5.1 Header
Back · Exit links (return to Stock Page v6d).

### 5.2 Title Block
`Memo` (small, c-700) · `Aritzia Inc · ATZ · Hurdle 20%` (large, c-white).
Intentional inversion: the page label is dim, the subject is bright.

### 5.3 Status Section
- Badge row: `● Live` / `● Draft` / (hidden when sealed empty)
- Meta line below: state-specific copy

### 5.4 Textarea
- `min-height: 420px`
- `padding: 16px 16px 56px 16px` (extra bottom space for indicators)
- Border: `0.5px solid var(--c-900)`
- Placeholder: `Write or paste your memo. Run the research prompt on the Stock Page, then paste the AI's response here directly. Edit as you go.`
- `spellcheck="false"`
- Auto-save on `input` event with 600ms debounce → `atz-memo-draft`

### 5.5 In-Frame Affordances
- **Saved status** — `Saving…` / `Saved just now` / `Not started`. Absolute-positioned bottom-left.
- **Paste icon** — SVG paste icon, absolute-positioned bottom-right (right: 26px, clears scrollbar). Click pastes clipboard into textarea.
- **Bottom fade** — `::after` gradient from transparent to `var(--c-black)` masks overlap between scrolling text and the in-frame indicators.

### 5.6 Seal Memo Button
Right-aligned below textarea. `Seal Memo` or `Re-seal Memo` based on `currentVersion > 0`.
On click:
1. `doSave()` — saves draft
2. Copy draft → `atz-memo-live`
3. Update state to `live`
4. Increment version
5. Set `sealedAt` to now
6. Apply state UI

### 5.7 Below Textarea
- Hint: `The first lines show on the Stock Page as a preview. Paste the full AI response if you like. No need to break it into fields.`
- `View Example Memo ›` — inline toggle showing the seeded example memo

### 5.8 Exit Modal
If `hasUnsavedChanges()` and user clicks Back / Exit: modal asks Save Draft & Exit · Discard Changes · Keep Editing.

---

## 6. Design Tokens

### 6.1 Palette
```
--c-black:   #000000  (body bg)
--c-1000:    #1C1C1C  (alt bg)
--c-900:     #232627  (hairlines, separators)
--c-800:     #565B5E  (compliance strip, dim labels)
--c-700:     #929292  (meta text)
--c-400:     #C7C7C7  (body text, values)
--c-white:   #FFFFFF  (primary, titles)
--c-elev:    #0A0A0A  (primary card background — sits between c-black and c-1000)
```

### 6.2 Severity
```
--c-warning: #FDAD00
--c-urgent:  #FF3533
--c-review:  #FBC308
--c-live:    #30D158
```

Only used to signal severity. Never decorative.

### 6.3 Type
- Font: Inter (300, 400, 500)
- Letter-spacing: `-0.02em` on all text
- Tabular nums: `font-feature-settings: 'tnum' 1`
- Title sizes: 22px (page title), 18px (subject), 15px (section title), 14px (body), 13px (label), 12px (meta), 11px (small meta), 9px (compliance)
- Title Case for UI labels (Chicago style). No uppercase except tickers (ATZ) and acronyms (DTC, AI, SOTP, FCF).

### 6.4 Hairlines
- All separators: `0.5px solid var(--c-900)`
- Primary card border: `0.5px solid var(--c-900)`
- Compliance strip border-bottom: `0.5px solid var(--c-1000)`
- No border-radius anywhere

### 6.5 Symbol Grammar
- `›` drill-in (navigate to another page)
- `→` commit / submit (irreversible action)
- `·` separator
- `●` status indicator
- `↺` loopback
- SVG paste icon (two overlapping rectangles) for copy action

---

## 7. Components

### 7.1 Primary Card (`.primary-card`)
Multi-row card on `var(--c-elev)` bg with `var(--c-900)` border. Used for Research Prompt and Fiscal AI.

```html
<div class="primary-card">
  <button class="primary-card-action">...</button>
  <div class="primary-card-structure">
    <button class="pc-structure-toggle">...</button>
    <div class="pc-structure-body" hidden>...</div>
  </div>
  <div class="primary-card-footer ai-tools-row">...</div>
</div>
```

Hairline divider between rows.

### 7.2 Memo Block (`.memo-block`)
Compound card. Status bar → content (preview + Read More toggle) → footer (reviewed + Re-underwrite).

### 7.3 Section (`.section`)
Generic vertical stack with `.section-header` (title + optional meta + optional chevron). `gap: 14px` between header and content.

### 7.4 Nav Row (`.nav-row`)
Single row drill-in. Title + meta + chevron (right). `.nav-row.primary` lifts to `var(--c-elev)` bg with border.

### 7.5 View Link (`.view-link` / `.mc-view-link`)
Small drill-in link. 11px, c-700, single `›` chevron.

### 7.6 Tappable Label (`.lbl-tap`)
Inline expandable definition. Dotted underline (`border-bottom: 0.5px dotted var(--c-800)`). Used for Read More / Read Less.

---

## 8. State Sync — Implementation

### 8.1 Stock Page v6d
```js
seedExampleMemoIfMissing();
syncMemoFromStorage();
window.addEventListener('pageshow', syncMemoFromStorage);
document.addEventListener('visibilitychange', function () {
  if (document.visibilityState === 'visible') syncMemoFromStorage();
});
window.addEventListener('storage', function (e) {
  if (e.key && e.key.indexOf('atz-memo-') === 0) syncMemoFromStorage();
});
```

### 8.2 ATZ Memo
```js
document.addEventListener('DOMContentLoaded', () => {
  seedExampleMemoIfMissing();
  loadDraft();
  ta.addEventListener('input', scheduleAutoSave);
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) loadDraft();
  });
  window.addEventListener('storage', function (e) {
    if (e.key && e.key.indexOf('atz-memo-') === 0) {
      if (document.activeElement !== ta) loadDraft();
    }
  });
});
```

The `activeElement !== ta` guard prevents overwriting the user's in-flight typing when a `storage` event fires from another tab.

### 8.3 Stock Page First
```js
if (!sessionStorage.getItem('first-time-initialized')) {
  // reset memo keys ...
  sessionStorage.setItem('first-time-initialized', '1');
}
```

---

## 9. Animations

### 9.1 Live Pulse
```css
@keyframes live-pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
animation: live-pulse 2.4s cubic-bezier(0.45, 0, 0.55, 1) infinite;
```

Applied to `.memo-state.live .state-dot`. Respect `prefers-reduced-motion`.

### 9.2 Active State
```css
.X:active { opacity: 0.5; transition: opacity 80ms ease; }
```

Standard for all tappable elements.

### 9.3 Chevron Rotation
```css
.pc-structure-chev { transition: transform 160ms ease; transform: rotate(0deg); }
.primary-card-structure.open .pc-structure-chev { transform: rotate(90deg); }
```

---

## 10. MVP Scope

Ship V3 with these guarantees:

✓ Stock Page v6d displays sealed memo content.
✓ ATZ Memo accepts free-form text, auto-saves to draft, seals on click.
✓ Seal commits draft → live, propagates to Stock Page.
✓ Edits to live memo do NOT propagate to Stock Page until Re-seal.
✓ Research Prompt copies on tap (clipboard or fallback).
✓ 4 AI tool links open in new tabs.
✓ Compliance strip on every page.
✓ State syncs across tabs and after bfcache restore.
✓ First-time persona starts with truly empty memo.

Post-MVP (V2):
- Hurdle picker UI (15 / 20 / 25 / 30 / 50%+)
- Capital Decision destination (Classification picker)
- Triggered / Stale / Closed memo states
- Per-tranche shadow benchmarking
- Re-underwriting threshold policy
- Multi-tab conflict resolution beyond last-write-wins

---

## 11. Mock Data

The example memo seeded into localStorage is hardcoded in both `Stock Page v6d.html` and `ATZ Memo.html` (see `seedExampleMemoIfMissing()` in each). Same string, different copies for resilience if pages are opened independently.

The seed includes Classification, Thesis, Why Now, Kill Criteria, Intrinsic Value, Sizing, Sources — formatted as prose with section labels, separated by `\n\n`. Total ~2,000 chars.

Sealed-at timestamp is set to "26 days ago" on seed so "Reviewed 26d ago" appears realistic.

---

## 12. Open Questions

Surface here. Resolve in V2 spec.

1. **Hurdle picker** — UI, persistence, scope (per-memo vs per-portfolio).
2. **Capital Decision page** — what does it lead to.
3. **Re-underwrite threshold** — how stale before UI escalates.
4. **Multi-tab conflict** — last-write-wins acceptable for V1.
5. **Persona transition** — First → seal memo → back to First. Redirect to v6d, or render whatever localStorage holds.
6. **About section depth** — "Read More on the Company" leads where.
7. **Performance section on freshly-entered position** — hide until 90 days, or render with "Insufficient signal yet" meta.
8. **Storage failure** — surface user-visible warning when persistence fails.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     