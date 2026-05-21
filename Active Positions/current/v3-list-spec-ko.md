# Active Position List — v3 Spec (한글)

**상태**: 초안 sketch, PM / 회장 review 대기
**기반**: 회장 v2 (Held 컬럼 포함)
**Doctrine 참조**: Mogo Design Philosophy §1, §6, §8, §10, §11, §13, §14, §15
**Sketch 파일**: `v3-list-sketch.html` (시각 reference)

---

## 목표

Active Position list를 **broker view** (잔고 + 최근 등락) 에서 **decision-system view** (commitment 컨텍스트) 로 옮긴다. List는 orientation surface, calibration의 깊은 분석은 Stock Detail에 위치.

---

## 회장 v2 대비 변경 사항

| # | 변경 | Rationale |
|---|------|-----------|
| 1 | 페이지 타이틀 위에 **계좌 scope 라벨** 추가 (예: "RRSP", "All accounts") | 기존 4 화면에서 계좌 scope이 암묵적이고 일관성 없음 (Dashboard에는 RRSP 선택기 있고, Active Positions list는 표시 없고, Stock Detail도 없고, Holdings는 "All Accounts" 라벨). 사용자가 *어느 계좌 보는 중인지* 추측해야 하고, 이게 조용히 신뢰를 깸. 작은 영구 라벨로 scope을 노출하면 그 추측이 사라짐. |
| 2 | "Held" 컬럼 → **"Held / Horizon"** (예: `1.5y / 3y`) | 단순 '들고 있는 시간' 은 자동 계산 데이터일 뿐. II에서 중요한 건 사용자가 *진입 시점에 한 commitment* 를 지키고 있는지. `held / horizon` 표시는 컬럼을 '경과 시간' 에서 '본인 commitment 대비 진행률' 로 reframe함 — 이게 doctrine §11 friction 원칙과 §13 memo 원칙을 list 레벨에 시각화한 것. `held == horizon` 일 때 자체가 re-calibration 시그널. |
| 3 | **Daily price + Daily ±% 제거** (회장 v2는 유지) | Doctrine §15가 명시: intraday noise를 minimize, activity는 returns과 negative correlation. Primary list에 daily ±% 를 보여주면 사용자가 매일 들어와 반응하도록 학습됨. `Value` 컬럼이 이미 today price 반영함 (`market value = shares × current price`) — today 영향은 *암묵적으로* 보임. 명시적 % 는 어제 vs 오늘 비교를 유도, 이게 doctrine §3 Enemy (Noise + Short-termism + Impulse). Daily 가격 검사처는 Stock Detail / Market 탭 (사용자가 *의도적으로* 들어간 surface). **Open question #6** — Ship 전에 회장 confirm. |
| 4 | **CAD 통화 표기를 row → column header 로 이동** ("Value CAD") | List의 모든 값이 자동으로 CAD 환산됨 (USD 종목 포함). 매 row마다 "CAD" 반복은 시각 무게 추가, 정보 추가 X — 사용자가 컬럼 이해하면 충분. 단일 표기 (header에 한 번) 충분. Doctrine §1: "Do not explain more than is necessary." |
| 5 | **Calibration 데이터 list에 의도적으로 미포함** — confidence pair (`stated · baseline`) 는 Stock Detail에만 | Calibration은 시스템의 본질이지만, Active Position list는 *orientation surface* (doctrine §14 논리를 list에 적용). `80%·76%` 같은 paired numeric은 헤더 레벨 explanation이 필요한데 ("어느 게 내 거?"), 그 explanation 자체가 시각 무게 추가 — doctrine §1과 충돌. Stock Detail의 calibration plot (선 + 위/아래 점) 은 *시각적으로 self-explanatory*, 이 challenge의 올바른 home. List에서 빼면 사용자가 self-evaluation metric을 *매일 슬쩍 보는 습관* 안 들이게 됨 (doctrine §15). |
| 6 | 페이지 타이틀 = **우측 정렬**, 숫자 컬럼 = **우측 정렬**, 글자 라벨 = **좌측 정렬** | Doctrine §8은 'no centering, ever' 라고만 함, 모든 것을 좌측 정렬해야 한다고는 안 함. MVP 시스템은 이미 일관된 컨벤션에 수렴: 페이지 타이틀 우측 정렬 (식별 anchor), 숫자 컬럼 우측 정렬 (functional magnitude scanning), prose와 글자 라벨은 좌측 정렬. v3는 시스템 컨벤션을 따름. (Doctrine §8에 Alignment Rules subsection 추가됨.) |

---

## 컬럼 정의 (확정)

```
Ticker   Weight   Held / Hor   Value (CAD)
좌측     우측      우측         우측 (숫자 위, since-entry % 아래)
```

**총 4 컬럼.** Confidence 컬럼 X, Daily 컬럼 X, Last Price 컬럼 X.

### Mock 데이터

| Ticker  | Weight | Held / Hor | Value     | Since   |
|---------|--------|-----------|-----------|---------|
| ORIO.TO | 74%    | 1d / 3y   | 513,240   | -18.3%  |
| BWEN    | 4.9%   | 2w / 5y   | 33,600    | +10.4%  |
| FND     | 3.9%   | 3w / 5y   | 26,862    | -2.5%   |
| OSCR    | 3.0%   | 6m / 3y   | 20,580    | -4.7%   |
| RELY    | 2.0%   | 1.5y / 3y | 19,456    | +26.1%  |
| GOOG    | 0.8%   | 2y / 5y   | 1.94M     | +26.1%  |

(모든 값 CAD 환산; column header에 "Value CAD" 한 번만 표기.)

---

## 시각 hierarchy

- **Primary** (off-white, `#EDEDED`): Ticker, Weight, Value (숫자)
- **Secondary** (회색, ~`#aaa`): Held / Hor, since-entry %
- **Chrome** (희미하게, ~`#444`–`#777`): scope 라벨, 컬럼 헤더, "CAD" 단위, divider (`#1a1a1a`–`#222`)

Rationale: Primary = 사용자 identity와 position 크기. Secondary = commitment 컨텍스트 (Held / Hor) 와 historical performance (since-entry %) — 있되 경쟁 X. Chrome = orientation만. Doctrine §8은 라벨이 body와 경쟁 안 하는 subtle hierarchy 요구.

---

## v1/v2 에서 제거된 것

- **Weight bar** (Weight 숫자 아래 시각 막대) — 회장 v2가 이미 제거. v3도 유지. *Rationale*: 장식적, % 숫자 외 정보 없음. Doctrine §8.
- **Daily ±% / Daily price** — 변경 #3 참조.
- **Last Price 컬럼** — 빠짐. *Rationale*: Last price는 본질적으로 intraday, list 레벨에서 decision-relevant 아님. 사용자가 Stock Detail에서 볼 수 있음. 제거하면 컬럼 폭을 Held/Horizon과 Value에 돌려줌.
- **Row마다의 "CAD" 텍스트** — column header로 이동. 변경 #4 참조.

---

## Calibration 데이터 위치 (와 그 이유)

**Buy / sell flow**: stated confidence + system baseline confidence 둘 다 결정 시점에 사용자에게 노출 (현재 calibration 디자인 기준 — WIP).

**Stock Detail 페이지**: calibration plot (선 + over/under 점). 시각적으로 self-explanatory. Self-audit의 dedicated surface.

**Active Position list (이 spec)**: 표시 X. **의도적 restraint.** List는 orientation과 commitment 진행률 (Held / Horizon) 만 보여줌.

이 분할은 doctrine-aligned: list = orientation, Stock Detail = analysis. Mogo Design Philosophy §14에서 Dashboard (orientation) 와 Stock Detail 분리하는 같은 원칙.

---

## Open questions (PM / 회장 / calibration owner와 결정)

1. **Horizon 출처**: `Horizon` 이 buy flow (calibration) 에서 사용자가 명시적으로 commit한 값인가, default에서 derive된 건가? Derive면 컬럼이 misleading. **이게 v3 ship의 blocker.**
2. **Held 만기 동작**: `held >= horizon` 일 때 (a) `3y / 3y` 그대로 표시, (b) row를 re-calibration용으로 flag, 아니면 (c) 자동으로 re-calibration 트리거?
3. **정렬 순서**: 현재 weight desc (v1/v2와 동일). 단일 고정 순서로 OK? 아니면 multi-sort? Sort control 추가는 broker 패턴으로 drift.
4. **Empty state**: active position 0개일 때 화면? (격려하는 톤이면 안 됨 — 진지한 투자자가 0 position이면 *의도적으로* 0임.)
5. **Currency 표시 detail**: USD 종목이 Stock Detail에서는 원본 currency (USD-native price + value) 같이 표시할까? (List는 전부 CAD라도.)
6. **Daily ±% / daily price 제거 — 회장 동의**: v2는 유지; v3는 변경 #3의 rationale로 제거 제안. Claude Design build 전에 회장 confirm. 회장이 daily 유지 고집하면, **대안 C** (|Δ| > 3% 일 때만 daily ± 표시) 가 가능한 타협.
7. **Calibration 컬럼 미포함 — 회장 / calibration-owner 동의**: confidence pair는 Stock Detail에만, list X 라는 결정 (변경 #5) confirm.

---

## Dependencies

- **Calibration 페이지 (WIP)**: 최소한 buy 시점에 `confidence` 와 `horizon` capture 필요 — `Held / Horizon` 작동에 필요.
- **Account scope 모델**: 4 화면 (Dashboard, Active Positions, Stock Detail, Holdings) 일관된 결정 필요 — v3 단독으로는 못 풂. 단지 *문제를 숨기지 않게* 해줄 뿐.
- **USD → CAD 환산** 로직 (data layer) — 모든 position을 CAD로 표시하기 위해.

---

## 다음 단계

1. PM 미팅 (11:00 또는 16:00) 에서 이 spec 같이 review.
2. Calibration 가정 (`confidence`, `horizon`) 확정.
3. Open Question #1, #6, #7 — 회장과 결정.
4. **Claude Design** 에서 II Design System 으로 build.
5. Claude Design URL 이 폴더에 다시 저장.
6. Internal test (Stage 2) — shadow data로, external rollout 전.

---

## 관련 파일

- `Mogo Design Philosophy.md` — doctrine (Alignment Rules 추가됨)
- `references/ICP Definition V1.md`
- `references/Figma vs Prototype Decision Rule.md`
- `v3-list-sketch.html` — 시각 reference (이 폴더)
- `v3-list-spec-en.md` — 영어본
