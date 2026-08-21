# II 랜딩 V12 — 배포본 (2026-08-20)

`V12/` 작업본에서 GitHub Pages 용으로 이름만 정리한 사본. 디자인·코드·카피 동일.

## 페이지 12장

홈 `index` · `self-directed` · `managed` · `pricing` · `manifesto` · `newsroom` · `press-release` · `get-the-app`
+ 체인지로그 상세 4장: `changelog-2026-08-17` / `-07-27` / `-07-17` / `-06-15`

(작업본의 `changelog-entry.html` 은 다음 달용 빈 뼈대라 배포에서 제외)

## 작업본과 다른 점 (이름 정리뿐)

| 작업본 | 배포본 |
|---|---|
| `Images/v5 images/` (+ video 하위 2개) | `Images/v5-images/` (`video-desktop` `video-mobile`) |
| `judgement section.png` | `judgement-section.png` |
| `II word logo.svg` | `II-word-logo.svg` |

이유: GitHub Pages 는 밑줄로 시작하는 이름을 배포에서 빼고, 공백 이름은 환경에 따라 깨진다.

## 올릴 때

1. 이 폴더 **내용물**을 리포의 원하는 위치에 그대로 복사
2. 새 파일 추가 시 이름에 공백·앞 밑줄 금지
3. 용량 83MB (동영상 12개 = 49MB). git 은 한 번 올린 파일이 히스토리에 영구히 남는다

## 검증 (2026-08-20)

- 참조 자산 180개 → 없는 파일 0 · 공백 0 · 밑줄 0
- 12장 브라우저 로드 → 404 · 빈 이미지 · 가로 스크롤 0
- 로고·글 시작선·글자 사다리 전 페이지 통일

## 알려진 대기 항목 (디자인 아님)

- 이미지 13곳 = 자리표시자 (인경이 교체 예정)
- `[Legal Entity Name]` = 법무 확정 대기
- 두 번째 프레스 릴리즈 · In the Press 커버리지 = 콘텐츠 대기
- Managed 수치 `[TBD]` = 데이터 대기
