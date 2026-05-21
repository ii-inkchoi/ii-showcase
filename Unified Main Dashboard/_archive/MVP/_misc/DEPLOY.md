# 배포 가이드 (보안)

## 적용된 보안 조치

1. **Basic Auth gate** — `middleware.js` 가 모든 요청을 가로채서 사용자명/비밀번호 확인
2. **검색엔진 차단** — 모든 HTML 에 `<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">` + `Final/robots.txt`
3. **보안 헤더** — `vercel.json` 에 X-Frame-Options, X-Content-Type-Options 등
4. **HTTPS** — Vercel 기본 제공

## Vercel 배포 단계

1. **Vercel 프로젝트에 연결** (이미 되어있다면 건너뛰기):
   ```
   npx vercel
   ```

2. **환경 변수 설정** — Vercel Dashboard → Project → Settings → Environment Variables
   - `AUTH_USER` = 예: `preview` (또는 원하는 사용자명)
   - `AUTH_PASS` = 강력한 비밀번호 (예: 16자 이상 랜덤 문자열)

   **중요**: 비밀번호는 GitHub / Slack / 이메일 평문으로 공유하지 마세요. 1Password / Bitwarden 등 사용.

3. **배포 트리거**:
   ```
   git push
   ```
   또는 `npx vercel --prod`

4. **테스트**: 브라우저에서 배포 URL 접속 → 인증 팝업에 USER/PASS 입력

## 공유 방법

- URL: `https://your-project.vercel.app/Final/Unified_Dashboard_Gallery.html`
- 자격 증명은 URL 과 **별도 채널** 로 전달

## 비밀번호 변경

Vercel Dashboard 에서 `AUTH_PASS` 환경 변수 업데이트 → 재배포 자동 트리거됨.

## 프리뷰 해제

배포 중단하려면 Vercel Dashboard 에서 project pause 또는 delete. 또는 `AUTH_PASS` 를 지우면 모든 요청 500 에러 (완전 차단).
