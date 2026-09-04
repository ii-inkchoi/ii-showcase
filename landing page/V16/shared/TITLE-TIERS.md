# 제목 크기 — 자리마다 하나씩

폰(375) 기준. 홈 · Self-Directed · Managed 실측값이고, 이게 캐논이다.

---

## 자리 네 개

### ① 히로 — 페이지 맨 위, 페이지당 하나

```
The market, every week,
without the decision.
```

**28 · 두께 500 · 행간 1.1 · 자간 −0.02em**

### ② 섹션 제목 — 섹션당 하나

```
NO. 08 · ACCOUNT TYPES          아이브로우 13
The account is a container.     28
The discipline is the point.
```

**28 · 두께 500 · 행간 1.1 · 자간 −0.02em**

히로와 **같은 크기다.** 위치와 아이브로우가 구분해주지, 크기로 구분하지 않는다.

### ③ 항목 제목 — 섹션 안에 여러 개

```
TFSA        RRSP        Non-Registered
01 Answer the questionnaire
Managed     Self-Directed     Fiscal.ai Max
```

**22 · 두께 500 · 행간 1.25 · 자간 0**

**두께는 안 떨어진다.** 제목은 크기가 뭐든 500 이다 (2026-08-19). 섹션 제목과는 크기로 갈린다.

### ④ 더 작은 항목 제목 — 목록이 촘촘할 때

```
Orion Digital Commercially Launches Intelligent Investing   (뉴스룸 기사 줄)
Multi-year financials                                       (SD 리서치 목록)
No market timing                                            (Managed 거절 목록)
```

**17 · 두께 500 · 행간 1.3 · 자간 0**

한 화면에 여러 줄이 들어가야 하는 목록에서 쓴다. 22 를 쓰면 다섯 줄이 화면을 다 먹는다.

### ⑤ 설명

**16 · 15 · 13 · 두께 400 · 행간 1.4**

---

## 두께는 두 개뿐 (2026-08-19 확정)

> **제목은 500. 본문은 400.** 끝.

| | 크기 | 두께 |
|---|---|---|
| 히로 · 섹션 제목 | 28 | **500** |
| 항목 제목 | 22 | **500** |
| 작은 항목 제목 | 17 | **500** |
| 설명 · 본문 | 16 · 15 · 13 | **400** |

**왜 이렇게 됐나** — 08-17 에 22 만 400 으로 정했었다. 그런데 17 은 원래 500 이었고, 그래서 크기가 **내려가는데 두께가 28 → 22 → 17 = 500 → 400 → 500 으로 튀었다.** 사다리가 자기 자신과 모순된 것이다. 22 에서 400 과 500 은 나란히 놓고 봐도 거의 구분이 안 돼서, 400 은 보여주지도 못하는 예외를 사고 있었다.

**본문 안의 굵은 리드인은 예외가 아니다** — SD 리서치 목록, Managed 거절 목록의 굵은 첫 마디는 17 항목 제목이라 500 이다. (실측 확인 2026-08-20: SD 10 곳, Managed 11 곳 전부 17/500.)

### 본문 크기의 500 — 강조 한 겹 (2026-08-20 추가)

위 표는 **제목**의 두께다. 이것과 별개로, **본문 크기(15 · 13)에서 500 을 쓰는 자리가 있다.** 9 페이지 실측 결과 45 곳이 넘고, 페이지끼리 값이 일치한다 — 드리프트가 아니라 계속 쓰여온 패턴인데 이름이 없었다.

> **400 본문 안에서 한 단위만 들어올릴 때 500 을 쓴다.** 크기는 그대로 두고 두께만 바꾼다. 세 자리로 한정한다.

| 자리 | 클래스 | 곳 |
|---|---|---|
| 리드 · 페이오프 문장 (섹션당 하나) | `.lead` `.cl` `.pricehd9` `.dlead` | 13 |
| 선언형 목록 항목 — 문장이 아니라 항목 | manifesto `.m-body ul li` · `em` | 32 |
| 표의 기준 행 | Managed `.tbl tr.bench td` (13/500) | 8 |

**크기를 올리지 않는 게 핵심이다.** 이 셋은 제목이 아니다. 제목으로 올리면 (17 로) 목록이 제목 사다리로 올라가버리고, 그러면 진짜 항목 제목과 구분이 안 된다. 무게만 한 겹 얹어서 “같은 층인데 이게 기준선” 이라고 말하는 것.

**여기 없는 자리에서는 본문에 500 을 쓰지 않는다.** 새로 쓰고 싶으면 위 세 줄 중 하나에 해당하는지 먼저 보고, 아니면 이 표에 줄을 추가할지를 결정해야 한다.

> ⚠ 이 문서는 08-19 까지 manifesto 목록 항목을 “17 항목 제목이라 500” 이라고 적어놨었다. **실측하니 15 였다.** 17 이 아니라 위의 “선언형 목록” 자리다. (2026-08-20 정정)

---

## 행간도 사다리다

| 크기 | 행간 |
|---|---|
| 28 | **1.10** |
| 22 | **1.25** |
| 17 | **1.30** |
| 16 · 15 · 13 | **1.40** |

**글자가 작아질수록 행간은 넓어진다.** 08-19 까지 17 이 1.15 였는데, 22 (1.25) 보다 **좁아서** 사다리가 거꾸로 갔다. 두 줄짜리 17 제목이 밑의 설명문에 눌려 보였다.

---

## 예외 — 숫자

```
9 in 10        ~$2,000        46,782        −7.60%
```

**34 · 두께 500 · 자간 −0.069em**

**제목보다 크다.** 하지만 제목이 아니라 **값**이다. 페이지에서 가장 큰 글자는 언제나 숫자다.
400 으로 내리면 숫자가 문장처럼 납작해지므로 500 을 유지한다.

---

## 라벨 (전부 모노)

| 크기 | 어디에 | 대문자 |
|---|---|---|
| **13** | 아이브로우 (`NO. 03 · HOW IT WORKS`) · 링크 · 버튼 | **쓴다** |
| **11** | 순번 (`01` `02` `03`) · 카드 라벨 · 표 머리 | **안 쓴다** |
| **9** | 그림 밑 설명 | **안 쓴다** |

---

## 대문자는 13 티어에서 끝난다 (2026-08-19 확정)

인경: *"약자가 아니면 대문자 풀어."*

> **대문자를 쓰는 곳은 13 모노 하나다** — 섹션 아이브로우, 링크, 버튼.
> **11 과 9 는 문장식으로 쓴다.** 예외는 **약자뿐** (`YTD`, `FAQ`, `CIRO`, `CIPF`, `TFSA`, `RRSP`, `S&P`).

**왜** — 대문자 모노는 "이건 읽는 글이 아니라 표시다" 라는 신호다. 그 신호가 한 크기에만 있어야 작동한다. 11 과 9 까지 번지면 페이지의 절반이 표시가 되어 아무것도 표시하지 않는다.

그리고 11px 대문자는 **짧을 때만 라벨로 읽힌다.** `TAX-FREE` 8 자는 라벨이지만 `SELF-DIRECTED INVESTING` 23 자는 읽기 힘든 문장이 된다.

**2026-08-19 에 바꾼 15 곳:**

| 전 | 후 | 페이지 |
|---|---|---|
| `TAX-FREE` `TAX-DEFERRED` `TAXABLE` | Tax-free · Tax-deferred · Taxable | SD · Managed |
| `PORTFOLIO` `ALLOCATION` `PEAK DRAWDOWN` `RISK LEVEL` `SINCE INCEPTION` | 문장식 | Managed 표 머리 |
| `FISCAL.AI MAX` | Fiscal.ai Max | SD |
| `SELF-DIRECTED INVESTING` `MANAGED INVESTING` | Self-Directed investing · Managed investing | pricing |
| `YTD` | **그대로** | Managed 표 머리 |

**새 페이지를 만들 때** — 11 이나 9 로 라벨을 쓸 거면 대문자를 쓰지 않는다. 대문자로 쓰고 싶으면 그건 13 티어라는 뜻이다.

**대문자를 푼 라벨은 Title Case 로 쓴다** (2026-08-19). `Press Release` · `In the Press` · `Changelog`. 문장식(`Press release`) 이 아니다 — 이건 문장이 아니라 분류 이름이라서.

**날짜 자리표시자는 한 모양** — `[MMM DD], 2026`. 실제 날짜(`JUL 27, 2026`) 와 같은 골격이라 목록에서 줄이 흔들리지 않는다. `[DATE]` · `JUL [DD], 2026` 처럼 섞어 쓰지 않는다.

---

## 한 섹션을 통째로 보면

```
NO. 03 · HOW IT WORKS          13   아이브로우
  ↓ 24
Three steps.                   28   섹션 제목
Then the schedule takes over.
  ↓ 52
01                             11   순번
  ↓ 8
Answer the questionnaire       22   항목 제목
  ↓ 16
It reads your objectives...    13   설명
  ↓ 48
02                             11
Answer...                      22
```

**28 은 위에 딱 한 번. 그 아래는 전부 22.**

---

## 룰 여섯 줄

1. **28** — 히로 하나, 섹션마다 하나. 그 이상 쓰지 않는다
2. **22** — 섹션 안에 여러 개 나오는 제목
3. **17** — 촘촘한 목록의 항목 제목
4. **34** — 숫자 전용. 제목에 쓰지 않는다
5. **제목은 전부 500, 본문은 전부 400**
6. **한 칸씩 건너뛴다** — 28 다음은 22, 그 다음은 17. 붙어 있는 크기를 나란히 두지 않는다. 차이가 안 보이면 층이 아니다

---

## 섹션 제목이 없어도 된다

pricing NO.02 · NO.03 이 그렇다. 아이브로우 다음에 바로 항목이 온다.

```
NO. 02 · THE STRUCTURE      13
Membership Structure        22   ← 네 블록 중 첫째
Trading & FX                22
Fiscal.ai Max               22
Managed Portfolio Fee       22
```

**첫 항목을 28 로 올려 제목처럼 만들지 말 것.** 마크업상 넷은 같은 층(`.p-block` 4개)이고, 하나만 올리면 내용에 없는 위계를 그리게 된다. 2026-08-19 에 그 제안을 냈다가 마크업을 열어보고 철회했다.

아이브로우가 섹션을 표시하므로 28 이 반드시 있어야 하는 것은 아니다.

---

## 색은 바탕이 정한다

| 바탕 | 제목 색 |
|---|---|
| 크림 · 흰색 | `#1C1C1C` |
| 검정 | 흰색 |
| 두 줄 중 둘째 줄을 죽일 때 | `#565B5E` |

**빨강(`#BE3C36`)은 두 가지에만** — 밴드 제목에서 말이 뒤집히는 문장, 그리고 마이너스 수치.
순번(`01` `02`)은 빨강이 아니다. 단, manifesto 의 `NO. 001` 은 인경이 유지하기로 결정 (2026-08-19).

---

## 실측 (9 페이지, 375 · 2026-08-19)

| 크기 | 두께 · 행간 | 개수 |
|---|---|---|
| 28 | 500 · 1.10 | 15 |
| 22 | 500 · 1.25 | 58 |
| 17 | 500 · 1.30 | 27 |
| 16 · 15 · 13 | 400 · 1.40 | 본문 |

**같은 크기가 페이지마다 다른 값을 갖는 곳은 없다.** 데스크탑(1440) 도 같은 상태로 맞췄다 — 크기만 페이지 종류에 따라 다르다 (밴드형 홈·SD·Managed 는 48 / 28 / 22, 콘텐츠 6 페이지는 36 / 28 / 22).

값을 바꿀 때는 `shared/v11.css` 를 고치고 `python shared/check-v11.py` 로 확인할 것.

---
---

# 데스크탑 TYPESETS — 이름으로 부르는 세트 (2026-09-01, Inkyung)

위 ①~④ 는 폰(375) 캐논이다. 아래는 **데스크탑(≥901)** 의 카드/항목 행에 쓰는 세트이고,
**이름으로 호출한다.** "typeset 2 로 해줘" = 아래 표의 2번을 그 행에 적용하라는 뜻.

값은 **1920 렌더 기준**. 토큰이 2545 프레임에서 자동으로 커진다.

## 세 세트

| 이름 | 제목 | 본문 | 토큰 |
|---|---|---|---|
| **TYPESET 1 · LARGE** | 28 / 500 / 1.25 / 0 | 17 / 400 / 1.3 / 0 | `--t-h34` + `--t-body` |
| **TYPESET 2 · MEDIUM** | 22 / 500 / 1.25 / 0 | 17 / 400 / 1.3 / 0 | `--t-read27` + `--t-body` |
| **TYPESET 3 · SMALL** | 17 / 500 / 1.25 / 0 | 15 / 400 / 1.3 / 0 | `--t-body` + `--t-small17` |

제목은 세 값, 본문은 두 값(17 / 15). **22 와 28 이 본문을 공유하므로 본문 크기로는 세트를 알 수 없다.**
그래서 어느 행이 어느 세트인지는 **유도하지 않고 아래 표에 기록한다.**

## 세 세트가 공유하는 행 규칙 (ROW RULES)

세트 번호와 무관하게 카드 행이면 전부 같다.

| 관계 | 값 |
|---|---|
| 제목 → 본문 | **14u** |
| 본문 → 모노 메타 | **14u** |
| 콘텐츠 → 텍스트 CTA | **42u**, 그리고 `margin-top:auto` 로 행의 CTA 를 한 선에 정렬 |
| 카드 열 간격 | **28u** |
| 카드 안 패딩 (배경/테두리 있는 카드) | **42u** |
| 모노 메타 | 11 (`--t-mono13` 의 데스크탑 렌더) |
| **행의 줄 수 일치** | 행 subgrid — 가장 긴 제목이 트랙을 정하고 나머지가 따라간다. `min-height` 금지(빈 줄이 생긴다). 한 줄이면 한 줄, 두 줄이면 두 줄. |

행 subgrid 구현: 부모에 `grid-template-rows:auto auto auto`, 항목에
`display:grid; grid-template-rows:subgrid; grid-row:span 3; justify-items:start`.
`@supports (grid-template-rows: subgrid)` 로 감싼다.
**주의 1** — 이 규칙은 항목의 `display` 를 덮어써야 하므로 그 항목의 마지막 `display` 선언보다
**뒤에** 놓아야 한다. index.html 에서 `.clog .ci{display:flex}` (base, 3400번대) 때문에 한 번 죽었다.

**주의 2 — span 은 흐름 자식 수와 정확히 같아야 한다.** 모자라면 에러가 아니라 **넘치는 자식이
마지막 트랙에 겹쳐 쌓인다.** 체인지로그에서 span 3 으로 날짜와 READ 가 본문 위에 겹쳐 찍혔고,
span 4 로도 마지막 둘이 겹쳤다. `.clog .ci` 는 `.cthumb / .ct / .cd / .cdate / .cread` = **5개**다.
규칙을 쓰기 전에 브라우저에서 흐름 자식을 세라.

## 배정 기록 (registry) — 유도하지 말고 여기를 볼 것

| 행 | 세트 | 파일 |
|---|---|---|
| MEMBERSHIP 카드 3장 | **TYPESET 2** | `index.html` `.sys.memb .mode` |
| 뉴스룸 피처 1건 | **TYPESET 2** | `index.html` `.latest .lt-feat` |
| 체인지로그 3건 | **TYPESET 3** | `index.html` `.clog .ci` |
| THE LOOP 스텝 4개 | **TYPESET 3** | `index.html` `.sdloop .lstrip4` |
| REFUSE 카드 3장 | **TYPESET 2** | `self-directed.html` · `managed.html` `.refuse .r b` |
| ACCOUNT 카드 3장 | **TYPESET 2** | `self-directed.html` · `managed.html` `.acct3 .a h3` |
| FISCAL.AI 패널 항목 7개 | **TYPESET 3** | `self-directed.html` `.fgrid .f b` |

2026-09-01: MEMBERSHIP 과 REFUSE 를 **둘 다 TYPESET 2** 로 맞췄다. 같은 모양의 3장 카드 행이
같은 세트를 쓴다 — 지금 TYPESET 1 을 쓰는 행은 없다. 28 은 계속 유효한 세트지만 현재 미사용.

## 세트 밖에 있는 것 (이 사다리로 세지 말 것)

- **디스플레이** — `.bigh2` `.hbar` `.sys h2` `.loop3 h2` = `max(40px, 64u)` / 500 / 1.05 / −0.02em
- **스탯 숫자** — 34px 고정 / 500 / −0.069em. 폭 무관이 의도다.
- **리드 / 진술문** — `.close9 .pricehd9`(22) `.std5b .a/.b`(28) 는 제목이 아니라 문장이다.
  `--t-lead24` · `--t-read27` 역할이고 뒤에 따라오는 "본문"이 없다.
- **모노 = 메타** — 스펙/날짜/캡션은 항상 IBM Plex Mono. `.acct3` 본문과 `.mlist2` 는 11 모노로
  두 세트 밖에 있다.


---

# 측정폭(measure) 규칙 — 화면 크기별 (2026-09-01, Inkyung)

레일: `margin-left:450u`, `width:1645u` (좌우 거터 450u 대칭). **12컬럼, 거터 30u, 컬럼 109.583u.**
n컬럼 = `n * 109.583 + (n-1) * 30` u.

## 두 개의 폭만 있다

| | 크기 | **1800↑** | **1799↓** |
|---|---|---|---|
| **디스플레이 타이틀** `.bigh2` `.sys h2` `.loop3 h2` | `max(40px, 64u)` | **9컬럼** = 1226u | **10컬럼** = 1366u |
| **본문 산문** | `--t-body` = `max(17px, 22u)` | **6컬럼** = 807.5u | **7컬럼** = 947.08u |

본문은 `var(--prose)` 토큰 하나로 선언한다. `:root` 에서 807.5u, `@media(min-width:901px) and
(max-width:1799px)` 에서 947.08u.

## 왜 브레이크포인트가 있는가

크기에는 **floor** 가 있고(디스플레이 40px, 본문 17px) 측정폭은 `--u` 로 계속 줄어든다.
그래서 크로스오버 아래에서는 글자는 그대로인데 줄이 짧아진다 — 같은 컬럼 수가 화면마다 다른
읽기 길이를 뜻하게 된다.

| 화면 | 본문 6컬럼 | 글자수/줄 | 본문 7컬럼 | 글자수/줄 |
|---|---|---|---|---|
| 1920 | 609px | 62–72 ✓ | 715px | ~80 ✗ |
| 1512 (맥북 15") | 480px | 48–52 ✗ | **563px** | **~59–62** ✓ |
| 1440 | 457px | 41–52 ✗ | **536px** | **~56–62** ✓ |

적정 읽기 구간 45–75자. 타이틀은 2026-08-31 에 9→10컬럼으로 이 보정을 받았고(§6), 본문은
2026-09-01 에 6→7컬럼으로 받았다.

## 이 규칙 밖 (컬럼 보정 안 함)

- **2단 그리드** `.pgrid5` · `.close9 .cols` — `807u + 28u + 807u` 로 레일을 꽉 채운다(6+6=12).
  넓힐 여백이 없으므로 모든 폭에서 6+6 유지.
- **`.latest .lt-sum`** — 자기 컨테이너의 컬럼 공식(`(100% + 30u)/12 * 9 - 30u`)을 쓴다. 레일이
  아니라 자기 컨테이너 기준이라 별도 체계.
- **캡션 티어** `.sdloop .d` 등 312u(2.45컬럼) — 산문이 아니라 캡션.
- **press-release 마스트헤드** — §1 "손대지 않은 것"에서 의도된 차이로 판정.

### 캡션의 폭은 컬럼이 아니라 대상이 정한다 (2026-09-02 추가, Inkyung)

위 줄은 캡션이 컬럼 보정을 받지 않는다고만 적어놨고, **그럼 무슨 폭을 쓰는지**가 없었다.
그 빈 곳에서 하루에 두 번 샜다 — 별자리 캡션과 managed 표 각주.

> **캡션은 자기가 설명하는 요소와 같은 폭을 쓴다. 컬럼 수로 고정하지 않는다.**
> `max-width` 에 숫자를 박지 말고 대상 컨테이너의 폭을 상속받게 둔다.

**이건 새 규칙이 아니라 이미 코드가 하고 있던 것을 적은 것이다.** 실측 (1512):

| 캡션 | 설명 대상 | 캡션 폭 | 대상 폭 |
|---|---|---|---|
| SD 메모 `.figcap` | `.dr-doc` | 391 | 391 |
| SD 벤치마크 `.figcap` | `.tri` | 962 | 962 |
| SD 캘리브레이션 `.figcap` | `.cal-card` | 391 | 391 |
| SD 별자리 `.fig-caps` | `.constplate` | 391 | 391 |
| MG 구체 `.figcap` | `.sphplate` | 309 | 309 |
| MG 리스크 `.figcap` | `.stackwrap` | 309 | 309 |
| MG 표 각주 `.figcap` | `.tblwrap` | 636 | 636 |

**왜 깨지는가** — `max-width` 에 박힌 숫자는 "그때 그 대상이 몇 칸이었나"의 화석이다. `.figcap` 의
`528.3u` 는 4컬럼 도형 아래 있던 시절의 값이고, 표 각주가 8컬럼 트랙으로 옮겨졌을 때 따라오지 않아
3.91컬럼에 갇혔다. 대상이 옮겨지거나 폭이 바뀌면 캡션은 스스로 따라가야 한다.

**캡션이 여러 줄일 때** — 같은 대상에 붙는 캡션 줄들은 한 덩어리다. 줄 사이 `margin` 은 **0**, 행간만
쓴다(§ROW RULES 의 "한 진술로 읽히는 두 문장" 과 같은 처리). 대상 → 첫 캡션은 **24px**.
전례: `.fig-leg` + `.fig-note`, managed 표의 두 각주.

## 통일한 드리프트

같은 6컬럼 본문 폭이 **804u / 807u / 807.5u** 세 값으로 선언돼 있었다. 정확값은 **807.5u**
(= 6*109.583 + 5*30). index.html 은 `var(--prose)` 로 통일 완료.
**남은 작업: self-directed · managed · pricing · manifesto · newsroom 에 같은 토큰 전파 (14곳).**


## 검산 — Inter 글자 폭 상수와 화면별 글자 수 (2026-09-01 실측)

**Inter 평균 글자 폭 = 0.503em** (Inkyung 맥북, Chrome, Inter 실제 로드 상태에서 측정).
산세리프의 교과서 값 0.5em 과 일치한다. 이 상수 하나로 어떤 폭이든 글자 수를 환산할 수 있다.

```
글자 수 = (박스 폭 px / font-size px) / 0.503
박스 폭 px = 글자 수 * 0.503 * font-size
```

측정 방법(다시 재야 할 때): Chrome 에서 페이지를 열고 콘솔에 `allow pasting` 입력 후, 본문 블록의
`width / (문자수 / 줄수) / font-size` 를 계산한다. **컨테이너 안 헤드리스 브라우저로는 재지 말 것** —
Google Fonts 가 막혀 fallback 폰트(숫자 1자 9.45px)로 재지므로 값이 틀린다.
박스 폭·간격·컬럼 같은 기하 값은 헤드리스로도 정확하다. 폰트 metrics 에 의존하는 값만 실기기 필요.

### 현재 설정의 화면별 글자 수

| 화면 | 컬럼 | 폭 | 글자/줄 |
|---|---|---|---|
| 2545 (Figma 프레임) | 6 | 807px | **73** |
| 1920 | 6 | 609px | **71** |
| **1512 (맥북 15", 기준 화면)** | **7** | **563px** | **66** |
| 1440 | 7 | 536px | **63** |
| 1280 | 7 | 476px | **56** |
| 390 (모바일) | — | 390px | **52** |

전부 적정 구간 45–75 안. 7컬럼 보정이 없었으면 1512 가 50자, 1440 이 48자로 하단에 붙었다.

### em 기반 선언은 검토했고 채택하지 않았다

`max-width: 34em`(=68자)로 고정하면 글자 수는 완벽히 일정해진다. 하지만 2545 프레임에서 본문이
22px 이 되므로 박스가 748px = **987u = 8.9컬럼**이 되어 **12컬럼 그리드에서 벗어난다.**
이 사이트의 전제가 2545 프레임과의 정확한 일치이므로, 그것을 깨고 얻는 것이 73자 → 68자 5자
차이라면 채택할 이유가 없다.

**결론: 측정폭은 컬럼으로 선언한다. em 은 선언 단위가 아니라 검산 도구다.**

### 미채택 옵션 (필요해지면)

1299↓ 에서 **8컬럼**(1087u)을 추가하면 1280 이 56자 → 68자가 된다. 한 줄이면 된다.
2026-09-01 시점에서는 1280 도 구간 안이고 기준 화면(1512)이 66자로 가장 좋은 상태라 넣지 않았다.


## 토큰 두 가지 spelling (2026-09-01 전파 완료)

같은 규칙인데 페이지마다 선언 방식이 달라서 토큰이 두 개다.

| 토큰 | 값 | 쓰는 페이지 | 선언 형태 |
|---|---|---|---|
| `--prose` | `807.5u` → `947.08u` | index · self-directed · managed | 절대 u 값 |
| `--prose-cols` | `6` → `7` | pricing · manifesto · newsroom | 컬럼 공식 `calc((100% + var(--gutter)) / 12 * var(--prose-cols) - var(--gutter))` |

둘 다 `@media(min-width:901px) and (max-width:1799px)` 에서 7컬럼으로 바뀐다.
**컬럼 공식 쪽이 더 나은 선언**이다(그리드 상대값이라 매직 넘버가 없다). 새로 쓰는 곳은 그쪽을 쓸 것.

실측 (6페이지 × 1920/1512): 1920 전부 **807u / 609px / 71자**, 1512 전부 **944–947u / 561–563px / 66자**.

### 전파에서 제외한 것 (의도적)

| 위치 | 이유 |
|---|---|
| `.trust9 .tl` (SD·Managed, 807.5u) | 트러스트 블록은 리드 + 로고를 한 행에 세로 중앙 정렬(편차 0)로 맞춰둔 곳. 폭이 바뀌면 줄 수가 바뀌고 그 균형이 깨진다 |
| `#calibration .bigh2` (SD, 807u) | 타이틀을 본문 열로 좁힌 것인데, 그 높이에 맞춰 목업 오프셋(`-296u`/`-271u`)을 손으로 맞춰뒀다. 폭을 바꾸면 목업 정렬이 어긋난다 |
| `.content > .figcap` (Managed) | 캡션 티어, 산문 아님 |
| `canvas` (Managed) | 이미지 |
| `.pgrid5` · `.close9 .cols` (index) | `807u + 28u + 807u` 로 레일을 꽉 채우는 2단 그리드. 넓힐 여백이 없다 |
| `.p-lead` (pricing, 8컬럼) | `--t-h34` 타이틀 티어. 본문이 아니다 |


### 고정폭 요소와 한 행을 쓸 때 — 줄이는 건 산문이 아니라 옆 요소다 (2026-09-01 추가, Inkyung)

위 제외 표는 `.trust9 .tl` 을 "리드 + 로고를 **한 행에**" 라고만 적어놨고, **그 한 행에 안 들어갈 때**
어떻게 되는지가 없었다. 그 빈 곳을 실제 렌더가 채우고 있었고, 답이 틀렸다.

> **산문 폭은 규칙값이다. 한 행이 좁아졌다고 산문을 줄이지 않는다.**
> 같은 행의 **고정폭 요소가 자기 줄로 내려가고, 내려간 줄에서는 왼쪽 정렬**한다.

**왜** — 로고·마크처럼 px 로 선언된 요소는 `u` 로 줄지 않는다. 그래서 한 행이 좁아지면 손실이
**전부 산문 쪽으로** 간다. 실측(자동 줄바꿈 넣기 전, `.trust9`):

| 창 | 리드 폭 | 줄 수 | 마크 폭 |
|---|---|---|---|
| 1512 | 480px (6컬럼) | 2줄 | 391 |
| 1280 | 397px | 2줄 | 391 |
| 1100 | 281px | 3줄 | 391 |
| 1000 | 216px | 4줄 | 391 |
| 901 | 152px | **5줄** | 391 |

6컬럼 + 거터 24 + 마크 391 = 레일(0.6464 × 창) 이므로 **창 1261 아래에서는 물리적으로 한 행에
안 들어간다.** managed 는 마크가 421px(IIWMI+CIRO+AMF)이라 더 일찍 깨져서 1000 에서 **마크가
리드 위로 겹쳤다.**

**마크를 같이 줄이는 안은 기각.** 901 에서 로고 높이가 17px 까지 내려간다. CIRO/CIPF/AMF 는
컴플라이언스가 요구하는 마크라 판독성이 조건이다.

**구현** (self-directed.html · managed.html, `@media (min-width:901px)`):

```css
.trust9 .thead{flex-wrap:wrap;row-gap:28px}
.trust9 .tl{flex:0 0 calc(807.5 * var(--u))}      /* 6컬럼 고정. 늘지도 줄지도 않는다 */
.trust9 .regmarks{margin-left:0;justify-content:flex-start}
```

`flex:0 0` 이 핵심이다. `flex-basis` 를 `auto` 나 0 으로 두면 산문이 남는 자리를 먹거나
반대로 눌리고, 둘 다 규칙 위반이다. 폭을 고정해야 **줄바꿈이 마크 쪽에서 일어난다.**

실측 결과 — **1512 이상은 손대기 전과 동일**(한 행, 리드 480px/6컬럼), 1280 이하에서 마크가
자기 줄로 내려가 왼쪽 정렬, managed 겹침 해소, 모바일(≤900) 영향 없음.

**이 규칙은 트러스트 블록 전용이 아니다.** px 고정 요소(로고·마크·배지·아이콘 행)가 산문과 한 행을
쓰는 모든 자리에 적용한다. 새로 만들 때 셋 중 하나를 고르는 게 아니라, **산문은 규칙 컬럼으로
고정하고 고정폭 요소가 줄바꿈을 받는다.**


## 22 전수 감사 — 어디에 쓰이고 있었나 (2026-09-01, 8페이지 1920 실측)

22 는 **두 역할로 섞여 쓰이고 있었다.** 제목으로 쓰는 건 맞고, 산문 칼럼 안의 강조 문장으로 쓰는 건
틀렸다. 후자를 전부 17 로 내렸다.

### 유지 — 제목 역할 (TYPESET 2), 11곳

| 페이지 | 위치 | 형제 본문 |
|---|---|---|
| self-directed | `#review .t` · `#refuses b` | 17 / 17 |   ← `#research b` 는 여기서 빠졌다 (아래 2026-09-01 감사)
| managed | `#how-it-works .t` · `#refuses b` · `#projection b` | 17 |
| pricing | `.q` (FAQ 질문) | 17 |
| index · self-directed · managed | MEMBERSHIP / REFUSE 카드 | 17 |

### 유지 — `.pricehd9` 3곳 (index · self-directed · managed 클로징)

자기 흰 박스 안의 **유일한 문장**이고 형제가 모노 13/11 이다. 산문 칼럼 안이 아니므로 22 유지.

### 내림 — 산문 칼럼 안의 코다, 8곳 → **17**

| 페이지 | 위치 | 처리 |
|---|---|---|
| self-directed | `#calibration .lead` + `.lead.mut` | 17/500 + 17/400 |
| self-directed | `#refuses .lead` | 17/500 |
| self-directed | `.specimens .snote .cl` | 17/500 (`--t-read27` 였음) |
| managed | `#default .lead` · `#fee .lead` | 17/500 |
| managed | `#how-it-works .lead` + `.lead.mut` | 17/500 + 17/400 |

**규칙**: 산문 칼럼은 한 크기(17)만 쓴다. 강조는 크기가 아니라 **무게**로 한다 — 2026-08-19 의
역할 규칙(제목 500, 산문 400)을 그대로 적용. `.lead.mut` 는 400 + `--c-700`: 위의 진술문보다
조용해야 하고, 500 두 줄이 연속되면 한 덩어리로 무겁게 읽힌다.

홈에는 "문단 하나만 크게" 장치가 **아예 없다.** 홈의 강조는 섹션 하나를 통째로 주거나(`.std5b` 28)
빨간 CTA 다. 이게 이 판단의 근거다.

### 실측 후 `#calibration` 밀도 (1512)

```
body 17/400 3줄  →24px→  body 17/400 5줄  →71u→  lead 17/500 2줄  →24px→  lead.mut 17/400 회색 3줄
```
한 크기, 세 무게/색. 22 두 개가 연속되던 것이 "빼곡함"의 원인이었다.


## 정정 — ACCOUNT 카드는 TYPESET 3 이 아니었다 (2026-09-01)

registry 에 TYPESET 3 으로 적었으나 실측하니 **17/500 제목 + 17/400 본문** — 제목과 본문이 같은
크기였다. TYPESET 3(17/500 + 15/400)도 아닌 **정의되지 않은 네 번째 조합**이었고, 카드에 멤버십
박스를 씌우자 드러났다. **TYPESET 2 (22/17) 로 교정.**

이제 사이트의 박스형 3장 카드 행 세 개가 모두 같은 세트다:

| 행 | 세트 | 박스 |
|---|---|---|
| MEMBERSHIP (index) | TYPESET 2 | #FFF on cream, 패딩 42u |
| REFUSE (SD·Managed) | TYPESET 2 | rgba(0,0,0,0.55) + 헤어라인, 패딩 42u (사진 위) |
| ACCOUNT (SD·Managed) | TYPESET 2 | #1C1C1C on #000, 패딩 42u |

~~⚠ 미해결: `.acct3 .a h3` 의 모바일 값이 두 페이지에서 다르다~~ → **해결 (2026-09-01)**. 실측하니
두 페이지 다 이미 `22/500` 이었고(내 첫 보고가 CSS 줄만 읽고 낸 오진), 진짜 컨트롤러는 두 페이지가
아니라 `shared/v11.css` 였다. 거기서 `17px/500` 으로 통일. 교훈: 두 페이지가 같은 값을 보이면
페이지 CSS 를 의심하기 전에 공유 시트를 먼저 grep 한다.


---

# 모노 (IBM Plex Mono) — 2026-09-01 전수 감사 후 확정

## 크기: 세 개

| 렌더 (1920·1512) | 2545 | 토큰 | 역할 |
|---|---|---|---|
| **13px** | 15 | `--t-mono15` | CTA 라벨 · 섹션 eyebrow · `.fee` |
| **11px** | 13 | `--t-mono13` | 메타 · 날짜 · 스펙 줄 · 법적 문구 |
| **9px** | 11 | `--t-mono11` | **캡션 전부** · 다이어그램 범례 · 스탬프 |

토큰 이름의 숫자는 2545 프레임 값이다. 데스크탑은 floor 가 렌더된다.
⚠ `--t-mono12` 는 데스크탑에서 `--t-mono13` 의 floor 와 동일하게 11px 로 렌더되는 **잉여 토큰**이다.
`--t-mono13` 으로 흡수 대기.

## 자간: 하나

**+0.04em** — 13px→0.52 / 11px→0.44 / 9px→0.36. 8페이지 예외 0.

## 행간: 규칙 B — 줄 수가 정한다

| | 값 | 대상 |
|---|---|---|
| 여러 줄로 흐르는 모노 산문 | **1.5** | `.tnotes` · `.metaline` · `.mut` · 법적 문단(`.pr-legal p` 등) |
| 한 줄 라벨 · 메타 · 날짜 | **1.4** | 언어 EN/FR · `.beatcap` · `.heyeb-b` · 브랜드 태그 · `.mmeta` · 날짜 · `.lim` · `.pr-dateline` · `.pr-fig-mark` · `.pr-attrib` · `.p-foot` · `.htrust` · 법적 `h2` |
| 13px 라벨 티어 | **1.5 고정** | 이미 균일하고 chrome 이라 손대지 않음 |

**판정은 컴포넌트 단위로** 한다. 인스턴스별로 하면 `.figcap` 처럼 한 페이지에서 1줄, 다른 데서 8줄인
클래스가 페이지마다 다른 행간을 갖게 되고, 이 규칙이 없애려는 드리프트를 그대로 재생산한다.

### 예외 하나 — 캡션

**캡션은 문장처럼 흐르지만 1.5 가 아니라 캡션 티어 9px / 1.4 를 쓴다.** 캡션은 산문이 아니라 주석이다.
2026-08-02 모노 티어 감사가 이미 "figcap/legend/stamp = 9 at 1.4, not the 13 label token" 이라고
적었고 모바일은 줄곧 9px 이었는데 데스크탑 `.figcap` 만 13 토큰에 남아 있었다(2026-09-01 교정).
지금 캡션 전부 9/1.4: `.figcap` `.sys-note` `.leg-cap` `.fig-note` `.fig-leg` `figcaption`.

## 남은 어긋남 (미해결)

| 클래스 | 문제 |
|---|---|
| `Managed assets carry an additional 0.10% fee.` | index·SD 는 `.fee9` 13/1.5, managed 는 `.metaline` 11 — 같은 문장 두 처리 |
| `.metaline` | SD 11px / managed 9px |
| `.mut` | SD 9px 모노 / managed 17px Inter — 이름만 같은 두 컴포넌트 |
| `.menuov-cta` | 모노 중 유일하게 무게 500 (5페이지 공통, 의도 여부 미확인) |
| 한 줄인데 1.5 로 남음 | `.k` · `thead th` · `.nr-tabs button` · `.step b`(비트 번호) · pricing `.sub` |

---

# RADIUS — 2026-09-01 확정

| 토큰 | 값 | 대상 |
|---|---|---|
| `--r-site` | **4px** | 사이트 카드·패널·이미지 타일·**버튼** |
| `--r-app` | **12px** | 앱 목업 **외곽** (`.dr-doc`) |
| `--r-app-in` | **6px** | 목업 **내부** 박스 (`.dr3-case` `.dr3-chip` `.cal-card`) — 외곽의 절반 |
| `--r-pill` | **99px** | 칩 |

**적용 대상은 "네 변이 있는 것"** — 채움이나 전체 테두리를 가진 박스. 풀블리드 밴드(`.v9band`),
헤어라인만 있는 디렉토리 행, 밑줄 탭, 텍스트 전용 접기 컨트롤은 박스가 없어 제외.

**왜 사이트 4 / 목업 12 인가:** 이전에는 사이트 0 / 목업 4 로 "각진 페이지 vs 둥근 소프트웨어" 였다.
0 이 카드 맥락에서 디자인 없는 느낌이라(Inkyung) 사이트를 4 로 올리되, 구분이 사라지지 않게 목업을
12 로 올렸다. 구분이 없어진 게 아니라 **0-vs-4 에서 4-vs-12 로 옮겨간 것**이다.

이미지 타일은 래퍼와 `img` 양쪽에 radius 를 주고 래퍼에 `overflow:hidden` 을 건다 — cover 로 맞춘
이미지가 코너를 각지게 덮는 것을 막기 위함.

8개 HTML 전부 같은 블록을 쓴다. 값 하나를 바꾸면 전역에 반영된다.

## TYPESET 전수 감사 (2026-09-01, Inkyung "typeset 검수")

데스크탑 1512 에서 다중 항목 행 **전부**를 실측했다. 결과: **미등록 조합 0개.**

| 행 | 제목/본문 | 세트 |
|---|---|---|
| MEMBERSHIP 카드 (index) | 22 / 17 | TYPESET 2 |
| REVIEW 행 (SD · managed) | 22 / 17 | TYPESET 2 |
| REFUSE 카드 (SD · managed) | 22 / 17 | TYPESET 2 |
| ACCOUNT 카드 (SD · managed) | 22 / 17 | TYPESET 2 |
| CHANGELOG 3건 (index) | 17 / 15 | TYPESET 3 |
| THE LOOP 스텝 4개 (index) | 17 / 15 | TYPESET 3 |
| FISCAL.AI 패널 항목 (SD) | 17 / 15 | TYPESET 3 |

**오늘 고친 것 하나**: FISCAL.AI 패널 항목이 `22 / 15` 였다 — 등록된 세 조합 중 어디에도 없는
네 번째 조합이고, 리스트 항목 제목이 섹션 본문(17)보다 컸다. TYPESET 3 으로 내렸다. 이 어긋남은
위 "유지 — 제목 역할" 표에 `형제 본문 17 / 15 / 17` 로 이미 기록돼 있었다 — 표가 문제를 적어두고도
고치지 않은 상태로 남아 있었던 것. **표에 이상값이 적혀 있으면 그것이 곧 할 일이다.**

⚠ ACCOUNT 카드를 셀렉터로 재볼 때 주의: `.acct3 .a p` 는 DOM 순서상 **모노 `.lim`(11px, "Tax-free")**
을 먼저 잡는다. 카드 구조는 `h3 / .lim / p / .lim` 이고 본문은 **두 번째** `p` 다. 이걸 놓치면
ACCOUNT 가 `22/11` 이라는 없는 조합으로 잘못 읽힌다(오늘 한 번 그렇게 읽었다).

세트가 왜 그 행에 붙는지는 여전히 **유도하지 말고 표를 본다.** 다만 관찰: TYPESET 2 는 항목 하나가
레일의 큰 몫을 차지하는 행(3장 카드 / 전폭 행), TYPESET 3 은 항목이 더 많거나 하나의 컨테이너 안에
들어 있는 행(패널 안 7개, 스텝 4개, 썸네일 리스트 3개)에 붙어 있다. 반례가 나오면 표가 이긴다.

---

## GRID GUTTER — 30u, always (2026-09-02)

The rail is 1645u = 12 tracks of 109.583u with **30u** between them. Any row that sits on the rail
uses 30u as its `column-gap`. Nothing else. 28u and 42u are spacing-scale values for *vertical*
rhythm; used as a gutter they put cells 2 and 3 a few u off the column lines, which reads as
"살짝 어긋남" and is invisible until you measure.

- 3-up row → `repeat(3,1fr)` + 30u = **columns 1-4 / 5-8 / 9-12**
- 4-up row → `repeat(4,1fr)` + 30u = 3 columns each
- 2-up row → the 6-col formula twice + 30u = **1-6 / 7-12**
- label + text → `109.58u 1fr` + 30u = **1 / 2-12**
- figure beside prose → `<6col> 1fr <4col>` + 30u = **1-6 / 9-12** (the 1fr is the slack, not a gutter)

The n-column formula, for any fixed track:
`calc((100% + 30 * var(--u)) / 12 * n - 30 * var(--u))`
Never a hardcoded u value (807u for 6 col was 0.5u short and compounded through the row).

Card-**internal** grids (a summary strip inside a mockup) are not on the rail and keep their own gaps.

**How to check:** measure each cell's left edge as `(x - railLeft) / railWidth * 12 + 1`.
A correct 3-up reads `1-4.85 | 5.07-8.93 | 9.15-13` — the fractions are the gutters, not error.

## FIGURE HEIGHT — derive it, don't ratio it (2026-09-02)

When a figure's bottom must line up with something in the neighbouring column, its height cannot come
from `aspect-ratio`. The ratio scales with `--u`; the neighbour is text and does not. Measured on the
closing constellation: the two bottoms were **149 / 119 / 52 / 45 px** apart at 1440 / 1512 / 1920 / 2200.

The fix is to derive the height from the row: `align-self:stretch` on the figure, `height:100%` +
`aspect-ratio:auto` on the plate, caption absolute below it. Width still comes from the column track.
Verify at four widths; the difference must be 0 at every one.

## DATA TABLES — one row height, fixed column shares (2026-09-02)

A data table has one row height. Content that happens to be longer does not get a taller row.

- `td{height:calc(2 * <line-height>em + <padding>);vertical-align:middle}` — derive it from the cell's
  own line-height and padding so it tracks the type token past its crossover. Never a hardcoded px.
- `table-layout:fixed` + a `<colgroup>` with explicit percentage shares. Auto layout hands width to
  whichever column asks loudest, so the column holding the longest string gets starved and drops to a
  third line at some widths and not others — which is what makes the rhythm look random.

Tune the shares against the LONGEST cell, not the header. Verify at 1366 / 1440 / 1512 / 1920 / 2560:
every row height must be within 1px (the 0.667px border rounds).

## MOBILE VERTICAL RHYTHM — the gap compensators do not survive the breakpoint (2026-09-03)

The base carries a family of `margin-top: calc(24px - N * var(--u))` rules. They are not spacing
values; they are **corrections for a desktop parent gap** — "the parent flex already gives 71u, so
subtract it and leave 24". The mobile block changes those parents (`row-gap` to 0, 16, 8, 24) and
did not change the compensators, so below 900 they subtract a gap that is not there — or add to one
that is. Measured at 390, the same paragraph-to-paragraph relationship rendered

`4.3 · 6.4 · 13.1 · 19.7 · 21.9 · 29.9 · 35.7 · 37.1 · 41.6 px` — a canon of 24.

**Rule: below 900 no spacing is derived from `--u`.** The gap is dropped to 0 and the margin carries
the whole step, flat:

| relationship | mobile |
|---|---|
| prose → prose, element → element | **24px** |
| figure → caption | **16px** |
| block group → block group | 40px |
| section-internal major break | 104px |

Each page now ends with a `@media (max-width:900px)` block that zeroes the parents and states the
flat values. When you add a compensator to the base, add its mobile flat value in the same edit.

**Two of them lost on SPECIFICITY, not order** — `#development .content>.mlink` (1,1,1) and
`.close9 .offer .fee9` (0,3,0) outranked the mobile block's (0,2,0) overrides and kept their u-margin.
Match the specificity; do not raise it further. self-directed already carried this fix for
`#research`, which is how the pattern was recognised.

**How to check:** at 390, every computed `margin-top` between 4 and 44px should be a whole number.
A fractional one (13.1, 19.7, 21.9) is a `--u` value that leaked past the breakpoint.
