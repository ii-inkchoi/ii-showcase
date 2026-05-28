# V4 Handoff Note

Snapshot for continuing V4 work in a fresh conversation. All files in `v4/` are the current state.

---

## V4 Direction (from CEO meeting 2026-05-26)

Two meeting transcripts available in user uploads:
- `2026-05-26 16-02-34.txt` — Performance + memo simplification
- `2026-05-26 16-44-39.txt` — Memo page details

Core principle: **serious operator tone**. Strip instructional copy. Trust the user. Simpler than V3.

---

## Completed in V4

| Area | Change |
|---|---|
| Folder | `v4/` created from `v3/` base |
| **ATZ Memo.html** | Seal Memo button removed · example panel split to separate page · all hints removed · exit modal removed · top `Example Memo ›` chevron drill-in · placeholder = "Write or paste your memo" · single localStorage key `atz-memo` · no draft/live separation |
| **Example Memo.html** (new) | Standalone page with full prose example. Back to Memo. |
| **Stock Page v6d Memo block** | Layout (d) — `The Memo ›` title row + meta row `Compounder · Hurdle 20% · Probability 62%`. Whole block is drill-in link. |
| **Research Prompt card** | `· ATZ` suffix removed · "Tailored to ATZ..." instructional copy removed · Output structure accordion removed · AI tools `Open in` label removed · SVG copy icon kept |
| **AI tools row** | Just `Claude · ChatGPT · Gemini · Perplexity` separated by `·` |
| **Copy feedback** | Inline `Copied` text next to title (c-700, 13px, 1.8s fade) · preserves title identity |
| **Stock Page First** | Same Research Prompt / AI tools transforms · "Tip · Run the Research Prompt" hint removed · placeholder = "Write or paste your memo" · sessionStorage `first-time-initialized` flag · single key |

---

## Still To Do (V4)

### 1. Performance Match-Mirror model (biggest)
CEO described in detail (2026-05-26 16:02). Apply to `Stock Page v6d.html` Performance section.

**What changes:**
- Label: "All Accounts" prefix, "Match-Mirror" methodology disclosure
- Show both `%` AND `$` (e.g., `+42.6%  +5,652 CAD`)
- Simple total return (not annualized) in V1
- ETF: VFV.TO (Vanguard S&P 500, CAD unhedged). Caveat: ETF doesn't include dividends.
- Methodology one-liner: "Match-mirror — same CAD amount allocated to S&P 500 ETF at each deposit date"
- Detail page (`ATZ Performance Detail.html` — needs to be created or updated): deposit-by-deposit math

**Direct quotes from CEO:**
> "Match mirror comparing for each external deposit and in kind of the same CAD amount is allocated to S&P 500. At the dates closed, converted to CAD"
> "This isn't annualized. This is just total returns"
> "You see the return as well as the dollar impact"
> "We can just always have a thing saying all accounts always all accounts"

### 2. Common Ranges language
Find where "Common Ranges" appears (likely in Position or Memo creation flow). Replace with `~10% · ~5% · ~1%` pattern using approximately symbol. CEO said: *"approximately 10% approximately 5% approximately 1% to use the approximate symbol and then you go these are just common ranges not meant to be prescriptive"*

### 3. About Aritzia section
Currently on `Stock Page v6d.html`. Decide whether to keep (V3 doctrine: yes, baseline context) or remove (V4 even more minimal). User has not weighed in.

### 4. User Flow + Memo Variants V4 reflection
`User Flow.html` and `ATZ Memo Variants.html` still describe V3 state. Update for V4 (no Seal, single key, Example Memo as separate page).

### 5. Documentation
`README.md`, `DEV_HANDOFF.md`, `RATIONALE.md`, `EDGE_CASES.md` all in V3 state. Need V4 rewrite or appended V4 update section.

---

## Doctrine Refresher

- Palette: `c-black #000 · c-1000 #1C1C1C · c-900 #232627 · c-800 #565B5E · c-700 #929292 · c-400 #C7C7C7 · c-white #FFF`
- Severity colors: warning amber, urgent red, review yellow, live green (`--c-live #30D158`)
- Elevation: `--c-elev #0A0A0A` for primary cards
- Hairlines: `0.5px solid var(--c-900)`
- Title Case (Chicago). No uppercase.
- Symbols: `›` drill-in · `→` commit · `·` separator · `●` status · `↺` loopback · SVG paste icon for copy
- No em-dashes in UI copy (em-dashes OK inside Research Prompt text sent to AI)
- Inter font, `-0.02em` letter-spacing, tabular nums

---

## File Inventory (`v4/`)

| File | Status |
|---|---|
| `index.html` | V3 state, needs V4 update |
| `Stock Page v6d.html` | V4 main transformations done · Performance section still V3 |
| `Stock Page First.html` | V4 main transformations done |
| `ATZ Memo.html` | V4 stripped · auto-save only |
| `Example Memo.html` | New, V4 |
| `ATZ Memo Variants.html` | V3 state |
| `User Flow.html` | V3 state |
| `README.md` | V3 state |
| `DEV_HANDOFF.md` | V3 state |
| `RATIONALE.md` | V3 state |
| `EDGE_CASES.md` | V3 state |
| `_HANDOFF.md` | This file |

---

## Restart Instructions

In a fresh Claude conversation, share or reference this file. Then say:

> "V4 작업 이어가자. _HANDOFF.md 참고. 다음은 Performance Match-Mirror 모델 적용."

(or whichever item from "Still To Do" comes next.)
