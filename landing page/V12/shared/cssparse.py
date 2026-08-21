# -*- coding: utf-8 -*-
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\p0107\OneDrive\바탕 화면\II Work\Product Design_work files\Prototype\landing page\V11_new"

def strip_comments(s):
    out=[];i=0
    while True:
        j=s.find('/*',i)
        if j<0: out.append(s[i:]);break
        out.append(s[i:j]); k=s.find('*/',j+2)
        if k<0: break
        i=k+2
    return ''.join(out)

def parse(css, media=None, out=None):
    """returns list of (media, selector, decls) in source order"""
    if out is None: out=[]
    i=0; n=len(css)
    while i<n:
        # find next '{' or end
        j=css.find('{', i)
        if j<0: break
        head=css[i:j].strip()
        # match brace
        depth=1; k=j+1
        while k<n and depth:
            if css[k]=='{': depth+=1
            elif css[k]=='}': depth-=1
            k+=1
        body=css[j+1:k-1]
        if head.startswith('@'):
            if head.startswith('@media') or head.startswith('@supports'):
                m = (media+' AND '+head) if media else head
                parse(body, m, out)
            else:
                out.append((media, head, ' '.join(body.split())))
        else:
            sel=' '.join(head.split())
            if sel: out.append((media, sel, ' '.join(body.split())))
        i=k
    return out

def blocks(fn):
    s=io.open(os.path.join(BASE,fn),encoding='utf-8').read()
    res=[]
    for m in re.finditer(r'<style id="([^"]+)"[^>]*>(.*?)</style>', s, re.S):
        res.append((m.group(1), m.group(2)))
    return res

PAGES=['index.html','self-directed.html','managed.html']
TAG={'index.html':'HOME','self-directed.html':'SD','managed.html':'MG'}
ALL={}
for f in PAGES:
    rules=[]
    for bid, css in blocks(f):
        if not bid.startswith('v11'): continue
        for r in parse(strip_comments(css)):
            rules.append((bid,)+r)
    ALL[TAG[f]]=rules
    print('%-5s v11 rules: %d' % (TAG[f], len(rules)))
import pickle
pickle.dump(ALL, open('rules.pkl','wb'))
print()
for t,rs in ALL.items():
    pg=[r for r in rs if '#' in r[2]]
    print('%-5s  #id-scoped %3d   class-only %3d' % (t,len(pg),len(rs)-len(pg)))
