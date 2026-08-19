# -*- coding: utf-8 -*-
"""Rebuild the three V11 pages from the pre-shared backup, deterministically.
   restore -> split MG hero exception -> link CSS -> link JS -> strip duplicates."""
import io, os, re, sys, shutil
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\p0107\OneDrive\바탕 화면\II Work\Product Design_work files\Prototype\landing page\V11_new"
BK = os.path.join(BASE, '_backups', 'pre-shared-20260819')
PAGES = ['index.html', 'self-directed.html', 'managed.html']

# ---------------------------------------------------------------- 0. restore
for f in PAGES:
    shutil.copyfile(os.path.join(BK, f), os.path.join(BASE, f))
print('restored 3 pages from pre-shared backup')

def rd(f): return io.open(os.path.join(BASE, f), encoding='utf-8').read()
def wr(f, s): io.open(os.path.join(BASE, f), 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- 1. MG hero exception
old = ".hero .hgroup{margin:32px 20px 32px;min-height:167px}"
new = """.hero .hgroup{margin:32px 20px 32px}

  /* PAGE EXCEPTION. The sub-page hero itself lives in _shared/v11.css; this is the one
     Managed-only value on top of it. Managed's title block is shorter than Self-Directed's,
     so the band divider landed at a different height. 167 pins the group so the divider sits
     at 231 and the video keeps the same 71.6% ratio as Self-Directed - the two product pages
     have to agree at the fold. */
  .hero .hgroup{min-height:167px}"""
s = rd('managed.html')
assert s.count(old) == 1, 'MG hero anchor'
wr('managed.html', s.replace(old, new))
print('managed: hero pin split into a documented page exception')

# ---------------------------------------------------------------- 1b. home: name the page type
# The home hero is its own grammar (full-viewport video, title laid over it) and must not
# inherit the sub-page hero from the shared layer. Naming it body.p-home makes that explicit
# instead of "the page that happens to have no class", and lets check-v11.py tell a real
# page exception apart from a component rule that leaked back into a page.
s = rd('index.html')
assert s.count('\n<body>') == 1, 'home body'
s = s.replace('\n<body>', '\n<body class="p-home">', 1)

HERO_SELS = ['.hero', '.hero>video,.hero>img', '.hero>video', '.hero>.heyeb',
             '.hero .heyeb .hlogo', '.hero .hgroup', '.hero .hgroup .hbars', '.hero .hbar',
             '.hero::after', '.v11-hero2', '.v11-hero2 .v11-wrap', '.v11-hero2 .hsub',
             '.v11-hero2 .ctarow', '.v11-hero2 .mlink', '.v11-hero2 .htrust',
             '.v11-hero2 .htrust .heyeb-sep', '.v11-hero2 .htrust .heyeb-b',
             '.v11-hero2 .htrust>span']
# ONLY inside the v11 blocks. The base sheets are the page as it was; raising the
# specificity of rules there would change a cascade nobody asked to change.
n = 0
for bid in ['v11-mobile', 'v11-global']:
    m = re.search(r'(<style id="%s"[^>]*>)(.*?)(</style>)' % bid, s, re.S)
    assert m, bid
    body = m.group(2)
    for sel in HERO_SELS:
        # followed by { OR , - the 22-tier rule lists .v11-hero2 .hsub as the first of
        # eight selectors spread over several lines, and leaving that one unprefixed
        # left it a step below the standalone rule, which then won: the hero descriptor
        # came back as 22/500/1.15 instead of 22/400/1.25.
        pat = re.compile(r'(?<![\w.>,\-])' + re.escape(sel) + r'(?=\s*[\{,])')
        body, c = pat.subn('body.p-home ' + sel, body)
        n += c
    # A selector list is visited once per entry, so a list like `.hero>video,.hero>img`
    # is prefixed as a whole and then `.hero>video` matches again inside it. The result,
    # `body.p-home body.p-home .hero>video`, asks for a body inside a body and matches
    # nothing - the hero video silently lost its one-viewport height. Collapse them.
    while 'body.p-home body.p-home ' in body:
        body = body.replace('body.p-home body.p-home ', 'body.p-home ')
        n -= 1
    s = s[:m.start(2)] + body + s[m.end(2):]
# .tri .cell belongs to the shared layer - drop it from the home's local hairline list
old_tri = '.gap2 .g2stat .rule,.def4 .dstats .cell,.dstats .cell,.tri .cell,.stats3 .cell'
new_tri = '.gap2 .g2stat .rule,.def4 .dstats .cell,.dstats .cell,.stats3 .cell'
assert s.count(old_tri) == 1, 'home tri list'
s = s.replace(old_tri, new_tri)
wr('index.html', s)
print('home: p-home named, %d hero rules scoped to it, .tri .cell handed to the shared layer' % n)

# ---------------------------------------------------------------- 2. link the CSS
LINK = ('\n<!-- THE SHARED LAYER. Loads last so it wins on source order at equal specificity.\n'
        '     Every rule that must be identical on every V11 page lives in this one file -\n'
        '     component sizes, weights, leading, and border treatment. Do not copy it into a\n'
        '     page; a page block may only carry #section-id rhythm and documented exceptions.\n'
        '     Verify with:  python _shared/check-v11.py                See _shared/v11.css -->\n'
        '<link rel="stylesheet" href="_shared/v11.css">\n')
for fn, lastblock, cls in [('index.html', 'v11-global', None),
                           ('self-directed.html', 'v11-global-sd', 'p-sub'),
                           ('managed.html', 'v11-global-mg', 'p-sub')]:
    s = rd(fn)
    i = s.find('<style id="%s"' % lastblock); assert i > 0, fn
    j = s.find('</style>', i) + len('</style>')
    s = s[:j] + LINK + s[j:]
    if cls:
        assert s.count('\n<body>') == 1, fn
        s = s.replace('\n<body>', '\n<body class="%s">' % cls, 1)
    wr(fn, s)
print('linked _shared/v11.css on 3 pages; p-sub set on the two sub pages')

# ---------------------------------------------------------------- 3. link the JS
TAG = ('\n<!-- THE SHARED SCRIPT LAYER. Replaces the four inline blocks v11-hero2 / v11-footer /\n'
       '     v11-trust / v11-reveal, which were byte-identical across the sub pages. No defer:\n'
       '     it must run at exactly the position those blocks did. See _shared/v11-sub.js. -->\n'
       '<script src="_shared/v11-sub.js"></script>\n')
for fn in ['self-directed.html', 'managed.html']:
    s = rd(fn)
    spans = []
    for sid in ['v11-hero2', 'v11-footer', 'v11-trust', 'v11-reveal']:
        m = re.search(r'\n?<script id="%s"[^>]*>.*?</script>\n?' % sid, s, re.S)
        assert m, fn + ' ' + sid
        spans.append((m.start(), m.end()))
    spans.sort()
    first = spans[0][0]
    for a, b in reversed(spans):
        s = s[:a] + s[b:]
    wr(fn, s[:first] + TAG + s[first:])
print('sub pages: 4 inline scripts -> 1 shared tag')

# ---------------------------------------------------------------- 4. strip duplicates
import strip
strip.run()
