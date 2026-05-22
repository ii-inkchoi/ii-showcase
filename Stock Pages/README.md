# II (Intelligent Investing) — Dashboard Prototype

Mobile-first prototype for the Intelligent Investing self-directed investing experience. Built around quality decisions, not activity.

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

### Stock detail

- [**Stock Page (ATZ)**](https://ii-inkchoi.github.io/ii-prototype/Stock%20Page%20v5.html) — individual stock detail: performance vs S&P, memo (thesis + kill line), position basics
- [**ATZ Performance Detail**](https://ii-inkchoi.github.io/ii-prototype/ATZ%20Performance%20Detail.html) — drill-in from stock page: annualized return, equity curve, performance metrics (TWR/MWR/drawdown/volatility), yearly breakdown

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
- **Performance order** anchored on truth: Price → Performance vs S&P → Thesis → Kill line

---

## Status

Prototype only. Numbers are illustrative (Aritzia / ATZ used as example holding). Production behavior — per-tranche shadow benchmarking, re-underwriting triggers, decision journal — to be implemented downstream.
