# SEAM_SPEC — Stock Page ↔ Capital Decision 핸드오프 계약

**For:** Capital Decision *이후* 페이지를 만드는 디자이너
**From:** Inkyung (Stock Page scope)
**Last updated:** 2026-06-08 · v13

---

## 1. 한 줄 요약

이 폴더에서 **"Capital Decision" CTA 클릭 = 두 사람의 경계선(seam)** 이다.
- **Zone A (Inkyung):** Stock Page + Memo 작성(draft) — CTA 누르기 *전까지* 전부.
- **Zone B (당신):** CTA 누른 *다음* — review → walkthrough → commit modal → buy/sell.

index.html 사이드바가 이 두 zone으로 나뉘어 있음. **Zone B 파일(First-time Memo Flow, Memo Review, Select Account)은 내가 플로우 보려고 만든 placeholder다 — 당신이 새로 만들 영역. 참고용으로만 봐라.**

---

## 2. Seam — 어느 Stock Page가 어디로 진입하나

| 출발 (Stock Page · Zone A) | 상태 | CTA | 도착 (Zone B · 당신) |
|---|---|---|---|
| Firsttime User | memo 없음 | "Underwrite" | `First-time Memo Flow.html?intent=buy` |
| Memo Only | V1, 포지션 없음 | "Capital Decision" | `Return user_Memo Review.html` |
| Return User | V1 + 보유 | "Capital Decision" → bottom sheet (Increase/Reduce/Exit) | `Return user_Memo Review.html` → `Select Account.html` |
| Multi-Quarter / History (V50) | V1+ 보유 | 동일 | `Return user_Memo Review.html` |
| **Core 변형 (VFV)** | 위와 동일 | 동일 | `Return user_Memo Review (Core).html` |

> Firsttime은 `?intent=buy`로 진입, 나머지는 sessionStorage로 상태 전달 (아래 §3).

---

## 3. 상태 계약 (당신 페이지가 읽고/써야 할 것)

### Stock Page → Zone B 진입 시 set 되어 있는 값 (당신이 READ)
**sessionStorage (transient):**
- `atz-cd-action` — Capital Decision 액션 (set by Stock Page CTA)
- `atz-cd-mode` — review mode
- `atz-memo-stock-source` — 돌아갈 Stock Page URL (back/cancel 시 사용)
- `atz-ft-intent` — Firsttime의 `intent=buy` 등

**localStorage (draft, 진입 시점 값):**
- `atz-memo-classification` / `atz-memo-sizing` / `atz-memo-probability` / `atz-memo-horizon` / `atz-memo-idea-origin` / `atz-memo-memo` — 5개 memo 필드 (Active)
- `atz-memo-role` / `atz-memo-target-weight` — Core 2필드
- `atz-memo-draft-progress` — "0"–"5" 채워진 필드 수
- `atz-memo-stance` — "active" / "core"

### Commit 시 당신이 WRITE 해야 immutable로 전환됨
- `atz-memo-version` = `"V1"` (또는 V_N+1) ← **이걸 set 해야 Stock Page가 "committed" 상태로 렌더**
- `atz-memo-history` = JSON 배열 (스냅샷 push)
- `atz-memo-decision` = `"Active Allocation"` / `"Core / Treasury Allocation"`
- 포지션 변경 시 `atz-position-status` = `"held"` 등

> 핵심 규칙 (chairman): **memo는 Capital Decision 전까지 draft (자유 편집·삭제 가능). Capital Decision commit 순간 immutable (version 부여, 수정 불가, 새 version으로만 supersede).**

전체 LS/SS 스키마: `_FLOW_REFERENCE.md` §5 참조.

---

## 4. Vocabulary (절대 바꾸지 말 것 — Zone A·B 공통)

| 첫 commit | 재commit | trail 보기 | prose 라벨 | 토글 |
|---|---|---|---|---|
| **Underwrite** | **Re-underwrite** | **Underwriting record** | **Investment Case** | **Read Full Memo** |

- Position: **Held / Exiting / No position**
- Trigger: Underwrite / Re-underwrite / Re-underwrite + Buy·Reduce·Exit / Buy / Reduce / Exit
- AI/시스템 insight 마크 = `//` Mogo wedge SVG (절대 "AI"라는 단어 X)
- "5 screens then boom, screen six = the money shot" (chairman) — review→walkthrough(누락 필드만)→commit modal 흐름.

---

## 5. 파일 맵 (이 폴더)

**Zone A — Inkyung 완성본 (당신이 이어붙일 대상, 건드리지 말 것):**
- `Stock Page *.html` (9개: Active+Core × Firsttime/Memo Only/Return User/History/Multi-Quarter)
- `Blank Memo.html` — draft 편집 entry
- `Edit *.html` (7개: 단일 필드 편집)
- `Memo History.html` — Underwriting record (버전 trail)
- `Example Memo.html` — ATZ V1 레퍼런스

**Zone B — 당신 영역 (현재 내 placeholder, 새로 제작):**
- `First-time Memo Flow.html` — 빈 draft의 Capital Decision (5+1 screens)
- `Return user_Memo Review.html` / `(Core).html` — 보유 포지션 re-underwrite / review gate
- `Select Account.html` — 계좌 선택 (capital action)

**문서:**
- `index.html` — 전체 뷰어 (Zone A/B 사이드바)
- `_FLOW_REFERENCE.md` — 아키텍처·플로우·LS 스키마 (먼저 읽어라)
- `_SCENARIOS.md` — 상태별 시나리오
- `HANDOFF.md` — v13 변경 이력
- `SEAM_SPEC.md` — 이 문서

---

## 6. 시작 순서 (당신이 할 일)

1. `index.html` 열어서 Zone A 페이지들 클릭하며 플로우 체험.
2. `_FLOW_REFERENCE.md` §3(플로우) + §5(LS 스키마) 정독.
3. 각 Stock Page에서 "Capital Decision"/"Underwrite" CTA 누르면 §2 표의 Zone B 파일로 간다 — 그 진입 시점의 sessionStorage/localStorage가 §3의 계약값.
4. 그 지점부터 review → walkthrough → commit 페이지를 새로 설계. commit 시 §3의 WRITE 키만 정확히 set하면 Stock Page가 자동으로 committed 상태로 렌더됨.
5. vocabulary(§4)는 고정.

---

## 7. 알려진 미해결 (참고)

- **Core Blank Memo 부재** — Firsttime User (Core)의 Underwrite가 현재 Active Blank Memo로 감 (gap, `_FLOW_REFERENCE.md` §3 Flow D).
- `atz-memo-probability` 키는 라벨이 "Confidence"로 바뀐 뒤에도 그대로 (rename 미적용).
