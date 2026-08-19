# -*- coding: utf-8 -*-
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, '.')
from cssparse import strip_comments, parse, BASE

shared = io.open(os.path.join(BASE, '_shared', 'v11.css'), encoding='utf-8').read()

def nsel(s):
    return re.sub(r'\s+', '', s)

def selset(sel):
    return frozenset(x for x in nsel(sel).split(',') if x)

def declset(d):
    return frozenset(x for x in re.sub(r'\s+', '', d).rstrip(';').split(';') if x)

# A page rule is removable when, at the same media, some shared rule covers BOTH
# its selectors and its declarations. Subset, not string equality - the same rule
# is written with the selector list in a different order on different pages, and a
# page rule that carries an EXTRA declaration (Managed pinned min-height on the
# shared .hero .hgroup) must survive, not be silently swallowed with it.
SH = []       # [(media, selectorset, declset)] the shared file owns everywhere
SH_SUB = []   # + the un-prefixed sub-hero forms, valid ONLY on p-sub pages
for m, sel, d in parse(strip_comments(shared)):
    med = re.sub(r'\s+', '', (m or ''))
    SH.append((med, selset(sel), declset(d)))
    if 'body.p-sub' in sel:
        SH_SUB.append((med, selset(sel.replace('body.p-sub ', '')), declset(d)))
SH_SUB = SH_SUB + SH

def covered(keys, media, sel, decls):
    """True when the shared file already says everything this rule says. The shared
       declarations are unioned across every shared rule whose selector list covers
       this one - the same property set is often split over two rules there (footer
       gets its border colour in the hairline group and its padding in the footer
       group) and a page that writes them as one line is still fully covered."""
    ss, ds = selset(sel), declset(decls)
    if not ss:
        return False
    union = set()
    for md, s2, d2 in keys:
        if md == media and ss <= s2:
            union |= d2
    return bool(union) and ds <= union

def comment_mask(t):
    mask = bytearray(len(t))
    i = 0
    while True:
        a = t.find('/*', i)
        if a < 0:
            break
        b = t.find('*/', a + 2)
        if b < 0:
            b = len(t) - 2
        for k in range(a, min(b + 2, len(t))):
            mask[k] = 1
        i = b + 2
    return mask

def strip_block(block, media, KEYS):
    mask = comment_mask(block)
    spans = []
    i = 0
    n = len(block)
    while i < n:
        j = block.find('{', i)
        if j < 0:
            break
        if mask[j]:
            i = j + 1
            continue
        head = block[i:j]
        c2 = head.rfind('*/')
        cut = max(head.rfind('}'), (c2 + 1) if c2 >= 0 else -1, head.rfind(';'))
        start = i + cut + 1 if cut >= 0 else i
        sel = (head[cut + 1:] if cut >= 0 else head).strip()
        depth = 1
        k = j + 1
        while k < n and depth:
            if mask[k]:
                k += 1
                continue
            if block[k] == '{':
                depth += 1
            elif block[k] == '}':
                depth -= 1
            k += 1
        if sel.startswith('@'):
            i = j + 1
            continue
        if sel and covered(KEYS, media, sel, block[j + 1:k - 1]):
            spans.append((start, k))
        i = k
    for a, b in reversed(spans):
        block = block[:a] + block[b:]
    return block, len(spans)

def strip_nested(body, KEYS):
    """strip inside every nested @media (min-width:...) block, back to front so
       the offsets of the earlier ones stay valid. There is more than one."""
    mask = comment_mask(body)
    hits = [mm for mm in re.finditer(r'@media\s*\(\s*min-width\s*:\s*901px\s*\)\s*\{', body)
            if not mask[mm.start()]]
    total = 0
    for hit in reversed(hits):
        st = hit.end() - 1
        depth, k = 1, st + 1
        while k < len(body) and depth:
            if mask[k]:
                k += 1
                continue
            if body[k] == '{':
                depth += 1
            elif body[k] == '}':
                depth -= 1
            k += 1
        inner = body[st + 1:k - 1]
        ni, c = strip_block(inner, '@media(min-width:901px)', KEYS)
        total += c
        body = body[:st + 1] + ni + body[k - 1:]
        mask = comment_mask(body)
    return body, total


NOTE = (
    "\n/* ---------------------------------------------------------------------------\n"
    "   2026-08-19: every rule that belongs to more than one page was DELETED from this\n"
    "   block and now lives in _shared/v11.css, which loads after it. If a value you\n"
    "   expect is not here, it is there. Comments left behind describe decisions whose\n"
    "   rule moved - the reasoning is kept, the duplicate is not.\n"
    "   THIS BLOCK MAY ONLY CARRY #section-id RHYTHM AND DOCUMENTED PAGE EXCEPTIONS.\n"
    "   --------------------------------------------------------------------------- */\n")

PAGES = [('index.html', SH, [('v11-mobile', '@media(max-width:900px)'), ('v11-global', '')]),
         ('self-directed.html', SH_SUB, [('v11-mobile-sd', '@media(max-width:900px)'), ('v11-global-sd', '')]),
         ('managed.html', SH_SUB, [('v11-mobile-mg', '@media(max-width:900px)'), ('v11-global-mg', '')])]

def run():
  for fn, KEYS, bids in PAGES:
      p = os.path.join(BASE, fn)
      s = io.open(p, encoding='utf-8').read()
      tot = 0
      for bid, med in bids:
          m = re.search(r'(<style id="%s"[^>]*>)(.*?)(</style>)' % bid, s, re.S)
          if not m:
              continue
          body = m.group(2)
          body, n1 = strip_block(body, med, KEYS)
          body, n2 = strip_nested(body, KEYS)
          body = re.sub(r'\n{4,}', '\n\n\n', body)
          s = s[:m.start(2)] + NOTE + body + s[m.end(2):]
          tot += n1 + n2
      io.open(p, 'w', encoding='utf-8').write(s)
      print('%-20s removed %d duplicated rules' % (fn, tot))


if __name__ == '__main__':
    run()
