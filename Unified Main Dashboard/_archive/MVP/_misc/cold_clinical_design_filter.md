# Cold / Clinical Design Filter

회의에서 언급된 **Alex Karp / Palantir / serious operator** 방향을 기준으로, 투자 앱 디자인을 평가할 때 사용할 수 있는 실무용 필터 문서.

이 문서의 목적은 단순히 화면을 "예쁘게" 만드는 것이 아니라,
**더 신뢰감 있고, 더 절제되어 있으며, 더 높은 품질의 판단을 돕는 디자인**인지 평가하는 데 있다.

---

## 1. Core Principle

이 필터의 핵심 질문은 아래 하나로 요약된다.

> **이 디자인이 serious operator의 더 나은 판단을 돕는가?**

즉, 아래 기준은 후순위다.
- 더 트렌디한가
- 더 소비자 친화적인가
- 더 화려한가
- 더 "cool"해 보이는가

우선 기준은 아래다.
- 더 신뢰감 있는가
- 더 차분하고 절제되어 있는가
- 더 빠르고 정확한 이해를 돕는가
- 더 높은 수준의 의사결정을 지원하는가
- retail trading app이 아니라 capital allocation system처럼 느껴지는가

---

## 2. Brand Lens

이 디자인은 일반 소비자용 투자 앱이 아니라,
**serious operator를 위한 high-trust capital allocation system**처럼 느껴져야 한다.

참고 이미지:
- Palantir 같은 high-stakes system
- Alex Karp가 납득할 만한 serious operator tool
- mission-critical dashboard

피해야 할 느낌:
- retail-friendly
- trendy startup app
- cool해 보이려고 만든 UI
- 감성적/장식적/consumer lifestyle app 느낌

지향해야 할 느낌:
- cold
- clinical
- exact
- credible
- restrained
- high-trust
- performance-oriented

### Palantir / Alex Karp Approach

회의에서 언급된 **Palantir / Alex Karp filter**는 단순히 시각 스타일을 뜻하는 것이 아니라,
디자인 의사결정 전반에 적용하는 **운영 철학**에 가깝다.

핵심은 다음과 같다.

> **이 화면이 일반 사용자를 즐겁게 만드는가보다, 중요한 판단을 더 잘 내리게 만드는가를 먼저 본다.**

즉, 이 접근은 화면을 "멋지게" 만드는 것이 아니라,
**고신뢰 · 고압력 · 고중요도 환경에서도 흔들리지 않는 인터페이스**를 만드는 데 가깝다.

### Palantir / Alex Karp식 판단 기준

- 디자인은 브랜드 장식이 아니라 **판단 인프라**여야 한다.
- 모든 요소는 "예뻐서"가 아니라 **의사결정 품질을 높이기 위해** 존재해야 한다.
- serious operator는 novelty보다 **clarity, precision, control**을 원한다.
- 감성적 친근함보다 **신뢰, 무게감, 냉정함**이 우선이다.
- UI는 사용자를 들뜨게 하기보다 **차분하게 만들고 집중하게 해야 한다.**

### 이 접근을 적용했을 때의 디자인 태도

#### 1. Remove retail behavior cues
- 짧은 주기 반응을 유도하는 표현을 줄인다.
- trading app처럼 보이는 시각적 습관을 경계한다.
- 사용자가 "반응"하기보다 "판단"하게 만든다.

#### 2. Design for seriousness, not friendliness
- 친절한 느낌보다 신뢰 가능한 느낌을 우선한다.
- consumer delight보다 operator confidence를 우선한다.
- “approachable”보다 “credible”이 더 중요한 기준이다.

#### 3. Optimize for mission-critical reading
- 첫 스캔에서 핵심 정보가 바로 잡혀야 한다.
- hierarchy가 엄격해야 한다.
- 숫자와 상태 정보는 흔들리지 않고 안정적으로 보여야 한다.
- 애매한 spacing이나 decorative emphasis는 신뢰를 깎는다.

#### 4. Eliminate anything that feels performative
- 스타일을 위한 스타일은 제거한다.
- personality가 강한 이미지, 과한 브랜딩 제스처, 장식적 표현을 줄인다.
- serious system이라면 없어야 할 요소는 과감히 뺀다.

#### 5. Let evidence improve credibility
- projection, modeled value, performance 같은 정보는 가능하면 근거 구조를 같이 보여준다.
- 단일 주장보다 range, assumption, context가 더 credible할 수 있다.
- sophisticated user가 “왜 이렇게 보이는지” 납득할 수 있어야 한다.

### Quick Test: “Would this survive the Palantir bar?”

아래 질문 중 하나라도 No라면 다시 손볼 필요가 있다.

- 이 화면은 mission-critical tool처럼 느껴지는가?
- serious operator가 봐도 가볍지 않은가?
- 이 요소는 진짜 판단 품질을 높이는가?
- 이 표현은 소비자 앱 습관을 답습한 것이 아닌가?
- 이 화면은 차분함, 통제감, 신뢰를 주는가?

---

## 3. Design Filter Questions

디자인 리뷰 시 아래 질문으로 판단한다.

### A. Trust
- 이 화면은 첫인상에서 **신뢰감**을 주는가?
- 장식보다 **정확성 / 안정감 / 일관성**이 먼저 느껴지는가?
- serious operator가 봤을 때 가볍거나 retail스럽지 않은가?

### B. Cognitive Load
- 사용자가 **빠르게 읽고 이해할 수 있는가?**
- 정보 우선순위가 명확한가?
- 시선이 불필요하게 흔들리지 않는가?
- 한 화면에서 생각해야 할 것이 너무 많지 않은가?

### C. Precision
- 이 정보 표현은 **필요한 정밀도만 보여주는가?**
- false precision처럼 보이지 않는가?
- 반대로, 너무 단순화되어서 불신을 만들지는 않는가?

### D. Seriousness
- 이 화면이 "투자 앱"보다 **capital allocation tool**처럼 느껴지는가?
- 장기적 판단을 돕는 구조인가, 아니면 단기 반응을 유도하는 구조인가?
- 사용자의 행동을 더 차분하고 전략적으로 만드는가?

### E. Discipline
- spacing, type, opacity, alignment가 **엄격하게 통제**되어 있는가?
- 각 요소에 존재 이유가 있는가?
- 불필요한 시각적 개성이 들어가 있지 않은가?

---

## 4. What Good Looks Like

좋은 화면은 아래 특징을 가진다.

### 4.1 Information is prioritized
- 가장 중요한 수치와 상태가 먼저 보인다.
- 덜 중요한 보조 정보는 시각적으로 뒤로 물러난다.
- hierarchy가 명확해서 사용자가 어디를 먼저 봐야 하는지 자연스럽다.

### 4.2 Layout feels controlled
- 여백은 intentional하다.
- 지나치게 넓거나 애매한 spacing이 없다.
- alignment가 정교해서 화면이 안정적으로 보인다.

### 4.3 Typography feels credible
- type system이 절제되어 있다.
- 숫자는 읽기 쉽고 비교 가능해야 한다.
- 특히 dashboard 숫자는 tabular lining numbers를 우선 고려한다.

### 4.4 Visual style is restrained
- decoration보다 function이 우선이다.
- unnecessary flair가 없다.
- 감성적 이미지나 소비자적 embellishment가 최소화되어 있다.

### 4.5 The system supports decisions
- 화면이 행동을 유도하기보다 **판단을 돕는다**.
- urgency보다 clarity를 준다.
- noise보다 signal을 강조한다.

---

## 5. What to Avoid

아래 요소는 기본적으로 경계 대상이다.

### 5.1 Retail trading cues
- 지나치게 실시간 느낌이 강한 표현
- short-term trading mentality를 자극하는 시각 언어
- consumer fintech app에서 흔히 보이는 과한 polish

### 5.2 False visual drama
- 너무 큰 대비
- 과한 강조
- 이유 없는 opacity 변화
- 장식적인 아이콘 / 이미지 / personalization

### 5.3 Unnecessary personality
- cool해 보이기 위한 스타일링
- playful한 tone
- 감정적/라이프스타일 중심 표현
- serious tool에 맞지 않는 custom imagery

### 5.4 Ambiguous hierarchy
- 뭐가 제일 중요한지 모르는 화면
- spacing이 애매해서 grouping이 무너진 화면
- 숫자, 라벨, 보조설명이 경쟁하는 화면

### 5.5 Precision mismatch
- 너무 많은 소수점으로 false precision을 주는 경우
- 반대로 정보를 과도하게 단순화해서 신뢰를 떨어뜨리는 경우

---

## 6. Practical Review Framework

디자인 시안 리뷰 때 아래 순서로 점검한다.

### Step 1. Remove what is not necessary
- 없어도 되는 정보는 없는가?
- 없어도 되는 장식은 없는가?
- 없어도 되는 스타일링은 없는가?

### Step 2. Reconfirm hierarchy
- 사용자가 첫 3초 안에 핵심을 이해하는가?
- 가장 중요한 숫자 / 상태 / 액션이 분명한가?
- 보조 정보가 주 정보와 경쟁하지 않는가?

### Step 3. Tighten presentation
- spacing이 목적에 맞는가?
- alignment가 정확한가?
- opacity와 font size가 정보의 중요도와 맞는가?

### Step 4. Test credibility
- 이 화면을 sophisticated investor가 봤을 때 credible한가?
- long-term capital allocation system처럼 보이는가?
- consumer retail app처럼 느껴지지 않는가?

### Step 5. Test cognition
- 숫자가 빨리 읽히는가?
- 비교가 쉬운가?
- 오해를 부르는 표현이 없는가?

---

## 7. Specific Guidance for Numbers

숫자 표현은 특히 중요하다.

### Principles
- 숫자는 decorative하지 않고 functional해야 한다.
- 빠르게 스캔 가능해야 한다.
- 비교 가능해야 한다.
- 신뢰를 줘야 한다.

### Recommendations
- 가능하면 **tabular lining numbers** 사용
- dashboard balance / value / performance 숫자는 흔들리지 않게 정렬
- 숫자 스타일은 marketing headline과 분리해서 운영 가능
- 필요 이상 정밀한 소수점은 지양
- 다만 소수점 제거가 인지적으로 어색하거나 신뢰를 해치면 유지

### Key rule
> **정밀함을 보여주는 것보다, 신뢰 가능한 판단을 돕는 숫자 표현이 더 중요하다.**

---

## 8. Design Review Prompt

시안을 볼 때 아래 문장으로 스스로 체크한다.

> “If Palantir were designing a capital allocation system for serious operators, would this screen look acceptable?”

또는 한국어로,

> **“이 화면이 serious operator를 위한 high-trust system처럼 보이는가?”**

No라면 아래 중 하나가 문제일 가능성이 높다.
- hierarchy가 약함
- spacing이 느슨함
- 숫자 표현이 흔들림
- retail app 습관이 남아 있음
- 설명 없이 주장만 있음
- 장식이 기능을 이기고 있음

---

## 9. One-Sentence Standard

> **Design for trust, clarity, and serious decision-making — not for charm, trend, or retail excitement.**

