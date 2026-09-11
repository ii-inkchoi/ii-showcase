"""Bake the Orion IR page into ONE self-contained .html for review.

Why: the Browser pane clips screenshots at its physical size, so a 1440-wide layout
cannot be captured there. A single self-contained file opens at full window width on
a double click, with no relative paths to break.

The hero JPEG is 8272px wide / 4.6MB. At a 1440 hero it renders into ~1666px, so the
original is ~5x more pixels than any reviewer will see and base64 costs a further 37%.
It is downscaled to 2880 wide (2x for retina) for the review file only. The source
image in the project folder is not touched.
"""
import base64, io, os, re, sys
from PIL import Image

# Defaults so a review build lands in the repo, not in a session temp folder.
#   python "_pending/bake_orion.py"                 -> _pending/review/latest.html
#   python "_pending/bake_orion.py" SRC OUT         -> explicit
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)  # the version folder
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'latest.html')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
HERO_W = 2880
JPEG_Q = 82

html = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()


def unq(p):
    return p.replace('%20', ' ').split('?')[0].split('#')[0]


def inline_css(m):
    href = unq(m.group(1))
    path = os.path.normpath(os.path.join(SRC, href))
    if not os.path.isfile(path):
        print('  MISSING css:', href)
        return m.group(0)
    css = open(path, encoding='utf-8').read()
    print(f'  css  {href}  {len(css):,}b')
    return f'<style data-from="{href}">\n{css}\n</style>'


def inline_js(m):
    src = unq(m.group(1))
    path = os.path.normpath(os.path.join(SRC, src))
    if not os.path.isfile(path):
        print('  MISSING js:', src)
        return m.group(0)
    js = open(path, encoding='utf-8').read()
    print(f'  js   {src}  {len(js):,}b')
    return f'<script data-from="{src}">\n{js}\n</script>'


_imgcache = {}


def inline_img(m):
    src = unq(m.group(1))
    if src in _imgcache:
        return m.group(0).replace(m.group(1), _imgcache[src])
    path = os.path.normpath(os.path.join(SRC, src))
    if not os.path.isfile(path):
        print('  MISSING img:', src)
        return m.group(0)
    if path.lower().endswith('.svg'):
        b = open(path, 'rb').read()
        uri = 'data:image/svg+xml;base64,' + base64.b64encode(b).decode()
        print(f'  svg  {src}  {os.path.getsize(path):,}b')
        _imgcache[src] = uri
        return m.group(0).replace(m.group(1), uri)
    im = Image.open(path)
    ow, oh = im.size
    has_alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
    if has_alpha:
        # PNG, alpha kept. Converting straight to RGB (the JPEG path below) drops
        # transparency and bakes whatever colour sits under it, which turned the logo
        # marks into solid black boxes on this review copy the first time.
        im = im.convert('RGBA')
        if ow > HERO_W:
            im = im.resize((HERO_W, round(oh * HERO_W / ow)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'PNG', optimize=True)
        b = buf.getvalue()
        print(f'  png  {src}  {ow}x{oh} {os.path.getsize(path):,}b -> {im.size[0]}x{im.size[1]} {len(b):,}b')
        uri = 'data:image/png;base64,' + base64.b64encode(b).decode()
        _imgcache[src] = uri
        return m.group(0).replace(m.group(1), uri)
    if ow > HERO_W:
        im = im.convert('RGB').resize((HERO_W, round(oh * HERO_W / ow)), Image.LANCZOS)
    buf = io.BytesIO()
    im.convert('RGB').save(buf, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
    b = buf.getvalue()
    print(f'  img  {src}  {ow}x{oh} {os.path.getsize(path):,}b -> {im.size[0]}x{im.size[1]} {len(b):,}b')
    uri = 'data:image/jpeg;base64,' + base64.b64encode(b).decode()
    _imgcache[src] = uri
    return m.group(0).replace(m.group(1), uri)


print('baking', SRC)
html = re.sub(r'<link[^>]+rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>',
              lambda m: m.group(0) if m.group(1).startswith('http') else inline_css(m), html)
html = re.sub(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*>',
              lambda m: m.group(0) if m.group(1).startswith('http') else inline_css(m), html)
html = re.sub(r'<script[^>]+src=["\']([^"\']+)["\'][^>]*>\s*</script>',
              lambda m: m.group(0) if m.group(1).startswith('http') else inline_js(m), html)
html = re.sub(r'<img[^>]+src=["\']([^"\']+)["\']',
              lambda m: m.group(0) if m.group(1).startswith(('http', 'data:')) else inline_img(m), html)

# defuse stub links so a click does nothing instead of a 404
html = re.sub(r'href=["\'](?!#|http|mailto)[^"\']*\.html["\']', 'href="#"', html)

# review banner: this is a work-in-progress with unconfirmed numbers
banner = '''<style>
#revbar{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#1C1C1C;color:#C7C7C7;
font:400 11px/1.5 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:0.04em;
padding:10px 20px;border-top:0.667px solid #565B5E;display:flex;gap:24px;flex-wrap:wrap}
#revbar b{color:#FFF;font-weight:400}
#revbar .u{border-bottom:1px dashed #C29A2A;padding-bottom:1px}
</style>
<div id="revbar">
<span><b>V2</b> · photographic ground, elements composed on it, some sections carry an image and some do not</span>
<span>Resize below 900px for mobile</span>
<span><span class="u">Dashed underline</span> = number not yet confirmed</span>
<span>Photography is a stand-in. V1 is untouched next door</span>
</div>'''
html = html.replace('</body>', banner + '\n</body>')

# REVIEW_HIDE_UNC: the shared file hides the unconfirmed-value markers
html = html.replace('</head>', '<style>.unc{border-bottom:0!important;text-decoration:none!important;background:none!important}.unc.draft{display:none!important}</style></head>', 1)
open(OUT, 'w', encoding='utf-8').write(html)
print(f'wrote {OUT}  {os.path.getsize(OUT):,}b')
