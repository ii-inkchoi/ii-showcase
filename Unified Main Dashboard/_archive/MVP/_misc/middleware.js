// Vercel Edge Middleware — Basic Auth gate.
// Set env vars AUTH_USER and AUTH_PASS in Vercel project settings.
// All requests require Basic Auth except /robots.txt and /favicon.ico.

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon\\.ico|robots\\.txt).*)'],
};

export default function middleware(req) {
  const USER = process.env.AUTH_USER || 'preview';
  const PASS = process.env.AUTH_PASS;

  if (!PASS) {
    return new Response('Auth not configured. Set AUTH_PASS in Vercel env vars.', { status: 500 });
  }

  const auth = req.headers.get('authorization');
  if (auth) {
    const [scheme, encoded] = auth.split(' ');
    if (scheme === 'Basic' && encoded) {
      try {
        const decoded = atob(encoded);
        const idx = decoded.indexOf(':');
        const u = decoded.slice(0, idx);
        const p = decoded.slice(idx + 1);
        if (u === USER && p === PASS) return;
      } catch (_) { /* fall through */ }
    }
  }

  return new Response('Authentication required', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="Preview"',
      'Content-Type': 'text/plain',
    },
  });
}
