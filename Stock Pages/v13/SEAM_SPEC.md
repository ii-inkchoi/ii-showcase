# SEAM_SPEC — Stock Page ↔ Capital Decision Handoff

**For:** the designer building the *post–Capital Decision* pages
**From:** Inkyung (Stock Page)
**Last updated:** 2026-06-08 · v13

---

## 1. One-line summary

Clicking the **"Capital Decision" / "Underwrite" button is the handoff line** between us.
- **Built by Inkyung (done):** the Stock Page + writing the memo draft — everything *before* the click.
- **Built by you (to build):** everything *after* the click — review → walkthrough → commit → buy/sell.
- **Shared:** the single-field editors (see §5) — opened while writing the draft, but the same fields are filled again in your walkthrough.

The `index.html` sidebar is grouped the same way. **The "Capital Decision onward" files (First-time Memo Flow, Memo Review, Select Account) are placeholders I built only to show the flow — they're yours to rebuild. Reference only.**

---

## 2. The handoff line — which Stock Page goes where

| From (Stock Page · built by Inkyung) | State | Button | To (you build this) |
|---|---|---|---|
| Firsttime User | no memo | "Underwrite" | `First-time Memo Flow.html?intent=buy` |
| Memo Only | V1, no position | "Capital Decision" | `Return user_Memo Review.html` |
| Return User | V1 + held | "Capital Decision" → bottom sheet (Increase/Reduce/Exit) | `Return user_Memo Review.html` → `Select Account.html` |
| Multi-Quarter / History (V50) | V1+ held | same | `Return user_Memo Review.html` |
| **Core variant (VFV)** | same as above | same | `Return user_Memo Review (Core).html` |

> Firsttime enters with `?intent=buy`; the rest pass state via sessionStorage (see §3).

---

## 3. State contract (what your pages read / write)

### Already set when your page opens (you READ)
**sessionStorage (temporary):**
- `atz-cd-action` — the Capital Decision action (set by the Stock Page button)
- `atz-cd-mode` — review mode
- `atz-memo-stock-source` — the Stock Page URL to return to (use on back/cancel)
- `atz-ft-intent` — Firsttime's `intent=buy`, etc.

**localStorage (the draft, as it stands at entry):**
- `atz-memo-classification` / `atz-memo-sizing` / `atz-memo-probability` / `atz-memo-horizon` / `atz-memo-idea-origin` / `atz-memo-memo` — the 5 memo fields (Active)
- `atz-memo-role` / `atz-memo-target-weight` — the 2 Core fields
- `atz-memo-draft-progress` — "0"–"5", number of filled fields
- `atz-memo-stance` — "active" / "core"

### Write on commit to lock the memo (you WRITE)
- `atz-memo-version` = `"V1"` (or V_N+1) ← **set this and the Stock Page shows the "committed" state**
- `atz-memo-history` = JSON array (push a snapshot)
- `atz-memo-decision` = `"Active Allocation"` / `"Core / Treasury Allocation"`
- on a position change, `atz-position-status` = `"held"`, etc.

> Core rule (chairman): **a memo is a draft — freely editable/deletable — until Capital Decision. The moment Capital Decision commits, it becomes locked (gets a version, can't be edited or deleted, only replaced by a new version).**

Full key list: `_FLOW_REFERENCE.md` §5.

---

## 4. Vocabulary (do not change — same words on both sides)

| First commit | Re-commit | View trail | Prose label | Toggle |
|---|---|---|---|---|
| **Underwrite** | **Re-underwrite** | **Underwriting record** | **Investment Case** | **Read Full Memo** |

- Position: **Held / Exiting / No position**
- Action: Underwrite / Re-underwrite / Re-underwrite + Buy·Reduce·Exit / Buy / Reduce / Exit
- AI/system insight is marked with the `//` Mogo wedge icon — never the word "AI".
- "Five screens then boom, screen six = the money shot" (chairman) — review → walkthrough (missing fields only) → commit.

---

## 5. File map (this folder)

**Built by Inkyung — done. Connect to these; please don't edit:**
- `Stock Page *.html` (9: Active + Core × Firsttime / Memo Only / Return User / History / Multi-Quarter)
- `Blank Memo.html` — where the draft is written
- `Memo History.html` — Underwriting record (version trail)
- `Example Memo.html` — ATZ V1 reference

**Shared — single-field editors. Used in the draft, but you own the look:**
- `Edit Classification / Sizing / Confidence / Idea Origin / Investment Case / Role / Target Weight`
- These open from `Blank Memo` while writing the draft. But the **same fields are filled again in your Capital Decision walkthrough**, so they belong to both flows. **You're the design reference for how a field input looks** — if you redesign a field screen, please update the matching Edit page too (or flag me).

**Built by you — to build (currently my placeholders):**
- `First-time Memo Flow.html` — Capital Decision for an empty draft (5+1 screens)
- `Return user_Memo Review.html` / `(Core).html` — held-position re-underwrite / review gate
- `Select Account.html` — account selection (capital action)

**Docs:**
- `index.html` — full viewer (grouped by who built what)
- `_FLOW_REFERENCE.md` — architecture, flows, key list (read this first)
- `_SCENARIOS.md` — per-state scenarios
- `HANDOFF.md` — v13 change log
- `SEAM_SPEC.md` — this document

---

## 6. Where to start

1. Open `index.html`, click through the Stock Page screens to feel the flow.
2. Read `_FLOW_REFERENCE.md` §3 (flows) + §5 (keys).
3. On each Stock Page, the "Capital Decision" / "Underwrite" button routes to the file in the §2 table — the sessionStorage/localStorage at that moment is the contract in §3.
4. Build the review → walkthrough → commit pages from there. On commit, set exactly the WRITE keys in §3 and the Stock Page updates itself.
5. Keep the field editors (§5 Shared) consistent with your walkthrough, and keep the vocabulary (§4) fixed.

---

## 7. Known open items (FYI)

- **No Core Blank Memo** — Firsttime User (Core)'s Underwrite currently routes to the Active Blank Memo (gap; `_FLOW_REFERENCE.md` §3 Flow D).
- The `atz-memo-probability` key is unchanged even though its label became "Confidence" (rename not applied).
