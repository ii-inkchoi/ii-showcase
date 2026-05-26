# Stock Page Family — Edge Cases

Two states are currently mocked: first-time user (`Stock Page First.html`) and standard recurring user with intact thesis (`Stock Page v5.html`). The Comparison file shows them side by side. This document enumerates the other states the system must answer to and ranks them by priority for the next round of mockups.

---

## State Map

The stock page sees one ticker through the eyes of one user. The user's relationship with that ticker progresses through a lifecycle. Each lifecycle position implies a different page composition.

```
DISCOVERY → WATCH → DRAFT MEMO → COMMIT → HOLD → REVIEW → EDIT → CLOSE
   (no memo, no position)      (memo + position exist)       (position closed,
                                                              memo retained)
```

The recurring-user mockup occupies the **HOLD** position with the thesis intact. The first-time mockup occupies **DISCOVERY**. Everything else is unmocked.

---

## Priority 1 — Thesis Status Variants

The status indicator (`Kill Criteria · 0 of 3 firing`) currently has one state. The doctrine declares three. Two of them need mockups.

**1A. One trigger approaching** — `Kill Criteria · 1 of 3 approaching`
- Color: `c-400` (slightly louder than the intact c-700)
- Body prose: same content, but the prose now reads with one true and two false embedded — the user must read carefully to identify which condition is the live concern
- Most realistic edge case in practice — positions slide into this state quietly
- Without a mockup, the warning state is just a CSS class waiting to be invoked

**1B. Multiple triggers firing** — `Kill Criteria · 2 of 3 firing` or `3 of 3 firing`
- Color: `c-white` (decision-forcing)
- The Capital Decision CTA at the bottom needs to feel like an obvious next step, not a suggestion
- Open question: does the page surface a "Close Position" affordance more prominently when in this state, or does it leave the decision to Capital Decision flow?
- Doctrine pull: II treats every position close as a deliberate act, so the answer is probably "no shortcut" — but worth mocking to confirm the friction holds at the breaking point

---

## Priority 2 — Memo Lifecycle Variants

The memo is the spine of the page. Its state changes how the page reads.

**2A. Memo drafted but not sealed** — V0 / Draft state
- User started writing but didn't complete the ten-field protocol
- No position yet
- Page should resume drafting where left off, not start over
- Capital Decision CTA inactive or removed — there is no decision to make until the memo seals
- Open question: is a draft memo visible to the recurring-user flow, or only the first-time flow?

**2B. Memo sealed, no position** — Wrote but waited
- User completed the memo, ran the protocol, then declined to buy
- Memo lives in the record
- Position section absent
- Performance section absent
- This is a legitimate doctrine state — writing the memo IS the discipline, not the buy. The decision to wait is a real decision.
- Page reads like the first-time variant but with memo present in section 1 instead of Draft Memo CTA

**2C. Stale memo** — Review date > 90 days
- Memo meta shows `Reviewed Jan 12, 2026 · 128d ago`
- Doctrine: re-underwriting trigger
- Open question: does the page surface a prompt (`Re-underwrite ›`), darken the memo block, or just let the meta tell the story?
- Subtler design: when staleness is the only signal, II doctrine says the meta itself should carry it — no extra ornament

---

## Priority 3 — Position Lifecycle Variants

The position section currently shows one shape: single entry, healthy gain, ~3 years held.

**3A. Loss position** — Unrealized P/L negative
- `-2,431.50 CAD (-12.8%)` instead of `+5,652.72 CAD (+42.6%)`
- The team praised the monochrome treatment because the `+42.6%` did the emotional work. With a `-12.8%`, the same monochrome treatment lets the minus sign do the work
- No red. The doctrine holds.
- Worth mocking to confirm the monochrome decision survives the loss case

**3B. Recently entered** — Held < 1 month
- Hold period: `12d` instead of `3y 2m`
- Performance section has thin data — `Cumulative · 12d` reads strangely
- Open question: does Performance section hide until enough history accumulates? Or render with the available data and a meta note (`Insufficient signal yet`)?
- Main dashboard pattern: the "Not yet signal" callout existed once and was removed. Worth reconsidering for the Performance card on a fresh position.

**3C. Multi-tranche position** — Sized up over time
- Already partially encoded: `12.2% entered 6.1%` — the journey from entry weight to current weight
- A deeper drill (Position Detail) would show each tranche: date, amount, weight delta
- Open question: does the page surface number of tranches in the summary, or only in the detail page?
- Suggestion: `Position · 3 tranches` as header meta if multi-tranche; absent if single tranche

---

## Priority 4 — Lifecycle Endpoints

**4A. Watching (starred, no memo)** — Bookmarked but not committed
- Star icon active in header
- Layout closer to first-time variant but with the star "lit"
- Question: is "Watching" a real state in II, or is starring just a shortcut to revisit? If the latter, this is not a distinct page state — the first-time mockup covers it.
- Doctrine instinct: starring without a memo is a non-commitment. II might explicitly NOT support a "watchlist" without forcing the user to at least start a memo. Worth deciding.

**4B. Closed position** — Sold, memo retained
- Position section shows `Closed Apr 5, 2026` instead of holdings data
- Performance section shows realized return frozen at close
- Capital Decision CTA absent (or replaced with `Re-enter Position` for users who want to come back)
- Memo remains as record — closing a position does not delete its thesis
- This is the most distinct edge case structurally. The page becomes a historical record, not a live diagnostic.

---

## Priority 5 — Data States (System-Level)

These are universal states, not investment-specific.

**5A. Market closed / data stale**
- Last Price shows a small meta `· closed` or `· delayed`
- Performance numbers don't refresh in real time anyway, so this only affects the price ticker

**5B. Loading**
- Pre-data render
- II doctrine: skeleton boxes are too much. Hairlines + label text in c-700 saying "Loading" feels more II.
- Or: render the page chrome immediately, fill data as it arrives, hold no spinners

**5C. Error / data fetch failure**
- Empty section with `· unavailable` meta
- No retry button — the page reloads itself naturally; no need for ornament

---

## Priority 6 — AI Research & Analysis Page

These are edge cases for the 11-step protocol surface.

**6A. Clipboard API unavailable / blocked**
- Older browsers, privacy-blocked contexts, or insecure HTTP origin
- Current implementation: `navigator.clipboard.writeText(...).catch(()=>{})` — fails silently
- Doctrine: do not fall back to a modal asking the user to manually copy. The action looks like it worked (label flips to `✓ Copied`) but the clipboard is empty.
- Fix: detect `navigator.clipboard === undefined` and replace label feedback with `· Copy unavailable` in `c-700`. Optional: render the prompt body as a `<textarea readonly>` so manual select-all works.

**6B. Copy All — clipboard size limit**
- Eleven prompts + bundle preamble ≈ 4–5KB. Well under any clipboard limit on iOS/Android/desktop.
- No edge case in practice, but document for future protocols that may grow.

**6C. User session breaks mid-protocol (kills Claude tab, restarts II)**
- No state is persisted. Returning to the AI Research page shows the same 11 steps, no progress indicator.
- Doctrine call: this is OK for MVP. The protocol is meant to be done in one sitting; if the user breaks the session, restarting from Step 01 is the correct behavior — context compounds in Claude, not in the prototype.
- Post-MVP: optional progress marker `· 4 of 11 copied` if telemetry justifies it.

**6D. Different model (ChatGPT) handles multi-turn context worse than Claude**
- Prompts are model-agnostic in copy ("Paste into Claude, ChatGPT, or another model")
- The 11-step protocol works on any model that supports multi-turn context. Single-turn models (older systems) will lose the compounding benefit.
- No design change needed — the user picks the model that works best for them.

**6E. User pastes Step 02 without running Step 01 first**
- Output will be generic because there is no prior context.
- The doctrine note at the top of the protocol metadata bar (`Copy each step into the same chat`) flags this. We do not enforce sequencing in UI — that would be parental.

**6F. Same-chat session loss in Claude (rate limit, model switch, expired session)**
- User has to start a new Claude chat and lose accumulated context.
- Mitigation: Copy All Prompts bundle exists for exactly this case — paste the full numbered list once, model has full context immediately.

---

## Priority 7 — Pressure Test Drawer (planned)

**7A. User cancels mid-drawer (taps outside, Cancel button)**
- Drawer dismisses, Memo Review screen stays as-is, no state change.
- The "skip" doctrine: not running Pressure Test is a valid choice, not an incomplete action. Cancel and Seal Memo are equivalent next moves.

**7B. User copies Bear Case prompt + memo, runs in Claude, comes back, taps Pressure Test again**
- Drawer re-opens with the four options visible. No history of previous runs.
- Doctrine call: ephemeral. The user knows what they ran. Surfacing run history would feel like grading.

**7C. Memo is incomplete when user taps Pressure Test (some fields empty)**
- Drawer should still open. Pressure Test against an incomplete memo will produce findings that effectively call out the gaps.
- Alternative: dim the Pressure Test button until all required fields are filled. Doctrine call: do not dim. Incomplete memos benefit most from external pressure-test feedback.

**7D. Same clipboard fallback as 6A**
- Apply identical detection and fallback rule.

**7E. Memo body too long for clipboard + prompt bundle**
- Practical limit: 100KB on most platforms. A maximum memo (8 sections, ~5000 words total) is well under this.
- No edge case in practice.

---

## Priority 8 — Fiscal AI · ATZ Page (planned)

**8A. Live data feed disconnected**
- Show last known data with `· delayed` or `· last sync 12m ago` meta on the workspace status line
- Do not blank the page

**8B. Filing list empty (no recent filings)**
- Doctrine call: still render the section header, with a one-line `No filings in the last 12 months` note
- Do not hide the section — its absence would suggest data error rather than data accuracy

**8C. Peer comps unavailable (missing peer data)**
- Render the ATZ row alone; dim peer rows or replace numbers with `—` placeholders
- Section meta updates to `peer data unavailable`

**8D. User clicks Open in Fiscal AI (external) but partner workspace is down**
- Browser shows partner's error page
- Out of scope for II — partner reliability is partner's responsibility
- Mitigation: II-side landing (this page) shows enough data for the user to do quick checks without leaving

---

## Recommended Next Mockups

Three new mockups would cover the most doctrine-relevant ground:

1. **`Stock Page v5 — Approaching.html`** — Same recurring user, but `Kill Criteria · 1 of 3 approaching` (c-400 status, prose unchanged)
2. **`Stock Page v5 — Invalidated.html`** — Same recurring user, but `Kill Criteria · 2 of 3 firing` (white status, prose unchanged, possible CTA emphasis)
3. **`Stock Page — Closed.html`** — Post-close historical record (memo retained, position frozen, no Capital Decision)

These three plus the existing two would cover the full memo-status axis (intact / approaching / invalidated / closed) plus the new-user state, giving the team a complete picture of the doctrine in action.

Lower-priority variants (loss position, recently entered, multi-tranche, stale memo) can wait until the four high-priority states are validated.

---

## Open Questions

The mockup work surfaces several decisions that need product-level answers before they can be locked into the design.

**Q1. Does II support a watchlist without forcing a memo?** If yes, "Watching" is a distinct state. If no, the first-time variant covers it.

**Q2. Does a closed position retain Capital Decision affordance for re-entry?** If yes, the CTA stays but with a different label. If no, the page becomes pure history.

**Q3. Does the page surface a "Re-underwrite" prompt for stale memos, or does the meta carry it silently?** This is a doctrine question: how loud does the system get about its own discipline rules?

**Q4. When does Performance section render on a fresh position?** Insufficient signal is a real state; the page needs an answer for the first 90 days.

**Q5. Does multi-tranche surface in the summary view, or only in detail?** Affects header meta and Position section design.

---

*Last updated 2026-05-20.*
**

- Output will be generic because there is no prior context.
- The doctrine note at the top of the protocol metadata bar (`Copy each step into the same chat`) flags this. We do not enforce sequencing in UI — that would be parental.

**6F. Same-chat session loss in Claude (rate limit, model switch, expired session)**

- User has to start a new Claude chat and lose accumulated context.
- Mitigation: Copy All Prompts bundle exists for exactly this case — paste the full numbered list once, model has full context immediately.

---

## Priority 7 — Pressure Test Drawer (planned)

**7A. User cancels mid-drawer (taps outside, Cancel button)**

- Drawer dismisses, Memo Review screen stays as-is, no state change.
- The "skip" doctrine: not running Pressure Test is a valid choice, not an incomplete action. Cancel and Seal Memo are equivalent next moves.

**7B. User copies Bear Case prompt + memo, runs in Claude, comes back, taps Pressure Test again**

- Drawer re-opens with the four options visible. No history of previous runs.
- Doctrine call: ephemeral. The user knows what they ran. Surfacing run history would feel like grading.

**7C. Memo is incomplete when user taps Pressure Test (some fields empty)**

- Drawer should still open. Pressure Test against an incomplete memo will produce findings that effectively call out the gaps.
- Alternative: dim the Pressure Test button until all required fields are filled. Doctrine call: do not dim. Incomplete memos benefit most from external pressure-test feedback.

**7D. Same clipboard fallback as 6A**

- Apply identical detection and fallback rule.

**7E. Memo body too long for clipboard + prompt bundle**

- Practical limit: 100KB on most platforms. A maximum memo (8 sections, ~5000 words total) is well under this.
- No edge case in practice.

---

## Priority 8 — Fiscal AI · ATZ Page

**8A. Live data feed disconnected**

- Show last known data with `· delayed` or `· last sync 12m ago` meta on the workspace status line
- Do not blank the page

**8B. Filing list empty (no recent filings)**

- Doctrine call: still render the section header, with a one-line `No filings in the last 12 months` note
- Do not hide the section — its absence would suggest data error rather than data accuracy

**8C. Peer comps unavailable (missing peer data)**

- Render the ATZ row alone; dim peer rows or replace numbers with `—` placeholders
- Section meta updates to `peer data unavailable`

**8D. User clicks Open in Fiscal AI (external) but partner workspace is down**

- Browser shows partner's error page
- Out of scope for II — partner reliability is partner's responsibility
- Mitigation: II-side landing (this page) shows enough data for the user to do quick checks without leaving

---

## Recommended Next Mockups

Three new mockups would cover the most doctrine-relevant ground:

1. **`Stock Page v5 — Approaching.html`** — Same recurring user, but `Kill Criteria · 1 of 3 approaching` (c-400 status, prose unchanged)
2. **`Stock Page v5 — Invalidated.html`** — Same recurring user, but `Kill Criteria · 2 of 3 firing` (white status, prose unchanged, possible CTA emphasis)
3. **`Stock Page — Closed.html`** — Post-close historical record (memo retained, position frozen, no Capital Decision)

These three plus the existing two would cover the full memo-status axis (intact / approaching / invalidated / closed) plus the new-user state, giving the team a complete picture of the doctrine in action.

Lower-priority variants (loss position, recently entered, multi-tranche, stale memo) can wait until the four high-priority states are validated.

---

## Open Questions

The mockup work surfaces several decisions that need product-level answers before they can be locked into the design.

**Q1. Does II support a watchlist without forcing a memo?** If yes, "Watching" is a distinct state. If no, the first-time variant covers it.

**Q2. Does a closed position retain Capital Decision affordance for re-entry?** If yes, the CTA stays but with a different label. If no, the page becomes pure history.

**Q3. Does the page surface a "Re-underwrite" prompt for stale memos, or does the meta carry it silently?** This is a doctrine question: how loud does the system get about its own discipline rules?

**Q4. When does Performance section render on a fresh position?** Insufficient signal is a real state; the page needs an answer for the first 90 days.

**Q5. Does multi-tranche surface in the summary view, or only in detail?** Affects header meta and Position section design.

**Q6. Pressure Test final prompt wording.** Four options specified; copy locked when CEO sign-off arrives. Build then.

**Q7. AI Research progress persistence.** Should the prototype track copy progress? MVP: no. Post-MVP decision pending telemetry.
