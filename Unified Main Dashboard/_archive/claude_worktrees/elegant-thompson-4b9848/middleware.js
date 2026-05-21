export const config = {
  matcher: ['/((?!_vercel|favicon.ico).*)'],
};

export default function middleware(request) {
  const auth = request.headers.get('authorization');
  const expected = process.env.SITE_PASSWORD;

  if (auth) {
    const [scheme, encoded] = auth.split(' ');
    if (scheme === 'Basic' && encoded) {
      const decoded = atob(encoded);
      const idx = decoded.indexOf(':');
      const pwd = idx >= 0 ? decoded.slice(idx + 1) : '';
      if (pwd === expected) {
        return;
      }
    }
  }

  return new Response('Authentication required', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="Protected"',
      'Content-Type': 'text/plain; charset=utf-8',
    },
  });
}
