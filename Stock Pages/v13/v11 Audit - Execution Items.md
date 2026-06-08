# v11 · Stock Page · Audit · 실행항목

**Date:** 2026-06-05
**Scope:** Post-MVP Stock Page only — Active + Core·Treasury variants per user state
**Rule:** Stock Page만 작업. Memo Flow / Capital Decision / Edit field pages는 다른 designer scope.

---

## 🔄 새 방향 (회의 + 이메일 directive 종합)

### Capital Role Routing — system 자동
- 종목별 system이 자동 분류 (whitelist 기반)
- User가 Active/Core 선택 안 함 (toggle 없음)
- V1 구현: `marketApprovedSymbols` + `treasuryApprovedSymbols` 두 list. 나머지 = Active default.
- 2-tier 시각 (Active vs Core·Treasury) 유지하되 시스템이 자동 routing

### Stock Page에 미치는 영향
1. **Active/Core 토글 완전 제거** — v10 잔재 정리
2. **종목별 2개 variant** — Active (ATZ) / Core·Treasury (VFV)
3. **Memo card click → Blank Memo (editable draft)** — destination은 다른 designer
4. **Investment Case prominent display** — quality 동기부여
5. **자동 routing** — 종목이 list에 어디 속하는지로 결정

### 다른 directive (회장 16-56 transcript)
- "Paste" 단어 X — "Type or paste OK"
- Probability section "Exceptional Compounding hurdle 20%" 중복 제거
- 1/3/5 year 작은 radio
- Memo Reveal magical artifact (memo flow scope)
- "Investment Case good portion on stock page" (Stock Page scope)

---

## 📂 v11 폴더 구조

### Stock Pages (6개 — 작업 대상)
```
Stock Page Firsttime User.html              (Active · ATZ · no memo)
Stock Page Memo Only.html                   (Active · V1 · no pos)
Stock Page Memo Only (Core).html            (Core·Treasury · VFV · V1 · no pos)
Stock Page Return User.html                 (Active · V1 · held)
Stock Page Return User - History.html       (Active · V50 · held)
Stock Page Multi-Quarter Alerts.html        (Active · earnings alert)
```

### Stock Pages — 신규 (Core·Treasury 확장)
```
Stock Page Firsttime User (Core).html       (Core·Treasury · VFV · no memo)
Stock Page Return User (Core).html          (Core·Treasury · VFV · held)
Stock Page Return User - History (Core).html (Core·Treasury · VFV · V50)
```
(Multi-Quarter Alerts Core 변형 — ETF는 분기 earnings 없음, skip)

### Stub placeholders (다른 designer scope)
```
_placeholder.html (master)
Blank Memo.html
First-time Memo Flow.html
Firstime user_Memo Review.html
Memo Intro.html
Return user_Memo Review.html
Return user_Memo Review (Core).html
User Flow.html
```

### Meta
```
index.html (수정 필요)
v11 Audit - Execution Items.md (이 파일)
```

---

## 🔒 v10에서 끌어온 lock (참고)

이 파일들은 v10에서 작업 완료된 reference:
- v10/Stock Page Firsttime User.html
- v10/Blank Memo.html
- v10/Example Memo.html
- v10/Stock Page Memo Only.html
- v10/Stock Page Memo Only (Core).html
- v10/Return user_Memo Review.html
- v10/Return user_Memo Review (Core).html

→ v11 작업 시 reference로 활용. 직접 수정 X.

---

## 📋 실행항목 (J 시리즈)

### J1 — index.html 정리
- v11에 없는 page link 제거 / disabled
- Stock Page section만 active
- VFV/CASH 종목별 Core·Treasury demo 추가 entry

### J2 — Stock Page Firsttime User.html (Active 정리)
- Active/Core 토글 완전 제거
- Memo card / field rows 정리
- Memo card click destination 확인 (다른 designer 작업할 Blank Memo)
- Investment Case prominent placeholder

### J3 — Stock Page Firsttime User (Core).html 신규
- Core·Treasury variant 생성 (VFV 종목 기준)
- Header: VFV info
- Memo card: Core·Treasury light fields (Decision: "Core / Treasury Allocation", etc.)

### J4 — Stock Page Memo Only.html (Active 검증)
- v10에서 이미 lock 완료. v11 복사본도 같은 상태.
- 추가 토글 잔재 점검

### J5 — Stock Page Memo Only (Core).html (Core·Treasury 검증)
- v10에서 lock 완료. 검증만.

### J6 — Stock Page Return User.html (Active 검증/정리)
- Active/Core 토글 제거
- Position section 검증

### J7 — Stock Page Return User (Core).html 신규
- Core·Treasury V1 + held position variant
- Position content for ETF

### J8 — Stock Page Return User - History.html (V50 Active 정리)
- 토글 잔재 제거
- History panel 검증

### J9 — Stock Page Return User - History (Core).html 신규
- V50 Core·Treasury variant
- (Core·Treasury memo도 multi-version 가능)

### J10 — Stock Page Multi-Quarter Alerts.html (Active 정리)
- 토글 잔재 제거
- Earnings alert 동작 확인

### J11 — Investment Case prominent on Stock Pages
- 현재 max-height 120px + Read more → 더 prominent하게
- (얼마나는 design judgment 후 결정)

### J12 — 종목별 demo content 설정
- Active = ATZ (그대로)
- Core·Treasury = VFV (S&P 500 ETF) — Decision/Role/Target 등 content

### J13 — Stub placeholder 점검
- 7개 stub 파일이 외부 link에서 작동하는지 확인
- placeholder copy 수정 필요 시

---

## 🤔 미확정 / 회장님 confirm 필요

### HOLD-A · Investment Case "good portion" 양
- 첫 paragraph 전체? 첫 section 전체? Read more 위치?

### HOLD-B · Core·Treasury Multi-Quarter Alerts
- ETF도 quarterly 분배 / 재구성 이벤트 있음 — 그것도 alert?
- 일단 skip 권장

### HOLD-C · Capital Decision routing
- Capital Decision 클릭 시 어디로? (다른 designer scope이지만 Stock Page에서 trigger)
- 현재 v10에서 First-time Memo Flow로 가는데, 새 directive에선 Draft Review로?

---

## 📅 변경 이력

| 날짜 | 항목 | 상태 |
|---|---|---|
| 2026-06-05 | v11 폴더 생성 + 7 파일 복사 + 7 stub placeholder | done |
| 2026-06-05 | Audit MD 작성 — 13 실행항목 + 3 HOLD 등록 | pending |
