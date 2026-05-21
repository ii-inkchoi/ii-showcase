# Self-Directed Calibration — 배치 전략

> **작성 기준 자료**: 회사 철학 기반 self-directed entry 와이어프레임(11 screens), brand 문서 3종(cold/clinical filter, invisible lifestyle, animation rule), 현재 사인업 Figma(Section 1~9), unified dashboard Figma(Capital Decision, Market Buy, Self-Directed states, Add Account)

---

## TL;DR

회사 철학을 담은 self-directed 11화면 흐름은 가입 절차가 아니라 **자기 규율 계약서를 쓰는 의식**이다. 사용자가 작성한 답을 시스템이 저장하고, 향후 매수·매도·변동성 시점에 그 답을 본인 앞에 다시 들이미는 메커니즘이 핵심이다. 따라서:

1. **온보딩 안에 넣지 않는다.** Managed onboarding은 그대로 유지.
2. **두 종류의 게이트로 분리한다.**
   - **Calibration Gate (1회성)**: 사용자가 Add Account → Self-Directed를 *처음* 선택할 때 발동. 11화면.
   - **Decision Gate (반복)**: 매번 매수/매도/변동성 시점에 저장된 답을 재생.
3. **Onfido 신원 확인은 self-directed 흐름에 들어가지 않는다.** 가입 시점에 이미 검증됨.
4. **이미 디자인 안에 자리가 마련돼 있다.** Buy gate / Sell gate / Decision Controls 라벨이 unified dashboard에 존재. 콘텐츠만 채우면 됨.

---

## 1. 결론 — 어디에 두는가

### 1.1 Calibration Gate 발동 조건

| 사용자 상황 | Add Account → Self-Directed 클릭 시 |
|---|---|
| Self-directed 계정 0개 (첫 시도) | ✅ 11화면 calibration 발동 |
| 이미 TFSA self-directed 보유, RRSP 추가 | ❌ 스킵, 바로 RRSP 선택으로 |
| 모든 self-directed 종류 보유 | "All available account types are already open" 메시지 |
| Managed 계정 추가 | ❌ 해당 없음 |

**원칙**: 11화면은 *self-directed라는 모드 자체*에 대한 commitment이지, 계정 종류별 commitment이 아니다. 한 번 자기 규율을 적었으면 모든 self-directed 계정에 자동 적용.

### 1.2 후보 위치 평가 (Calibration Gate)

| 후보 위치 | 판정 | 이유 |
|---|---|---|
| Section 1 (Calibration) 분기 | ❌ | managed thesis 집중 깨짐. 가입 길이 폭증. |
| Section 5 (Investor Profile) 직후 | △ | KYC 결과로 분기 가능하나 마무리 단계 abandonment 위험. |
| Section 9 (Finalizing) 직전, 모든 사용자 | ❌ | managed-only 사용자에게 불필요한 마찰. 회사 전략과 충돌. |
| 첫 매수 시도 시점 | △ | 가능하나 SCREEN 11("Enter Self-Directed Investing")의 약속과 어긋남. |
| **Add Account → Self-Directed 선택 시점 (첫 시도)** | ✅ | 사용자가 모드 전환을 *명시적으로* 결정하는 순간. |

### 1.3 권고 위치: Add Account 화면의 Self-Directed 선택 시점

**근거**

- **명시적 commitment의 순간**: 사용자가 "Managed가 아니라 Self-Directed"를 의식적으로 고르는 행동.
- **회사 철학과 정확히 일치**: SCREEN 11의 "Enter Self-Directed Investing"는 *self-directed에 입장*하는 의식. 매수가 아니라 모드 진입의 의식.
- **"Active investing isn't a starting point. It's something you earn."**: 자격 획득 = 11화면 통과. 자격 사용 = 매번 Decision Gate.
- **managed-only 사용자 보호**: 이들은 Self-Directed를 한 번도 클릭하지 않으므로 calibration을 절대 보지 않음.

---

## 1.4 왜 가입 흐름 마지막(Section 9)에 두면 안 되는가 — 회사 철학과의 8가지 충돌

가입 흐름의 Section 9 직전 또는 직후에 11화면 calibration을 끼워 넣는 안은 표면적으로는 자연스러워 보인다. 사용자가 막 가입을 마쳤고, 다음 단계로 self-directed를 활성화한다면 한 번에 끝낼 수 있다. 하지만 이 위치는 회사 철학과 정면으로 충돌한다.

### 충돌 1 — "Active investing isn't a starting point. It's something you earn."

**회사 철학** (Section 1 calibration 마지막 문장):
> "Great investors don't start fully exposed. They build from a position of strength. A disciplined core. Then selective, high-conviction bets. Active investing isn't a starting point. It's something you earn."

**Section 9 배치의 문제**: self-directed가 *starting point*가 된다. 사용자는 가입과 동시에 self-directed를 받게 되므로, *자격을 얻는 행위*가 사라진다. 11화면은 starting line의 통과 의식이 아니라 *모드를 바꾸기로 능동적으로 결정한 순간*의 의식이어야 한다. 가입 마지막에 두면 결정의 능동성이 사라지고 *통과의 수동성*만 남는다.

### 충돌 2 — Managed-first 전략의 약화

**회사 철학**: 회사는 명시적으로 managed(특히 Core S&P 500 3개)를 시리어스 투자자의 우선 상품으로 내세운다. Section 1 calibration의 거의 모든 메시지가 managed thesis다.

**Section 9 배치의 문제**: 가입 마지막에 self-directed calibration을 띄우면 모든 사용자에게 "self-directed도 한 번 고려해보세요"라는 신호가 자동으로 간다. managed-only를 의도한 사용자에게도 self-directed라는 옵션이 *기본값으로* 노출되는 셈이다. managed-first 우선순위가 흐려지고, 사용자는 두 모드 사이에서 망설이게 된다.

### 충돌 3 — Section 1과 Section 9 메시지의 모순

**회사 철학**: Section 1에서 "Most intelligent investors start here" / "This is not a trading app. It's an investing system designed for long-term compounding"이라고 선언한다. 이 선언이 가입 전체의 톤을 정한다.

**Section 9 배치의 문제**: 시작 메시지가 "여기서 시작하라(managed)"인데, 끝 메시지가 "그런데 적극 투자도 하고 싶으면 11화면 거쳐라"라면 톤이 어긋난다. 시작과 끝이 같은 방향을 가리켜야 한다. Section 9는 *managed의 마무리*여야지, self-directed의 *입구*가 되면 안 된다.

### 충돌 4 — "Hold to Proceed Deliberately" ritual의 희석

**회사 철학**: Section 9의 1초 hold는 managed 입장의 ritual moment이다. "What you are about to experience will feel different. Deliberately." 이 ritual은 가입 전체의 마침표이자, 사용자가 처음으로 *시스템의 무게*를 인터랙션으로 경험하는 순간이다.

**Section 9 배치의 문제**: 이 마침표 직전 또는 직후에 11화면을 끼우면 Hold to Proceed가 진짜 입구의 ritual이 아니라 *중간 정류장*이 된다. ritual의 단일성·희소성이 사라지고, 한 가입 흐름에 두 번의 ritual이 겹치면 둘 다 약해진다. ritual은 여러 번 반복되면 ritual이 아니다.

### 충돌 5 — 규칙은 *대상*이 있을 때 의미가 있다

**회사 철학**: 11화면 SCREEN 7은 "I will not invest if: ___" 같은 규칙을 적게 한다. 이 규칙의 가치는 *작성하는 순간*이 아니라 *나중에 사용자가 종목을 마주하고 매수하려는 순간 자기 자신을 차단하는 무기가 될 때* 발생한다. 즉 규칙은 미래의 자기에게 보내는 편지다.

**Section 9 배치의 문제**: 가입 직후엔 사용자가 self-directed surface를 본 적도, 종목을 본 적도, 가격을 본 적도 없다. 사용자는 자기가 어떤 회사에 끌릴지조차 모른다. 이 상태에서 적은 규칙은 추상적 의식 행위에 불과하다. 회사 철학이 강조한 "nothing performative" 원칙에 정확히 어긋난다 — 자기 자신에 대한 *공연*이 된다.

### 충돌 6 — "Start with conviction, discover discipline after losses" — 구조적으로 같은 실수

**회사 철학** (Section 1 직접 인용):
> "Most people reverse this. They start with conviction. And only discover discipline after losses."

**Section 9 배치의 문제**: 가입 직후에 11화면을 강제하면, 사용자는 *최고조의 conviction 상태*(방금 결제하고 가입한 흥분)에서 규율을 적게 된다. 이건 회사 철학이 *피하라고 한 패턴 그 자체*다. 규율은 사용 경험과 모드 전환의 능동적 결정 후에 적어야 한다. 가입 마지막은 conviction이 가장 높은 시점이지, 규율이 가장 진실해지는 시점이 아니다.

### 충돌 7 — "Invisible Lifestyle" / Anti-Interface 원칙과 충돌

**회사 철학** (brand 문서 직접 인용):
> "Most fintech brands explain everything immediately. Show no interface, show fragments. The strongest systems do not demand attention."

**Section 9 배치의 문제**: 가입 직후 사용자가 처음 마주해야 하는 것은 *대시보드의 정적*이지 추가 11화면이 아니다. 가입 끝에 11화면을 끼우면 "stillness as feature"의 첫 순간이 사라진다. 사용자는 dashboard의 calm을 *경험하기 전에* 또 다른 수술을 받게 된다. brand의 "calm before action" 흐름이 깨진다.

### 충돌 8 — SCREEN 11의 의미적 구분이 사라진다

**회사 철학**: 11화면의 마지막 SCREEN 11은 "Enter Self-Directed Investing → Research companies"라는 명시적 모드 전환의 의식이다. *입장*이라는 단어가 핵심이다. 사용자는 어떤 새로운 공간으로 *들어간다*.

**Section 9 배치의 문제**: 가입 마지막에 두면 사용자가 "Entering Self-Directed"한 직후 마주하는 것은 *전체 dashboard*이다. dashboard에는 managed도 있고 self-directed도 있다. 사용자는 어느 쪽으로 들어왔는지 헷갈린다. self-directed로 *입장했다*는 의미적 경계가 사라진다. SCREEN 11의 마지막 한 줄이 무력해진다.

---

### 요약: Section 9 배치는 11화면의 모든 의도를 무력화한다

11화면의 각 화면은 사용자가 *모드 전환의 무게*를 느끼게 설계됐다. 가입 흐름 안에 묻으면 그 무게가 완전히 사라진다. **11화면은 자신의 위치 자체로 의미를 만든다 — *언제 발동되는가*가 *무엇을 묻는가*만큼 중요하다.**

따라서 권고 위치는 Section 9가 아니라, 사용자가 메인 대시보드에서 self-directed 모드로의 전환을 *능동적으로* 결정하는 순간 — **Add Account 화면에서 Self-Directed를 첫 선택하는 시점**이다. 이 위치에서만 SCREEN 4의 "Active investing is optional. Yes/No"가 실제 결정이 된다. Section 9에 두면 그 결정은 가입 흐름의 한 단계로 묻혀 의미를 잃는다.

---

## 2. 사용자 여정 — 두 게이트 통합 흐름

### 2.1 Account Opening 단계 (Calibration Gate)

```
1. 가입 (managed onboarding Section 1~9, Onfido 포함)
2. 메인 대시보드 진입
3. Active 섹션: "No Accounts" + "Open Account"
4. "Open Account" 클릭
5. Add Account 화면:
   [01] Managed
   [02] Self-Directed
   [08] Decision Controls
6. ★ "Self-Directed" 선택
   ├─ 첫 시도 → Calibration Gate (7번)
   └─ 이미 보유 → 8번으로 직접
7. ★★ Calibration Gate (11화면)
   - SCREEN 1~10 통과
   - SCREEN 4 "No" → 5번 Add Account로 복귀 (침묵, 메시지 없음)
   - SCREEN 11 통과 → "Enter Self-Directed Investing"
8. Open Account 화면: TFSA/RRSP/Non-Registered 선택
   (이미 보유한 종류는 제외)
9. Agreement 화면:
   "I have reviewed and agree to the [TFSA/RRSP/Non-Registered] Declaration of Trust"
10. "Open Account" CTA
11. "Creating account..." 로딩 (1.5–3.0초 텍스트 애니메이션)
    회전 카피:
    - "Earned conviction"
    - "Active decisions"
    - "Capital compounds"
    - "Activity does not"
12. 대시보드 복귀, 새 계정 표시
13. 새 계정 상태: "No Capital Deployed" + "Add Funds"
14. 입금 → 자금 도착
```

**참고**: Self-directed 흐름에 **Onfido 단계 없음**. 신원 확인은 가입의 Section 7에서 이미 끝남. 기존 제안에서 잘못 포함시켰던 부분, 제거.

### 2.2 Trade Decision 단계 (Decision Gate)

```
15. 종목 상세 페이지
16. [Capital Decision] 탭
17. Modal: Initiate position / Increase exposure / Reduce exposure / Cancel
    (시나리오 A/B/C에 따라 옵션 분기)
18. ★★★ Decision Gate (Buy gate / Sell gate)
    - 사용자의 stored answers 재생
    - [Yes] / [No, cancel] 강제 선택 (passive dismiss 불가)
19. Account 선택 (1개면 스킵)
20. Shares 입력 + 주문 타입 (Limit 디폴트)
21. Review 화면 — "Standard applied: '[기준 한 줄]'" 표시
22. Execute Buy/Sell
23. Submitting → Filled / Queued / Submitted
```

### 2.3 Buy gate / Sell gate 콘텐츠

**Buy gate** (시나리오 A — 첫 매수)

> 당신의 매수 기준:
>
> 1. 사업을 이해한다고 판단할 때: *"[user input]"*
> 2. 회사가 매수할 만하다고 판단할 때: *"[user input]"*
> 3. 다음의 경우 매수하지 않는다: *"[user input]"*
>
> 이 거래가 그 기준에 맞습니까?
>
> [예]   [아니오, 취소]

**Buy gate** (시나리오 B/C — 추가 매수)

기존 보유 종목에 대한 추가 매수는 가벼운 형태:
> 이미 통과한 종목입니다. 추가 매수도 같은 기준에 부합합니까?
>
> [예]   [아니오, 취소]

**Sell gate** (매도)

매수보다 강한 마찰. 매도는 더 감정적이기 때문.

> 당신의 매도 규칙:
>
> *"[user input]"*
>
> 지금 이 매도가 그 규칙과 일치합니까?
>
> [예, 일치]   [아니오, 취소]

선택적으로 SCREEN 6 인용 추가 검토:
> "Most investors fail like this: cut winners / hold losers."

### 2.4 Volatility Intervention

**트리거 후보** (회사 철학 spec의 "During Volatility"):

- SPY 일중 변동 ±2% 이상
- 사용자 보유 종목 일중 변동 ±10% 이상
- 사용자 보유 종목 일주일 누적 ±20% 이상

**개입 형태**: 푸시 알림 또는 in-app 배너 (UI 형태 미정)

> 당신은 이렇게 적었습니다:
>
> *"[user input — SCREEN 5 답]"*
>
> 지금 그것을 따르고 있습니까?
>
> [예]   [아니오]

passive dismissal 불가. 응답 자체가 timestamped 기록.

---

## 3. Self-Directed 상태별 게이트 매핑

unified dashboard의 self-directed 섹션은 다음 8가지 상태를 가짐. 각 상태에서 게이트가 어떻게 작동하는지:

| 상태 | UI 표시 | Calibration Gate | Decision Gate |
|---|---|---|---|
| New user, No Self-Directed Account | "No Accounts" + Open Account | ✅ Open Account → Add Account → Self-Directed 첫 선택 시 | — |
| Account Opening In Progress | "Opening In Progress" | (이미 통과) | — |
| Identity Verification Pending | "Verification In Progress" | (이미 통과) | — |
| Identity Verification Failed | "Identity Verification Failed" + Try Again | (이미 통과) | — |
| Two/Three Accounts Exist, No Capital | "No Capital Deployed" + Add Funds | (이미 통과) | — |
| One Account, No Capital, Pending Interac | "Transfer Pending" | (이미 통과) | — |
| Negative Balance | "Cash balance requires settlement" | (이미 통과) | — |
| Active (with positions) | Active Positions / Under Review / Open Orders | (이미 통과) | ✅ 매수/매도 시점 |

---

## 4. 확장 Surface — Onboarding 밖에서 의식의 일관성 유지

### 4.1 Pre-Trade Confirmation (회사 철학 명시)
2.2의 Decision Gate가 이를 직접 충족.

### 4.2 Volatility Intervention (회사 철학 명시)
2.4 참조.

### 4.3 Decision Controls (이미 디자인됨, 콘텐츠 채워야 함)

Add Account 화면의 [08] 위치에 **"Decision Controls — Review triggers and Fiscal.ai"**라는 항목이 이미 존재. 이는 사용자가 Decision Gate의 트리거를 직접 관리하는 surface로 해석됨. 별도 노드 분석 후 정의 필요.

### 4.4 Standards 탭 (제안)
앱 하단 navigation에 별도 탭. 사용자의 모든 stored rule + 적용 이력을 시간순 노출.

원칙: No scoring. No badges. No ranking. *기록만.*

### 4.5 Position Detail 각인 (제안)
보유 종목 상세 화면 하단:
> *Acquired on Apr 14 under standard: "[당시 기준 한 줄]"*

### 4.6 연간 Standards Review (제안)
연 1회 또는 분기 1회, 사용자가 자기 규율을 *append* 또는 *supersede*.
Append-only: 옛 rule은 "superseded on [date]" 표기. 기록 보존.

### 4.7 우선순위 (개발 순서)

| 우선순위 | Surface | 회사 철학 명시? |
|---|---|---|
| 1 | Calibration Gate (11 screens) | ✅ |
| 2 | Buy gate | ✅ |
| 3 | Sell gate | ✅ |
| 4 | Volatility intervention | ✅ |
| 5 | Decision Controls 콘텐츠 | (자리 있음, 정의 필요) |
| 6 | Review 화면 한 줄 추가 | 제안 |
| 7 | Position Detail 각인 | 제안 |
| 8 | Standards 탭 | 제안 |
| 9 | 연간 Standards Review | 제안 |

---

## 5. 디자인 안에 이미 존재하는 단서

이 권고는 새로 발명된 게 아니다. 현재 디자인이 이미 말하고 있는 방향을 따라간다.

| 단서 | 위치 | 의미 |
|---|---|---|
| `Buy gate` / `Sell gate` 텍스트 라벨 | unified dashboard, Capital Decision section | 게이트 자리 명시. 콘텐츠만 비어 있음. |
| `Decision Controls` 메뉴 항목 | Add Account 화면 [08] | 게이트 트리거 관리 surface. 정의 필요. |
| **"Capital Decision"** 단어 | 종목 페이지 진입 버튼 | "Trade"가 아닌 자본 배분 언어. |
| **"Initiate / Increase / Reduce exposure"** | Capital Decision modal | 매수/매도 단어 회피. |
| Limit order 디폴트 | Market Buy 흐름 | 즉시 체결 회피. 가격 결정 강제. |
| **"Hold to Proceed Deliberately"** (1초 hold) | Section 9, onboarding 마지막 | 의식적 friction 패턴. |
| 로딩 카피 회전 | Account Creating | "Earned conviction / Active decisions / Capital compounds / Activity does not" |
| Dashboard taglines | Core / Active 영역 | Managed: "Long-term core / Minimal activity"<br>Self-Directed: "Earned conviction / Active decisions" |
| Section 1 마지막 문장 | "Active investing isn't a starting point. It's something you earn." | 사상적 근거. |

브랜드 메시지가 매 화면에서 사용자에게 다시 말을 거는 구조. anti-dopamine, calm-as-feature 철학의 일관된 구현.

---

## 6. 회사 철학 명시 vs 본 문서 제안 — 책임 구분

### 회사 철학에 명시된 것

- self-directed entry 11화면 흐름과 카피
- Replay at Decision Moments 트리거 3종 (Before Buy / Before Sell / During Volatility)
- Force Acknowledgment 원칙 (Yes/No 강제, passive dismiss 불가)
- "No scoring (MVP)" — 답변 채점·등급화 없음
- Store everything: timestamped, immutable, tied to user
- 디자인 원칙 7가지 (typography, spacing, timing, inputs, no feedback, CTA, transitions)

### 본 문서의 추가 제안

- **Calibration Gate 위치**: Add Account → Self-Directed 첫 선택 시점
- 첫 시도 vs 추가 계정 분기 로직
- UI 형태 추측: gate = 전체 화면 또는 모달, volatility = 푸시 알림 또는 배너
- Review 화면 한 줄 추가
- Standards 탭 신설
- Position Detail 매수 기준 각인
- 연간 Standards Review
- Append-only 정책 (회사 철학은 immutable이라 했고, 본 문서는 append-only로 해석)
- 인풋 글자 수 하한·상한 (~30자/~140자)
- 시나리오 B/C에서 가벼운 게이트
- 매도 게이트 강도가 매수보다 높아야 한다는 원칙
- SCREEN 4 "No" → Add Account 복귀

---

## 7. 출시 전 풀어야 할 것 (전제조건)

체크리스트. 하나라도 미해결이면 MVP 출시 보류 검토.

- [ ] **Backend replay 인프라**: 사용자 답변 저장 + Buy/Sell/Volatility 트리거 시점 호출. 이게 없으면 11화면이 의미 없는 의식이 됨.
- [ ] **Calibration Gate 발동 조건 backend 로직**: "첫 self-directed 시도인가?" 판단. 사용자 self-directed 계정 보유 여부 체크.
- [ ] **SCREEN 4 "No" 분기**: Add Account로 복귀. 메시지 없음. 침묵.
- [ ] **인풋 길이 정책**: 하한(~30자, 너무 짧으면 CTA 비활성), 상한(~140자).
- [ ] **수정 정책**: append-only 권고.
- [ ] **세션 중단 시 resumable 여부**: 사용자가 SCREEN 5에서 이탈하면 다시 어디서부터?
- [ ] **Compliance 검토**: 사용자 작성 규칙을 시스템이 매수/매도 직전 들이미는 행위가 "investment advice"로 해석될 여지가 있는지. 안전하게는 "self-stated standard" 표기.
- [ ] **Override 기록**: 사용자가 게이트에서 "예"를 눌렀지만 자기 기준과 다른 거래를 강행하는 경우, override 자체가 timestamped 기록되는지.
- [ ] **Sell gate 강도 결정**: 매수와 동일 강도 vs 매수보다 무거움. 본 문서는 후자 권고.
- [ ] **Decision Controls 정의**: Add Account [08] 항목의 콘텐츠. 사용자가 트리거를 끌 수 있는지, 강도를 조절할 수 있는지 등.

---

## 8. 다음 작업 후보 (우선순위 순)

| # | 산출물 | 형태 | 가치 |
|---|---|---|---|
| 1 | Calibration Gate 11화면 1차 시안 (와이어프레임 + 카피) | Figma 또는 마크업 | 가장 큰 산출물. 회사 철학의 직접 구현. |
| 2 | Buy gate / Sell gate 화면 1차 시안 | Figma 또는 마크업 | Decision Gate의 핵심 surface. |
| 3 | First Self-Directed → Calibration Gate 사용자 여정도 | flow diagram | 본 문서 부속 자료. ✅ 작성됨. |
| 4 | Decision Controls 노드 분석 + 콘텐츠 정의 | 문서 | Add Account [08] 항목 채우기. |
| 5 | 11화면 카피 brand-filter 문장별 리뷰 | 문서 | cold/clinical filter 통과 점검. |
| 6 | Volatility intervention 트리거 정의 | 스펙 문서 | backend 팀 인풋 필요. |
| 7 | Standards 탭 와이어프레임 | Figma | 별도 큰 기능. v1 이후. |

---

## 부록 — 원칙 한 줄

> *이것은 가입(onboarding)이 아니다. 교육(education)도 아니다. 미래의 자신에게 사용될 규율을 자기 손으로 적게 하는 의식이다. 자리는 이미 디자인 안에 있다. 우리가 채우는 것은 그 자리에 들어갈 콘텐츠뿐이다.*
