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

The status indicator (`Kill Line · 0 of 3 firing`) currently has one state. The doctrine declares three. Two of them need mockups.

**1A. One trigger approaching** — `Kill Line · 1 of 3 approaching`
- Color: `c-400` (slightly louder than the intact c-700)
- Body prose: same content, but the prose now reads with one true and two false embedded — the user must read carefully to identify which condition is the live concern
- Most realistic edge case in practice — positions slide into this state quietly
- Without a mockup, the warning state is just a CSS class waiting to be invoked

**1B. Multiple triggers firing** — `Kill Line · 2 of 3 firing` or `3 of 3 firing`
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

## Recommended Next Mockups

Three new mockups would cover the most doctrine-relevant ground:

1. **`Stock Page v5 — Approaching.html`** — Same recurring user, but `Kill Line · 1 of 3 approaching` (c-400 status, prose unchanged)
2. **`Stock Page v5 — Invalidated.html`** — Same recurring user, but `Kill Line · 2 of 3 firing` (white status, prose unchanged, possible CTA emphasis)
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
