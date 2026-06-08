# II Stock Page — User Experience Structure

> 🔒 **LOCKED at J49** (v11 baseline). **L 시리즈 active iteration** (v13, 2026-06-07).
> 회장 doctrine 기반 user flow + V bump + history 룰 + reaffirmation tracking.
> 큰 구조 + Memo Review II-tone + bottom sheet 패턴.
> v11: locked baseline. v12: K-series (step indicator). v13: L-series (II-tone reframe, intent-aware copy, reaffirmation).
> 매수/매도 *뒤*에 일어나는 디테일은 제외 (Rio scope, Select Account.html placeholder).

## 변경 로그

| 단계 | 내용 |
|---|---|
| **J39** | Memo Review row tap = single edit, Edit 페이지 Exit 시 CD 플래그 클리어 |
| **J40** | History 진입점 위치 결정 — Memo Review 페이지 우측 (Stock Page 아님) |
| **J41** | Buy flow wiring — Capital Decision Bottom Sheet → Memo Review → Save 분기 + Select Account 라우팅 |
| **J42** | History entry 생성 (V1/V2 commit 시 trigger + position 메타데이터 포함) + Memo History list page 신규 |
| **J43** | First-time Memo Flow의 Commit V1 후 → Stock Page Memo Only 대신 Select Account (Buy flow 진입) |
| **J44** | hasChanges() 버그 fix — JS 변수 → history 마지막 snapshot 비교 (page reload 안전) + Re-underwrite CTA의 atz-cd-action 클리어 |
| **J45** | Memo Review back button 버그 fix — goToHistory가 atz-memo-stock-source 덮어쓰던 버그, 별도 키 atz-history-from 도입 |
| **J46** | First-time Memo Flow도 변경 detect — V_N 이미 있고 변경 없으면 V bump 없이 Buy flow 직행 (모달도 skip) |
| **J47** | CTA + Modal 라벨 통일 — "Commit V_N" → "Save as V_N" 전역 통일 (First-time Memo Flow ↔ Memo Review 일관성) |
| **J48** | Firsttime User Re-underwrite stub 라우팅 fix — Active + Core 모두 Return user_Memo Review (Core)로 정정 + atz-cd-action 클리어 추가 |
| **J49** | 한치 오차 없는 flow audit — 잔여 stub 라우팅 일소 (Multi-Quarter Alerts·Memo Only selectCdAction · Firsttime User (Core) Capital Decision source setter · Memo History 인코딩 일관성 · empty state 카피 "Save V1"로 통일) |
| **K1** | v12 Edit 페이지에 step indicator "n/5" 추가 (CD mode 한정) |
| **K2** | Step indicator gate 강화 — URL `?cd=1` + no V_N (session flag leak 방지) |
| **K3** | Step indicator를 fresh walkthrough only로 한정 — `atz-fresh-walkthrough` flag |
| **K4** | Step indicator edge case audit — Exit/back/Reset/Core/mid-walkthrough back 모든 경로 + #2 fix (filled>0 분기 flag clear 제거) |
| **K5** | Memo Review defensive clear (atz-cd-mode 포함) — Re-underwrite mode에서 walkthrough flag leak 방지 |
| **K6-K7** | Runtime click-through test (Chrome MCP via localhost) — 16개 시나리오 PASS |
| **K8** | Runtime audit 발견 regression 2건 fix: (1) Memo Review JS `'Commit V_N'` → `'Save as V_N'` (J47 regression) (2) Reset state LS_KEYS/SS_KEYS 4개 누락 추가 |
| **L0** | v13 폴더 생성 — v12 baseline에서 새 iteration 시작 |
| **L1** | Memo Review intent-aware copy — Re-underwrite vs Capital Decision (buy/increase/reduce/exit) 별로 hero, explainer, save 버튼 동적 변경 |
| **L2** | II-tone hero reframe — action-first hero ("Adding ATZ", "Reducing ATZ" 등) + stance subtitle + institutional ticker line (가격+%change+날짜). 회장 디자이너 패턴 차용 |
| **L3** | Memo Review borrows — "Save memo" 라벨, "→ Discard changes" secondary CTA (변경 있을 때만 visible), section header "Tap each to update" hint, subtitle "↗" lbl-tap. Field inline description은 시도 후 revert (memo block은 clean summary 유지) |
| **L4** | Stance ↗ inline panel → full bottom sheet. Eyebrow + headline + stock-specific inner card + Active/Core doctrine + compliance disclaimer footer |
| **L5** | Reaffirmation history entries — Memo 변경 없는 거래도 history에 기록 (trigger: "Buy"/"Reduce"/"Exit" 단독, V 그대로). "operation 측정" 강화. Memo History UI에 reaffirmation vs V bump 시각 구분 |
| **L6** | L1-L5 종합 audit (12 시나리오 매트릭스) — 모두 PASS. Type 2 cdSheet 'open'/'pass' dead code 발견 (실제 flow는 top-level CTA 'buy' 사용) |
| **L7** | Doctrine + artifact 동기화 (이 changelog 포함) |

---

## 핵심 원칙 (회장님 doctrine)

### 1. Memo와 Position은 별개 axis
```
MEMO    :  Draft → V1 → V2 → V3 ...   (분석)
POSITION:  None → Held → None ...      (보유 여부)
```

### 2. No capital action without memo review
모든 자본 액션 (Buy/Sell/Exit) 은 **Memo Review를 거쳐야 함**.
거래는 독립적 액션이 아니라 *메모의 결과*.

### 3. 필드 하나라도 바뀌면 V bump
Memo Review에서 어느 필드든 수정되면 → **V bump (V2, V3...)**
안 바뀌면 V 그대로.

→ 거래 자체로는 V 안 만듦. V bump 트리거는 **필드 변경**.

---

## 유저 타입 3가지

### Type 1 — First-time user
처음 종목 본 사람. 메모 없음 또는 작성 중, 보유 없음.

Type 1은 sub-state 3개:
- **1a Fresh** — 메모 시작 안 함
- **1b Draft 진행중** — 1-4/5 채움 (V1 아님)
- **1c Draft 완성** — 5/5 채움 (V1 commit 직전)

### Type 2 — Memo-only user
메모는 있는데 보유는 없는 사람.
(메모만 쓰고 안 산 사람 + Exit한 사람)

### Type 3 — Return user
메모도 있고 보유도 있는 사람.

---

# 🌱 Type 1 — First-time User

> 시작: 메모 없음, 보유 없음

## Type 1 — 두 진입 경로

```
Stock Page Firsttime User에서 두 CTA:
  ① Underwrite     → 메모만 작성 의도 (Memo Only로 끝낼 수도)
  ② Capital Decision → 매수 의도 (V1 commit 후 Buy flow 진입)
```

## 가능한 흐름

### 흐름 A — Capital Decision 경로 (매수 의도)
```
Type 1a (Fresh)
    │ Capital Decision 탭
    ↓
First-time Memo Flow
    │ Continue → 빈 필드 walkthrough → 5/5 채움
    │ Commit V1 모달
    ↓
★ V1 시점 → V1 commit + history (Underwrite, none)
    │
    ↓
Select Account (Buy flow 진입 ※ 다른 디자이너)
    ↓ 매수 체결
Stock Page Return User (Type 3)
```

### 흐름 B — Underwrite 경로 (메모만 의도)
```
Type 1a (Fresh)
    │ Underwrite → Blank Memo
    │ 5/5 모두 채움 → Save & Return
    ↓
Type 1c (Draft · 5/5)        ← 아직 V1 아님
    │
    │ 여기서 결정:
    │  (a) Capital Decision → 흐름 A로 합류 (매수)
    │  (b) 그냥 둠 → Draft로 유지 (V1 아님, 보유 없음)
```

### 흐름 C — 부분 작성 후 재개
```
Type 1a (Fresh)
    │ Underwrite → Blank Memo
    │ 3개만 채움 → Save & Return
    ↓
Type 1b (Draft · 3/5)        ← 영구 저장됨, V1 아님
    │
    │ (며칠 후) Resume Draft → 나머지 채움
    ↓
Type 1c (Draft · 5/5) → Capital Decision → Commit V1 → Buy flow
```

### 흐름 D — 부분 작성 상태에서 Capital Decision (walkthrough)
```
Type 1b (Draft · 3/5)
    │ Capital Decision 탭                   ★ 5/5 아닌데 눌렀음
    ↓
체크포인트 페이지: "2 fields left"
    │ Continue → 빈 필드 walkthrough
    │ 5/5 채워짐
    ↓
Commit V1 → Buy flow 진입
```

### 흐름 E — Draft 삭제
```
Type 1b/1c → Resume → Blank Memo → Delete draft → 확인
    ↓
Type 1a로 복귀 (모든 필드 wipe)
```

→ **Capital Decision = 매수 의도** (회장 doctrine). V1 commit 후 자동으로 Buy flow 진입.
→ **Underwrite만으로는 V1 안 만들어짐.** Draft state만 가능 — Capital Decision 거쳐야 V1.

---

# 📜 Type 2 — Memo-only User

> 시작: V1+ 메모 있음, 보유 없음

## 가능한 행동 3가지

### 행동 A — 그냥 둠
변화 없음. 메모는 audit log로 보존.

### 행동 B — 매수 (Memo Review 경유 → Type 3 전환)
```
Stock Page Memo Only
    │
    │ Buy / Capital Decision
    ↓
Memo Review 페이지                   ★ V1 hydrate, 수정 가능
    │
    │ 옵션 1: 수정 없이 진행
    │   → Save → 거래 체결, V1 유지
    │
    │ 옵션 2: 필드 수정
    │   → Save → V2 commit + 거래 체결
    ↓
Type 3로 전환
```

### 행동 C — Re-underwrite만 (V bump, 거래 없음)
```
Stock Page Memo Only
    │
    │ Re-underwrite
    ↓
Memo Review 페이지
    │
    │ 필드 수정 → Save (거래 없이)
    ↓
Commit V2                          ★ V2 시점
    ↓
Type 2 유지 (V2, 여전히 보유 없음)
```

→ **Type 2에서 V bump는 두 가지 경로**: 매수 도중 수정 / Re-underwrite 단독.

---

# 🌳 Type 3 — Return User

> 시작: V1+ 메모 있음, 보유 있음

## 회장님 구조 — 모든 자본 액션은 Memo Review를 거침

```
Stock Page Return User
    │
    │ Capital Decision CTA 탭
    ↓
Bottom Sheet (액션 선택)
  [Buy more] [Sell some] [Exit]
    │
    │ 하나 선택
    ↓
Memo Review 페이지                   ★ 모든 자본 액션의 교차점
  - 현재 V_N 필드 모두 hydrate
  - 각 필드 tap해서 수정 가능
  - 수정 detect 로직
    │
    ↓
필드 변경 여부에 따라 분기:

  변경 있음 → V bump (V2/V3...) + 거래 체결
  변경 없음 → V 그대로 + 거래 체결
```

## 가능한 행동

### 행동 A — Increase (더 사기)
- Memo Review 경유 → Save
- 필드 바꿨으면 V bump
- 보유 ↑

### 행동 B — Reduce (일부 매도)
- Memo Review 경유 → Save
- 필드 바꿨으면 V bump
- 잔여 > 0 → Type 3 유지
- 잔여 = 0 → Type 2 전환

### 행동 C — Exit (전량 매도)
- Memo Review 경유 → Save
- 필드 바꿨으면 V bump
- 보유 → 0 → Type 2 전환 (메모는 history)

### 행동 D — Re-underwrite (V bump, 거래 없음)
- Memo Review 진입 (Re-underwrite intent)
- 필드 수정 → Save
- V bump
- Type 3 유지 (보유 변동 없음)

---

## Memo Review 페이지 — 통합 진입점

```
들어오는 경로:
  ① Capital Decision (거래 의도)
  ② Re-underwrite CTA (분석만 업데이트 의도)

페이지 동작:
  - V_N 필드 hydrate
  - 사용자가 tap해서 수정 가능
  - 변경 detect
  - 하단 CTA = "Save" (단일)

Save 탭 시 동작 분기:

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Re-underwrite intent
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  변경 있음:
    → 모달: "계속 편집 / 새 버전 만들기"
      ├ 계속 편집 → Memo Review로 돌아감
      └ 새 버전 만들기 → V bump → Stock Page 복귀
  변경 없음:
    → "No changes" 경고 (또는 그냥 Stock Page 복귀)

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Capital Decision intent
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  변경 있음:
    → 모달: "계속 편집 / 새 버전 만들기"
      ├ 계속 편집 → Memo Review로 돌아감
      └ 새 버전 만들기 → V bump → 사는 경험으로 진입 (Select Account)
  변경 없음:
    → 사는 경험으로 직행 (Select Account) — V 그대로
```

→ 페이지 자체는 하나. **진입 의도가 Save 후 동작을 결정.**
→ 모달은 "변경 사항 있을 때 V bump 확인" 용도.

## 사는 경험 (Buy Flow) — 다른 디자이너 scope

회장님께서 별도 디자이너가 이미 구현한 흐름:

```
1. Select account       (Non-Registered / TFSA / RRSP 중 선택)
2. Order entry          (Limit Price, Shares 입력, numpad)
3. Order details        (Duration, Estimated cost, Calibration)
4. Review & execute     (Memo summary 포함, "Hold to confirm")
5. Order filled         (체결 완료, Done)
```

→ **이 prototype (v11 Stock Page) 작업 범위 밖.**
→ 우리는 Memo Review의 Save (Capital Decision intent) 가 이 흐름의 첫 페이지 (**Select Account**) 로 라우팅하면 됨.
→ 거래 체결 후 돌아올 때 Return User 상태로 Stock Page 표시 (LS state로 추적).

---

# 🔁 타입 간 전이 다이어그램

```
   ┌──────────── Type 1: First-time user ────────────┐
   │                                                  │
   │   1a Fresh ──Underwrite──▶ 1b Draft (1-4/5)     │
   │                                  │               │
   │                                  │ 마저 채움      │
   │                                  ▼               │
   │                            1c Draft (5/5)       │
   │                                  │               │
   │                          Capital Decision        │
   │                          → Commit V1 모달        │
   └──────────────────────────────────┼───────────────┘
                                      │
                              ★ V1 시점 (단 하나)
                                      │
                                      ▼
        ┌─────────────────────────────────────┐
        │   ┌──────────────────┐              │
        │   │ Type 2           │              │
   ─────┤   │ Memo-only user   │◀────────────┤
   Buy  │   │ (memo O, hold X) │   Exit      │
        │   └────────┬─────────┘              │
        │            │                        │
        │            │ Re-underwrite          │
        │            │ → V bump               │
        │            │ (Type 2 유지)          │
        │            ▼                        │
        │   ┌──────────────────┐              │
        │   │ Type 3           │              │
        └──▶│ Return user      │──────────────┘
            │ (memo O, hold O) │
            └──────────────────┘
              ↑          ↓
              └──────────┘
              Increase / Reduce / Re-underwrite
              (모두 Memo Review 경유)
```

> Type 2 ↔ Type 3 사이를 오갈 때마다, 그리고 같은 타입 안에서 거래나 Re-underwrite할 때마다 **Memo Review를 거침**.

---

# ⚡ V 시점 — 한 줄 요약

| V trigger | 시점 |
|---|---|
| **V1** | Type 1c → Capital Decision → Commit V1 모달 확인 |
| **V2/V3...** | Memo Review에서 필드 하나라도 수정 + Save / Save (Capital Decision intent) |

> **V bump 룰**: Memo Review에서 어떤 필드든 바뀌면 V bump. 거래만으로는 V 안 만듦.

---

# 📚 Memo History에 미치는 영향

## 기본 룰

> **V bump 1번 = History entry 1개 추가.**
> V bump 안 일어나면 history 안 늘어남.

History는 V1, V2, V3... 각 버전의 **snapshot 리스트**. 거래 자체는 history에 추가 안 됨 (V bump이 동반될 때만 함께 기록).

## History entry 내용

각 entry가 담는 것:

```
{
  version:      "V2",                    ← 버전 번호
  timestamp:    1735000000000,           ← commit 시점
  trigger:      "Re-underwrite + Sell",  ← V bump 일으킨 액션
  position:     "held"                   ← commit 당시 보유 상태
                | "none"
                | "exiting",
  classification: "Compounder",
  sizing:         "Conviction",
  confidence:     50,
  horizon:        "3y",
  idea-origin:    "13F",
  investment-case: "...",
}
```

→ Version의 5개 필드 전체 snapshot + 메타데이터 (timestamp, trigger, position).

## Trigger 종류

| Trigger | 의미 |
|---|---|
| `Underwrite` | First-time V1 commit (최초 분석) |
| `Re-underwrite` | Memo Review에서 분석만 업데이트 (거래 없음) |
| `Re-underwrite + Buy` | Memo Review에서 분석 수정 + 매수 |
| `Re-underwrite + Reduce` | Memo Review에서 분석 수정 + 일부 매도 |
| `Re-underwrite + Exit` | Memo Review에서 분석 수정 + 전량 매도 |

→ trigger가 "분석을 왜 바꿨는지" context를 audit log에 남김.

## Action별 History 영향 매트릭스

| Action | 필드 변경 | V bump | History entry 추가 | Trigger 기록 |
|---|---|---|---|---|
| Underwrite (Type 1c → V1) | — | V1 생성 | ✅ 1개 | `Underwrite` |
| Re-underwrite (Save) | ✅ | V → V+1 | ✅ 1개 | `Re-underwrite` |
| Re-underwrite (Save) | ❌ no-op | X | ❌ | — (경고 모달) |
| Buy (변경 없음) | ❌ | X | ❌ | — |
| Buy (변경 있음) | ✅ | V → V+1 | ✅ 1개 | `Re-underwrite + Buy` |
| Reduce (변경 없음) | ❌ | X | ❌ | — |
| Reduce (변경 있음) | ✅ | V → V+1 | ✅ 1개 | `Re-underwrite + Reduce` |
| Exit (변경 없음) | ❌ | X | ❌ | — |
| Exit (변경 있음) | ✅ | V → V+1 | ✅ 1개 | `Re-underwrite + Exit` |

> **핵심**: 거래 자체는 history 안 만듦. **분석 (필드) 바뀐 commit만** history에 기록.

## Position 상태 기록

각 history entry는 commit 시점의 **position 상태**를 함께 저장:

- `none` — 보유 없음 (Type 2 상태에서 commit)
- `held` — 보유 중 (Type 3 상태에서 commit)
- `exiting` — Exit과 함께 commit된 V (보유 → none으로 전환되는 순간)

→ 이걸로 audit 시 "이 버전은 보유 중에 만든 것 / 매도하면서 만든 것" 구분 가능.

## 예시 시나리오 → History 결과

### 시나리오 1 — V1 commit만, 안 삼
```
Action          : Type 1c → Commit V1
History         : [V1 (trigger: Underwrite, position: none)]
```

### 시나리오 2 — V1 commit + 며칠 후 매수 (분석 변경 없음)
```
Action 1        : Commit V1
Action 2        : Type 2 → Capital Decision → Memo Review → Save (필드 안 바꿈)
History         : [V1 (trigger: Underwrite, position: none)]
                  ← V 안 늘어남, 위치만 none → held로 변환
```

### 시나리오 3 — Re-underwrite하면서 매수 (Confidence 수정 + 매수)
```
Action 1        : Commit V1 (안 삼)
Action 2        : Capital Decision → Memo Review에서 Confidence 70 → 80 수정 → Save
History         : [
                    V1 (trigger: Underwrite, position: none),
                    V2 (trigger: Re-underwrite + Buy, position: held)
                  ]
```

### 시나리오 4 — Return User가 Re-underwrite 후 Exit
```
Action 1        : V1 commit + 매수 → Type 3
Action 2        : Memo Review (Confidence 떨어뜨려 Pass) + Exit
History         : [
                    V1 (trigger: Underwrite, position: none),
                    V2 (trigger: Re-underwrite + Exit, position: exiting)
                  ]
```

### 시나리오 5 — 분석 자주 바꾸지만 거래는 안 함
```
Action 1        : Commit V1
Action 2        : Re-underwrite (Sizing만 수정) → Save
Action 3        : Re-underwrite (Confidence만 수정) → Save
History         : [
                    V1 (Underwrite, none),
                    V2 (Re-underwrite, none),
                    V3 (Re-underwrite, none)
                  ]
```

### 시나리오 6 — Reduce하면서 분석은 그대로 (V 안 늘어남)
```
시작: V2, 100주 보유
Action          : Capital Decision → Reduce → Memo Review (수정 안 함) → Sell 50주
History         : [V1 (...), V2 (...)]  ← 변화 없음
Position        : 100주 → 50주
```

---

## History UI 시사점

- Stock Page History 페이지에는 **V1, V2, V3 각 entry가 row로 표시**됨
- 각 row 클릭 시 해당 시점의 메모 snapshot 보기 가능
- Trigger 정보로 "왜 이 버전이 만들어졌는지" 빠르게 파악
- Position 정보로 "이 버전은 held 상태에서 만든 것" 등 audit 컨텍스트

---

# 📌 정리 (한 화면)

1. **유저는 3 타입**: First-time → Memo-only → Return user
2. **타입은 (memo 있냐) × (보유 있냐)** 의 2x2 조합
3. **V1 시점은 단 하나**: Capital Decision flow의 Commit V1
4. **V bump 룰**: Memo Review에서 필드 변경 시 V2/V3 자동 생성
5. **모든 자본 액션은 Memo Review를 거침** (회장님 doctrine: no action without review)
6. **거래만으로는 V 안 만듦** — V는 분석 (필드) 변경할 때만 bump
7. **History entry 추가도 V bump 동반시에만** — 거래 자체로는 history 안 늘어남

매수/매도 *이후*의 디테일 (Order Confirmation 폼, Sizing 경고, Pass 처리 등)은 별도 문서로.

---

# ✅ Audit Checklist (Mockup 적용 추적)

> 각 항목 audit 후 ☐ → ☑ 로 마킹.
> 회장님 doctrine 기준으로 현재 v11 상태 검증.

## A. Type 1 (First-time User)

- [x] **A1** Stock Page Firsttime User — 1a (Fresh) 상태 표시 정확 ✅
- [x] **A2** Stock Page Firsttime User — 1b (Draft 1-4/5) indicator 표시 정확 ✅
- [x] **A3** Stock Page Firsttime User — 1c (Draft 5/5) indicator + Capital Decision CTA 가시성 ✅ (fixed)
       - ✅ Capital Decision CTA 항상 가시
       - ✅ FIXED: 1c indicator "Ready · 5 of 5 fields" (1b "Draft · N of 5"와 구분)
       - ✅ FIXED: 1c CTA "Edit Draft" (resume 아님)
       - 시각 강조는 indicator/CTA 라벨 변화로 충분
- [x] **A4** Underwrite CTA → Blank Memo 라우팅 ✅
- [x] **A5** Blank Memo Save & Return → Stock Page (Draft state 유지) ✅
- [x] **A6** Resume Draft 진입 시 hydrate 정확 ✅
- [x] **A7** Delete draft → 모든 LS wipe + Type 1a 복귀 ✅
- [x] **A8** Capital Decision (1b에서) → 빈 필드 walkthrough chain ✅
- [x] **A9** Capital Decision (1c에서) → Commit V1 모달 ✅
- [x] **A10** Commit V1 후 routing → **Select Account (Buy flow)** ✅ J43
       - ✅ LS set (version, decision, stance), draft cleanup
       - ✅ J42: V1 commit 시 history entry 추가 (trigger='Underwrite', position='none')
       - ✅ J43: routing — Stock Page Memo Only 대신 Select Account로 직행 (Capital Decision = 매수 flow doctrine)
       - 매수 안 하려면 Select Account에서 Cancel

## B. Type 2 (Memo-only User)

- [x] **B1** Stock Page Memo Only 진입 조건 정확 (V1+ AND no position) ✅
       - ✅ V1+ seed, position 키 없음 (= 보유 없음)
       - ✅ FIXED 🐛: 7개 stock 페이지 setItem/getItem 잘못된 인자 (`'atz-memo-draft-progress','atz-memo-demo-schema', SCHEMA` → 정상 형태로) — schema check이 영구 실패하던 버그
- [x] **B2** Re-underwrite CTA → Memo Review 페이지 ✅
- [x] **B3** Capital Decision CTA → Memo Review 페이지 ✅ J42 (routing fix)
- [x] **B4** Memo Review에서 변경 없이 Save → Select Account 직행 ✅ J41
- [x] **B5** Memo Review에서 변경 후 Save → 모달 → V bump → Select Account ✅ J41/J42/J44
- [x] **B6** Re-underwrite (Save only) → V bump ✅ J44 (no-op detection 정확히 작동)
- [x] **B7** Type 2 → Type 3 전환 routing ✅ Select Account 진입까지 wiring 완료 (Buy flow 자체는 다른 디자이너)

## C. Type 3 (Return User)

- [x] **C1** Stock Page Return User 진입 조건 정확 (V1+ AND position held) ✅ (Position LS key는 GAP, → G5/G6)
- [x] **C2** Capital Decision CTA → Bottom Sheet [Buy / Sell / Exit] ✅ (+ 🐛 4개 파일 broken routing fix)
- [x] **C3** Bottom Sheet 선택 → Memo Review 페이지 ✅ (J41 — selectCdAction 라우팅 수정)
- [x] **C4** Memo Review에서 변경 없이 거래 → 거래만 (Select Account 직행), V 그대로 ✅ (J41 onSave)
- [x] **C5** Memo Review에서 변경 후 거래 → 모달 → V bump + 거래 (Select Account) ✅ (J41 onSave + commitMemo)
- [x] **C6** Re-underwrite CTA → Memo Review (intent: Save only) ✅ (J41 — atz-cd-action 없으면 Re-underwrite)
- [⚠️] **C7** Reduce 결과 잔여 0주 → Type 2 전환 — Buy flow 다른 디자이너 영역 (Order page에서 처리)
- [⚠️] **C8** Exit → Type 2 전환, 메모 history로 보존 — 동일

## D. Memo Review 페이지 (통합 진입점)

- [x] **D1** 진입 의도 detect (Capital Decision vs Re-underwrite) ✅ (J41 — `getIntent()` reads `atz-cd-action`)
- [x] **D2** 현재 V_N 필드 hydrate 정확 ✅ (`hydrateRows()`)
- [x] **D3** 각 필드 tap → Edit 페이지 → 저장 후 복귀 ✅
- [x] **D4** 필드 변경 detect 로직 (diff) ✅ (J41 — `snapshotBaseline` + `hasChanges`)
- [x] **D5** 하단 CTA = "Save" (단일 버튼, 의도에 따라 동작 분기) ✅ (J41 `onSave`)
- [x] **D6** Save 시 (Re-underwrite intent + 변경 있음): 모달 → 새 버전 → V bump → Stock Page 복귀 ✅
- [x] **D7** Save 시 (Re-underwrite intent + 변경 없음): 그냥 Stock Page 복귀 (no-op) ✅ (Active+Core 둘 다)
- [x] **D8** Save 시 (Capital Decision intent + 변경 있음): 모달 → 새 버전 → V bump → Select Account ✅
- [x] **D9** Save 시 (Capital Decision intent + 변경 없음): Select Account 직행 (V 그대로) ✅

★ Active (Return user_Memo Review.html) + Core (Return user_Memo Review (Core).html) 둘 다 완료

## E. V bump & History 룰

- [x] **E1** V bump 트리거 — 필드 변경 detect 정확 ✅ J41 (`hasChanges` in Memo Review 둘 다)
- [x] **E2** History entry 추가 — V bump 동반시만 ✅ J42 (3개 파일 commitMemo)
- [x] **E3** History entry 필드 — version, timestamp, trigger, position, 5 fields ✅ J42
- [x] **E4** Trigger 라벨링 — Underwrite / Re-underwrite / + Buy / + Reduce / + Exit ✅ J42 (`buildTrigger`)
- [x] **E5** Position 상태 기록 — none / held / exiting ✅ J42 (`inferPosition` — source URL 기반 추론)
- [x] **E6** No-op detection (변경 없는 Save) 작동 ✅ J41 (Save 후 변경 없으면 모달 skip)

## F. History UI

- [x] **F1** History 진입점 — Memo Review 페이지에 "History" 링크 (J40) ✅
       - 디자인 결정: Stock Page 대신 Memo Review에 위치 (메모의 속성이라는 컨텍스트)
- [x] **F2** History 페이지 — V1, V2, V3... row 리스트 ✅ J42 (`Memo History.html` 신규)
- [x] **F3** 각 row tap → 해당 V의 snapshot 보기 ✅ J42 (modal로 전체 필드 + memo 표시)
- [x] **F4** Trigger 정보 표시 (왜 이 V가 만들어졌는지) ✅ J42 (row meta에 표시)
- [x] **F5** Position context 표시 (held / none / exiting) ✅ J42 (row meta에 표시, 색상 구분)

## G. 누락 / 미구현 (★ 우선순위 높음)

- [x] **G1** Stock Page Memo Only의 Capital Decision CTA 라우팅 수정 (→ Memo Review) ✅ J42 (Active + Core 둘 다)
- [x] **G2** Stock Page Return User의 Capital Decision Bottom Sheet (Buy / Sell / Exit 선택 → Memo Review) ✅ J41
- [x] **G3** Memo Review의 Save 시 "계속 편집 / 새 버전 만들기" 모달 ✅ J41
- [x] **G4** 필드 변경 detect → V bump 자동 트리거 ✅ J41
- [x] **G5** Memo Review의 "새 버전 만들기" → V bump → Select Account 라우팅 ✅ J41
- [ ] **G6** Position 상태 추적 LS 키 (atz-position-status) — 다른 디자이너 Buy flow에서 set
- [x] **G7** Trigger 라벨링 로직 — history entry에 기록 ✅ J42 (`buildTrigger` + `inferPosition`)

**※ Buy flow (Select Account → Order entry → Review → Filled) 는 다른 디자이너 scope. 우리는 진입점만 wiring 완료.**

---

**다음 단계**: 위 checklist 항목 하나씩 audit하면서 현재 mockup과 비교 → gap 식별 → 우선순위 매겨서 구현.

---

# 🔒 J44 LOCKED — 최종 상태

## 진척도

| 그룹 | 진행 | 비고 |
|---|---|---|
| **A** Type 1 First-time | ✅ 10/10 | A3 fix + A10 routing fix |
| **B** Type 2 Memo-only | ✅ 7/7 | J41/J42/J44 |
| **C** Type 3 Return User | ✅ 6/8 | C7, C8은 Buy flow 다른 디자이너 영역 |
| **D** Memo Review 페이지 | ✅ 9/9 | J41 |
| **E** V bump & History 룰 | ✅ 6/6 | J42/J44 |
| **F** History UI | ✅ 5/5 | J42 (Memo History.html 신규) |
| **G** GAP | ✅ 6/7 | G6 Position LS key는 다른 디자이너 영역 |

## 신규/수정 파일 (이번 작업)

### 신규
- **Select Account.html** — Buy flow 진입점 placeholder (다른 디자이너 영역 표기)
- **Memo History.html** — V1, V2, V3... list view + snapshot modal

### 수정
- **First-time Memo Flow.html** — J42 (history entry 추가) + J43 (V1 commit 후 Select Account 라우팅)
- **Return user_Memo Review.html** — J41 (onSave 분기, modal 2 옵션) + J42 (history entry, trigger/position) + J44 (hasChanges history 기반)
- **Return user_Memo Review (Core).html** — 동일 (stub → full implementation)
- **Stock Page Return User.html** — J41 (Bottom Sheet routing) + J44 (Re-underwrite atz-cd-action clear) + 🐛 setItem fix
- **Stock Page Return User - History.html** — 동일
- **Stock Page Return User (Core).html** — 동일
- **Stock Page Return User - History (Core).html** — 동일
- **Stock Page Memo Only.html** — J42 (Capital Decision routing) + J44 (Re-underwrite clear) + 🐛 setItem fix
- **Stock Page Memo Only (Core).html** — 동일
- **Stock Page Multi-Quarter Alerts.html** — J44 (Re-underwrite clear) + 🐛 setItem fix
- **Stock Page Firsttime User.html** — A3 (1c 라벨 차별화)

## 발견 + fix된 핵심 버그

| 버그 | 영향 파일 | 영향 |
|---|---|---|
| 🐛 `setItem('atz-memo-draft-progress','atz-memo-demo-schema', SCHEMA)` 잘못된 인자 | 7개 stock 페이지 | demo schema check 영구 실패 → 매번 재seed |
| 🐛 Bottom Sheet → 존재하지 않는 `Capital Decision Review.html` | 4개 stock 페이지 | Capital Decision 액션 broken |
| 🐛 Memo Only Capital Decision CTA → stub 페이지 | 2개 (Active+Core) | Capital Decision 끝점 없음 |
| 🐛 Re-underwrite CTA가 stale `atz-cd-action` 안 비움 | 7개 stock 페이지 | Memo Only 재진입 시 잘못 Buy flow로 |
| 🐛 hasChanges()가 JS 변수 → page reload 시 손실 | 2개 Memo Review | 변경 detect 영구 false → 모달 안 뜸 |

## 최종 동작 매트릭스

```
Type 1 (First-time) Capital Decision flow:
  Stock Page Firsttime → Capital Decision CTA
  → First-time Memo Flow walkthrough → 5/5
  → Commit V1 모달 → confirm
  → V1 commit + history(Underwrite, none)
  → Select Account (Buy flow 진입) ★ 다른 디자이너 영역

Type 2 (Memo Only) Re-underwrite:
  Stock Page Memo Only → Re-underwrite CTA (atz-cd-action 클리어)
  → Memo Review → 필드 수정 → Save
  → 모달: "Save as V2 / Keep editing"
  → "Save as V2" → V2 commit + history(Re-underwrite, none)
  → Stock Page Memo Only (V2 반영)

Type 2 (Memo Only) Capital Decision:
  Stock Page Memo Only → Capital Decision CTA (atz-cd-action='buy')
  → Memo Review → (옵션: 필드 수정) → Save
  → [변경 있으면 모달] → "Save as V2" → V2 commit + history(Re-underwrite+Buy, held)
  → Select Account (Buy flow 진입)
  → [변경 없으면 직행] Select Account

Type 3 (Return User) Capital Decision:
  Stock Page Return User → Capital Decision CTA → Bottom Sheet
  → [Increase/Reduce/Exit 선택] (atz-cd-action 설정)
  → Memo Review → (옵션: 필드 수정) → Save
  → [변경 있으면 모달] → "Save as V2" → V bump + history(trigger, position)
  → Select Account (Buy flow 진입)

Type 3 (Return User) Re-underwrite:
  Stock Page Return User → Re-underwrite CTA (atz-cd-action 클리어)
  → Memo Review → 필드 수정 → Save
  → 모달 → V bump + history(Re-underwrite, held)
  → Stock Page Return User (V bump 반영, 보유 그대로)

History:
  Memo Review → "History" 링크 → Memo History.html
  → V1, V2, V3... row 리스트 (trigger + position 메타)
  → row tap → modal로 V_N snapshot 전체 보기
```

## 핵심 룰 (변하지 않음)

1. **Memo와 Position은 별개 axis**
2. **No capital action without memo review** — 모든 자본 액션이 Memo Review 경유
3. **필드 변경 시에만 V bump** — Memo Review에서 어느 필드든 바뀌면 새 버전
4. **History entry 추가는 V bump 동반시만** — 거래만으로 history 안 늘어남
5. **Capital Decision = 매수 flow** (Buy/Sell/Exit) — V1 commit 후 자동으로 Select Account 진입
6. **Re-underwrite = 분석만 업데이트** — V bump 후 Stock Page 복귀 (보유 변동 없음)

## 남은 GAP (다른 디자이너 영역)

- **Buy flow 자체** (Select Account → Order entry → Review → Filled)
- **Position 상태 LS 키** (atz-position-status) — Buy flow 완료 시 set
- **Type 2 ↔ Type 3 자동 전환** — Position 상태 기반 동적 routing

---

# 🔍 Modal & CTA Audit (J47)

## 핵심 룰

> **V bump = Modal 등장.** 변경 없으면 modal 없이 직행.

UX 톤: 모든 V bump 모달은 **"Save as V_N"** wording 통일 (이전 "Commit V_N"에서 J47에 변경).

## 모달 종류

| 모달 | 페이지 | 목적 |
|---|---|---|
| **commitSheet** | First-time Memo Flow, Return user_Memo Review (Active/Core) | V bump 확인 |
| **cdSheet** | Stock Page Return User (+ History, Multi-Quarter Alerts, Core 변종) | Buy/Sell/Exit 선택 |
| **deleteSheet** | Blank Memo | Draft 삭제 확인 |
| **snapSheet** | Memo History | V_N snapshot 보기 |

## commitSheet 등장 매트릭스 (V bump 모달)

| 상황 | 변경 | 결과 |
|---|---|---|
| First-time Memo Flow · V 없음 · 5/5 | — | ✅ **Modal "Save as V1?"** (첫 commit은 항상 confirmation) |
| First-time Memo Flow · V_N 존재 · 변경 있음 | ✅ | ✅ Modal "Save as V_(N+1)?" |
| First-time Memo Flow · V_N 존재 · 변경 없음 | ❌ | ❌ Skip → Buy flow 직행 (V 그대로) |
| Memo Review · Re-underwrite · 변경 있음 | ✅ | ✅ Modal "Save as V_(N+1)?" |
| Memo Review · Re-underwrite · 변경 없음 | ❌ | ❌ Skip → goBack to Stock Page (no-op) |
| Memo Review · Capital Decision · 변경 있음 | ✅ | ✅ Modal "Save as V_(N+1)?" |
| Memo Review · Capital Decision · 변경 없음 | ❌ | ❌ Skip → Buy flow 직행 (V 그대로) |

> **일관성**: V bump 발생 시에만 모달. 변경 없을 시 모달 skip. **이는 의도된 행동** (회장 doctrine: V bump 가 commit 의 본질).

## UX 톤 통일 (J47)

| 위치 | 라벨 |
|---|---|
| First-time Memo Flow 하단 CTA (5/5) | "→ Save" |
| First-time Memo Flow 하단 CTA (1-4) | "→ Continue" |
| First-time Memo Flow 하단 CTA (0) | "→ Start" |
| Memo Review 하단 CTA | "→ Save" |
| commitSheet 제목 | "Save as V_N?" |
| commitSheet 버튼 | "→ Save as V_N" |
| commitSheet body | "Your memo has changes. Save as V_N to lock — V_(N-1) stays on record." (V_(N+1) commit) 또는 "This saves your memo as V1..." (첫 commit) |

---

# 📊 유저 플로우 다이어그램 (사용자별 × 상황별)

## Type 1 — First-time User

```
┌──────────────────────────────────────────────────────────────┐
│  Stock Page Firsttime User                                    │
│  (메모 X, 보유 X)                                              │
└─────┬────────────────────────────────┬───────────────────────┘
      │                                 │
   ① Underwrite CTA                  ② Capital Decision CTA
      ↓                                 ↓
┌──────────────┐               ┌─────────────────────────────┐
│  Blank Memo  │               │  First-time Memo Flow        │
│  (Draft)     │               │  (체크포인트 / walkthrough)   │
└──────┬───────┘               └─────────────┬───────────────┘
       │                                      │
       │ 필드 채움                            │ filled === 0?
       │ Save & Return                        │  YES → auto-redirect
       ↓                                      │       → Edit Classification
┌──────────────────────────┐                  │       → walkthrough chain
│  Stock Page (Draft N/5)  │                  │  NO → render fields
└──────────────────────────┘                  │
                                              │ filled === 5 + tap Save
                                              ↓
                              ┌───────────────────────────────────────┐
                              │  변경 detect 분기                       │
                              ├───────────────────────────────────────┤
                              │  V 없음 (첫 commit)                    │
                              │  → Modal "Save as V1?"                │
                              │  → Save → V1 commit + history          │
                              │     (Underwrite, position: none)       │
                              │                                        │
                              │  V_N 있음 + 변경 있음 (재진입 후 수정)  │
                              │  → Modal "Save as V_(N+1)?"           │
                              │  → V bump + history                    │
                              │     (Re-underwrite + Buy, none)        │
                              │                                        │
                              │  V_N 있음 + 변경 없음 (J46)            │
                              │  → Modal SKIP                          │
                              │  → V 그대로                            │
                              └────────────────┬──────────────────────┘
                                               │
                                  atz-cd-action = 'buy' 설정
                                               ↓
                              ┌────────────────────────────────────────┐
                              │  Select Account.html (Buy flow 진입)    │
                              │  ★ 다른 디자이너 영역                  │
                              └────────────────────────────────────────┘
```

## Type 2 — Memo-only User

```
┌──────────────────────────────────────────────────────────────┐
│  Stock Page Memo Only                                         │
│  (V_N memo, 보유 X)                                            │
└─────┬─────────────────────────────┬──────────────────────────┘
      │                              │
   ① Re-underwrite CTA            ② Capital Decision CTA
      atz-cd-action 클리어          atz-cd-action = 'buy'
      ↓                              ↓
┌──────────────────────────────────────────────────────────────┐
│  Return user_Memo Review.html                                 │
│  (V_N 필드 hydrate, tap to edit)                              │
└──────────────────────┬───────────────────────────────────────┘
                       │ 필드 수정 (선택)
                       │ Save 탭 → onSave()
                       ↓
       ┌─────────────────────────────────────────────────┐
       │  intent + 변경 detect 분기                       │
       ├─────────────────────────────────────────────────┤
       │  Re-underwrite + 변경 있음                       │
       │  → Modal "Save as V_(N+1)?"                     │
       │  → V bump + history(Re-underwrite, none)        │
       │  → Stock Page Memo Only (V_(N+1) 반영)          │
       │                                                  │
       │  Re-underwrite + 변경 없음                       │
       │  → Modal SKIP                                    │
       │  → Stock Page Memo Only (변화 없음)             │
       │                                                  │
       │  Capital Decision + 변경 있음                    │
       │  → Modal "Save as V_(N+1)?"                     │
       │  → V bump + history(Re-underwrite + Buy, none)  │
       │  → Select Account                               │
       │                                                  │
       │  Capital Decision + 변경 없음 (J41)             │
       │  → Modal SKIP                                    │
       │  → Select Account (V 그대로)                     │
       └─────────────────────────────────────────────────┘
```

## Type 3 — Return User

```
┌──────────────────────────────────────────────────────────────┐
│  Stock Page Return User                                       │
│  (V_N memo, 보유 ✓)                                            │
└─────┬─────────────────────────────┬──────────────────────────┘
      │                              │
   ① Re-underwrite CTA            ② Capital Decision CTA
      atz-cd-action 클리어          ↓
      ↓                       ┌────────────────────────┐
      │                       │  cdSheet (Bottom Sheet) │
      │                       │  [Increase|Reduce|Exit] │
      │                       └────────┬────────────────┘
      │                                │ 선택
      │                                │ atz-cd-action 설정
      │                                ↓
      └──────────────┬─────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────────┐
│  Return user_Memo Review.html                                 │
│  (V_N 필드 hydrate)                                            │
└──────────────────────┬───────────────────────────────────────┘
                       │ Save 탭 → onSave()
                       ↓
       ┌─────────────────────────────────────────────────────────┐
       │  intent + 변경 detect 분기                                │
       ├─────────────────────────────────────────────────────────┤
       │  Re-underwrite + 변경 있음                                │
       │  → Modal → V bump + history(Re-underwrite, held)         │
       │  → Stock Page Return User                                 │
       │                                                           │
       │  Re-underwrite + 변경 없음                                │
       │  → Skip → Stock Page Return User                          │
       │                                                           │
       │  Increase + 변경 있음                                     │
       │  → Modal → V bump + history(Re-underwrite + Buy, held)   │
       │  → Select Account                                         │
       │                                                           │
       │  Increase + 변경 없음                                     │
       │  → Skip → Select Account (V 그대로)                       │
       │                                                           │
       │  Reduce + 변경 있음                                       │
       │  → Modal → V bump + history(Re-underwrite + Reduce, held)│
       │  → Select Account                                         │
       │                                                           │
       │  Reduce + 변경 없음                                       │
       │  → Skip → Select Account                                  │
       │                                                           │
       │  Exit + 변경 있음                                         │
       │  → Modal → V bump + history(Re-underwrite + Exit, exiting)│
       │  → Select Account                                         │
       │                                                           │
       │  Exit + 변경 없음                                         │
       │  → Skip → Select Account                                  │
       └─────────────────────────────────────────────────────────┘
```

## History 진입 (모든 Type)

```
Return user_Memo Review (Memo Review)
       │
       │ History 링크 탭 → atz-history-from 설정 (J45)
       ↓
Memo History.html
       │
       │ V_N row 탭 → snapSheet (snapshot 보기)
       │ Back 탭 → atz-history-from 사용 → Memo Review 복귀
       │
       │ Memo Review에서 다시 Back → atz-memo-stock-source → Stock Page 복귀 ✓
```

---

# 🧭 핵심 라우팅 매트릭스

| 진입점 | CTA | 라우팅 | atz-cd-action |
|---|---|---|---|
| SP Firsttime User | Underwrite | Blank Memo | (clear) |
| SP Firsttime User | Capital Decision | First-time Memo Flow | (none — page-internal logic) |
| SP Memo Only | Re-underwrite | Memo Review (Active) | **clear** (J44) |
| SP Memo Only | Capital Decision | Memo Review (Active) | **'buy'** (J42) |
| SP Memo Only (Core) | Re-underwrite | Memo Review (Core) | **clear** |
| SP Memo Only (Core) | Capital Decision | Memo Review (Core) | **'buy'** |
| SP Return User | Re-underwrite | Memo Review (Active) | **clear** |
| SP Return User | Capital Decision | cdSheet → Memo Review (Active) | **'increase'/'reduce'/'exit'** |
| SP Return User (Core) | Re-underwrite | Memo Review (Core) | **clear** |
| SP Return User (Core) | Capital Decision | cdSheet → Memo Review (Core) | action |
| SP Return User - History | 동일 | 동일 | 동일 |
| SP Multi-Quarter Alerts | 동일 | 동일 | 동일 |

> **Re-underwrite는 항상 atz-cd-action을 clear** — Memo Review가 Re-underwrite intent로 인식 (Save 시 모달 → 새 버전 → Stock Page 복귀, NOT Buy flow).
> **Capital Decision은 atz-cd-action 설정** — Memo Review가 Buy intent로 인식 (Save 시 모달/skip → Buy flow).

---

# 🔧 L-series Changelog (2026-06-07)

## L8 — Full flow audit (v13 baseline)
- 27 files inventoried, 9 Stock Page CTAs verified, all intents handled in Memo Review.

## L9 — Edge case audit (6 categories)
- State integrity (V_N empty, reaffirm guards) ✓
- Refresh / pageshow handlers ✓
- Bottom-sheet modal layering (false positive — backdrop blocks subtitle clicks)
- Form/input boundaries (min/max, empty guards) ✓
- Reaffirmation edge cases ✓
- Dead code: cd-sheet `open`/`pass` in Memo Only — confirmed unreachable

## L10 — Select Account intent-aware hero
- File: `Select Account.html`
- Reduce / Exit / Increase intents previously landed on "Buy Flow" page (bug).
- Now: `buy → Buy Flow`, `increase → Add to Position`, `reduce → Reduce Position`, `exit → Exit Position`.
- Hero title + subtitle + 4-step list rendered dynamically based on `atz-cd-action`.

## L11 — Dead code cleanup
- Removed cd-sheet HTML / CSS / JS (`openCdSheet`, `closeCdSheet`, `selectCdAction` with `'open'`/`'pass'` options) from Stock Page Memo Only Active + Core.
- These options were unreachable (no CTA invoked `openCdSheet`).

## L12 — History UX flow audit (II user perspective)
- Findings:
  - **Critical**: No entry point from Stock Pages to Memo History — page was orphaned
  - **Medium**: memo block hero V_N · Live badge — JS expected element that didn't exist in HTML
  - **Low**: Bottom-sheet had no ←→ navigation between V entries

## L13 — Memo History entry point
- Added right-aligned link at top of memo-block in 7 Stock Pages:
  - Stock Page Return User (Active + Core)
  - Stock Page Return User - History (Active + Core)
  - Stock Page Memo Only (Active + Core)
  - Stock Page Multi-Quarter Alerts
- Link visible only when `atz-memo-history` LS has ≥1 entry
- `openHistory()` sets `atz-memo-stock-source` and navigates to `Memo%20History.html`

## L14 — Label iteration
- Initial: "12 versions ›" (engineer-speak)
- Then: "Memo log ›" (cleaner but understated)
- Final (L17): "Underwriting record ›" (doctrine-aligned, matches Underwrite / Re-underwrite verb family)

## L15 — User-type audit (Type 1 / 2 / 3 detailed flow trace)
- All CTAs / hrefs / onclick handlers traced end-to-end
- All goBack() functions verified
- 0 broken links
- 1 bug found: openHistory() race with stale `atz-history-from` flag

## L16 — Fix L15 bug
- 7 Stock Pages: `openHistory()` now clears `atz-history-from` before setting `atz-memo-stock-source`
- Prevents back button from routing to Memo Review when user came directly from Stock Page

## L17 — Underwriting record (label unification)
- 7 Stock Page Memo log links → "Underwriting record"
- Memo History page hero label: "Memo History" → "Underwriting record"
- Page title (browser tab) updated
- Vocabulary now consistent: Underwrite → Re-underwrite → Underwriting record

## L18 — memoVersion dead JS cleanup
- 7 Stock Pages: removed dead `getElementById('memoVersion')` calls
- The element never existed in HTML; JS calls returned null and skipped harmlessly but were confusing

## L19 — Memo History bottom sheet ←→ navigation
- Added `‹` `›` chev buttons in sheet head
- `navSnap(dir)` function — increment/decrement entry index, re-render
- Boundary disable (Prev disabled at first entry, Next disabled at last)
- Keyboard: ArrowLeft / ArrowRight navigate, ESC closes (existing)
- `_snapIdx` state tracks current open V
- Reset to -1 on closeSnap()

## L20 — Position label semantics
- Audit verified `inferPosition()` logic — `'none'` means "never held" (Type 2 / Type 1 first commit), not "exited"
- "No position" label is semantically correct
- L9-suggested change to "Exited" was based on incorrect analysis — kept current labels

---

# 🔒 v13 LOCKED — L-series complete

**Canonical files** (last modified 2026-06-07):
- Stock Page Return User.html (Active + Core)
- Stock Page Return User - History.html (Active + Core)
- Stock Page Memo Only.html (Active + Core)
- Stock Page Multi-Quarter Alerts.html
- Return user_Memo Review.html (Active + Core)
- First-time Memo Flow.html
- Memo History.html (←→ nav added L19)
- Select Account.html (intent-aware L10)
- Edit Memo / Classification / Sizing / Probability / Idea Origin / Role / Target Weight (7 pages, K-series step indicator)

**Vocabulary lock-in:**
- Action: Underwrite (V1) / Re-underwrite (V_N+1)
- Artifact: Underwriting record (memo trail page + Stock Page entry link)
- Memo body: Investment Case (prose label)
- Position field: Held / Exiting / No position
- Trigger field: Underwrite / Re-underwrite / Re-underwrite + Buy / + Reduce / + Exit / Buy / Reduce / Exit

**SessionStorage keys** (cleaned on appropriate transitions):
- `atz-cd-action`: 'buy' | 'increase' | 'reduce' | 'exit' | null (Re-underwrite)
- `atz-cd-mode`: walkthrough mode flag
- `atz-fresh-walkthrough`: step indicator gate (K3)
- `atz-cd-auto-redirected`: auto-redirect guard
- `atz-memo-source`: Edit page return target
- `atz-memo-stock-source`: Memo Review / History return target
- `atz-history-from`: Memo History return target (Memo Review entry only)

**LocalStorage keys** (persistent memo state):
- `atz-memo-version`, `atz-memo-history` (canonical)
- `atz-memo-classification`, `atz-memo-sizing`, `atz-memo-probability`, `atz-memo-horizon`, `atz-memo-idea-origin` (Active)
- `atz-memo-role`, `atz-memo-target-weight` (Core)
- `atz-memo-memo`, `atz-memo-stance`, `atz-memo-decision`, `atz-memo-draft-progress`, `atz-memo-notes`, `atz-memo-hurdle-rate`

---

# 🔧 L-series 후반 Changelog (L24-L37, 2026-06-07)

## L24 — V1 commit timing audit
검증 결과: doctrine 일치. V1은 "Save as V1" 클릭 시 `commitMemo()` 호출 시점에 생성 (draft / 부분 채움 / Select Account 도달 시점 X).

## L25 — Memo Review "History" → "Underwriting record"
L17 통일 작업에서 누락된 Memo Review의 "History ›" 버튼 캐치:
- `Return user_Memo Review.html` / `(Core).html` 의 `goToHistory()` button text 변경

## L26 — Firsttime User memoFilled에 Underwriting record link 추가
L13에서 누락된 2개 페이지 (Active + Core) memoFilled section에 진입 link 추가.

## L27 — Notes 섹션 위 divider 전폭 적용
새 클래스 `.memo-block-divider-full` (margin: 4px -16px) 도입. 9개 Stock Page Notes 위 divider 전폭화.

## L28 — Notes 아래 divider 전폭 (Firsttime blank)
Firsttime User Active + Core blank state의 reverse 패턴 (Notes 위, divider 아래)도 전폭 적용.

## L29 — Investment Case 위 divider 제거
memo block 내부 fields ↔ IC divider 제거. memo unified artifact doctrine 강화. `.memo-prose-label { margin-top }` 추가로 typography break.

## L30 — Spacing 일관성 audit
9개 Stock Page spacing token 검증. 대부분 일관 (`.col` 48px gap, `.section` 14px gap, `memo-block` 16px padding). Firsttime User dual header (-34px hack) 유지.

## L31 — Blank Memo hero 28px + 행간 8/8 통일
m6-ticker-hero 34→28px. 행간 12/4/6 → 8/8 통일.

## L32 → L33 — Typography audit + 통일
모든 hero 28px / Edit 22px / section 15px 시스템 확정.

## L34 — Hero 28 → 24px (사용자 피드백)
"한단계 더 작게" 요청 반영. m6-ticker-hero / m6-action-hero / hero-ticker 모두 28→24px.

## L35 — Investment Case prose unification (max-height/margin/case)
- max-height: 120 → 100px (좁은 쪽으로 통일)
- margin-top: 4px (Firsttime만) → 0 (전체)
- line-height: 1.7 → 1.65
- toggle: "Read full memo" → "Read Full Memo" (Title Case)

## L36 — Investment Case canonical prose
4개 Active Stock Page demo seed를 Example Memo Thesis 형식으로 통일:
- "Thesis. Aritzia is a US growth story in its middle innings..."
- Structural decomposition (Revenue / Margin / Capital returns / Multiple)
- Load-bearing assumption

Core variant는 VFV index/treasury thesis 유지.

## L37 — Reference 섹션 audit (Blank Memo)
**Pending decision** (Claude Code에서 처리):
- Blank Memo의 "How Underwriting Works" 카드 → Memo Intro (STUB)
- 권장: A. 카드 제거 (broken link 방지)
- 대안: B. "Coming soon" 라벨 / C. 그대로

