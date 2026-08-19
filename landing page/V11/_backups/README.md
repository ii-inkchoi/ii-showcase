# 백업 — 2026-08-18 세션

작업 순서대로. 각 파일은 그 단계 **직전** 상태다.

## 홈 (`index.html`)

| 파일 | 이 시점으로 되돌리면 사라지는 것 |
|---|---|
| `index.html.bak-before-no05` | NO.05 QUESTION 비트(24/24/104) · 푸터 상단 104 |
| `index.html.bak-before-typefloors` | 데스크탑 타입 플로어 1차 (body 17 · h34 28 · mono15 15 · mono13 13 · 디스플레이 48) |
| `index.html.bak-before-batch2` | 타입 플로어 2차 (read27 22 · lead24 22 · small17 15) |

## SD (`self-directed.html`)

| 파일 | 이 시점으로 되돌리면 사라지는 것 |
|---|---|
| `sd.bak-before-herobits` | 히로 2비트 분할 · 아이브로 재배치 · 비트2 |
| `sd.bak-before-sheets` | 목업 3개 → 바텀시트 · 컨트롤 3개 |
| `sd.bak-before-tail` | NO.07 인덴트 제거 · NO.08 · CLOSE · 도해 수복 |

**주의**: SD 백업에는 그 시점까지의 앞선 수정이 **모두 포함**돼 있다 (기계적 이식 6건,
NO.01~NO.06 비트 등). 즉 `sd.bak-before-herobits` 로 되돌려도 선 c-800·`.mlink`·리빌·타입
플로어·내브·푸터는 남는다.

**원본**: `../V10/self-directed.html` 은 이 세션에서 한 번도 수정하지 않았다. 완전 초기화가
필요하면 거기서 다시 복사할 것.

전체 맥락은 `../SESSION-2026-08-18-SD.md`.

## pre-shared-20260819/
2026-08-19, `_shared/v11.css` + `v11-sub.js` 로 공유 레이어를 뽑아내기 **직전**의 홈 · Self-Directed · Managed.
`_shared/build-from-backup.py` 가 이 세 파일에서 현재 상태를 결정적으로 재생성한다 (히로 예외 분리 → 홈 `p-home` 스코프 → CSS 링크 → JS 링크 → 중복 삭제). 공유 레이어 작업을 다시 돌려야 하면 여기서 시작할 것.
