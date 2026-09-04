"""Bake each page into ONE self-contained .html file.

The reviewer is not technical, and the files get dropped into Claude, where size is a hard limit.
That rules out a folder of files on relative paths: they will email a single .html or drag it to
the desktop, and every image will vanish. So the stylesheet, the scripts, the images AND the video
go INSIDE the file as data URIs. Each file opens on its own with a double click.

Video is re-encoded harder than the folder build - 960 wide, CRF 34, no audio - because base64
costs a further 37% and this is where the file size is won or lost. The MOBILE variant (data-m) is
dropped: mobile is not part of this review and it would double the video weight. Two of the home
hero clips carry no poster (they are slides 2 and 3 of the rotator), so a frame is pulled from the
clip itself and nothing is blank while the video loads.

Links to pages outside the review are defused to "#" so a click does nothing instead of opening a
browser error page - in the HTML and in the JavaScript that builds the nav.
"""
import base64, io, mimetypes, os, re, subprocess, sys, tempfile

SRC = sys.argv[1]
OUT = sys.argv[2]

PAGES = [
    ('index.html',          '1 - Home.html'),
    ('self-directed.html',  '2 - Self-Directed.html'),
    ('managed.html',        '3 - Managed.html'),
]
KEEP = {a: b for a, b in PAGES}

mimetypes.add_type('image/svg+xml', '.svg')
TMP = tempfile.mkdtemp(prefix='iishare_')
Q = '["\']'
ASSET_EXT = r'(?:svg|png|jpe?g|webp|gif|woff2?|ico)'


def unquote(p):
    return p.replace('%20', ' ').split('?')[0].split('#')[0]


def datauri(rel, cache={}):
    rel = unquote(rel)
    if rel in cache:
        return cache[rel]
    full = os.path.normpath(os.path.join(SRC, rel))
    if not os.path.isfile(full):
        return None
    mime = mimetypes.guess_type(full)[0] or 'application/octet-stream'
    with open(full, 'rb') as f:
        uri = 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode('ascii'))
    cache[rel] = uri
    return uri


def _ff(args, out):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + args, capture_output=True)
    if not os.path.isfile(out) or os.path.getsize(out) == 0:
        return False
    # ffprobe every output: an ffmpeg run segfaulted during an earlier build and left a file with
    # no moov atom, which plays nowhere and looks like a broken page
    p = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', out], capture_output=True, text=True)
    return p.returncode == 0 and bool(p.stdout.strip())


def video_uri(rel, cache={}):
    rel = unquote(rel)
    if rel in cache:
        return cache[rel]
    full = os.path.normpath(os.path.join(SRC, rel))
    if not os.path.isfile(full):
        return None
    tmp = os.path.join(TMP, re.sub(r'[^A-Za-z0-9]+', '_', rel) + '.mp4')
    ok = _ff(['-i', full, '-vf', 'scale=960:-2', '-c:v', 'libx264', '-preset', 'medium',
              '-crf', '34', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', tmp], tmp)
    if not ok:
        return None
    with open(tmp, 'rb') as f:
        cache[rel] = 'data:video/mp4;base64,' + base64.b64encode(f.read()).decode('ascii')
    return cache[rel]


def frame_uri(rel, cache={}):
    """A poster for a <video> that has none: its own first frame."""
    rel = unquote(rel)
    if rel in cache:
        return cache[rel]
    full = os.path.normpath(os.path.join(SRC, rel))
    if not os.path.isfile(full):
        return None
    tmp = os.path.join(TMP, re.sub(r'[^A-Za-z0-9]+', '_', rel) + '.jpg')
    if not _ff(['-i', full, '-frames:v', '1', '-vf', 'scale=1280:-2', '-q:v', '6', tmp], tmp):
        return None
    with open(tmp, 'rb') as f:
        cache[rel] = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('ascii')
    return cache[rel]


def inline_css(css_text, css_dir):
    """url(...) inside a stylesheet resolves against the stylesheet, not the page."""
    def rep(m):
        raw = m.group(1).strip('\'"')
        if re.match(r'^(data:|https?:|//)', raw):
            return m.group(0)
        rel = os.path.relpath(os.path.normpath(os.path.join(css_dir, unquote(raw))), SRC)
        uri = datauri(rel.replace(os.sep, '/'))
        return 'url("%s")' % uri if uri else m.group(0)
    return re.sub(r'url\(\s*([^)]+?)\s*\)', rep, css_text)


def build(src_name, out_name):
    html = io.open(os.path.join(SRC, src_name), encoding='utf-8').read()
    rep = {'css': 0, 'js': 0, 'img': 0, 'video': 0, 'frames': 0, 'embedded': 0,
           'strings': 0, 'defused': 0, 'missing': []}

    def css_rep(m):
        href = unquote(m.group(1))
        if re.match(r'^(https?:|//)', href):
            return m.group(0)                     # Google Fonts stays a link
        full = os.path.normpath(os.path.join(SRC, href))
        if not os.path.isfile(full):
            rep['missing'].append(href)
            return m.group(0)
        rep['css'] += 1
        return '<style>/* inlined from %s */\n%s</style>' % (
            href, inline_css(io.open(full, encoding='utf-8').read(), os.path.dirname(full)))
    html = re.sub(r'<link[^>]+rel=' + Q + r'stylesheet' + Q + r'[^>]*href=' + Q +
                  r'([^"\']+)' + Q + r'[^>]*>', css_rep, html)
    html = re.sub(r'<link[^>]+href=' + Q + r'([^"\']+)' + Q + r'[^>]*rel=' + Q +
                  r'stylesheet' + Q + r'[^>]*>', css_rep, html)

    def js_rep(m):
        src = unquote(m.group(1))
        if re.match(r'^(https?:|//)', src):
            return m.group(0)
        full = os.path.normpath(os.path.join(SRC, src))
        if not os.path.isfile(full):
            rep['missing'].append(src)
            return m.group(0)
        rep['js'] += 1
        return '<script>/* inlined from %s */\n%s</script>' % (
            src, io.open(full, encoding='utf-8').read())
    html = re.sub(r'<script[^>]*\ssrc=' + Q + r'([^"\']+)' + Q + r'[^>]*>\s*</script>',
                  js_rep, html)

    def vid_rep(m):
        tag = m.group(0)
        pm = re.search(r'poster=' + Q + r'([^"\']+)' + Q, tag)
        sm = re.search(r'\ssrc=' + Q + r'([^"\']+)' + Q, tag)
        if pm:
            uri = datauri(pm.group(1))
            if uri:
                tag = tag[:pm.start(1)] + uri + tag[pm.end(1):]
        elif sm:
            uri = frame_uri(sm.group(1))
            if uri:
                tag = tag[:-1] + ' poster="%s">' % uri
                rep['frames'] += 1
        sm = re.search(r'\ssrc=' + Q + r'([^"\']+)' + Q, tag)   # re-find, the tag moved
        if sm:
            uri = video_uri(sm.group(1))
            if uri:
                tag = tag[:sm.start(1)] + uri + tag[sm.end(1):]
                rep['embedded'] += 1
            else:
                rep['missing'].append(sm.group(1) + ' (video re-encode failed)')
        tag = re.sub(r'\sdata-m=' + Q + r'[^"\']*' + Q, '', tag)
        rep['video'] += 1
        return tag
    html = re.sub(r'<video\b[^>]*>', vid_rep, html)

    def attr_rep(m):
        attr, raw = m.group(1), m.group(2)
        if re.match(r'^(data:|https?:|//|#)', raw):
            return m.group(0)
        uri = datauri(raw)
        if not uri:
            rep['missing'].append(raw)
            return m.group(0)
        rep['img'] += 1
        return '%s="%s"' % (attr, uri)
    html = re.sub(r'\b(src|poster)=' + Q + r'([^"\']+)' + Q, attr_rep, html)

    def url_rep(m):
        raw = m.group(1).strip('\'"')
        if re.match(r'^(data:|https?:|//)', raw):
            return m.group(0)
        uri = datauri(raw)
        if not uri:
            return m.group(0)
        rep['img'] += 1
        return 'url("%s")' % uri
    html = re.sub(r'url\(\s*([^)]+?)\s*\)', url_rep, html)

    def href_rep(m):
        raw = m.group(1)
        if re.match(r'^(https?:|//|mailto:|tel:|#)', raw):
            return m.group(0)
        base, _, frag = raw.partition('#')
        base = unquote(base)
        if base in KEEP:
            return 'href="%s%s"' % (KEEP[base].replace(' ', '%20'), ('#' + frag) if frag else '')
        if base.endswith('.html'):
            rep['defused'] += 1
            return 'href="#"'
        return m.group(0)
    html = re.sub(r'href=' + Q + r'([^"\']+)' + Q, href_rep, html)

    # paths that live inside JavaScript strings rather than HTML attributes - the nav logo and the
    # newsroom links are built by script, so the passes above never saw them
    def str_asset(m):
        q, raw = m.group(1), m.group(2)
        if re.match(r'^(data:|https?:|//)', raw):
            return m.group(0)
        uri = datauri(raw)
        if not uri:
            return m.group(0)
        rep['strings'] += 1
        return q + uri + q
    html = re.sub(r'(["\'])([^"\'<>]+\.' + ASSET_EXT + r')\1', str_asset, html, flags=re.I)

    def str_page(m):
        q, raw = m.group(1), m.group(2)
        base = unquote(raw.split('#')[0])
        frag = raw.split('#')[1] if '#' in raw else ''
        if base in KEEP:
            return q + KEEP[base].replace(' ', '%20') + (('#' + frag) if frag else '') + q
        rep['defused'] += 1
        return q + '#' + q
    html = re.sub(r'(["\'])([A-Za-z0-9._-]+\.html(?:#[A-Za-z0-9_-]+)?)\1', str_page, html)

    io.open(os.path.join(OUT, out_name), 'w', encoding='utf-8').write(html)
    size = os.path.getsize(os.path.join(OUT, out_name))
    print('%-24s %5.1f MB   css %d  js %d  img %d(+%d js)  video %d/%d  poster-cut %d  defused %d'
          % (out_name, size / 1048576.0, rep['css'], rep['js'], rep['img'],
             rep['strings'], rep['embedded'], rep['video'], rep['frames'], rep['defused']))
    if rep['missing']:
        print('   MISSING: ' + ', '.join(sorted(set(rep['missing']))))


if not os.path.isdir(OUT):
    os.makedirs(OUT)
for a, b in PAGES:
    build(a, b)
