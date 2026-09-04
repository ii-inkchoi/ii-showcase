"""Build a shareable copy of the three content pages.

Assets are found by SCANNING the HTML, never by hand: a hand-written list missed six mobile videos
and five newsroom images last time. Anything referenced by src / poster / data-m / href / url() or
as a quoted path inside a <script> gets picked up.

Images: long edge 1600, JPEG q78 (opaque sources only; anything with alpha stays PNG).
Videos: 1280 wide (mobile encodes 960), CRF 30, no audio, +faststart.
Every ffmpeg output is ffprobed - one run segfaulted last time and left a file with no moov atom.
"""
import io, os, re, shutil, subprocess, sys

SRC = sys.argv[1]
OUT = sys.argv[2]
PAGES = ['index.html', 'managed.html', 'self-directed.html']

REFS = re.compile(
    r'(?:src|poster|data-m|href)\s*=\s*["\']([^"\']+)["\']'
    r'|url\(\s*["\']?([^"\')]+)["\']?\s*\)'
    r'|["\']((?:\.\./)*(?:Images|assets|shared|changelog[ %20]images)/[^"\']+)["\']',
    re.I)

SKIP = re.compile(r'^(https?:|//|data:|mailto:|tel:|#)', re.I)
IMG = ('.png', '.jpg', '.jpeg', '.webp')
VID = ('.mp4', '.webm', '.mov')


def unquote(p):
    return re.sub(r'%20', ' ', p).split('?')[0].split('#')[0]


def collect(path, seen, queue):
    try:
        txt = io.open(path, encoding='utf-8', errors='ignore').read()
    except Exception:
        return
    for m in REFS.finditer(txt):
        raw = m.group(1) or m.group(2) or m.group(3)
        if not raw or SKIP.match(raw):
            continue
        rel = unquote(raw.strip())
        if rel in seen:
            continue
        full = os.path.normpath(os.path.join(SRC, rel))
        if not os.path.isfile(full):
            continue
        seen.add(rel)
        if rel.lower().endswith(('.css', '.js')):
            queue.append(full)


def main():
    seen, queue = set(), []
    for p in PAGES:
        collect(os.path.join(SRC, p), seen, queue)
    while queue:                       # css/js reference more assets
        collect(queue.pop(), seen, queue)

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for p in PAGES:
        shutil.copy2(os.path.join(SRC, p), os.path.join(OUT, p))

    from PIL import Image
    stats = {'img': [0, 0, 0], 'vid': [0, 0, 0], 'copy': [0, 0], 'fail': []}

    for rel in sorted(seen):
        s = os.path.join(SRC, rel)
        d = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        sz = os.path.getsize(s)
        low = rel.lower()

        if low.endswith(IMG):
            try:
                im = Image.open(s)
                opaque = im.mode in ('RGB', 'L') or (
                    im.mode in ('RGBA', 'LA', 'P') and
                    (im.convert('RGBA').getchannel('A').getextrema()[0] == 255))
                w, h = im.size
                if max(w, h) > 1600:
                    r = 1600.0 / max(w, h)
                    im = im.resize((max(1, int(w * r)), max(1, int(h * r))), Image.LANCZOS)
                if opaque:
                    im.convert('RGB').save(d, 'JPEG', quality=78, optimize=True,
                                           progressive=True)
                else:
                    im.save(d)
                stats['img'][0] += 1
                stats['img'][1] += sz
                stats['img'][2] += os.path.getsize(d)
                continue
            except Exception as e:
                stats['fail'].append(rel + ' (image: %s)' % e)
                shutil.copy2(s, d)
                continue

        if low.endswith(VID):
            width = 960 if ('/video mobile/' in low or low.endswith('-m.mp4')) else 1280
            cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', s,
                   '-vf', 'scale=%d:-2' % width, '-c:v', 'libx264', '-preset', 'medium',
                   '-crf', '30', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', d]
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                probe = subprocess.run(
                    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                     '-of', 'csv=p=0', d], capture_output=True, text=True)
                if probe.returncode != 0 or not probe.stdout.strip():
                    raise RuntimeError('ffprobe rejected the output (no moov atom?)')
                stats['vid'][0] += 1
                stats['vid'][1] += sz
                stats['vid'][2] += os.path.getsize(d)
                continue
            except Exception as e:
                stats['fail'].append(rel + ' (video: %s)' % e)
                shutil.copy2(s, d)
                continue

        shutil.copy2(s, d)
        stats['copy'][0] += 1
        stats['copy'][1] += sz

    mb = lambda n: '%.1fMB' % (n / 1048576.0)
    print('pages    %d' % len(PAGES))
    print('images   %d   %s -> %s' % (stats['img'][0], mb(stats['img'][1]), mb(stats['img'][2])))
    print('videos   %d   %s -> %s' % (stats['vid'][0], mb(stats['vid'][1]), mb(stats['vid'][2])))
    print('verbatim %d   %s  (css / js / svg / fonts)' % (stats['copy'][0], mb(stats['copy'][1])))
    total = sum(os.path.getsize(os.path.join(r, f))
                for r, _, fs in os.walk(OUT) for f in fs)
    print('FOLDER   %s' % mb(total))
    if stats['fail']:
        print('\nFAILED (copied verbatim instead):')
        for f in stats['fail']:
            print('  ' + f)


main()
