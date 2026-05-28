# Stock Page + Memo · Rationale (V3)

This document records the *why* behind every V3 design choice. It is a companion to the doctrine files in `II Work/Doctrine` and the IA in `II Work/Structure/mogo-ii-ia.md`.

V3 (2026-05-26) is a deliberate simplification of V2. The V2 ambitions (structured memo with eight fields, 9-step creation flow, AI Research v2 page, Pressure Test drawer, 5-state lifecycle) were the right destination but the wrong V1. V3 ships the minimum viable shape, validates user behavior, then earns each addition back.

---

## Doctrine Lens

Five principles drove every V3 decision.

**§8 Visual Design — "feels inevitable, not designed."** Hairlines and typography do all structural work. No cards, no badges, no accents, no decorative color. Severity colors only when meaning demands them.

**§11 Friction Doctrine.** Friction is placed at memo *commit*, not at memo *creation*. Auto-save removes the activation cost. Seal Memo is the deliberate gesture — only sealing propagates to the Stock Page.

**§13 Memos as Living Documents.** V3 lets the memo BE living. Auto-save to draft. Re-seal commits. Sealed copies stay as the source of truth on Stock Page. The user is never blocked from typing.

**§17 Anti-Patterns.** "If it looks normal in fintech — it's probably wrong." We rejected: multi-color price tickers, sparkline candy, holdings-first layouts, performance dashboards, structured form fields. The Stock Page is a thinking surface.

**V1 Simplification.** Strip until the user does something. Add back when their behavior tells us what they need. V2's eight fields were an answer to a question no V1 user had yet asked.

---

## Why V3 Collapsed the Structured Memo

The V2 memo had eight numbered fields: Classification, Sizing, Thesis, Kill Criteria, Intrinsic Value, Exceptional Compounding, Source, Note. The 9-step creation flow walked the user through each. The Memo Variants page showed five lifecycle states.

V3 replaces all of this with a single textarea. Reasons:

**The fields were a guess about how users would write.** No V1 user had written enough memos for us to know the right shape. The eight fields were imported from doctrine theory, not from observed practice.

**Free-form prose matches the AI-augmented workflow.** V3 assumes the user runs the Research Prompt in an external AI tool, pastes the response into the textarea, then edits. A multi-field form would force the user to manually parse the AI's output into buckets — adding friction with no diagnostic value.

**Single-field is forward-compatible.** When user behavior reveals which structure is needed (Classification picker? Kill criteria schema?), we extract from the prose. We don't have to re-architect.

**The CEO directly asked for the simplification.** The 2026-05-26 review made the call: "All that stuff is gone. V1. We're going to start to see what sort of behavior happens." This document records the deference.

---

## Why Research Lives on the Stock Page (Not a Separate Page)

V2 had `ATZ AI Research v2.html` — an 11-step protocol page with phases (Discovery / Stress / Value & Size / Synthesis). V3 deletes it.

**Drill-in into a separate research page added two clicks before any research happened.** First-time users especially: they're on a Stock Page, ready to think, and we asked them to navigate away to a planning page first.

**The Stock Page already has the company in context.** Fiscal AI link, ticker, position summary. Adding the Research Prompt as one card on this page removes the navigation tax.

**One prompt is enough.** V2's 11 prompts were aspirational coverage; V3's single prompt asks for 9 output sections, 2,500–3,500 words. The same coverage, delivered as one document the user can paste into one AI tool, returned as one prose response.

**Four AI tools matter.** Different users prefer different tools. Pinning the prompt to Claude only is unnecessarily prescriptive. The inline `Claude · ChatGPT · Gemini · Perplexity` links let the user pick.

---

## Why Draft / Live Separation

Auto-save would have been simple: every keystroke writes to one localStorage key, Stock Page reads from it. We didn't ship that.

**The Stock Page is a record, not a draft surface.** Users go to the Stock Page when they want to be told what the sealed thesis says. If auto-save propagated every keystroke, the Stock Page would show fragmented half-thoughts. The "Live" badge would be a lie.

**Sealing is a discipline.** The act of clicking "Seal Memo" is a moment of commitment. The user looks at their draft and declares it ready. Without that gesture, every edit is silently authoritative.

**Two keys, one truth.** `atz-memo-draft` is the in-progress copy. `atz-memo-live` is the committed record. Stock Page reads live. ATZ Memo writes to draft, copies draft → live on Seal. The model is borrowed from any version-controlled system.

---

## Why Memo State Collapsed to Three

V2 had five states: Draft, Live, Triggered, Stale, Closed.

**Triggered requires alerts.** A "Triggered" memo state assumes some monitoring service is comparing live market data to kill criteria thresholds. V3 doesn't have that service. Without it, the state is purely decorative.

**Stale requires a threshold policy.** A "Stale" state assumes we know N days since re-underwriting that flips the page from Live to Stale. The threshold (60? 90? per-ticker?) is unsettled. Adding a state for an undecided rule is premature.

**Closed is a position state.** When the user exits a position, the memo doesn't change — the position does. Conflating "Closed memo" with "Closed position" was a category error.

**Live / Draft / Sealed Empty are the three states that fall directly out of localStorage.** They need no external service, no policy threshold. They're determined entirely by the contents of `atz-memo-live` and `atz-memo-draft`.

---

## Stock Page v6d — Recurring User

The canonical page for users who already hold a position.

**Section order: Alert mirror → Memo → Position → Performance → About → Fiscal AI / Research / 4 AI tools → Market / News / History → Capital Decision.**

The Memo sits high because returning users come back to re-read their thesis, not to look at price. Alerts go above the memo because if there's an active concern (Q4 earnings posted, kill criteria triggered), the user needs to know before reading the memo prose.

**Memo block: preview + Read More + Re-underwrite.** The preview is the first paragraph of the sealed memo. Read More expands inline (no page change). Re-underwrite is the action — drill into ATZ Memo to edit. This separates *reading* (Stock Page) from *editing* (ATZ Memo).

**About Aritzia added even on the recurring page.** When the memo is in sealed-empty state, the preview reads "Memo cleared." Without an About section, the user has no baseline context about what the company is. The About section provides that baseline regardless of memo state.

**Capital Decision CTA is fixed-bottom with a fade scrim.** Prose, not a button — `→ Capital Decision`. II treats buy/sell as a sentence, not a click. (Currently a dead link — destination is a Classification picker that hasn't been built.)

---

## Stock Page First — First-Time User

A user landing on a ticker they don't yet hold.

**Memo entry is first.** Even though the user has nothing written, the act of starting a memo is the entry into the II discipline. The Memo entry row says "Write your memo ›" with a hint underneath: "Tip · Run the Research Prompt below first, then paste the AI's response here." The hint surfaces the intended flow without breaking page hierarchy.

**About Aritzia is a single short paragraph.** No founder photos, no logo lockup. Just enough to confirm the company.

**Same Fiscal AI + Research Prompt + 4 AI tools as v6d.** The same surfaces on both pages. The persona difference is the memo state, not the toolset.

**First-time clears localStorage on initial session entry.** This forces the memo to be empty (so the demo persona is honest). Uses sessionStorage flag to clear only ONCE per session — preserves any sealed content if the user navigates back during the same session.

---

## ATZ Memo — The Editor

The full-page memo editor. Single textarea, auto-save, seal.

**Header carries the hurdle.** `Memo · Aritzia Inc · ATZ · Hurdle 20%`. The hurdle is first-class context — the AI's research output is tailored to it, and the user's thesis should be too.

**State badge above the textarea.** ● Live (sealed) · ● Draft (unsealed edits) · hidden (sealed empty). The badge communicates whether the textarea content matches the live record.

**Auto-save with 600ms debounce.** Writes to draft only. Stock Page never sees this until Seal.

**Bottom-right paste icon, inside the textarea.** Users paste from AI tools. The icon must be visible without competing with the scrollbar (right: 26px clears it).

**Bottom fade gradient.** When scrolled, text rising from the bottom would collide visually with the Saved status and Paste icon. A gradient fades the bottom of the textarea to black, masking the collision without hiding the text on click-and-drag.

**Re-seal Memo button at right-bottom of textarea.** Position implies "commit" without needing an outlined box. The right-bottom is where form submits live in every interface convention.

**View Example Memo toggle below.** Inline expand showing the full example memo (the seed content). Lets a new user see what a full memo looks like before they write their own.

---

## ATZ Memo Variants — State Reference

Three columns: Live · Draft · Sealed Empty. Each column shows the memo status block + textarea mockup + spec table.

**Engineering reference, not user-facing.** This page is for the engineer wiring the state machine. It documents what each state looks like, when it triggers, and what storage values produce it.

---

## User Flow — Navigation Map

Three entries → Stock Page → persona split (First / Recurring) → on-page surfaces (Fiscal AI / Research Prompt / 4 AI tools) → The Memo → loopback.

**The map is the V3 IA in one image.** When you need to remember which surface lives where, this is the canvas.

---

## What V3 Did NOT Decide

- **Hurdle picker UI.** Hardcoded to 20%. Three locations need it: memo header label, prompt meta, prompt body.
- **Capital Decision destination.** Dead link. Classification picker is the implied destination but not built.
- **Re-underwrite threshold.** `Reviewed Xd ago` is informational. No automatic state escalation.
- **Multi-tab conflict resolution.** Last-write-wins. Acceptable for prototype.
- **Persona transition policy.** User navigates First → seals memo → returns to First. First page renders whatever localStorage holds. Should it redirect to v6d? Undecided.

These return as V2 work when behavior data confirms the question.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          