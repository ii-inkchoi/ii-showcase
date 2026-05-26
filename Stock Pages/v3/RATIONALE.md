# Stock Page Family — Rationale

This document records the *why* behind every page and section in the II Stock Page prototype family. It is a companion to the doctrine files in `II Work/Doctrine` and the IA in `II Work/Structure/mogo-ii-ia.md`. If you only have time for one section, read **Doctrine Lens** below.

---

## Doctrine Lens

Five doctrine principles drove every decision. Reference these when reviewing a change.

**§8 Visual Design — "feels inevitable, not designed."** Layouts should read as the only possible answer, not as styled. We rejected cards, badges, chips, accents. Hairlines and typography do all structural work. The palette stays severe (black, c-700, c-400, white).

**§11 Friction Doctrine.** Friction is placed at memo creation and at edit. Each memo edit creates a new immutable version — the cost is intentional. The Capital Decision CTA sits at the bottom of every stock page so that any buy/sell action requires a deliberate scroll past thesis and kill criteria.

**§13 Memos as Living Documents.** The memo is the primary record of thought, not a form to fill. We elevated memo visual weight by giving it the top position on the stock page and a dedicated full-page drill-in. Research artifacts and user notes hang off the memo, not the position.

**§17 Anti-Patterns.** "If it looks normal in fintech — it's probably wrong." We removed multi-color price tickers, sparkline candy, holdings-first layouts, and any "performance dashboard" framing. The stock page is a thinking surface, not a trading surface.

**Accountability Mechanics.** Alpha is shown in percentage points, not dollars, on the summary view (matching the main dashboard pattern). Per-tranche shadow benchmarking is preserved in the Performance Detail drill-in.

---

## Stock Page v5 — Recurring User

This is the canonical stock page for users who already hold a position.

**Section order: Memo → Holdings → Performance → Market / News / Research → Capital Decision.**

The memo sits at the top because the memo is the first thing a returning user should re-read before doing anything else. Dave's meeting feedback confirmed this: the question on every revisit is *does my thesis still hold?*, not *what's the price?* Putting Holdings or Performance first inverts the doctrine — those become drivers of decision instead of consequences of thesis.

**Memo section shows Thesis and Kill Criteria as full prose.** We tried four truncation variants — 2-line clamp, Read More/Less toggle, dotted-underline `.lbl-tap` expansion, and chevron-only expand — and rejected all of them. The reasoning: if a writer commits to a memo, the reader trusts them with the screen real estate. Truncation implies the memo is overhead. Showing it in full says the memo IS the page.

**Holdings and Performance are separated, not merged.** They answer different questions. Holdings = *what is my current position* (weight, entry, average cost). Performance = *how is the position behaving* (alpha vs S&P, drawdown, hold duration). Merging them into a "Position Performance" block looks tidier but blurs the diagnostic intent. Each gets its own drill-in.

**Capital Decision CTA is fixed-bottom with a fade scrim.** This is the only action surface on the page. It uses prose, not a button — "→ Capital Decision" — because II treats buy/sell as a sentence, not a click. The scrim ensures it never collides with content while remaining always-reachable.

---

## Stock Page First — First-Time User

A user landing on a ticker they don't yet hold gets a different page. The same chrome, the same Capital Decision CTA at bottom, but the body answers a different question: *should I underwrite this?*

**Draft Memo · ATZ is the primary section.** A first-time user has no position, no holdings, no performance. What they have is the choice to either write a memo or walk away. The Draft Memo CTA is the entry point to the ten-field memo protocol. The supporting `Field Reference · 10 Questions ›` link lets cautious users see what they're committing to before they start.

**About Aritzia Inc. is a single short paragraph.** No founder photos, no logo lockup, no marketing copy. Just the minimum needed to confirm the company is what the user thinks it is. A `Read More on the Company ›` drill-in handles users who want depth.

**Market / News / Research nav lives at the bottom.** A first-timer who is not ready to write a memo can wander into market data, news, or research artifacts. The nav is intentionally below About so that the page does not become a research portal. The hierarchy is: draft a memo → learn about the company → explore peripheral info. Not the reverse.

---

## ATZ Memo — Full Detail

Drilling into the memo from Stock Page v5 reveals the complete sealed document.

**Memo status block exposes the version contract.** V3, the review date, days since review, count of prior versions, and the doctrine note: *"Memos are immutable once sealed. Each edit creates a new version. Prior versions stay on the record."* This is not legalese — it is the page teaching the user the edit mechanic. Any edit anywhere on the page creates V4. The user sees this at the top so the cost is visible before they act.

**Five canonical sections: Thesis, Kill Criteria, Margin of Safety, Confidence, then Research and Notes.** These are the ten-field memo protocol collapsed into five reading blocks. Each section header is a hairline with a single label and no chrome.

**Kill Criteria is prose, not bullets.** We tried `·` middle-dot bullets and rejected them. Bullets imply a checklist; II treats kill conditions as a single decision rule expressed as three sentences. Three conditions, any one of which closes the position — written as prose, the reader experiences them as commitments, not items. (See `II Work/Doctrine/Mogo Design Philosophy.md` §30 for the rejected variants.)

**Margin of Safety uses two-column data rows, not cards.** Key on the left, value on the right, no border. The footnote below explains the valuation anchor in plain language ("22× FY26 earnings on retail plus 15× online, blended and discounted 12%"). No formula widget, no calculator UI — the math is recorded, not interactive.

**Research and Notes are now separate sections, not merged.** This was the most recent change. The original "Notes & Research" mixed three categories — Mogo-generated analysis (prefixed with `//`), source documents (10-K filings, transcripts), and user-written observations. Visually they looked the same and the user lost the ability to distinguish *input to my thinking* from *output of my thinking*. Splitting into `Research · 3` and `Notes · 2` restores that distinction. The `//` wedge still marks Mogo-generated items within Research; documents have no wedge.

**View-link pattern at the bottom of each list.** `View All Research ›` and `View All · Add Note ›` both follow the doctrine drill-in pattern — small font, c-700 color, single chevron. Add Note doubles as a write-action because for a user reviewing their memo, adding a note IS the most common action.

---

## ATZ Notes — User Notes Detail

A focused page for user-written notes only. Research artifacts do not appear here.

**New Note input is a bracketed frame.** Four hairline corner brackets, not a full border. This matches the memo edit UI from the existing II prototype set and signals "input surface" without the consumer-fintech rectangle. The placeholder is intentionally evocative — *"A thought, an observation, a price level you want to track…"* — because II notes are not just status updates.

**Paste and attach icons live inside the frame at bottom-left.** An early version put them in a separate row below the frame with a redundant "Paste · attach a file" text label. Three problems: the icons collided visually with the bottom corner brackets, the label duplicated the icons, and the affordance felt detached from the input surface. The fix puts the icons inside the frame where the action happens, removes the label, and lets the brackets define the boundary cleanly. Paste is the critical affordance — users paste from ChatGPT, articles, internal docs — so the icon must remain visible.

**Save Note uses → arrow, not chevron.** Doctrine: `→` for commit actions, `›` for navigation. Saving a note is a commitment (it becomes part of the record), so it gets the arrow. The link goes c-700 by default and white when the textarea has content — a single bit of state, no other UI feedback.

**All Notes list uses hairline separators only.** No card around each note, no metadata grid, no badge. Just body text in white, date in c-700 below. Order is chronological. We discussed whether to put the Save row above the list (so new notes are an immediate next action) or below. Below won — scrolling through past notes before adding a new one is intentional friction. It encourages re-reading before piling on.

---

## ATZ Performance Detail

A drill-in for users who want to interrogate position performance.

**Annualized return is the headline, not cumulative.** Cumulative appears on the Stock Page v5 summary card; the drill-in switches to annualized because that's the comparison metric. Equity curve below the headline with a hairline x-axis only.

**Per-year breakdown follows the main dashboard pattern.** Years stacked top to bottom, each row showing return, alpha, and signal status. Years before the position was held are omitted. The current year shows partial data with no signal-status flourish.

**Removed: "Not yet signal" callout, "2028 Signal" placeholder, "Memo Anchors" section.** All three were flagged as performance-dashboard creep — they treat the page as a scoreboard instead of a diagnostic. The signal status appears inline per-year where it belongs; we don't need an aspirational future-year row on a backward-looking page.

**Alpha is shown in percentage points, no dollar values on the summary.** Dave's reconcile pain ($5,652 vs $3,768 confusion) traced back to the dollar display being read as a benchmark figure when it was a delta. Removing $ from Alpha on the summary, while keeping % everywhere, eliminated the ambiguity. The full dollar detail lives one level deeper.

---

## Cross-Page Patterns

These are conventions applied everywhere; deviations from them are bugs.

**Title Case follows proper Chicago style.** Articles (a, an, the), short prepositions (on, in, of, for, to, by, with, at), and conjunctions (and, or, but, nor) stay lowercase unless they are the first word. So "Read More on the Company" — *not* "Read More On The Company." Earlier drafts used CSS `text-transform: capitalize` which capitalizes every word; we removed it everywhere and wrote Title Case directly in HTML.

**The `//` wedge marks Mogo-generated insight.** Never "AI," never "Claude," never "Generated by." Just `//`. It appears in Research items and in any synthesis the system produced — never on user-written content, never on source documents.

**Section headers are hairlines, not dividers.** A hairline at 0.5px with `var(--c-900)` color. The section title sits above; the section content sits below. Optional `·` count appears in `c-700` next to the title. No icons in headers, no chevron in headers — chevron lives at the row that drills in.

**Drill-in chevrons (`›`) on whole-row anchors.** When an entire row is clickable (section header → detail page), the chevron sits flush-right and the whole row gets `active:opacity-0.5`. No hover states, no underlines, no button styling.

**Capital Decision CTA is the only fixed element.** It exists on Stock Page v5 and Stock Page First. Detail pages (Memo, Notes, Performance) do not have it because the decision belongs on the stock page, not in the artifact pages.

---

## What This Is Not

This prototype is intentionally *not*:

- a trading interface (no buy/sell buttons, no order ticket)
- a research portal (news, charts, peer comps live elsewhere)
- a portfolio dashboard (the main dashboard handles that)

It is a *thinking surface for one position*. Every design decision was tested against that frame. If a section would look at home in Robinhood, Wealthsimple, or any retail broker, it failed.

---

## AI Research & Analysis — 11-Step Protocol Page

**Why a separate page, not inline on Stock Page.** The protocol is heavy work — eleven prompts, multiple Claude/ChatGPT round-trips, user time outside the app. Inlining it on the Stock Page would either (a) compress the protocol into one prompt — which loses the multi-step depth that is the entire point — or (b) bloat the Stock Page beyond its monitoring purpose. The drill-in card mirrors how Bloomberg surfaces dense analytical work behind keystroke entry: the landing screen stays calm; depth lives one step away.

**Why 11 steps and not fewer.** Per CEO doctrine: "intelligent investing has this pre-described 11-step prompt." Foundation models are equal at the baseline. The edge is in iteration — challenge, verify, pressure-test. Eleven is II's entry-level edge (hedge funds run 50-step protocols). Fewer steps means less depth means we collapse into "single prompt answer" — the table-stakes layer that everyone has access to. The protocol's existence is itself a sophistication signal — it tells the user "this is a serious instrument."

**Why phase grouping (4 phases, not 11 flat steps).** Information design principle from FT-style editorial layouts. Eleven undifferentiated cells reads as a checklist. Four phases reads as a research narrative: Discovery (frame the business and opportunity) → Stress (attack the thesis) → Value & Size (anchor the price and the position) → Synthesis (cross-check and compress). The user moves through the work the way a disciplined investor would, not the way a task list runs.

**Why output hints under each prompt.** They are quality checklists. The user knows before sending to Claude what shape of answer to expect — three narratives with verdict and rationale, five bear arguments ranked by probability × impact, three valuation methods with explicit inputs. If Claude returns less, the user catches the gap and re-prompts. The hint is calibration scaffolding for the user, not decoration.

**Why Copy All Prompts at the top.** Optionality. Some users will work step-by-step; others will paste the full bundle and run sequentially in one long Claude session. The bundle preserves numbering and adds a "Use the same chat. Run sequentially." preamble so the user does not lose multi-turn context — which is where the edge accumulates.

**Why the visual register is denser than the Stock Page.** Brand vs Product distinction (per `Doctrine/Product Design Principles.md`). The Stock Page is the calm environment; AI Research is one of the dense analytical surfaces. The Bloomberg pattern. Quick stats row, phase headers with structural copy, hairline-accented prompt bodies, per-step meta tags. Density appears where the work warrants it.

**Why not bundle Pressure Test in the same page.** Different surface, different job. AI Research is *pre-memo* — the user has not written anything yet and needs to develop the thesis. Pressure Test is *post-memo* — the thesis is drafted and needs a final fail-safe before sealing. Different stage in the workflow, different prompts, different copy semantics. Bundling them would conflate "build" with "stress-test." We kept them on separate surfaces.

---

## Pressure Test — Post-Memo Fail-Safe (Planned)

**Why a drawer, not a separate page.** Pressure Test is optional and ephemeral. The user is mid-memo at the Review stage; they should not leave the memo to run a check on it. A drawer slides up, the user picks an option, copies prompt + memo, runs in Claude, returns to the same Review screen to decide whether to seal or revise. Pages would interrupt the flow; the drawer preserves it.

**Why four options, not one.** Different angles produce different findings. Bear case stress catches narrative weakness; valuation check catches arithmetic weakness; kill criteria stress catches discipline weakness; compounding stress catches long-horizon weakness. A single prompt would consolidate these and produce a generic answer. Four discrete options let the user pick the angle most relevant to their specific concern, or run multiple in sequence.

**Why "Copy Prompt + Memo," not just "Copy Prompt."** The memo is the payload. Without it the prompt is generic and the answer will be generic. The combined copy is the materially valuable action — prompt provides the framing, memo provides the substance.

**Why optional.** Per CEO doctrine: "you might say, hey, I'm already comfortable with this. I don't need a pressure test at all." Pressure Test is a fail-safe, not a gate. Users who completed the 11-step Research protocol have already pressure-tested the thesis through iteration; they should be allowed to skip. Users who bypassed Research and typed their memo directly are the ones the fail-safe exists for.

---

## Fiscal AI · ATZ — Workspace Landing

**Why a dedicated page, not just an external link.** Two reasons. First, the page establishes II's role as the index of truth — the user sees ATZ's fundamentals, valuation, filings, and peer comps in II's visual register, not in a partner's interface. Second, the page sets expectations: when the user clicks "Open Full Workspace" and lands in Fiscal AI proper, they already know what they came for. The II-side landing is the calibration step.

**Why this surface is dense.** Per Product Design Principles §V — density appears where the work warrants it. Fiscal AI is the data surface. Live Fundamentals are numerical (Revenue, Margin, ROIC, etc.), Valuation is multiples (P/E, EV/EBITDA, P/FCF), Comps is a tabular comparison. The work itself is dense; the design honors the density rather than hiding it behind a single summary number. Bloomberg/IBKR pattern.

**Why no Capital Decision CTA on this page.** Fiscal AI is data, not decision. The decision lives on the Stock Page. The user leaves Fiscal AI, returns to Stock Page, makes the call there. Keeping the Capital Decision CTA off this page reinforces the role separation: Fiscal AI is for understanding the business, not for buying it.

---

## Considered and Decided Against

Team feedback proposed grouping the four Position fields into two semantic clusters: Market Value + Unrealized P/L (outcome) and Portfolio Weight + Hold period (discipline). The logic is sound — these fields genuinely answer different questions. We tried it. The result felt either broken (small gap differential read as misalignment) or like two separate sections (larger gap differential broke the "one Position section" frame). Every visual treatment we tried — added hairline divider, color differential, cluster labels — either added ornament or invented vocabulary the user has to learn. We reverted to uniform 25px spacing across all four rows.

The doctrine call: each field has its own label (Market Value, Portfolio Weight, Unrealized P/L, Hold period) that already declares its character. The reader does not need spatial grouping to understand the semantic difference. Uniform spacing communicates "these are peer attributes of one position" — itself a true statement. We chose adequacy over visual encoding of every semantic distinction. This is II — not every difference deserves typographic emphasis.

If the same feedback surfaces again, the answer is the same: considered, intentionally declined. Reorder (without spacing change) is a low-risk fallback if a future round insists on some grouping signal — adjacent semantic pairs without visual differentiation.

---

## Open Questions

A few items remain undecided. Flagging them so the team can weigh in.

**Research drill-in destination.** `View All Research ›` currently points to `#`. We need to decide whether Research deserves its own detail page (analogous to ATZ Notes for notes) or whether it merges with a broader "Sources" view. Tradeoff: separation reinforces the input-vs-output distinction; a merged sources page reduces page count.

**Memo edit entry point.** The doctrine permits edits (each edit = new sealed version) but the prototype has no edit entry yet. Two candidates: tap-a-row-to-edit on ATZ Memo, or a Re-underwrite CTA on Stock Page v5. The first is light-touch; the second is ceremonial. Both are doctrine-valid; the choice is which feels more II.

**Holdings/Performance consolidation.** They are split today. A merged "Position" section is tidier visually but blurs intent. Worth a second pass with the design team before locking.

---

*Last updated 2026-05-20.*
tock Page.** Brand vs Product distinction (per `Doctrine/Product Design Principles.md`). The Stock Page is the calm environment; AI Research is one of the dense analytical surfaces. The Bloomberg pattern. Quick stats row, phase headers with structural copy, hairline-accented prompt bodies, per-step meta tags. Density appears where the work warrants it.

**Why not bundle Pressure Test in the same page.** Different surface, different job. AI Research is *pre-memo* — the user has not written anything yet and needs to develop the thesis. Pressure Test is *post-memo* — the thesis is drafted and needs a final fail-safe before sealing. Different stage in the workflow, different prompts, different copy semantics. Bundling them would conflate "build" with "stress-test." We kept them on separate surfaces.

---

## Pressure Test — Post-Memo Fail-Safe (Planned)

**Why a drawer, not a separate page.** Pressure Test is optional and ephemeral. The user is mid-memo at the Review stage; they should not leave the memo to run a check on it. A drawer slides up, the user picks an option, copies prompt + memo, runs in Claude, returns to the same Review screen to decide whether to seal or revise. Pages would interrupt the flow; the drawer preserves it.

**Why four options, not one.** Different angles produce different findings. Bear case stress catches narrative weakness; valuation check catches arithmetic weakness; kill criteria stress catches discipline weakness; compounding stress catches long-horizon weakness. A single prompt would consolidate these and produce a generic answer. Four discrete options let the user pick the angle most relevant to their specific concern, or run multiple in sequence.

**Why "Copy Prompt + Memo," not just "Copy Prompt."** The memo is the payload. Without it the prompt is generic and the answer will be generic. The combined copy is the materially valuable action — prompt provides the framing, memo provides the substance.

**Why optional.** Per CEO doctrine: "you might say, hey, I'm already comfortable with this. I don't need a pressure test at all." Pressure Test is a fail-safe, not a gate. Users who completed the 11-step Research protocol have already pressure-tested the thesis through iteration; they should be allowed to skip. Users who bypassed Research and typed their memo directly are the ones the fail-safe exists for.

---

## Fiscal AI · ATZ — Workspace Landing

**Why a dedicated page, not just an external link.** Two reasons. First, the page establishes II's role as the index of truth — the user sees ATZ's fundamentals, valuation, filings, and peer comps in II's visual register, not in a partner's interface. Second, the page sets expectations: when the user clicks "Open Full Workspace" and lands in Fiscal AI proper, they already know what they came for. The II-side landing is the calibration step.

**Why this surface is dense.** Per Product Design Principles §V — density appears where the work warrants it. Fiscal AI is the data surface. Live Fundamentals are numerical (Revenue, Margin, ROIC, etc.), Valuation is multiples (P/E, EV/EBITDA, P/FCF), Comps is a tabular comparison. The work itself is dense; the design honors the density rather than hiding it behind a single summary number. Bloomberg/IBKR pattern.

**Why no Capital Decision CTA on this page.** Fiscal AI is data, not decision. The decision lives on the Stock Page. The user leaves Fiscal AI, returns to Stock Page, makes the call there. Keeping the Capital Decision CTA off this page reinforces the role separation: Fiscal AI is for understanding the business, not for buying it.

---

## Considered and Decided Against

Team feedback proposed grouping the four Position fields into two semantic clusters: Market Value + Unrealized P/L (outcome) and Portfolio Weight + Hold period (discipline). The logic is sound — these fields genuinely answer different questions. We tried it. The result felt either broken (small gap differential read as misalignment) or like two separate sections (larger gap differential broke the "one Position section" frame). Every visual treatment we tried — added hairline divider, color differential, cluster labels — either added ornament or invented vocabulary the user has to learn. We reverted to uniform 25px spacing across all four rows.

The doctrine call: each field has its own label (Market Value, Portfolio Weight, Unrealized P/L, Hold period) that already declares its character. The reader does not need spatial grouping to understand the semantic difference. Uniform spacing communicates "these are peer attributes of one position" — itself a true statement. We chose adequacy over visual encoding of every semantic distinction. This is II — not every difference deserves typographic emphasis.

If the same feedback surfaces again, the answer is the same: considered, intentionally declined. Reorder (without spacing change) is a low-risk fallback if a future round insists on some grouping signal — adjacent semantic pairs without visual differentiation.

---

## Open Questions

A few items remain undecided. Flagging them so the team can weigh in.

**Research drill-in destination.** `View All Research ›` currently points to `#`. We need to decide whether Research deserves its own detail page (analogous to ATZ Notes for notes) or whether it merges with a broader "Sources" view. Tradeoff: separation reinforces the input-vs-output distinction; a merged sources page reduces page count.

**Memo edit entry point.** The doctrine permits edits (each edit = new sealed version) but the prototype has no edit entry yet. Two candidates: tap-a-row-to-edit on ATZ Memo, or a Re-underwrite CTA on Stock Page v5. The first is light-touch; the second is ceremonial. Both are doctrine-valid; the choice is which feels more II.

**Holdings/Performance consolidation.** They are split today. A merged "Position" section is tidier visually but blurs intent. Worth a second pass with the design team before locking.

**Pressure Test exact prompt copy.** Four options specified (Bear / Valuation / Kill Criteria / Compounding stress) but final prompt wording pending CEO sign-off. Build after copy is locked.

**AI Research progress persistence.** Should the prototype track which of the 11 steps the user has copied? MVP: no persistence (start fresh each session). Post-MVP: telemetry to inform whether progress markers add value.
