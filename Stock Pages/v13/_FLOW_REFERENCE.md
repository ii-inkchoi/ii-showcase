# v11 Stock Page — Flow Reference & Audit

**Status:** v11 (Post-MVP) · audit as of 2026-06-05
**Owner:** Inkyung Choi (Stock Page scope) · Rio (Memo Flow scope)
**Purpose:** Single source of truth for v11 — flow architecture, state contracts, LS schema, known bugs. Used as context anchor for future sessions.

---

## 1. Project Context (the why)

v11 is the Post-MVP iteration of the Stock Page + Memo system. It implements the chairman's June 4 2026 directives:

1. **No user-facing Active/Core toggle** — system auto-routes via symbol whitelist. Two categories only: **Active Allocation** (e.g., ATZ) or **Core / Treasury Allocation** (e.g., VFV).
2. **Memo = draft until Capital Decision** — user can freely create, edit, save partial, or delete memos. Only when they go through Capital Decision flow does it become an immutable version (V1, V2, …).
3. **Two independent flows:**
   - **Memo Flow** (this file's authoring) — pure draft editing (Stock Page → Underwrite → Blank Memo → Edit pages → Save & Return).
   - **Capital Decision Flow** (Rio's scope, currently stubs) — review current draft → walkthrough missing fields → commit modal → immutable memo + buy/sell.

Chairman quotes (canonical):
> "Experiment with these memos and edit the memo and delete the memo when it's not tied to a capital decision. Once you do a memo that's tied to a capital decision, then it's immutable." — 2026-06-04 16:35:56
>
> "I clicked capital decision, I had to go through five screens and then boom, screen six. That's the money shot." — 2026-06-04 16:56:38
>
> "Your draft memo currently only includes two sections filled in, that's the first thing you see. If you say, no, this is all good, I continue, then it's gonna bring you to the next step, which is the next piece that you haven't filled in." — 2026-06-04 16:35:56

---

## 2. File Inventory

### Stock Page side (Inkyung's scope)
- `Stock Page Firsttime User.html` — no memo, no position (Active)
- `Stock Page Firsttime User (Core).html` — Core variant (VFV)
- `Stock Page Memo Only.html` — V1 memo, no position (Active)
- `Stock Page Memo Only (Core).html` — Core variant
- `Stock Page Return User.html` — V1 + held position (Active)
- `Stock Page Return User (Core).html` — Core variant
- `Stock Page Return User - History.html` — V50 + held (Active)
- `Stock Page Return User - History (Core).html` — Core variant
- `Stock Page Multi-Quarter Alerts.html` — V1 + held + 3 quarter alerts (Active)
- `Blank Memo.html` — Draft entry point, pure memo editor (Active only — Core memo is single-stance handled elsewhere)
- `Edit Classification.html`, `Edit Sizing.html`, `Edit Probability.html`, `Edit Idea Origin.html`, `Edit Memo.html` — 5 single-field edit pages (Save semantics, no page numbers)
- `Example Memo.html` — reference (ATZ V1 demo)
- `index.html` — entry index with 5 sections (Active, Core, Memo Flow stubs, Edit pages, Reference)

### Rio scope (currently stubs from `_placeholder.html`)
- `First-time Memo Flow.html`
- `Firstime user_Memo Review.html`
- `Return user_Memo Review.html`
- `Return user_Memo Review (Core).html`
- `Memo Intro.html`
- `User Flow.html`

---

## 3. Canonical User Flows

### Flow A — First-time user creates and commits a memo (Active)

```
1. index.html → "Firsttime User (ATZ)"
2. Stock Page Firsttime User (blank, no LS) — rows show "—", Underwrite CTA visible
3. Tap "Underwrite" → sessionStorage[atz-memo-stock-source] = stock page URL
4. Blank Memo (Draft) — 5 rows, all "—", Save & Return locked, no Delete
5. Tap a row, e.g., "Classification" → sessionStorage[atz-memo-source] = Blank Memo URL
6. Edit Classification — select "Compounder" → Save → LS[atz-memo-classification] = "Compounder"
7. Return to Blank Memo — row populated with "Compounder ›". Save & Return now active.
8. Continue: tap other rows, save each, OR tap "Save & Return"
9. Save & Return → LS[atz-memo-draft-progress] = N → Stock Page (Firsttime User)
10. Stock Page now shows:
    - Memo card rows reflect partial values (Idea Origin = "13F", Classification = "Compounder", etc.)
    - "Draft · N of 5 fields" indicator + "Resume Draft ›" CTA label
11. Tap "Resume Draft" → back to Blank Memo with values preserved → continue or finish
12. When ready: Tap "Capital Decision" CTA (sticky bottom of Stock Page) — Rio's flow
13. (Rio scope) Capital Decision Review → walkthrough missing → commit modal "Create V1?"
14. Confirm → LS[atz-memo-version] = "V1", immutable, transitions to Memo Only / Return User state
```

### Flow B — Discard draft

At any point in Blank Memo with ≥1 field filled:
1. Tap "Delete draft" (left of sticky CTA bar)
2. confirm() → wipes all LS draft fields
3. Returns to Stock Page (Firsttime User) blank state

### Flow C — Exit without saving

In Blank Memo or any Edit page:
1. Tap `‹` (back chevron) or `Exit` — does NOT modify LS
2. Routes to sessionStorage[atz-memo-stock-source] (Blank Memo) or sessionStorage[atz-memo-source] (Edit pages)
3. Any value saved before this exit point persists

### Flow D — Core·Treasury memo (VFV)

Same shape as Flow A but:
- Stock Page Firsttime User (Core) is the entry
- Blank Memo would route to a Core variant (currently uses same Blank Memo.html — Core Blank Memo not yet built; this is a gap)
- Edit pages would be 2 (Role + Target) instead of 5
- Decision = "Core / Treasury Allocation"

**Gap:** Core Blank Memo page does not exist. Underwrite from Stock Page Firsttime User (Core) currently routes to the Active Blank Memo. This is a known TODO.

---

## 4. State Matrix per Page

### Stock Page Firsttime User (Active)
| State | LS Preconditions | UI | Navigation Out |
|---|---|---|---|
| Blank (S0) | no `version`, no `notes` | All rows "—", CTA="Underwrite", no draft indicator | Underwrite → Blank Memo |
| Notes only (S1) | no `version`, `notes` exists | Same as S0, notes textarea pre-filled, `is-saved` | Same |
| Draft resumed | no `version`, `draft-progress > 0` | Saved fields rendered; empty stay "—". "Draft · N of 5" indicator. CTA="Resume Draft" | Resume → Blank Memo |
| Filled (committed) | `version = V1` | Filled memo card with all values, Re-underwrite CTA | Re-underwrite → Memo Review (Rio) |

### Blank Memo (Draft)
| State | LS Preconditions | UI |
|---|---|---|
| Not started | 0 of 5 LS keys set | Status = "Draft · Not started". Save & Return locked. Delete hidden. |
| Partial (N of 5) | 1–4 fields set | Status = "Draft · N of 5 fields". Save & Return active. Delete visible. |
| Full draft | All 5 fields set | Same as partial — still a draft (no version) |

### Stock Page Memo Only (Active)
- Always filled state (seeded with V1 ATZ memo on fresh entry)
- Memo card hydrated from LS via `reflectStockMemo()`
- No position section → "No position yet" empty state
- Capital Decision CTA → Memo Review (Rio) `?mode=cd`

### Stock Page Return User (Active)
- Filled + held position
- Memo card + Position section + Performance vs S&P 500
- Capital Decision opens bottom sheet (Increase / Reduce / Exit)

### Stock Page Return User - History (V50)
- Filled + 50-version history seeded
- "50 versions ›" link in memo card
- Same Capital Decision sheet as Return User

### Stock Page Multi-Quarter Alerts
- Filled + held + 3 pending quarterly alerts above memo
- Alert dismissal is DOM-only (no LS) — known gap

### Stock Page Core variants
- Memo card shows only Role + Target rows
- Decision = "Core / Treasury Allocation" (header label, not row)
- Performance row: VFV vs S&P 500 (tracking, near-zero difference)
- Capital Decision sheet → `Capital Decision Review.html` (Rio scope)

---

## 5. LS Schema (canonical)

### Active Allocation memo
| Key | Type | Values | Owner |
|---|---|---|---|
| `atz-memo-classification` | string | "Compounder" / "Emerging compounder" / "Situational mispricing" / "Speculative" | Edit Classification (write) |
| `atz-memo-sizing` | string | "Core" / "Conviction" / "Starter" / "Speculative" | Edit Sizing (write) |
| `atz-memo-probability` | string (int) | "10"–"100" | Edit Probability (write) |
| `atz-memo-horizon` | string | "1 yr" / "3 yrs" / "5 yrs+" | Edit Probability (write) |
| `atz-memo-idea-origin` | string | "Social media" / "Screener" / "Podcast" / "Newsletter" / "Friend" / "13F" / `Other: <user text>` | Edit Idea Origin (write) |
| `atz-memo-memo` | string | Multi-line prose (Investment Case) | Edit Memo (write) |
| `atz-memo` | string | Legacy duplicate of memo (backward compat) | Auto-mirror on commit |
| `atz-memo-draft-progress` | string (int) | "0"–"5" — count of filled fields | Blank Memo Save & Return (write) |
| `atz-memo-decision` | string | "Active Allocation" / "Core / Treasury Allocation" | Set on commit by Rio flow |
| `atz-memo-version` | string | "V1", "V2", … | Set only on commit (Rio) |
| `atz-memo-history` | JSON array | Array of snapshots | Set on commit (Rio) |
| `atz-memo-stance` | string | "active" / "core" | Set by seed or commit |
| `atz-memo-demo-schema` | string | Per-page schema tag (`firsttime-v0`, `memo-only-v1`, `return-v1`, `return-v50`, `multi-quarter`, `memo-only-core`) | Set by seed |
| `atz-memo-notes` | string | Light notes scratchpad (legacy V1 notes feature) | Stock Page Notes (still present in some pages) |
| `atz-memo-user-created` | string | "true" if user explicitly created — prevents re-seed | Stock Page write |

### Core·Treasury memo
| Key | Type | Values |
|---|---|---|
| `atz-memo-role` | string (enum) | "liquidity" / "index" / "bond" / "cash" / "yield" |
| `atz-memo-target-weight` | string (int %) | "1"–"100" |
| (Active keys above) | — | Wiped/absent in Core mode |

### sessionStorage
| Key | Set by | Read by |
|---|---|---|
| `atz-memo-stock-source` | Stock Page Underwrite/Resume CTA | Blank Memo goBack |
| `atz-memo-source` | Blank Memo row tap | Edit pages goBack / onSave |
| `atz-blank-stance` | Stance toggle (legacy) | Restore stance — mostly dead in v11 |
| `atz-cd-action` | Capital Decision CTA | Rio's review page |

---

## 6. Bug Inventory (from audit 2026-06-05)

**Status as of 2026-06-05 (post J26/J27/J28):**
- ✅ All Critical (C1–C5) fixed
- ✅ All Medium (M1–M6) fixed
- ✅ User-facing Low (L4 capitalization, L5 breadcrumb, L6 Attach disabled, L7 paste toast) fixed
- ⏸ Remaining Low (L1 dead stance toggle JS, L2 latent Decision swap, L3 Aritzia comments, L8 source clear, L9 hardcoded weight, L10 dead arrays) — backlog. JS no-ops or unreachable code paths only.

### CRITICAL — fix before next demo
| # | Page | Issue | Fix direction |
|---|---|---|---|
| **C1** | Return User - History.html | Duplicate `<script id="researchPromptText">` blocks (lines 934 + 1158). Invalid HTML, regression of G38. | Remove the duplicate (truncated) block |
| **C2** | All 4 Core files | Active `researchPromptText` Aritzia/ATZ block remains as dead code in single-stance Core pages | Delete or replace content with VFV |
| **C3** | Return User - History (Core).html | TWO `researchPromptText` blocks (lines 918, 1139), both Aritzia text | Same as C1 + C2 |
| **C4** | Return User (Core).html | Dismiss callback uses undefined `list` variable (line 1083–86) — JS ReferenceError when X tapped | Restore the missing declaration |
| **C5** | Memo Only (Core).html | Capital Decision CTA routes to `Firstime user_Memo Review.html` (Active flow) instead of Core review | Change href to `Return user_Memo Review (Core).html?mode=cd` |

### MEDIUM
| # | Page(s) | Issue |
|---|---|---|
| **M1** | Memo Only, Return User, Return User - History, Multi-Quarter Alerts | Q4/quarterly alert "Re-underwrite" CTA points to `Firstime user_Memo Review.html` instead of `Return user_Memo Review.html` (`Return user_Memo Review (Core).html` for Core) |
| **M2** | Memo Only, Return User, Multi-Quarter (Active) | Corruption guard wipe lists omit `atz-memo-draft-progress` and (inconsistently) `atz-memo-notes` |
| **M3** | Edit Probability.html | Save button never `.locked` — inconsistent with other 4 Edit pages. Allows committing default values (70% / 3 yrs) without user interaction |
| **M4** | Blank Memo.html | Dead notes handler code remains (onNotesInput, saveNote, FIELD_KEYS.notes) — UI removed but JS surface area persists |
| **M5** | Memo Only, Return User, History (Core) | Q4 earnings concept inappropriate for an index ETF (VFV has no quarterly earnings) |
| **M6** | Memo Only (Core) | Active stance else-branch in reflectStockMemo (lines 993–1036) is dead code in single-stance Core page |

### LOW (cleanup)
| # | Page(s) | Issue |
|---|---|---|
| **L1** | Firsttime User, Firsttime (Core), Memo Only, Memo Only (Core), Return User, Return User (Core) | Large dead code blocks: setStance, restoreStance, uwRowsCore selectors, mr-active/mr-core toggle JS — survive after single-stance cleanup |
| **L2** | Firsttime User | Decision row swap code targets `:first-child .uw-val` (now Classification) — latent bug if Core decision string ever appears in LS |
| **L3** | Core files (Return User, History) | Aritzia leftover CSS/HTML/JS comments |
| **L4** | All Edit pages | Hero "Active allocation" sentence-case vs Blank Memo "Active Allocation" title-case — inconsistent capitalization |
| **L5** | Edit Idea Origin | Breadcrumb composition includes probability + horizon with trailing space if horizon missing |
| **L6** | Edit Memo | Attach button is silent no-op (no visual disabled state, no toast) |
| **L7** | Edit Memo | `navigator.clipboard.readText()` rejection only focuses textarea — no user-visible failure feedback |
| **L8** | All Edit pages | sessionStorage `atz-memo-source` never cleared — stale source could route incorrectly on direct entry |
| **L9** | History (Active + Core) | Sizing meta hardcoded "· 12.2%" in JS — doesn't reflect actual portfolio weight per version |
| **L10** | History | Active V50 dead arrays (probs/horizons/classifications/sizings) declared but unused in Core variant |

### EDGE CASES (worth flagging)
- **Cross-page navigation contamination:** First-time partial draft → other seed page → back to First-time. Some pages' wipe lists omit `atz-memo-draft-progress` (M2), creating orphan draft indicator UI. Safe in normal index-mediated navigation.
- **Stance schema corruption guard:** All 4 seed pages check `version` against `/^V\d+$/` and wipe if invalid. Defensive — good.
- **Capital Decision routing per state:**
  - Firsttime User → `First-time Memo Flow.html?intent=buy` (Rio stub)
  - Memo Only → `Firstime user_Memo Review.html?mode=cd` (Rio stub)
  - Return User → bottom sheet (Increase/Reduce/Exit) → `Capital Decision Review.html`
  - This routing matrix is **not yet enforced** by Rio's stubs

---

## 7. Open Work / Rio Dependencies

### Rio scope (Memo Flow pages)
1. **Memo Intro.html** — instructions/example/workflow before user enters Blank Memo (Dave directive: "instructions, example, memo")
2. **First-time Memo Flow.html** — Capital Decision flow for empty draft (5 screens + 6th money-shot screen)
3. **Firstime user_Memo Review.html** — Capital Decision flow for memo-only state, with `?mode=cd` query
4. **Return user_Memo Review.html** — Re-underwrite / Capital Decision flow for held position
5. **Return user_Memo Review (Core).html** — Core variant
6. **Capital Decision Review.html** — Generic review used by Return User CD sheet selections

All currently identical to `_placeholder.html` template — display "Built by another designer" message.

### Stock Page side TODOs
1. **C1–C5 critical bugs** — fix before next demo
2. **Core Blank Memo page** — currently Active Blank Memo handles both (gap)
3. **Memo Only / Return User Core pages** — VFV demo content cleanup (mostly done, but C4 dismiss bug remains)
4. **Edit Probability Save lock logic** — match other Edit pages' pattern (M3)
5. **Quarterly alert persistence** — currently DOM-only dismissal (B11/M-related)
6. **Position section LS-backing** — Market Value / P&L / weight hardcoded; flag for real implementation
7. **Schema-wipe consistency** — unify wipe-list across all seed pages (M2)

---

## 8. Doctrine Anchors

Per `Doctrine/Stock Page + Memo - v10 Update (June 2026).md`:

- **§43** Active / Core — Stance Toggle (now system-routed per v11 directive)
- **§44** lbl-tap Pattern — Universal Tap-to-Learn (dotted underline + info-panel)
- **§45** Investment Case — Naming + Visual Hierarchy
- **§46** Notes — Inline Editable, Single-Text V1 (now removed from Blank Memo per J17)
- **§47** Memo Block Architecture — S3/S4 Field Hierarchy (now: Classification → Sizing → Probability → Idea Origin → Investment Case, IC always last per J18)
- **§48** Research Prompt Card — Operational Pattern
- **§53** Self-Audit Workflow — 7-point checklist
- **§55** Snapshot-Diff-Report Protocol — mandatory for structural changes

Per **2026-06-04 chairman directive (this v11)**:
- Decision row removed from Stock Page memo cards — replaced with header category label (J16)
- Idea Origin row added — sourced from Rio's 5/6 Source page (J17/J18)
- Capital Decision CTA removed from Blank Memo (Draft) — lives only on Stock Page (J23)
- Save & Return semantics on Blank Memo (Draft) — pure draft persist, no commit
- Stock Page blank state hydrates partial draft + "Resume Draft" CTA + "Draft · N of 5" indicator (J24)

---

## 9. Quick Reference — what to read first when returning

1. This file (`_FLOW_REFERENCE.md`) — overall architecture
2. `Doctrine/Stock Page + Memo - v10 Update (June 2026).md` — foundational doctrine
3. Latest chairman transcripts in `uploads/` (search for "capital decision" or "memo draft")
4. `Blank Memo.html` — read header comment block for draft semantics
5. `Stock Page Firsttime User.html` lines 540–680 — renderMemo() blank-state hydration logic
6. `Edit Idea Origin.html` — reference implementation of single-field Edit page with Other inline pattern

---

## 10. Glossary

- **Active Allocation** — Position where user claims edge over S&P 500. 5 memo fields. ATZ = demo.
- **Core / Treasury Allocation** — Diversification / liquidity / long-term compound. 2 fields (Role + Target). VFV = demo.
- **Draft** — Memo state before Capital Decision commit. Freely editable, deletable, partial allowed.
- **Immutable memo** — Memo after Capital Decision commit. Has version (V1, V2, …). Cannot be edited or deleted; only superseded by new version.
- **Capital Decision** — The flow that takes draft → walkthrough missing → commit modal → immutable + (buy/sell).
- **Re-underwrite** — Same flow as Capital Decision minus buy/sell — used to version-up an existing memo.
- **Capital Decision Review** (Rio scope) — The page that shows "you have N of 5 filled, continue?" before walkthrough.

---

End of v11 Flow Reference. Update this file when adding tasks (J26+) that alter flow architecture or LS schema.
