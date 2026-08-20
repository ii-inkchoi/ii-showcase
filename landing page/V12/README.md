# II 랜딩 V12 — 배포본

`V12/` 작업본에서 **GitHub Pages 용으로 이름만 정리한 사본**이다. 디자인/코드는 동일.

## 작업본과 다른 점 (이게 전부)

| 작업본 `V12/` | 배포본 `V12_github/` | 이유 |
|---|---|---|
| `Images/v5 images/` | `Images/v5-images/` | 이름의 공백 제거 |
| `.../video desktop/` `.../video mobile/` | `video-desktop/` `video-mobile/` | 〃 |
| `judgement section.png` | `judgement-section.png` | 〃 |
| `II word logo.svg` | `II-word-logo.svg` | 〃 |
| `_archive/`, `START-HERE-V12.md` 등 문서 | 제외 | 배포 대상 아님 |

공유 폴더는 이미 `shared/` (밑줄 없음) 라 그대로 복사했다.

## 올릴 때 주의

1. **밑줄로 시작하는 폴더·파일은 GitHub Pages 가 배포에서 뺀다.** 이 폴더에는 없다 (확인 완료). 새로 추가할 때도 밑줄 금지.
2. **이름에 공백 금지.** 공백이 있으면 경로가 `%20` 으로 인코딩되면서 일부 환경에서 깨진다.
3. 용량 **83MB**, 그중 동영상 12개가 대부분이다. 한 번 올리면 git 히스토리에 영구히 남는다.

## 검증 결과 (2026-08-20)

- 참조 자산 131개 → **없는 파일 0, 공백 이름 0**
- 9 페이지 브라우저 로드 → **404 · 빈 이미지 · 영상 오류 · 가로 스크롤 전부 0**
- 공유 CSS 9 페이지 모두 적용 확인

## 페이지

`index` · `self-directed` · `managed` · `pricing` · `manifesto` · `newsroom` · `press-release` · `changelog-entry` · `get-the-app`
