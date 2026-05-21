# II Doctrine

Reference for every design, product, and engineering decision on the II Self-Directed accountability layer.

**Source.** Internal documents authored by Dave Feller (Founder & CEO, Mogo) plus the chairman conversation log on the Performance Dashboard, 2026-05.

**Structure.** This document is in two parts:
- **Part I — Design & Brand Philosophy.** The severe brand posture, visual language, tone of voice, and anti-patterns that govern all II products.
- **Part II — Accountability Mechanics.** The measurement system specific to the Performance Dashboard: per-tranche shadow benchmarking, anti-hiding rules, computed metrics, UX patterns.

> ⚠️ When the two parts conflict, Part I wins. Severity is non-negotiable; accountability lives within it.

---

# Part I — Design & Brand Philosophy


## 0. Brand identity

- **Parent company**: Orion Digital Corp. (NASDAQ & TSX: ORIO)
- **Product / brand / app**: **Intelligent Investing (II)**
- **Positioning**: Not a fast-trading tool. A **discipline-first system** presented with restraint, seriousness, and intentional absence.
- **Brand posture**: Severe. Quiet authority. Adult autonomy. **No reassurance.**

**Naming**: across all doctrine and design conversations, use **II**.
(The `mylo-` prefix in code/repo names is technical legacy.)

---

## 1. The Prime Directive

> **Do not explain more than is necessary.**
>
> Mystery is preserved by withholding, not obscurity.
> Rigor exists underneath, not on the surface.

**Core line**:
> "We are not building a popular product. We are building a serious one."

---

## 2. Core Cult Belief

> **There is no alpha in consensus.**

This belief governs:
- How we invest
- How we build product
- How we design
- How we market
- How we grow

Anything that feels consensus-driven is suspect by default.

---

## 3. The Enemy

Every cult has a clear enemy. Ours is not a person or a company.

Our enemies:
- **Noise**
- **Impulse**
- **Short-termism**
- **Misaligned incentives**
- **Behavioral exploitation**

We do **not** attack competitors. We attack **systems that produce bad outcomes**.

---

## 4. Core Product Philosophy (6 Principles)

1. **Investor performance > company revenue**
2. **Behavioral outcomes > feature count**
3. **Discipline beats intelligence**
4. **Fewer, better decisions beat more options**
5. **Long-term trust > short-term growth**
6. **Products should protect users from their worst instincts**

### Skeptical of (built into our system):
- Gamification that increases activity without improving outcomes
- Engagement metrics that don't map to real value
- Dark patterns, FOMO, artificial urgency
- "Best practice" SaaS thinking applied blindly to investing

---

## 5. The Identity We Offer

We are not selling tools. We are offering an **identity**:

> **The Intelligent Investor**

This identity is defined by:
- Long-term thinking
- Behavioral discipline
- Intellectual honesty
- Restraint
- Seriousness
- Self-awareness

Using II should feel like:
> "This reflects how I think — or how I want to think."

---

## 6. Who This Is For — ICP (Karp-approved V1)

> Full ICP document: `references/ICP Definition V1.md`

### Core Principle
> We do not build for "people who want to invest". We build for "people who want to **become better investors**".

### Primary ICP
**The Self-Aware, Underperforming Active Investor.**

Someone who believes they should be able to outperform, knows they currently aren't, and is actively looking for a better system.

### Psychological profile (most important)
- Has been investing for years
- Has made real decisions (not hypotheticals)
- Has experienced both wins and mistakes
- Feels the gap between potential and actual

Inner thoughts:
- "I should be better than this."
- "I don't actually track my performance properly."
- "I don't have a real system."
- "I want to take this seriously."

The most important trait:
> **They are willing to be measured, challenged, and proven wrong in order to improve.**

### Trigger moment
- Underperforms the S&P 500.
- Realizes they aren't tracking their results.
- A painful mistake (sold early, held too long, chased hype).
- Senses inconsistency in their decision-making.
- → "I need a better system."

### What they want
**Explicit**: Better returns, decisions, research tools.
**Implicit (more important)**: Discipline, structure, confidence in decisions, the sense of becoming a "real investor".
- Not seeking: **convenience**.
- Seeking: **competence**.

### Identity they aspire to
- They want to become: a disciplined, long-term, high-performance investor.
- Inspirations: Buffett, Munger, Pabrai.

### Who this ICP is NOT
- ❌ Beginners
- ❌ Passive-only investors
- ❌ Gamblers / traders
- ❌ Institutional / elite professionals (initially)

### Demographic proxy (secondary)
- Portfolio: $10K – $250K
- Experience: 2–10 years
- Age: 25–45 (not required)
- **Psychology > demographics.**

### Internal litmus test
> "**Would this attract someone serious about becoming a better investor?**"

If casual users / traders / beginners are attracted → likely wrong.

> "If this feels restrictive, that response is informative."

---

## 7. Core Truths You Must Accept (System is Built Around These)

1. Most investors underperform due to **behavior**, not lack of information.
2. **Activity** correlates **negatively** with long-term returns.
3. Skill is rare and must be **proven**, not assumed.
4. **Time in the market** > timing the market.
5. **Friction** improves decision quality when applied correctly.

These are not opinions; they are constraints the system is built around.

---

## 8. Visual Design — Severe Mode (Non-Negotiable)

### What "severe" means
> "**Unapologetically functional, emotionally cold, and indifferent to approval.**"
>
> "This wasn't designed to persuade you — it was designed to work."

### Color Palette (ABSOLUTE)

**Allowed (only)**:
- Absolute black: `#000000`
- Charcoal / near-black: `#111111` to `#1A1A1A`
- Off-white / bone: `#EDEDED`

**Rules**:
- ❌ NO gradients
- ❌ NO brand color accents
- ❌ NO green/red (ever) — even for gain/loss
- ❌ NO warmth
- ❌ NO decorative color

> "If color feels expressive, it's wrong. Severe palettes don't guide emotion. They remove it."
> "Color is for legibility only."

### Typography
- **Sans-serif only**
- Neutral, slightly condensed
- Zero personality
- Tight line-height
- Generous margins
- **No centering, ever** (specific alignment rules below)
- No italics, no playful weights, no decorative spacing
- Hierarchy: subtle. Section labels must not compete with body text.

> "Typography must feel engineered, not styled."
> "Severe typography reads like documentation, not branding."

### Layout & Composition
- **Single primary column**
- Left-aligned by default (page titles and numbers are exceptions — see Alignment Rules)
- **Large negative space** (= refusal, not elegance)
- Repetition over novelty
- Asymmetry preferred (symmetry = consumer)
- ❌ No cards
- ❌ No visual modules
- Layouts should feel **inevitable**, not designed.

> "If it feels 'nice', remove something."

### Alignment Rules (system convention)

The concrete interpretation of the "no centering, ever" doctrine. **Already established across the MVP system** — new screens follow these rules.

| Element | Alignment | Reason |
|---|---|---|
| **Page titles** (Active Positions, Holdings, Market — top-of-screen labels) | **Right** | System convention. Consistent across screens — page-identification anchor. |
| **Section labels** (Position Summary, Position Details) | Left | Prose rule. |
| **Text-column content** (Ticker, company name) | Left | Prose rule. |
| **Number-column content** (Value, Weight, Price) | **Right** | Functional — magnitude scanning, digit alignment. |
| **Column headers** | Same as the column's content | Alignment consistency. |
| **Body prose** | Left | Doctrine. |
| **Centering of any kind** | ❌ Strictly forbidden | Doctrine §8. |

Core line:
> **"Right-align for identification (titles) and magnitude (numbers). Left-align for everything else. Never center."**

### Imagery (mostly avoid)
**Allowed (if any)**:
- Grids
- Cropped tables
- Partial charts with labels removed
- Blurred system diagrams
- Interfaces without explanation

**NEVER**:
- People
- Faces
- Lifestyles
- Aspirational scenes
- Money imagery
- Smiling anything

> "Imagery should feel like evidence, not inspiration."
> "Text is the primary artifact."

### Motion / Interaction
- **Mechanical**, linear, delayed
- ❌ No easing curves
- ❌ No bounce
- ❌ No delight
- Fade or hard cuts only

> "If animation draws attention to itself → delete it."
> "Interaction should feel procedural, not emotional."

### Brand Presence
- Logo appears **rarely**.
- Small, bottom corner.
- Sometimes not at all.

> "You'll figure out who this is."

---

## 9. Transition Design (Specific)

### Direction
- **Left → right** (forward progress, time advancing)
- ❌ Right → left (feels like undo)
- ❌ Vertical (feels content-y)
- ❌ Zoom (feels playful)

### Motion Profile
- Duration: **220–280ms** (never longer)
- Easing: ease-in-out, **heavily damped**
- ❌ No acceleration "snap"
- ❌ No elastic overshoot

### Asymmetry (Critical)
- New screen enters from right.
- Old screen does NOT slide off symmetrically.
- Outgoing screen: **fade slightly (5–8%)** + move less than the incoming screen.

> "You're progressing deeper, not flipping cards."
> "**Symmetry is consumer. Asymmetry is institutional.**"

### Micro-Delay (II Signature)
- 120–180ms pause before transition begins.
- Especially on the first screen.
- Effect: breaks muscle-memory scrolling, **introduces patience as a value**.

### Swipe-Back Rule
- ❌ NOT in commitment spaces (signup, buy/sell, memo creation).
- ✅ OK in exploration spaces (education, research browsing, help).

> "Tapping 'Back' = intention. Swiping back = reflex. In a discipline-driven product, reflex is the enemy."

### Emotional Test
How a transition should feel:
> "**This feels inevitable.**"
>
> Not: Fun, Fast, Responsive, Slick.
> Yes: Calm, Deterministic, Serious, Unremarkable.

> "If no one comments on the transition, you nailed it."

---

## 10. Tone of Voice (Non-Negotiable)

### Allowed
- Declarative
- Neutral
- Calm
- Precise
- **Emotionally flat**

### Disallowed
- Inspirational language
- Marketing adjectives
- Urgency
- Reassurance
- Humor
- Hype
- Emoji
- Conversational fluff

> "If copy sounds like it is convincing someone, it is wrong."

### Language Rules
- Statements over explanations
- ❌ No metaphors
- ❌ No superlatives
- ❌ No promises
- ❌ No questions

**Correct**: "The system records decisions."
**Incorrect**: "We help you make better decisions."

### Marketing Forbidden Phrases
- "Beat the market"
- "Outperform"
- "Easy" / "Simple"
- "Anyone can"
- "Proven strategy"
- "Join thousands"
- "Get started now"

> "These phrases degrade authority instantly."

---

## 11. Friction Doctrine

> "**Friction is not a bug. It is a signal of seriousness.**"

### What friction does
- Forces intention.
- Prevents impulsive mistakes.
- Separates tourists from operators.

### Conditions for good friction
- Intentional
- Fair
- Explainable
- Aligned with outcomes

> "Bad friction breaks trust. Good friction builds identity."
> "**Speed is for execution. Slowness is for judgment.**"

### Where friction belongs
- Buy gate
- Memo creation
- Capital-allocation moments
- Identity formation (signup)

### Where friction does NOT belong
- Help / education
- Reading flows
- Research browsing

---

## 12. The Buy Gate (Specific Doctrine)

### Why it exists
- Capital allocation is **irreversible**.
- Decisions deserve documentation.
- Memory is unreliable under emotion.
- Decisions made quickly are rarely reviewed honestly.

### Purpose
> "**The purpose of the buy gate is not compliance. It is self-audit.**"

### Bypass
- A bypass exists for legitimate reasons (prior work, incremental, time-sensitive).
- Bypass does NOT mean "skip thinking".
- Bypass means "responsibility has already been taken".

---

## 13. Investment Memos as Living Documents

> "Memos are not checklists. They are records of thought over time."

### Doctrine
- Capture reasoning at the time of action.
- Preserve context.
- Expose bias in hindsight.
- Improve future judgment.

### Expected
> "You will disagree with your past self. **That is evidence of learning.**"

### What memos must NOT look like
- ❌ Form
- ❌ Compliance
- ❌ Homework

---

## 14. The Dashboard (Restraint Doctrine)

### Purpose
> "What do I own, and how meaningful are those decisions?"

### NOT for
- Checking progress
- Timing moves
- Seeking reassurance

### Why minimal
- Orientation surface, not decision surface.
- Visual explanation implies fragility.
- Professionals should "read" instinctively.
- Over-explaining the dashboard feels consumer.

> "**The restraint is the signal.**"

---

## 15. Behavioral Constraints (Why the App Feels "Quiet")

The system minimizes:
- Intraday noise
- Emotional color signals
- Alerts that encourage action
- Metrics that reward restlessness

> "**Silence is a feature. Calm is an advantage.**"

### Volatility ≠ Risk
- **Volatility** is movement.
- **Risk** is permanent loss of capital.
- Conflating them is expensive.
- Discomfort is unavoidable. Panic is optional.

---

## 16. The Non-Negotiables (Internal Behavior)

Things II never does internally:
- Chase trends.
- Add features for engagement.
- Simplify uncomfortable truths.
- Optimize for short-term metrics.
- Break tone to hit growth targets.

> "If something works but breaks doctrine — it is rejected."
> "Discipline internally is what makes discipline externally credible."

---

## 17. Anti-Patterns (Marketing & Comms Blacklist)

### Never ship:
- Feature comparison tables
- Testimonials about "making money"
- Urgency CTAs ("now", "don't miss", "act today")
- Time-bound promos
- Referral incentives
- Influencer partnerships
- Emojis or slang
- Performance bragging
- Reactive content tied to daily market moves
- "Friendly" tone designed to increase conversion

> "**If it looks normal in fintech — it's probably wrong.**"

---

## 18. Marketing Doctrine

### Core Principle
> "**Marketing is not explanation. It is selection.**"
>
> "Marketing is not persuasion. Marketing is public proof of belief."

### Goal
- Not to attract everyone.
- **Repel the wrong audience.**
- Quietly resonate with the right one.

### Channel posture
- **Instagram** — visual posture, monochrome statements.
- **X** — compressed truth, declarative statements (no threads).
- **LinkedIn** — institutional legitimacy.
- **Paid Media** — filtering, not scaling.
- **Silence** — often the correct response.

### Success metric
- ❌ Likes / shares / CTR / CPM / followers
- ✅ Quality of inbound, seriousness of users, long-term retention, behavioral outcomes

> "Marketing that performs well but degrades the audience is a failure."

---

## 19. The Manual (Foundational IP)

### What it is
- A doctrinal document, **not** onboarding / tutorial / marketing copy.
- "Read this once carefully. Re-read when unsure."
- Format: black/white/grayscale, dense typography, no illustrations.
- Designed like a military / aviation / industrial manual.

### Function
- Signals seriousness.
- Sets behavioral constraints.
- Filters users (some bounce — that's a feature).
- Scales philosophy.

### Visual Hierarchy in the Manual
- **Stock Page**: ✅ annotated (decision orientation)
- **Memo Page**: ✅ annotated (thought documentation)
- **Dashboard**: ❌ text only (professional baseline)

---

## 20. The Decision-Making Framework (Use This Constantly)

### High-Status Test (before shipping anything)

1. **Does this try to persuade?** → If yes, remove.
2. **Does this reassure?** → If yes, remove.
3. **Does this explain too much?** → If yes, remove.
4. **Does this feel friendly?** → If yes, remove.

Then:

5. **Does this respect the reader?** → If yes, proceed.
6. **Does this assume competence?** → If yes, proceed.
7. **Does this feel durable?** → If yes, proceed.

### The 5-Minute Cult Check (before shipping any external artifact)
1. What belief does this reinforce?
2. What behavior does this encourage?
3. Who does this intentionally filter out?
4. What temptation did we resist by shipping this?
5. Would this still exist if growth metrics disappeared?

If the answers are hand-wavy → not ready.

### The Ultimate Test
> "**Would a serious, patient, non-consensus investor feel smarter for being associated with this?**"
>
> Not happier. Not more confident. **Smarter.**

---

## 21. "Break Character" Alarm

### Dangerous phrases (stop the moment you hear one)
- "We need to soften the language to improve conversion."
- "Let's just test a lighter version."
- "This works for competitors."
- "Users expect this."
- "We can add it quietly."
- "It's only temporary."

### Default response
> "**Pause. We're breaking character.**"

> "Every cult dies from a thousand small exceptions. We will not make them."

---

## 22. Status Hierarchy (overall decision guide)

```
Friendly  →  Approachable  →  Neutral  →  Reserved  →  Severe
   ↓              ↓              ↓            ↓           ↓
Low status  →  Mid-market  → Undifferentiated → Respectable → Highest
```

II's target: **Severe** (highest status — **if earned**).

What we already have (why severity isn't performative):
- ✅ No hype
- ✅ No promises
- ✅ Transparent economics
- ✅ Autonomy respected
- ✅ Incentives aligned

> "Severity + dishonesty collapses instantly. But severity + integrity compounds."

---

## 23. Status-Safe Metrics

### Tier 1 — North Star
- Accelerating earned organic growth
- Private sharing (DMs, screenshots)
- Direct traffic
- Brand-driven inbound

### Tier 2 — Status Health Indicators
- **NPS language quality** (not score average)
- Polarization (good NPS bifurcation)
- AUM per user growth
- Retention through boredom and drawdowns

### Tier 3 — Operational
- Absolute retention
- Net inflows
- Unit economics
- (Necessary, but never decisive on their own)

### Intentionally deprioritized
- ❌ CTR / CAC efficiency / virality / follower counts / DAU/MAU

### NPS question (status-safe)
❌ "How likely are you to recommend II to a friend?" (assumes friendliness)
✅ "How would using Intelligent Investing reflect on you?" (status-aligned)

> "Fewer promoters with better reasons > more promoters."

### High-status NPS language
- "This aligns with how I think."
- "It forces discipline."
- "It doesn't lie to me."
- "It feels serious."
- "It makes me calmer."

### Low-status NPS language (red flag)
- "Easy"
- "Fun"
- "Exciting"
- "Feels friendly"
- "Makes me confident"

---

## 24. Industrial Design Thesis (One Sentence)

> "**Intelligent Investing should feel like a professional instrument — quiet, opinionated, emotionally neutral, and built to reward discipline over time, not attention in the moment.**"

### Key rules
- "If a screen feels clever, it's probably wrong."
- "II should feel like something you could still use unchanged in 2035."
- "Authority comes from refusal."

---

## 25. Final Canon (Lock these forever)

### The constitution
> "**We do not advertise a product. We signal a standard. Those who recognize it are welcome.**"

### Internal sanity check
> "**We are not trying to feel approachable. We are trying to feel credible.**"

### Industry challenge
> "**In investing, comfort is the product most people sell. We refuse to sell it.**"

### The bar
> "**We are not building a popular product. We are building a serious one. That is the advantage.**"

---

## 26. Using this doctrine with AI

### Layer 1 (include in every ideation prompt)

Attach the full document, or use the core summary:
```
II core doctrine:
1. Severe brand posture — emotionally flat, declarative, calm
2. Friction is a feature, not a bug
3. Filter, don't persuade
4. Mass colors only: #000, #111-1A, #EDEDED (no green/red)
5. Marketing = selection, not explanation
6. There is no alpha in consensus

Anti-patterns (never):
- Friendliness, urgency, gamification, emojis
- Persuasion, reassurance, hype
- Faces, lifestyle imagery, decorative color
- Symmetry (use asymmetry), bounce/easing curves
```

### Critical-review prompt
> "Critique this design against the II Mogo Design Philosophy. Find anti-pattern violations / places where friendliness or reassurance has leaked in / places where severity has weakened. Be ruthless."

---

## 27. Update rules

- When new doctrine material arrives, integrate it.
- Quarterly review with PM (Dave).
- Add reinforcement as Inkyung receives additional source material.
- The original documents in `references/` remain the source of truth.

---

## 28. Final Anchor (in one line)

> **"We're not building an investing app. We're building better investors."**

---

## 29. Related documents

Complementary docs (all in `references/`):

- `ICP Definition V1.md` — full ICP definition
- `Figma vs Prototype Decision Rule.md` — tool selection rule (Karp × Musk)
- `Testing Standard V1.md` — Prototype → Internal → External 3-stage
- `cult.txt` — original Cult Document
- `manual.txt` — original Intelligent Investing Manual V1.0
- `3.txt` — original Severe Design & Brand System
- `Severe Visual Design Guidance.txt` — original visual design guidance
- `transition.txt` — original transition design
- `industrial design.txt` — original industrial design principles
- `1.txt` — CeraVe brand lessons
- `2.txt` — Product Thought Partner instructions
- `Marketing Strategy.txt` — original marketing strategy + status-safe metrics
- `High Status Severe Brand and Product Strategy.txt` — original synthesis thesis
- `manual 2.txt` — Manual appendix structure

---

## TODO (this week)

- [ ] Receive and integrate the additional source material agreed upon.
- [ ] Share with Leo — adopt as a shared doctrine document.
- [ ] Apply these rules to current work and gather feedback.
                                                            
---

# Part II — Accountability Mechanics

---

## 0. One-line definition

> **"Accountability = a measurement system that prevents users from lying to themselves about the quality of their decisions."**

The performance dashboard is not simply a "how am I doing" view — it is an **anti-hiding system**. People instinctively reframe their decisions in a flattering light. This doctrine mechanically prevents that.

---

## 1. Per-Tranche Shadow Benchmarking

### Core principle
> "Every time capital is deployed, the system simultaneously creates a shadow benchmark position of the same dollar amount in [benchmark] at that moment."

### How it works
Every time the user deploys capital (buy / add / DRIP):
1. A **shadow position** of the same dollar amount is automatically created at the exact same timestamp (using VFV.TO total-return adjusted close).
2. The shadow is assumed to be held for exactly the same period as the real position.
3. **Alpha = real return − shadow return**, over that tranche window.

### Why it matters
- Portfolio-level comparisons ("my portfolio is +X%, the market is +Y%") are gameable.
- Selection bias: "from when do you compare?" / "ignoring cash drag?" / "ignoring new buys?"
- Per-tranche means every dollar is held accountable. No hiding.

### Data model
```
Account → benchmark_ticker (default VFV.TO for CAD)
Position → ticker, status (open/closed)
Tranche → each buy/sell, executed_at, shares, fees
ShadowTranche → auto-created, 1:1 match per buy
```

### Sells
- FIFO matching (shadow tranche also closed FIFO).
- Pro-rata is possible, but FIFO produces cleaner attribution.
- Allows the statement: "this buy decision generated X alpha".

---

## 2. Alpha Calculation (CAD basis)

```
cost_cad        = (price_local * shares + fees_local) * fx_to_cad
proceeds_cad    = (price_local * shares - fees_local) * fx_to_cad   -- on sell
divs_cad        = sum of dividends, pro-rated to tranche

real_value_end  = proceeds_cad + divs_cad           -- if closed
                = current_mkt_cad + divs_cad         -- if open
real_return_pct = real_value_end / cost_cad - 1

shadow_end      = cost_cad * (vfv_adj_end / vfv_adj_entry)
shadow_return_pct = vfv_adj_end / vfv_adj_entry - 1

alpha_pct       = real_return_pct - shadow_return_pct      -- in pp
alpha_cad       = real_value_end - shadow_end              -- the dollars
```

**Position-level alpha** = sum of tranche-level numerators / denominators.

**Account-level alpha** uses a parallel `shadow_account_cad` series (mirrors deposits/withdrawals into VFV at that day's close — captures cash drag, which per-tranche math doesn't).

---

## 3. Anti-Hiding Rules (System-Level Invariants)

> These are not toggles. They are **invariants**. The user cannot turn them off.

### Rule 1: Open + Closed on the same ledger
> "Mental accounting separates them; the system shouldn't."

No screen separation. Same view, weighted by capital deployed.

### Rule 2: Surface both TWR and MWR
- TWR (time-weighted) = stock-selection skill.
- MWR (money-weighted, IRR) = timing skill.
- Gap between them = timing skill (almost always negative for active investors).
- Showing only one allows cherry-picking.

### Rule 3: Cash is a position
> "If you're 40% cash in a rising market, that's a bet you made."

Cash weight surfaces as opportunity cost. Show it as a **Cash drag callout** in dollars.

### Rule 4: Decision journal at-the-time, immutable
Thesis / target / kill line / horizon — captured at buy time, cannot be edited. Same for sells.
Without this, every loss gets retroactively reframed as "I knew it was risky".

### Rule 5: Position-level alpha is dollar-weighted in summary
> "A 200% return on a 1% position should not visually outweigh a -30% return on a 15% position."

Summary view default sort = **alpha ascending** (worst dollar contributor at top).
Toggle: "Sort by $ impact" (largest absolute movers, both directions).

---

## 4. Default Sort Doctrine — Anti-Hiding by Order

> "Investors instinctively scroll to their winners; the system needs to do the opposite."

### Closed positions ledger
- **Default sort: alpha ascending** (worst at top).
- Every time the page opens, the worst position appears first.
- Toggle: Recent / $ Impact / Alpha.
- Anti-doctrine: a separate "Winners only" page is forbidden — that is precisely the hiding behavior we are preventing.

### Open positions
- **Default sort: discipline severity → alpha ascending.**
- Discipline violations (kill-line breach / horizon breach / overdue review) come first.
- Status badge for instant identification.

### Diagnostic rows
> "Both show positive returns (looks like a win), but both show negative alpha — they lost vs the alternative of just holding [benchmark]."

A row with positive return but negative alpha must be visible in the same view. Hiding it = failure.

---

## 5. Exit Reason Enum (Constrained, Not Free Text)

```
exit_reason: 'target_hit' | 'stop_hit' | 'thesis_broke' | 'horizon' | 'rebalance' | 'other'
hit_target:  bool         -- did price ever touch entry_target?
```

**Why an enum**:
- Free text invites retroactive narrative ("I knew it was risky").
- Enum + immutable journal enables later analysis: "of positions where I claimed `thesis_broke`, what % actually had price move against my entry target — vs me just losing conviction at a drawdown?"

**Second-order analytics**:
- Hit rate by exit reason.
- "Of positions where I exited claiming `thesis_broke`, what % had price actually moved against my entry target vs me just losing conviction at a drawdown?"

---

## 6. Re-underwriting Triggers

> The user must not be able to claim "doing nothing isn't a decision."

### Auto triggers
1. **Price move ≥ 20%** from last completed assessment.
   - Reference: last assessment price, not entry price (slow grinding moves trigger multiple assessments).
2. **Earnings date** (from ticker calendar).
3. **Manual** — user can initiate.

### Forcing function
- Alert fires → re-underwrite surface forced.
- If not done within 5 trading days → status = "overdue".
- Confidence shift ≥10pp → notes are required.
- Ignoring an alert = "decision by not deciding" = recorded in the ledger.

---

## 7. Cash Drag Callout

Always surfaced on screen (doctrine):
```
Cash drag cost you [amount] — sat at [N]% avg cash while [benchmark] returned +[Y]%.
```

**Why a hero metric**:
- Inaction is a decision.
- Active investors are least likely to recognize this cost.
- Translating it to dollars makes it painful (% is abstract).

---

## 8. Confidence + Calibration

### Confidence input
- Discrete 5 levels: **40 / 50 / 60 / 70 / 80** (prevents false precision).
- Anchored: "P(outperforms [benchmark] over [horizon])".
- < 60% → buy is not recommended.
- ≥ 80% → system warns "possible overconfidence bias".
- 90 / 100 = effectively unwritten rule (impossible territory).

### Re-assessment is also a forecast
> "When you re-underwrite at 50% confidence, that's a new forecast: 'from this moment, P(outperforms from here to close) = 50%.'"

Each assessment is a separate forecast → its own calibration data point.
3-year hold + quarterly re-underwrites × 12 = 12 calibration data points (not 1).

### Calibration visualization
- X axis: stated confidence (50–60% / 60–70% / 70–80% / 80–90% / 90–100%).
- Y axis: actual outperformance rate.
- Dot size: number of forecasts in the bucket.
- Diagonal = perfect calibration.
- Above the line = underconfident / below = overconfident.

> "Almost no active investor is calibrated — virtually everyone is systematically overconfident, especially at the high end."

### Sector calibration (second-order)
> "You're well-calibrated on Canadian financials but you should never touch biotech."

By sector / by setup type (turnaround / compounder / cyclical) → real coaching insight.

---

## 9. View Patterns (UX)

### Account dashboard (hub)
1. KPI cards (3): Your portfolio | If you'd held [benchmark] | **Total alpha**.
2. **Equity curve**: solid actual vs **dashed counterfactual** (the dashed line = "the alternative you bypassed").
3. Strip: TWR (annualized) | MWR (annualized) | Max drawdown | Avg cash %.
4. **Cash drag callout**.
5. Period toggles: 1Y / 3Y / 5Y / All.

### Closed positions ledger (post-mortem accountability)
- KPI cards: Positions closed | Win rate vs bench | **Total alpha** | Avg hold.
- Default sort: alpha ↑.
- Sort toggle: Alpha ↑ | $ Impact | Recent.
- Columns: Ticker · Period · Capital · Return · Bench · Alpha % · **Alpha $** · Exit reason.
- Drill-down: row click → Position detail.

### Open positions (live discipline)
- KPI cards: Open | **Discipline flags** | Unrealized alpha | Capital deployed.
- Sorted by: discipline severity → alpha ↑.
- Status badge: Below kill line / Past horizon / Overdue review / On track.
- Discipline violation = highlighted row (color exception: red / amber / neutral).

### Position detail (drill-down)
- Per-tranche shadow breakdown (each buy → its own alpha).
- **Confidence trajectory** (confidence over time).
- Real vs shadow mini equity curve over hold period.
- Position-scoped journal (thesis updates, re-underwrites, rule violations).

### Decision journal (immutable archive)
- Append-only, newest first.
- Filter: by position / by event type / search.
- Event types: open / add / trim / close / target_revision / thesis_update / milestone.
- Re-underwriting alerts visible.

### Re-underwriting surface (when alert fires)
- Left: original thesis (locked) + kill line (locked).
- Right: trigger context + form for new assessment.
- Confidence trajectory (over time).
- "Notes required" indicator if confidence shift ≥10pp.

### Calibration view
- Buckets / Over time / By sector tabs.
- Avg stated confidence | Actual outperformance | **Calibration gap**.
- Scatter plot with diagonal reference.

---

## 10. Color Usage (Performance Signaling Exception)

> See the narrow exception in `Mogo Design Philosophy.md` §8 Color Palette.

### Allowed
- Alpha sign: + green / − red (auxiliary sign emphasis).
- Discipline status: Below kill line (red) / Past horizon (amber) / Past target (amber) / On track (neutral).
- Rule violation: red badge.

### Still forbidden
- ❌ Color on simple price +/− moves.
- ❌ Decorative / brand-emotional color.
- ❌ Color-only meaning (must be paired with sign / label).
- ❌ Gradient / glow / animation.

### Litmus test
> "Is this color essential to communicating truth? Are sign and label sufficient on their own?"
> If removing the color still conveys the information → remove it. That is the doctrine.

---

## 11. Methodology Defaults

| Spec | Default | Reason |
|---|---|---|
| Benchmark (CAD) | VFV.TO unhedged | Reflects FX exposure honestly |
| Tax | Pre-tax | Cleaner skill measurement |
| Return type | Both TWR + MWR | Prevents cherry-pick |
| Cost basis | Per-tranche, FIFO | Cleaner attribution |
| Dividends | Reinvested (total return) | Accurate comparison |
| Currency | CAD only at top-level (no $ sign) | II currency convention |
| Decimals | 2 places (.00) | Precision |
| Period | All-time fixed (toggle available) | Prevents cherry-pick |

---

## 12. Edge Cases

- **Splits / consolidations**: handled automatically by adjusted close. Do not destructively rewrite original tranches.
- **Spinoffs**: split cost basis by opening price ratio. Each new position requires a fresh thesis / kill line / horizon.
- **Cash + stock mergers**: realize partial gain/loss on the cash portion; carry remaining basis to the new ticker.
- **Return-of-capital distributions**: reduce cost basis (do not treat as dividend income).
- **DRIP**: each reinvestment = a new buy tranche → its own shadow.
- **Halted / delisted at zero**: −100% real return; shadow continues (this is exactly the comparison — the user cannot escape this case).
- **Benchmark non-trading days**: use prior trading day's adjusted close.
- **USD-denominated stocks**: capture `fx_to_cad` per transaction → FX gain/loss is absorbed automatically.

---

## 13. Anti-Patterns (Accountability-specific)

> Never add these.

- ❌ "Winners only" / "Losers only" separate view (reinforces the hiding behavior).
- ❌ "Today's gain" surface (intraday noise violates the doctrine).
- ❌ Animated celebration on profit.
- ❌ Default sort = recent (allows the "winners on top" effect).
- ❌ Free-text exit reason.
- ❌ Editable thesis / journal.
- ❌ Closed-positions view without a performance summary.
- ❌ Portfolio view that doesn't show alpha.

---

## 14. Cross-Reference

- `Mogo Design Philosophy.md` §8 Color Palette + Performance Signaling Exception.
- `Self-Directed Experience.md` §5 Calibration / §6 History / §7 Re-underwriting.
- `Dashboard Doctrine.md` — Performance Dashboard composition.
- `Component Patterns.md` — sort UI 