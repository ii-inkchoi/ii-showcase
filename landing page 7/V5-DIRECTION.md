# V5 랜딩 — 새 디렉션 핸드오프 (2026-07-20)

> **용도**: 다른 컴퓨터/새 Claude 세션에서 이 작업을 이어받기 위한 문서. 이것만 읽으면 처음부터 설명할 필요 없음.
> **워킹 폴더**: `Product Design_work files/Prototype/landing page/V5/`
> **전신**: V3 (Figma 픽셀 재현, full-on Swiss) → V4 (V3 비주얼 + CEO 콘텐츠) → **V5 (새 디렉션, 이 문서)**. V3/V4는 동결 — 절대 수정하지 말 것.

---

## 1. 디렉션이 어떻게 정해졌나 (CEO 회의 2026-07-20)

CEO(회장) 회의 녹취(`바탕 화면/2026-07-20 10-37-26.txt`) 핵심 지시:

1. **방향 확정** — 탐색 종료. "full-on Swiss" 버리고 **미니멀리스트 Swiss** ("Swiss인 걸 아는 사람만 알아채는 수준"). 지금(V3/V4) 디자인은 "way more Swiss modern, you'd see it right away" → 과함.
2. **레퍼런스 = The Mercer Edition** (Instagram `@themerceredition` + themerceredition.com). 그리드/캐러셀 중심. **"실행이 쉬운 포맷"이 핵심** — Tarsila가 CEO 콘텐츠 + 비주얼 찾아서 조립할 수 있어야 함.
3. **"프레임" = v8 브랜드 시스템 문서가 정의** — 로고(//), 시리얼, 카피 요소, 헤어라인. "폴리시 필요하지만 그게 general."
4. **웹사이트 조정 과제**:
   - **풀블리드 비주얼 + 카피 온 이미지** 도입 (현재 사이트에 없던 것)
   - **섹션당 Swiss 요소 감축** — 기존엔 빅넘버+앱스트랙트 비주얼+카피오버이미지가 섹션마다 3~4개씩 → 미니멀로
   - ⚠️ 카피 오버 이미지 **가독성 문제**를 CEO가 반복 지적 ("too often hard to read") → 해결책 필요 (Mercer의 솔리드 바 or 강한 다크닝)
   - **B/W 사진 + 컬러 빅넘버** 류 기존 에셋은 개별 소셜 포스트용으로 유지, 사이트 전체가 그 느낌이면 안 됨
   - Mercer **아티클 포맷** (롱폼: 카피+비주얼) 좋다고 함 — 콘텐츠 페이지 참고용
5. **콘텐츠 = CEO가 지난주 보낸 새 섹션/카피** (= `ceo-content-source.html`)
6. **히로 = 미결, 디자이너 재량** — 기존 서클 그래프(aperture)는 확정 거부. "미니멀 넘버" 방향 힌트.

## 2. V5 방정식 (확정)

| 레이어 | 소스 |
|---|---|
| **콘텐츠/카피** | `V5/ceo-content-source.html` — **전문 빠짐없이**. 단 이 파일의 디자인은 무시 (Claude로 급히 돌린 목업, 내용만 정확). em-dash만 no-em-dash 규칙대로 쉼표/콜론 치환 |
| **프레임 (브랜드 가구)** | **v8 브랜드 시스템 덱** `design-system/II Brand System v8 - The Work (2).html` — 워드마크 INTELLIGENT(700)+INVESTING(300), `//` 사인오프, 시리얼(NN/NN), mono 아이브로우, "one idea leads", "colour encodes never mood", 뉴트럴 스테이지 |
| **비주얼 무드** | **Mercer** — 에디토리얼 매거진, 사진이 레이아웃, 미니멀 크롬 |
| **타입** | **Inter(읽기) + IBM Plex Mono(mono/라벨/시리얼/CTA)** — Chakra Petch 완전 은퇴(2026-07-15). Serif 도입 안 함 |
| **제품 아티팩트** | V3에서 코드 그대로 추출 (§6) — **재구현 절대 금지** |

> v8 덱 참고: Claude 아티팩트 번들 구조라 실제 페이지는 line 388에 JSON 문자열로 임베드됨. 공식 doctrine 채택은 아직 보류 상태(메모리 `brand-system-v8-pending`)지만 CEO가 회의에서 "그게 프레임"이라고 지목함.

## 3. Mercer 레퍼런스에서 읽은 문법

**Instagram 그리드**: 모든 카드에 마스트헤드("The Mercer.") 좌상단 고정 + 헤드라인은 하단에 볼드 화이트 그로테스크(Helvetica Now 류), Title Case, 타이트 행간, 사진 위 오버레이. 컬러 사진(컬처/캔디드/인물). 중간중간 텍스트-온-블랙 인용 카드로 리듬. 우하단 mono 시리얼(FA_RH_05/26 형태). 캐러셀 = 이미지 슬라이드 ⇄ 텍스트-온-블랙 교차.

**웹사이트**: 중앙 마스트헤드("MERCER." + "Post-Institutional-Media." 태그라인) + 햄버거, 크롬 최소. 풀블리드 이미지 밴드가 페이지 단위. **헤드라인은 솔리드 블랙 바 안에 화이트**로 이미지 위에 얹음 (가끔 컬러 바로 액센트). 아티클 = 흰 배경 + 대형 센터 헤드라인(마침표) + mono 아이브로우 + 풀폭 사진.

주의: **그대로 따라하면 안 됨** (인경 지시: "너무 따라하면 안되고"). 인물 중심 사진도 기존 II "objects over personalities"와 충돌 — V5는 거리/군중/사물 위주로 절충 중.

## 4. 현재 산출물 (2026-07-20 기준, 전부 빌드·검증 완료)

### 히로 탐색 (`_experiments/`)
- `v5-hero-A.html` — Mercer 풀블리드+블랙 바. **컨셉 채택** (단독으론 "너무 레퍼런스랑 비슷")
- `v5-hero-B.html` — 미니멀 타입-온리. 인경 개인 선호였으나 "비어 보임"
- `v5-hero-C.html` — 스플릿(타입 좌+사진 우). **폐기** ("애매", SaaS 클리셰)
- `v5-hero-D.html` — 커버 구조(타입 위+사진 밴드 아래). 반응 없음
- `v5-hero-E.html` — 풀이미지 다크닝+타입 직접. **컨셉 채택**
- **확정**: 헤더 크롬 (햄버거 / 중앙 워드마크 INTELLIGENT·INVESTING + "A Capital Allocation System" 태그라인 / OPEN AN ACCOUNT 보더 버튼) — "해더는 맘에 들어"

### 풀페이지 4버전 (V5 루트) — **A와 E 두 컨셉으로 전체 리디자인, 인경 승인 하에 동의 없이 진행됨**
| 파일 | 컨셉 | 레일 |
|---|---|---|
| `index-A.html` | **A: Mercer 바** — 풀블리드 사진 밴드(솔리드 바 헤드라인) ⇄ 텍스트-온-블랙 슬라이드 | 풀블리드 (frame 패딩만) |
| `index-E.html` | **E: 풀이미지 타입-리드** — 풀화면 다크닝 사진(grayscale+brightness 0.42, 화이트 타입 직접) ⇄ 크림 데이터 섹션 | 풀블리드 |
| `index-A-grid.html` | A와 동일 | **컨테인드 1680px** 중앙 |
| `index-E-grid.html` | E와 동일 | 컨테인드 1680px |

**미결**: A vs E vs 혼합, 풀블리드 vs 컨테인드. 내(Claude) 추천 = 컨테인드(-grid): 노트북에선 차이 없고, 와이드에서 레일 안정, Mercer도 콘텐츠는 캡, CEO 목업도 1680.

`index.html` = 아직 V4 계열 복사본 (건드리지 않음). 버전 확정되면 그 파일을 index.html로 승격 + 나머지 `_experiments/`로.

### index-H.html — 인경 Figma 하이브리드 1:1 구현 (2026-07-20, 유력 후보)
인경이 A/E를 참고해 Figma에서 재구성한 **하이브리드**(노드 `2776:628`)의 1:1 코드 구현. `--u = 100vw/2545` 픽셀 재현. **audit 수정사항 반영 완료**: 03 헤드라인 sentence case, typed caps(uppercase transform 0), 스케일 스냅(11.4→11 / 12.4→12 / 14.5→15 / 29→28 / 36→34 / 20.7→22 / #bbb→c-600), 9-in-10 풀 설명+SPIVA 소스, 18%→−11% 설명 추가, CTA = `ENTER THE SYSTEM` 단일(OPEN AN ACCOUNT 폐기 — 인경 확정), FIG.02 캡션 풀 라벨.
- 구조: 화이트 nav(중앙 워드마크 22px) → 히로(사진+블랙 바 3장, 440/462) → 01 System(크림: 좌 텍스트 804u + 우 루프 640u + 모드 3열 그리드) → 02 Missing Layer(다크, 사진 2장+바, 본문 3문단) → 스탯 인터루드(블랙, 9-in-10/18→−11/4% 3열) → 03 Loop(크림 2817u: 블리드 숫자 03 + 캡스→sentence 헤드라인 + 문단 3 + 스텝 4열 + 스페시멘 카드 2 + 클로징)
- 루프 = 라이브 sysLoopCanvas(코드 그대로), 호라이즌 링 = 라이브 캔버스. 사진 = 인경이 고른 Figma 에셋 로컬 다운로드(`Images/figma-h/`, 7일 만료 전 확보).
- **04 Default / 05 Standard / Close = 인경 Figma 미완성 — Figma 진행되는 대로 이어붙일 것.**

### 섹션 구조 (CEO 콘텐츠 순서 그대로, 4버전 공통)
1. **Hero** — "The market remembers every decision. / Most investors do not." + def + EXPLORE THE SYSTEM(#system) / OPEN AN ACCOUNT + CIRO 트러스트 라인
2. **NO. 01 THE SYSTEM** — "One system. Two ways to allocate." + Managed/Self-Directed 모드 + $20/month 강조 + fee 메타 + Fiscal.ai Max 블록($99 standalone 메타) + **FIG. 01 Operating Loop** (V3 이식)
3. **NO. 02 THE MISSING LAYER** — "The industry solved access. / It never solved judgment." + 3문단 + 9 IN 10 스탯(SPIVA 풀 소스) + READ THE MANIFESTO
4. **NO. 03 THE LOOP** — "Record. Benchmark. Review. Calibrate." + 3문단 + 4스텝 + 리드 + **스페시멘 카드 2** (Decision Record: Compounder/Core/12.2%/HURDLE 12%/확률 45·62·71/"Not yet written" + Investment Case v1→v3 히스토리) + FIG. 02 캡션
5. **NO. 04 THE DEFAULT** — "The default is the market. / Everything else is earned." + 스탯 3개 **+11 / +31 / −20**(−20 = `--c-urgent-muted`) + 리드 + BENCHMARK METHODOLOGY + FIG. 03 캡션
6. **NO. 05 THE STANDARD** — "The standard is high. / The door is open." + 2문단 + THE QUESTION 박스 + WHAT THIS ASKS(4) / NOT BUILT FOR(5) 리스트
7. **CLOSE** — "Nobody can buy a ten-year record. / It has to be kept." + 2문단 + **Archive Reel**(V3 이식) + $20 오퍼 + OPEN AN ACCOUNT/READ THE MANIFESTO + 트러스트 그리드(CIRO/CIPF/Custody/Orion NASDAQ&TSX: ORIO) + 푸트 라인

## 5. CSS 아키텍처 (4버전 공통)

- **토큰** (`:root`): 표준 `--c-*` + `--c-urgent-muted #BE3C36`, `--c-live-muted #288752`, `--c-review-muted #966E26`, `--c-research #3F6DA6`(시스템 유일 파랑, 루프 리서치 노드용) + `--frame 28px`, `--gap clamp(20px,2vw,40px)`
- **12컬럼 그리드**: `.wrap`(A) / `.data .wrap`+`.pic .in`(E) = `grid-template-columns:repeat(12,1fr); column-gap:var(--gap)`. 자식 기본 `grid-column:1/-1`, 헤드라인 `1/9`, 리드 `1/9`, qbox `1/8`. **내부 2/3/4컬럼 블록이 같은 `--gap`을 쓰면 마스터 컬럼선에 수학적으로 정렬됨** (실측 0px 편차 확인). 새 블록 추가 시 내부 grid gap은 반드시 `var(--gap)`.
- **A 전용**: `.band`(사진 밴드, min-height 92vh) + `.bars`/`.bar`(솔리드 블랙 바, clamp(26px,3.2vw,50px)) + `.slide`(텍스트-온-블랙, 아이브로우 = NO. 0X · 타이틀 + `//`)
- **E 전용**: `.pic`(풀이미지, `filter:grayscale(1) brightness(0.42) contrast(1.1)` — **그라데이션 금지, 하드 다크닝만**) + `.data`(크림 섹션)
- **CTA 규칙** (사이트 공통 확정): ALL-CAPS typed(절대 text-transform 금지) · IBM Plex Mono · 13px · tracking 0.077em · `↗`(arr-svg). primary=박스, secondary=텍스트 링크
- 스크롤 리빌 `.rv`/`.in` (IntersectionObserver), 숫자 카운트업 `.cnum`(data-pre/to/suf)
- 모바일: 880px 브레이크, 헤드라인 스팬 풀로

## 6. V3에서 이식된 제품 아티팩트 (코드 그대로 — **재구현 절대 금지**)

과거 루프를 재구현했다가 여러 번 깨진 이력 있음. 반드시 기존 코드 추출·이식만.

1. **Operating Loop** (`sysLoopCanvas` IIFE, V3 index.html의 `// entry-03 sys-loop - operating loop (v6...` 주석 블록) — 01 System의 `.loopfig` 크림 박스(v8 "boxed light figure") + 2단 레전드(Nodes/Status) + `FIG. 01 · Operating Loop` 노트. 캔버스는 `cv.parentElement` 기준이라 유동 박스 OK
2. **Archive Reel** (V3 `/* No.07 Archive Reel (M13 port)` IIFE) — Close의 `.reelfig`: 18플레이트 240ms 사이클 + 캔버스 스탬프(mix-blend-difference) + **레드 주차 숫자**(rgba(255,53,51) — 인코딩된 시그널, v8 승인 패턴). 셀렉터만 `.reelbox`로 변경됨. 이미지 = `Images/reel/reel-1..18.jpg`
3. **카운트업** — +11/+31/−20/9-in-10
4. **의도적 제외** (CEO 미니멀 지시): aperture 그래프(거부됨), 400u 블리드 숫자, fig-band 픽셀 시스템(`--u`), all-caps 이중웨이트 디스플레이 헤드라인. Constant 계단 포스터 = 소셜 에셋으로 보존(사이트 X)
5. **2차 후보 (미이식)**: V3 Benchmark 카드(bm-card) → 04 Default에 제품 아티팩트로 넣을 수 있음

## 7. 사진 배정 (`Images/flashcard1/` — 2026-07-20 추가된 45장, 콘텐츠 주제 매칭)

| 섹션 | 파일 | 이유 |
|---|---|---|
| Hero | `cyrus-gomez-pYdqyf4uMUA` | 도시 항공 B/W, 시장=거리 |
| 02 Missing Layer | `sebastian-schuster-z-GbfYI7CLI` | 군중 = "9 in 10" |
| 03 Loop | `ethan-rougon-QF-ILRbBfSM` | 노트+펜 = the record |
| 04 Default | `quan-you-zhang-dNle_4cOc38` | 마라톤 무리 = 같은 레이스(인덱스) |
| 05 Standard | `j-paulo-mag-QOmqwUBncQE` | 고독한 러너 = temperament |
| Close | `joachim-schnurle-jtQ5xJo3Ne8` | 아카이브 파일철 = ten-year record |

교체 시 콘택트 시트 재생성: 스크래치패드 `contact_sheet.py` 참조 (PIL로 45장 그리드 1장).

## 8. 검증 상태 & 알려진 함정

- 4버전 전부 `node .claude/scripts/validate-design.js` **0 errors / 0 warnings**
- 그리드 정렬 실측(1280px): copy/modes/tkts 2단→col7, steps 4단→col4, stats 3단→col5 전부 **0px 편차**
- E-grid 2000px 실측: 컨테이너 중앙(1680), def 515px, 버튼 허그, 스탯 3컬럼 — 정상
- ⚠️ **프리뷰 pane은 canvas rAF를 멈춤** → 루프/리얼 애니는 프리뷰에서 정지로 보임. 실브라우저에서 확인할 것. 스크린샷 도구도 캔버스 페이지에서 타임아웃 잦음 → **측정(getBoundingClientRect/getComputedStyle)으로 검증**
- ⚠️ **OneDrive**: 생성 직후 파일을 비우거나(dehydrate) 브라우저가 mid-write 캐시를 잡는 사고 여러 번. 이상하게 깨져 보이면 먼저 **Ctrl+F5** + 파일 크기 확인(`index-A/E*.html ≈ 48KB`). 파일 끝 `</html>` 확인
- 서버: `.claude/launch.json`의 `ii-landing` (python http.server 8123, `landing page` 디렉토리) → `localhost:8123/V5/...`

## 9. 구속 규칙 (요약 — 상세는 Doctrine/)

- **em-dash 금지** (영구), CTA ALL-CAPS typed / uppercase transform 금지, 색은 토큰만(hex는 :root)
- **측정 없이 치수 주장 금지** (measure rendered, never guess)
- 병렬 아이템 = 렌더 줄 수 동일
- Dave/CEO 카피 = canon, 수정 말고 플래그만
- 스코프: 요청된 것만, plan-first (단, 명시 요청은 재확인 없이 즉시)

## 9.5 이미지 스탠다드 — The Mann Standard (CEO 회의 2026-07-20 16:02, 확정)

CEO가 문서 2개로 웹사이트 이미지 독트린을 확정 (원본 PDF = `Marketing/references/The_Mann_Standard.pdf` + `Website_Image_Standard.pdf`, 녹취 = `바탕 화면/2026-07-20 16-02-02.txt`, Slack growth 채널에도 공유됨 — Tarsila 콘텐츠 소싱에도 적용):

**핵심**: Michael Mann 스쿨 (Heat·Collateral) — 실제 거리·실제 빛·일에 몰입한 프로페셔널, cool/composed 감정 온도. "판단은 조용히 찍힌다." 크래프트만 빌리고 내용(범죄/마초/아드레날린)은 안 가져옴.

- **B/W 축소, 컬러 기본** — "리얼리즘은 컬러 포함, B/W는 스타일라이즈드". 단 muted/desaturated/cool-documentary, 필름 그레인, earthy 팔레트. **골든 럭셔리 틴트 절대 금지**. B/W는 특정 목적 있을 때만.
- **서피스별**: 히로 = 와이드 건축적 다큐 프레임 + 타입 들어갈 딥 룸 (blue hour의 실물 경제: 항만·변전소·반도체 팹·다리·곡물 터미널·송전선, 또는 조용한 기관 인테리어: 리딩룸·긴 책상·아카이브. 한 피사체가 프레임 지배) / 제품 = 다큐 증거, 데모 아님 (실제 UI·실제 데이터·아티팩트처럼 프레임) / 에디토리얼 = 아이디어당 한 프레임 (공장·발전소·랩·데이터센터·인프라, 또는 마크업된 메모·데이트된 저널) / 사람 = 일에 몰입한 사람 (읽기·쓰기·리포트에 선 긋기·클러터드 책상, 자연광/창광, 포즈 금지) / 배경 = 재료(콘크리트·유리·강철·돌·종이·나무)와 빛.
- **스토리라인 프레임**: 밤 오피스(야근하는 집착), 지하철/트램(일 가는/오는 사람), 다운타운 코어, 산업 아티팩트(컨테이너·데이터센터 = 분석 대상 기업들).
- **금지**: 웃는 인물 라이프스타일, 트레이딩 플로어, 티커 월, 핀테크 그라데이션, 3D 렌더, 글로시 디바이스 목업, 손에 폰, 네온, HDR, "리테일 은행이 쓸 만한 것" 전부, 부·트로피·수익 스펙터클.
- **3 테스트**: become 테스트(갖고싶다 X, 되고싶다 O) / mute 테스트(음소거 시 광고인가 기관인가) / two-question 테스트(뭘 보고 있고 왜 여기 있나).
- **회의 개별 판정**: 현 히로(도시 항공) = **킵** ("Michael Mann 샷 같다", 컬러) / 마스크 쓴 여성 트램(judgement section2.png) = **거부** → 컬러 야간 트램(kevin-kruger)으로 교체됨 / B/W 고가철도(judgement section.png) → 컬러 등가물(michael-sala)로 교체됨.

**스톡 소싱 키워드 뱅크** (히로/에디토리얼용): `port blue hour`, `electrical substation dusk`, `semiconductor fab exterior`, `grain terminal`, `transmission lines overcast`, `container terminal night`, `data center exterior`, `bridge infrastructure documentary`, `reading room long desk window light`, `archive shelves interior`, `office at night workers windows`, `commuter train night`, `subway platform documentary`, `downtown core dusk`, `person reading report window light`, `hands writing desk`, `marked up documents desk`, `cluttered desk night work`, `factory floor documentary`, `power plant interior`. 필터 워드: muted, overcast, blue hour, 35mm, documentary, grain. 제외 워드: golden hour, neon, corporate smiling, startup office.

## 10. 다음 할 일 (미결 큐)

1. **A vs E vs 혼합 + 풀블리드 vs 컨테인드 결정** (인경) → 승자를 `index.html`로 승격, 탈락본 `_experiments/`
2. 히로 최종안 — 채택 컨셉 기준으로 미세조정 (CEO도 미결로 남김, 디자이너 재량)
3. Benchmark 카드 이식 여부 (04 Default)
4. 사진 파인튜닝 (교체/크롭/다크닝 정도), 모바일 QA
5. Mercer 아티클 포맷 → Manifesto/콘텐츠 페이지 적용 검토
6. 소셜 캐러셀/릴 템플릿 (Tarsila 실행용) — v8 포맷 기준, 사이트와 별개 트랙
