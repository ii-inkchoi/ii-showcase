# V8 — 표시 텍스트·표면 변경 통보 (2026-08-02)

> 대상: Dave (카피 캐논) + 컴플라이언스 확인 항목 2건.
> 오늘 인경님 승인으로 적용 완료된 것들의 사후 통보 + 미결 질문. 코드는 전부 반영된 상태.

---

## 1. 적용 완료 — Dave 확인 요청 (표시 텍스트 변경)

### 1.1 Pricing NO.01 항목명 통일 (6건)
같은 세 항목을 홈과 Pricing 이 다른 이름으로 부르고 있었음. 홈 쪽(짧은 형)으로 통일.

| 전 (Pricing) | 후 |
|---|---|
| Managed Portfolios | **Managed** |
| Self-Directed Investing | **Self-Directed** |
| Fiscal.ai Research | **Fiscal.ai Max** ← 파트너사 실제 제품명. "Research" 는 존재하지 않는 이름 |
| VIEW MANAGED | **MANAGED** |
| VIEW SELF-DIRECTED | **SELF-DIRECTED** |
| VISIT FISCAL.AI | (유지) — 외부 fiscal.ai 로 나가므로 홈의 RESEARCH(내부 앵커)와 달라야 정상 |

### 1.2 마감 CTA 라벨 통일 (5건)
GetTheApp 으로 가는 링크 28개 중 23개가 `OPEN AN ACCOUNT`, 5개(Pricing·Manifesto·Newsroom·PR·Changelog 마감)가 `ENTER THE SYSTEM` 이었음. 인경님 결정으로 **전부 `OPEN AN ACCOUNT`** 통일.
- **참고:** 라이브 사이트는 같은 자리에서 `Enter the System` 을 쓰고 있어 라이브와 갈라짐.
- **참고 2:** 목적지(GetTheApp)는 계좌 개설 페이지가 아니라 앱 다운로드 페이지 ("Built for iOS. Access begins with Calibration."). `OPEN AN ACCOUNT` 라벨이 목적지와 어긋난다는 지적은 기록해 둠.

### 1.3 홈 NO.01 모바일 축약문(.msum) 삭제 (3건)
모바일 전용 한 줄 요약이 데스크탑 문장과 별도로 존재 → 같은 문장의 승인 대상이 두 벌이 되는 문제. 삭제하고 모바일도 데스크탑 문단을 그대로 노출.
- 삭제된 문장: "Disciplined, low-cost portfolios." / "Every decision on the record before the outcome." / "Research, included."
- **모바일 화면에 새로 노출되는 문장** (기존 데스크탑 승인 문구 그대로): Managed·Self-Directed·Fiscal.ai Max 의 풀 문단. 특히 Fiscal.ai 의 "Research supplies evidence. Judgment remains yours." 가 이전 모바일에는 없었음.

### 1.4 푸터 법무 전면 교체 (9개 페이지)
프로토타입에 법무 문구가 3벌 혼재 → **라이브(intelligentinvesting.ai) 승인본 8문단을 글자 그대로** 이식. 인경님 지시 ("wording 그대로, 컴플라이언스 확답본").
- 삭제됨 (라이브에 없음): "Past returns are no guarantee of future performance." / Reset Cookie Preferences
- 추가됨 (라이브에만 있음): AMF 주 규제기관 문장, "order execution only", 주/준주 등록 문단, IISI/IIWMI 약칭, Disclosures 링크

### 1.5 SD 벤치마크 tri 라벨 케이싱 (07-31 기존 플래그)
ALL CAPS → 첫 글자 대문자. 마크업 수정이라 데스크탑에도 반영된 상태.

---

## 2. 모바일에서 접근 불가해진 카피 (07-31~08-01 기존 플래그, 재확인 요청)

폴드 제거+위임으로 모바일에서 안 보이게 된 문단들. 비필수인지 Dave 확인 필요:
- 홈 NO.02 문단 2–3, NO.03 문단 2–3 + 페이오프
- SD NO.01/04/05 문단 2, 페이오프, 크로스셀 프로즈
- SD 히로 아이브로우 둘째 줄 "PART OF THE INTELLIGENT INVESTING SYSTEM" (모바일 제거)

---

## 3. 컴플라이언스 확인 항목 (미적용, 답 대기)

1. **Press Release 법무 블록 위치** — IMPORTANT INFORMATION + FORWARD-LOOKING STATEMENTS (1.68 화면) 이 MORE UPDATES 와 마감 CTA **앞**에 있음. 뒤로 내리면 독자 흐름이 좋아지는데, 법무 문구의 배치(본문 인접 등)가 요건인지 확인 필요. 문구는 무변경, 순서만.
2. **Manifesto·PR·Changelog 본문 하단 법무 블록** — 푸터는 라이브 승인본으로 교체됐으나, 이 페이지들 본문 안의 IMPORTANT INFORMATION 블록([Legal Entity Name] 포함)은 라이브에 대응물이 없는 프로토타입 문구. 확정 문구 필요.

---

## 4. 표면(비카피) 변경 — 참고

- 마감 CTA 색: 홈·SD·Managed 검정 → **빨강** (8개 페이지 통일, 빨강 = 마감 신호 유지)
- PR·Changelog 마지막 섹션: 전면 빨강 밴드 → 밝은 바탕 + 빨간 버튼 (사이트 표준)
- GetTheApp: App Store 배지·사인인 링크 → 라이브 Branch 딥링크(go.moka.ai), 아이브로우 텍스트 → 회사 워드마크 SVG
- 소셜 4계정 연결 (IG·TikTok·X·YouTube), 대비(WCAG) 수정 9건, 모노 티어 정리 7건
