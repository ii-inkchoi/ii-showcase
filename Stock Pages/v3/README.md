# II (Intelligent Investing) — Prototype

Mobile-only prototype (393×852) for the Intelligent Investing self-directed investing experience. Built around quality decisions, not activity.

🌐 **Live demo**: https://ii-inkchoi.github.io/ii-prototype/

> Designed for mobile (max-width 393px). On desktop, open DevTools (F12) → Toggle Device Toolbar (Ctrl/Cmd + Shift + M) → iPhone for the intended view. Or open on your phone directly.

---

## Pages

### Dashboards

- [**Unified Dashboard**](https://ii-inkchoi.github.io/ii-prototype/) — main landing, all account states (Core managed + Self-directed) in one view
- [**Performance Dashboard**](https://ii-inkchoi.github.io/ii-prototype/Performance%20Dashboard.html) — portfolio-level performance with annualized returns, equity curve, yearly breakdown, and decisions/discipline metrics

### Positions

- [**Open Positions**](https://ii-inkchoi.github.io/ii-prototype/Open%20Positions.html) — currently held positions, sorted by discipline severity then alpha
- [**Closed Positions**](https://ii-inkchoi.github.io/ii-prototype/Closed%20Positions.html) — post-mortem ledger, sorted by alpha ascending (worst alpha first — anti-hiding doctrine)

### Stock detail (Stock Page + Memo family)

- [**Stock Page (Returning user) · v6d**](https://ii-inkchoi.github.io/ii-showcase/Stock%20Pages/Stock%20Page%20v6d.html) — current canonical. Memo box (Thesis + Kill Criteria + IV/MoS/Probability) + Position + Performance vs SPY + Fiscal AI / AI Research / Market / News / History
- [**Stock Page (First-time user)**](https://ii-inkchoi.github.io/ii-showcase/Stock%20Pages/Stock%20Page%20First.html) — no memo yet; Draft Memo entry + Fiscal AI + AI Research cards
- [**The Memo · Full**](https://ii-inkchoi.github.io/ii-showcase/Stock%20Pages/ATZ%20Memo.html) — 8 numbered sections (Classify / Size / Thesis / Kill Criteria / IV / Compounding / Source / Note)
- [**The Memo · Lifecycle Variants (5)**](https://ii-inkchoi.github.io/ii-showcase/Stock%20Pages/ATZ%20Memo%20Variants.html) — Draft / Live / Triggered / Stale / Closed
- [**AI Research & Analysis · ATZ**](https://ii-inkchoi.github.io/ii-showcase/Stock%20Pages/ATZ%20AI%20Research.html) — 11-step protocol page, 4 phases (Discovery / Stress / Value & Size / Synthesis)
- [**ATZ Performance Detail**](https://ii-inkchoi.github.io/ii-prototype/ATZ%20Performance%20Detail.html) — drill-in: annualized return, equity curve, TWR/MWR/drawdown/volatility, yearly breakdown

### Reference

- [**Benchmark**](https://ii-inkchoi.github.io/ii-prototype/Benchmark.html) — S&P 500 reference page
- [**Open Questions**](https://ii-inkchoi.github.io/ii-prototype/Open%20Questions.html) — decision prompts surface (Big Move / Material Move / Thesis Review / Memo Pending)

---

## Doctrine notes

The visual system is intentionally minimal:

- **Severe palette** — absolute black, charcoal grays, off-white only. No decorative color, no gradients
- **Right-align for magnitude** (numbers, page titles); **left-align for prose**; **never center**
- **Hairline borders only** as visual separators; no cards
- **No "AI" labels** — system-generated insights are marked with the `//` Mogo wedge
- **Friction is a feature** — limit orders default; deliberate proceed on commitment actions
- **Performance order** anchored on truth: Price → Performance vs S&P → Thesis → Kill criteria

---

## Status

Prototype only. Numbers are illustrative (Aritzia / ATZ used as example holding). Production behavior — per-tranche shadow benchmarking, re-underwriting triggers, decision journal — to be implemented downstream.
