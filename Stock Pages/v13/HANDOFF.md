# HANDOFF — II Stock Page v13 (L-series FINAL)

**Last updated**: 2026-06-08 (L0–L37)
**Working directory**: `C:\Users\p0107\OneDrive\바탕 화면\II Work\AI ProJects V2\Prototype\Stock Pages\Stock - Post MVP\v13`
**Status**: 🔒 **LOCKED** — Doctrine §73-§93, _SCENARIOS.md changelog 동기화 완료
**User**: inkyung.choi@mogo.ca (Chairman doctrine — II identity)

---

## Goal

v13 = v12에서 복사한 L-series iteration. **37개 task 완료** (L0-L37). Doctrine 전체 lock-in.

Claude Code에서 이어서 작업할 수 있도록 HANDOFF + Doctrine MD + _SCENARIOS 모두 동기화.

---

## L-series 전체 완료 항목 (L0-L37)

### Early (L0-L7): 기반
- L0 v13 폴더 생성
- L1-L5 Memo Review intent-aware copy + II-tone + reaffirmation
- L6 user audit / L7 doctrine sync

### Mid (L8-L17): UX 확장
- L8 full flow audit / L9 edge case audit
- L10 Select Account intent-aware hero
- L11 dead code 정리 (cd-sheet)
- L12 History UX audit
- L13 Stock Page → Memo History 진입점 (7 pages)
- L14 → L17 "Memo log" → "Underwriting record" 라벨 통일 (8 surfaces)
- L15 user-type audit (Type 1/2/3) + L16 race condition fix
- L18 memoVersion dead JS 정리
- L19 Memo History ←→ navigation
- L20 Position 라벨 audit (변경 불필요)

### Lock-in (L21-L22)
- L21 _SCENARIOS.md + Doctrine §80-§83
- L22 HANDOFF.md 업데이트

### Index + sidebar (L23)
- L23 index.html sidebar doctrine 통일

### V1 timing + History label completion (L24-L26)
- L24 V1 commit timing audit (코드 doctrine 일치 확인)
- L25 Memo Review "History" → "Underwriting record" (L17 누락분)
- L26 Firsttime User memoFilled에 진입 link 추가 (L13 누락분)

### Spacing + divider 정비 (L27-L30)
- L27 Notes 위 divider 전폭 (memo-block-divider-full)
- L28 Notes 아래 divider 전폭 (Firsttime blank reverse 패턴)
- L29 Investment Case 위 divider 제거 + margin-top 16px
- L30 페이지 spacing 일관성 audit (Firsttime dual header 유지)

### Typography 통일 (L31-L34)
- L31 Blank Memo hero 34→28px + 행간 8/8
- L32-L33 typography audit + 통일 (28/22/15/13/11)
- L34 hero 28→24px ("한단계 더 작게" 사용자 피드백)

### Investment Case content + format (L35-L36)
- L35 IC max-height 100px + margin-top 0 + line-height 1.65 + "Read Full Memo" Title Case
- L36 IC prose canonical (Example Memo Thesis 형식) — 4개 Active Stock Page

### Reference audit (L37) — PENDING
- L37 Blank Memo의 "How Underwriting Works" → Memo Intro (STUB) 처리 결정 보류
- 권장: 카드 제거

---

## Final Locked System

### Vocabulary

| Action | 첫 V1 | V_N+1 | trail 보기 | prose 라벨 | 토글 |
|---|---|---|---|---|---|
| Term | **Underwrite** | **Re-underwrite** | **Underwriting record** | **Investment Case** | **Read Full Memo** |

### Typography (L34 final)

| 위계 | 크기 |
|---|---|
| Page hero | **24px** |
| Sub-page hero (Edit) | 22px |
| Sheet title | 16px |
| Section title | 15px |
| Subtitle | 13-14px |
| Body | 13px |
| Meta | 11-12px |
| Compliance | 9px |

### Spacing (L27-L30 final)

| 항목 | 값 |
|---|---|
| `.col` padding / gap | 48px 20px 120px / 48px |
| `.section` gap | 14px |
| `.section-header` padding | 0 0 14px |
| `.memo-block` padding / gap | 16px / 8px |
| `.uw-rows` gap (rows) | 10px |
| `.memo-prose-label` margin-top | 2px (→ 10px total) |
| Notes divider | `memo-block-divider-full` (margin: 4px -16px) |
| Investment Case 위 divider | **제거됨** (L29) |

### Investment Case prose (L36)

**Active Stock Pages canonical:**
> "Thesis. Aritzia is a US growth story in its middle innings. The US flywheel (flagship-led brand-building, app-driven engagement, and disciplined new-box openings that pay back in under a year) can roughly double the US fleet..."

**Core Stock Pages:** VFV index/treasury thesis 별도 유지.

---

## Pending Issues (Claude Code 작업 권장)

### 1. L37: "How Underwriting Works" 카드 broken link

**위치:** Blank Memo.html `<section aria-label="Reference">`
**문제:** Memo Intro.html이 stub → 클릭 시 "Built by another designer" placeholder
**옵션:**
- A. 카드 제거 (가장 깔끔)
- B. "Coming soon" 라벨 추가
- C. 그대로 (placeholder UX 받아들임)

### 2. Memo Intro 페이지 자체 구현

다른 디자이너 영역. 다음 구조 가능:
- Principles section (chairman doctrine 요약)
- Workflow diagram (V1 commit → Re-underwrite → Underwriting record)
- 5 fields 의미 (Classification / Sizing / Confidence / Idea Origin / Investment Case)

### 3. V50 historical version prose seeds 정합성

Stock Page Return User - History.html에 proseV1, proseV2... 시리즈 존재. L36에서 V50 current는 canonical thesis로 업데이트했지만 V1 historical은 short prose 유지. 의도된 historical evolution인지 검토 권장.

### 4. Reference 섹션 위계 재고

doctrine §85 (L27) — Notes를 secondary로 시각적 분리. doctrine §87 (L29) — IC와 fields는 unified. 그러면 Reference 섹션 자체의 doctrine 위계는?
- 현재: memo-block 외부, 별도 section
- 옵션: aux/footer 영역으로 더 subtle하게 처리

### 5. Edit Probability / Confidence 명명 통일

Edit pages에서 "Edit Probability" → "Edit Confidence" 라벨 적용 (J38) 완료. localStorage key는 여전히 `atz-memo-probability`. JS 변수 이름도 그대로. 추후 rename 작업 가능.

---

## File Inventory (v13 final)

**Stock Pages (9):**
- Firsttime User.html / (Core).html — L26 진입 link 추가
- Memo Only.html / (Core).html — L13/L17 진입 link, L27 Notes divider, L29 IC divider 제거, L35 IC fade, L36 canonical prose
- Return User.html / (Core).html — 동일 적용
- Return User - History.html / (Core).html — 동일 적용 (V50 demo)
- Multi-Quarter Alerts.html — 동일 적용

**Memo flow (6):**
- First-time Memo Flow.html — L33/L34 hero 24px
- Firstime user_Memo Review.html — STUB
- Memo Intro.html — STUB (L37 broken link target)
- Return user_Memo Review.html / (Core).html — L25 라벨 통일
- Memo History.html — L17 "Underwriting record" hero, L19 ←→ nav, L34 hero 24px

**Edit pages (7):** L18 dead JS 정리, K-series step indicator
**Other (5):** Blank Memo (L34 hero 24px), Example Memo, Select Account (L10), User Flow, index.html (L23 sidebar)

**Docs (4):**
- _SCENARIOS.md (1127 lines, L8-L37 changelog)
- _FLOW_REFERENCE.md
- v11 Audit - Execution Items.md
- HANDOFF.md (this file)

---

## Doctrine § References (v13 LOCKED)

**Original (pre-L):** §44 audit-trail, §55 SDR, §56 memo/position separation

**L-series (§73-§93):**
- §73-§79 L1-L7 (intent copy, bottom sheet, reaffirmation)
- §80 L10 (Select Account intent-aware)
- §81 L13+L17 (Underwriting record)
- §82 L19 (←→ navigation)
- §83 L16 (sessionStorage cleanup)
- §84 L26 (Firsttime memoFilled link)
- §85 L27 (Notes divider 전폭)
- §86 L28 (Notes 아래 divider reverse)
- §87 L29 (Investment Case unified artifact)
- §88 L30 (Spacing audit)
- §89 L31+L34 (Hero size 24px final)
- §90 L35 (IC fade/case/spacing)
- §91 L25 (Memo Review label completion)
- §92 L36 (IC canonical prose)
- §93 v13 LOCKED summary

**Doctrine MD:** `C:\Users\p0107\OneDrive\바탕 화면\II Work\Doctrine\Stock Page + Memo - v11 Update (June 2026).md` (685 lines)

---

## Critical Constraints (for Claude Code)

1. **명시적 요구만 변경**: 사용자 명령 외 디자인 변경 금지
2. **OneDrive sync issue**: 큰 파일 Write 시 truncation. **bash heredoc 사용** (`cat > file << 'EOF'`)
3. **localStorage keys** (canonical):
   - `atz-memo-version`, `atz-memo-history`, `atz-memo`
   - `atz-memo-classification`, `atz-memo-sizing`, `atz-memo-probability`, `atz-memo-horizon`, `atz-memo-idea-origin`
   - `atz-memo-role`, `atz-memo-target-weight` (Core)
   - `atz-memo-stance`, `atz-memo-decision`, `atz-memo-draft-progress`, `atz-memo-notes`, `atz-memo-hurdle-rate`
4. **sessionStorage keys** (transient):
   - `atz-cd-action`, `atz-cd-mode`, `atz-fresh-walkthrough`, `atz-cd-auto-redirected`
   - `atz-memo-source`, `atz-memo-stock-source`, `atz-history-from`
5. **Vocabulary** (do not deviate):
   - Underwrite → Re-underwrite → Underwriting record → Investment Case → Read Full Memo
   - Position: Held / Exiting / No position
   - Trigger: Underwrite / Re-underwrite / Re-underwrite + Buy/Reduce/Exit / Buy / Reduce / Exit

---

## v13 → v14 시작 가이드

새 iteration 시작 시:
1. v13 → v14 폴더 복사
2. Pending Issues (위 1-5) 우선순위 결정
3. Reference 섹션 위계 재고
4. Memo Intro 페이지 컨텐츠 구현 (다른 디자이너 영역인 경우 stub 라벨 명확화)

