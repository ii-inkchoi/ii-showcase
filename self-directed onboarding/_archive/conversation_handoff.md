# Conversation Handoff — Intelligent Investing Self-Directed Calibration

> **목적**: 다른 컴퓨터의 Claude에게 이 작업의 컨텍스트를 전달하는 핸드오프 문서. 새 Claude 세션을 시작할 때 이 파일과 같은 폴더의 다른 파일들을 같이 첨부하면 작업이 끊김 없이 이어진다.

---

## 1. 프로젝트 개요

**회사**: Intelligent Investing (캐나다 기반 투자 앱, MVP 단계)

**핵심 컨셉**:
- Wealthsimple Invest의 통합 대시보드와 유사한 구조: **Core (Managed)** + **Active (Self-Directed)**
- 가입은 **managed onboarding** (Section 1~9, "Calibration"부터 시작)으로만 시작
- Self-directed 활성화는 가입 후 별도 단계
- Brand identity: cold/clinical, Palantir/Alex Karp 같은 serious operator tone, anti-retail, anti-dopamine, "Invisible Lifestyle"

**제품 우선순위**:
- Managed (특히 Core S&P 500 기반 3개 포트폴리오)가 회사의 메인 상품
- Self-directed는 *자격을 얻는* 옵션. "Active investing isn't a starting point. It's something you earn."
- Long-term compounding이 회사 thesis

---

## 2. 핵심 발견 (이 대화에서 정리된 것)

### 2.1 Calibration의 본질

회사 철학 11화면(self-directed entry)은 **가입 절차가 아니라 자기 규율 계약서를 쓰는 의식**이다. 사용자가 매수 기준·매도 규칙·실수 대응을 직접 작성하면, 시스템이 그 답을 timestamped + immutable로 저장하고, 향후 매수/매도/변동성 시점에 사용자에게 다시 들이민다.

핵심 메커니즘: **"writing rules used against you later."**

### 2.2 두 게이트 구조

- **Calibration Gate (1회성)**: 사용자가 *처음* self-directed를 선택하는 순간 발동
- **Decision Gate (반복)**: 매수/매도/변동성 시점마다 저장된 답 재생, Yes/No 강제

### 2.3 Calibration Gate의 정확한 위치

**최종 권고 위치**: 메인 대시보드 → Active 섹션 "Open Account" 클릭 → Add Account 화면 → **"Self-Directed" 첫 선택 시점**

권고 *제외* 위치들과 그 이유는 strategy 문서 Section 1.2와 1.4에 8가지 충돌로 상세히 적힘.

### 2.4 Self-directed 흐름에 Onfido 없음

신원 확인은 가입(managed onboarding)의 Section 7에서 이미 완료. self-directed 계정 추가는 *이미 검증된 사용자에게 새 계정 종류를 붙이는 것*이라 재검증 불필요.

### 2.5 디자인 안에 이미 있는 단서

unified dashboard Figma에 다음 라벨이 이미 존재 (콘텐츠는 비어 있음):
- `Buy gate`, `Sell gate` (Capital Decision section, node 10577:7741)
- `Decision Controls` 메뉴 항목 (Add Account 화면 [08])
- 로딩 카피: "Earned conviction / Active decisions / Capital compounds / Activity does not"
- Dashboard taglines: Managed = "Long-term core / Minimal activity", Self-Directed = "Earned conviction / Active decisions"

---

## 3. 폴더에 있는 파일

| 파일 | 내용 |
|---|---|
| `self_directed_placement_strategy.md` | 전체 전략 문서. 8개 섹션 + 부록. 권고와 근거. |
| `self_directed_flow_diagram.svg` | 사용자 여정 시각화 — Section A(Account Opening) + Section B(Trade Decision). |
| `conversation_handoff.md` | 이 파일. 다른 컴퓨터 Claude에게 던질 컨텍스트. |
| `CLAUDE.md` | 보안 규칙 (API 키 등) |
| `cursorrules` | 동일 보안 규칙 |
| `cold_clinical_design_filter.md` | Brand 평가 필터 (Palantir/Alex Karp 기준) |
| `confluence_design_direction_invisible_lifestyle.md` | Invisible Lifestyle 브랜드 방향 문서 |
| `animation rule.txt` | 모션·폴리시 시스템 V1 |

---

## 4. 참조한 Figma 노드 (file: mQhJFtyphUZhzApAeM6OtV)

| 노드 ID | 이름 | 비고 |
|---|---|---|
| 15742:84120 | calibration | Section 1 — managed thesis 교육 |
| 21868:9721~9728 | Section 2~9 placeholder | 대부분 빈 직사각형 |
| 14727:15617 | Section 6: Bank linking | 완성됨 (Flinks/void cheque) |
| 15964:11325/11326/11821 | TFSA/RRSP/Non-Registered agreements | self-directed account agreements |
| 21868:9728 | Section 9 finalizing | "Hold to Proceed Deliberately" 1초 hold ritual |
| 10577:7741 | Capital Decision modal | Buy gate/Sell gate 라벨 존재 |
| 21873:11973 | Market Buy 흐름 | Limit order 디폴트 |
| 21873:11976 | Self-Directed states | 8가지 상태 (No Account, Pending, Failed 등) |
| 7552:10154 | Self-Directed Open Account 흐름 | Add Account → Self-Directed → 계정 종류 → Agreement |

---

## 5. 미해결 / 다음 작업

### 우선순위 높음

1. **Calibration Gate 11화면 1차 시안** (와이어프레임 + 카피)
2. **Buy gate / Sell gate 화면 1차 시안**
3. **Decision Controls 노드 분석** (Add Account [08] 항목 정의)
4. **시나리오 B/C에서 Increase exposure 게이트 강도 결정**
5. **Sell gate 강도가 Buy gate보다 높아야 하는지 합의**

### 출시 전 검토 필요

- Backend replay 인프라 (이게 없으면 11화면이 의미 없음)
- SCREEN 4 "No" 처리 (Add Account 복귀, 침묵)
- 인풋 글자 수 정책 (~30자 하한, ~140자 상한 권고)
- Append-only 정책
- Compliance 검토 ("self-stated standard" 표기)
- Override 기록
- 세션 중단 시 resumable 여부

---

## 6. 다른 컴퓨터의 Claude에게 — 컨텍스트 인계

**아래 프롬프트를 그대로 던지면 된다:**

```
이 폴더에 있는 다음 파일들을 읽고 작업을 이어가줘:
- conversation_handoff.md (이 파일, 컨텍스트 핸드오프)
- self_directed_placement_strategy.md (전체 전략 문서)
- self_directed_flow_diagram.svg (사용자 여정 다이어그램)
- cold_clinical_design_filter.md (브랜드 필터)
- confluence_design_direction_invisible_lifestyle.md (브랜드 방향)
- animation rule.txt (모션 시스템)

이전 Claude 세션에서 Intelligent Investing 앱의
self-directed onboarding 배치 전략을 정리했어.
지금부터 [다음 작업]을 진행하자.
```

`[다음 작업]`은 Section 5의 우선순위 높음 항목 중 하나로 채우면 됨.

---

## 7. 사용자 선호 (시스템 레벨)

- 한국어 응답 우선 (영어 인용은 원문 유지)
- 보안 규칙 (CLAUDE.md / cursorrules):
  - API 키는 `.env.local`에만
  - `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_` 프리픽스 금지
  - 외부 API 호출은 서버사이드 라우트로만
- 브랜드 톤:
  - Cold/clinical, restrained
  - 장식적 emoji/색상 회피
  - 리스트와 표는 정보 밀도가 필요할 때만
  - 단문, operator-grade language

---

## 부록 — 한 줄 원칙

> *Calibration Gate fires once. Decision Gate fires forever. The first writes the rules. The second uses those rules against the user at every decision.*
