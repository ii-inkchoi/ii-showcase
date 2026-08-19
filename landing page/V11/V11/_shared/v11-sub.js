/* ==========================================================================
   v11-sub.js - THE SHARED SCRIPT LAYER for every page that is not the home
   2026-08-19. Extracted from self-directed.html and managed.html, whose copies
   of hero2 / footer / reveal were already byte-identical - three pages could
   not stay that way by hand, and a fourth certainly would not.

   CONTAINS, in the order they must run:
     1. v11-hero2   splits the hero into band + title block
     2. v11-footer  wraps the legal paragraphs so they can go two-column
     3. v11-trust   builds the REGULATORY STANDING fold
     4. v11-reveal  the scroll-reveal observer (label / text / media roles)

   NOT LOADED BY index.html. The home has its own hero, its own footer builder,
   and its reveal lives inside script#v11-mobile-js. Unifying it is a separate
   job with its own verification - see PORT-TO-PAGES.

   LOADED WITHOUT defer, at the position the inline blocks used to occupy, so
   the execution timing is unchanged. Do not move it into <head>.
   ========================================================================== */


/* ---- 1. HERO -> TWO BITS -------------------------------------------------- */
/* Moves the deck, the trust line and the CTA row out of .hero into their own section, so the hero
   is one bit (eyebrow + statement + clip) and these three are the second bit. Mirrors what the home
   does; see the CSS note in style#v11-mobile-sd.
   MOBILE ONLY - the V10 desktop is left as it is, with all of this inside .hero in an absolutely
   positioned .hgroup. Gated on matchMedia rather than a resize listener, same as the home: the
   restructure runs once, for the width the page loaded at.
   ORDER MATTERS AND IS NOT THE DOM ORDER. Source order is deck -> CTAs -> trust; bit 2 wants
   deck -> trust -> CTAs, because the trust line qualifies the statement above it rather than the
   button. Appending in the order below is what performs that swap. */
(function(){
  if(!window.matchMedia('(max-width:900px)').matches) return;
  function build(){
    var hero=document.querySelector('.hero');
    if(!hero||document.querySelector('.v11-hero2'))return;
    var sub=hero.querySelector('.hsub'),
        trust=hero.querySelector('.htrust'),
        btns=hero.querySelector('.btnrow');
    if(!sub&&!trust&&!btns)return;
    var sec=document.createElement('section');
    sec.className='band v11-hero2';
    var rail=document.createElement('div');
    rail.className='h2rail';
    sec.appendChild(rail);
    /* the eyebrow's qualifier leads bit 2. Deliberately NOT given class="rv": the reveal script
       collects .rv synchronously at parse time, so an element created here would never be observed
       and would sit at opacity 0 forever. Plain and visible is the right trade for one mono line. */
    var qual=hero.querySelector('.heyeb .heyeb-b');
    if(qual){
      var eb=document.createElement('div');
      eb.className='h2eyeb';
      eb.textContent=qual.textContent;
      rail.appendChild(eb);
    }
    [sub,trust,btns].forEach(function(el){ if(el) rail.appendChild(el); });
    hero.parentNode.insertBefore(sec,hero.nextSibling);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',build);
  else build();
})();

/* ---- 2. FOOTER LEGAL WRAPPER ---------------------------------------------- */
/* Wraps the run of .footer-legal paragraphs in one container so desktop can column-count them.
   Ported verbatim from V11/index.html. Done in JS rather than in the markup so the footer stays
   byte-identical to the compliance-approved block that ships on every other page - the wording,
   order and element structure are untouched and only a wrapper is introduced.
   The wrapper also carries the 48 group boundary at BOTH widths (see the CSS note): before it
   existed, that 48 sat on .footer-legal:first-of-type, which stops separating the block from the
   social row the moment the paragraphs move inside a wrapper. */
(function(){
  function build(){
    var f=document.querySelector('footer .container')||document.querySelector('footer');
    if(!f||f.querySelector('.footer-legalwrap'))return;
    var legals=[].slice.call(f.querySelectorAll(':scope > .footer-legal'));
    if(legals.length<2)return;
    var w=document.createElement('div'); w.className='footer-legalwrap';
    legals[0].parentNode.insertBefore(w,legals[0]);
    legals.forEach(function(el){w.appendChild(el);});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',build);
  else build();
})();

/* ---- 3. REGULATORY STANDING fold ------------------------------------------
   Home grammar, verbatim (2026-08-18). Mobile only, like the home.
   COMPLIANCE UNCONFIRMED - see PORT-TO-PAGES 7-1.
   MERGED 2026-08-19: Managed still carries the RETIRED VIEW MORE .tmore in its
   markup (display:none since 07-31). It is removed first - otherwise the guard
   below sees "a .tmore already exists" and bails, and the page ends up with a
   fold that never opens. The removal is a no-op on pages that never had it. */
(function(){
  if(!window.matchMedia('(max-width:900px)').matches) return;
  function build(){
    var tw=document.querySelector('.close9 .trust9')||document.querySelector('.trust9');
    if(!tw) return;
    var legacy=tw.querySelector('.tmore');
    if(legacy&&/VIEW MORE/.test(legacy.textContent)) legacy.parentNode.removeChild(legacy);
    if(tw.querySelector('.tmore')) return;
    var tg=tw.querySelector('.tg'); if(!tg) return;
    var tb=document.createElement('button');
    tb.className='tmore'; tb.type='button'; tb.setAttribute('aria-expanded','false');
    tb.innerHTML='<span>REGULATORY STANDING</span><span class="sign" aria-hidden="true">+</span>';
    tw.insertBefore(tb,tg);
    tb.addEventListener('click',function(){
      var open=tw.classList.toggle('open');
      tb.setAttribute('aria-expanded',open?'true':'false');
      tb.querySelector('.sign').textContent=open?'\u2212':'+';
      if(open) tg.querySelectorAll('.rv:not(.in)').forEach(function(el){el.classList.add('in');});
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',build);
  else build();
})();

/* ---- 4. SCROLL REVEAL ------------------------------------------------------ */
/* ============ V11 REVEAL - ported verbatim from V11/index.html (2026-08-18) ============
   This replaced the V9-era single-animation observer that used to sit here (one 14px Y fade for all
   44 .rv elements, rootMargin -8%, threshold .06, no stagger, no roles). The home page's rewrite
   and the reasons for every value are documented in V11/index.html and HANDOFF-V11.md 4-B-1.
   Nothing here is new work: same three roles, same 160ms stagger, same flat -60px rootMargin,
   same load+120ms deferral. Role assignment is data-driven, so it sorts THIS page's elements by
   the same test rather than by a hand-written list. */
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rv=[].slice.call(document.querySelectorAll('.rv'));

  /* sort every reveal into one of the three roles (see the CSS note in style#v11-global) */
  if(!reduce){
    rv.forEach(function(el){
      var t=el.tagName;
      if(t==='IMG'||t==='VIDEO'||t==='FIGURE'||el.classList.contains('ph1')){el.dataset.rv='media';return;}
      /* mono eyebrows only, and only when they hold nothing but text - an eyebrow carrying the
         wordmark <img> would be emptied by the scramble's text rewrite. */
      if((/(^|\s)(eyeb|eyebrow|eyebrow5|htrust)(\s|$)/.test(el.className)
          ||/^NO\.\s*\d/.test((el.textContent||'').trim()))&&!el.querySelector('img,svg')){el.dataset.rv='label';return;}
      el.dataset.rv='text';
    });
  }

  /* ---- scramble decode, for data-rv="label" ---- */
  var GLYPH='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  function scramble(el){
    var nodes=[], total=0;
    (function walk(n){
      for(var i=0;i<n.childNodes.length;i++){
        var c=n.childNodes[i];
        if(c.nodeType===3){ if(c.textContent.length){nodes.push({n:c,t:c.textContent}); total+=c.textContent.length;} }
        else if(c.nodeType===1) walk(c);
      }
    })(el);
    if(!total) return;
    var DUR=520, t0=null;
    function frame(now){
      if(t0===null)t0=now;
      var p=Math.min(1,(now-t0)/DUR), done=p*total, seen=0;
      nodes.forEach(function(r){
        var out='';
        for(var i=0;i<r.t.length;i++){
          var ch=r.t[i];
          out+=(seen+i<done||!/[a-z0-9]/i.test(ch))?ch:GLYPH[(Math.random()*GLYPH.length)|0];
        }
        r.n.textContent=out; seen+=r.t.length;
      });
      if(p<1)requestAnimationFrame(frame);
      else nodes.forEach(function(r){r.n.textContent=r.t;});
    }
    requestAnimationFrame(frame);
  }

  /* ---- stagger: everything that crosses in the same frame goes 160ms apart, capped at 4 ---- */
  var queue=[],pending=false;
  function reveal(el,i){
    var d=Math.min(i,4)*160;
    if(el.dataset.rv==='label'){setTimeout(function(){scramble(el);},d);el.classList.add('in');return;}
    el.style.transitionDelay=(d/1000)+'s';
    el.classList.add('in');
  }
  function enqueue(el){
    if(reduce){el.classList.add('in');return;}
    queue.push(el);
    if(pending)return; pending=true;
    requestAnimationFrame(function(){
      queue.forEach(function(e,i){reveal(e,i);});
      queue=[];pending=false;
    });
  }

  /* ---- media role: the band photography (2026-08-18) ----
     Role sorting above only reaches elements that already carry .rv, and this page's band images
     never had a reveal at all - so all three would have stayed static while everything around them
     animated. Ported from the home's binder verbatim.
     ★ WATCH THE PARENT, NOT THE IMAGE. clip-path:inset(0 100% 0 0) leaves the element with zero
     visible area and IntersectionObserver measures the clipped box: an image sitting squarely in the
     viewport reports isIntersecting:false, ratio 0.00, so the observer never fires and the image
     stays wiped out forever - the effect blocks its own trigger. .v9band is never clipped. It is
     also taller than the image (it holds the masthead too), so the margin is -35% rather than -60px:
     that lands the trigger where the IMAGE reaches the viewport, not the masthead.
     .v9band is built by the V9 mobile JS at the bottom of this file, so the wrappers may not exist
     yet - a MutationObserver picks them up whenever they land, and gives up at load. Desktop matches
     nothing here (no .v9band wrappers), which is correct: the home leaves full-bleed desktop band
     photography out of the media role because a 0.9s wipe across 1666px reads as an event, not an
     entrance. */
  if(!reduce){(function(){
    function go(){
      var med=[].slice.call(document.querySelectorAll('.v9band>img,.v9band>video'))
        .filter(function(m){return !m.dataset.rv;});
      if(!med.length) return false;
      var mio=new IntersectionObserver(function(es){
        es.forEach(function(e){
          if(!e.isIntersecting) return;
          var t=e.target.__rvMedia; if(t) t.classList.add('in');
          mio.unobserve(e.target);
        });
      },{rootMargin:'0px 0px -35% 0px',threshold:0});
      med.forEach(function(m){
        m.classList.add('rv'); m.dataset.rv='media';
        var r=m.getBoundingClientRect();
        if(r.top<window.innerHeight&&r.bottom>0){m.classList.add('in');return;}
        var host=m.parentElement||m;
        host.__rvMedia=m;
        mio.observe(host);
      });
      return true;
    }
    go();
    var mo=new MutationObserver(go);
    mo.observe(document.documentElement,{childList:true,subtree:true});
    window.addEventListener('load',function(){ go(); mo.disconnect(); });
  })();}

  if(reduce||!('IntersectionObserver' in window)){rv.forEach(function(el){el.classList.add('in');});}
  else{
    /* flat -60px, not -8%: on an 812 screen -8% puts the trigger at 747, above the hero's own
       second line - a one-viewport hero would wait for a scroll that never comes. */
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){enqueue(e.target);io.unobserve(e.target);}});},{rootMargin:'0px 0px -60px 0px',threshold:0});
    var observeAll=function(){
      if(observeAll.done) return; observeAll.done=true;
      setTimeout(function(){ rv.forEach(function(el){io.observe(el);}); },120);
    };
    if(document.readyState==='complete') observeAll();
    else window.addEventListener('load',observeAll);
  }
})();
(function(){
  var nav=document.querySelector('.nav');
  function onScroll(){nav.classList.toggle('scrolled',window.scrollY>24);}
  window.addEventListener('scroll',onScroll,{passive:true});
  onScroll();
})();

/* horizon ring glyph (ported verbatim from index-H) */
(function(){
  var cv=document.getElementById('recRingH'); if(!cv) return; var ctx=cv.getContext('2d');
  var DPR=Math.min(devicePixelRatio||1,2), S=44; cv.width=S*DPR; cv.height=S*DPR; ctx.scale(DPR,DPR);
  var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cx=S/2, cy=S/2, R=15, PROG=0.10; /* 5-year, early */
  function frame(now){
    ctx.clearRect(0,0,S,S);
    var pulse=0.55+0.45*Math.sin(now*0.004);
    ctx.strokeStyle='rgba(244,243,240,0.14)'; ctx.lineWidth=2;
    ctx.beginPath(); ctx.arc(cx,cy,R,0,6.28); ctx.stroke();
    ctx.strokeStyle='rgba(244,243,240,0.9)'; ctx.lineWidth=2; ctx.lineCap='round';
    ctx.beginPath(); ctx.arc(cx,cy,R,-Math.PI/2,-Math.PI/2+PROG*6.28); ctx.stroke(); ctx.lineCap='butt';
    ctx.strokeStyle='rgba(244,243,240,'+(0.5+0.4*pulse).toFixed(3)+')'; ctx.lineWidth=1.3;
    ctx.beginPath(); ctx.arc(cx,cy,3.4,0,6.28); ctx.stroke();
    if(!RM) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();

/* below 900px the clip is served from its light encode (data-m) instead of the 4K master */
(function(){
  if(!window.matchMedia('(max-width:900px)').matches)return;
  [].slice.call(document.querySelectorAll('video[data-m]')).forEach(function(v){
    v.src=v.dataset.m; v.load();
  });
})();

/* menu overlay */
(function(){
  var burger=document.querySelector('.nav .burger');
  var ov=document.getElementById('menuov');
  if(!burger||!ov)return;
  function toggle(){var open=document.body.classList.toggle('menu-open');ov.classList.toggle('open',open);ov.setAttribute('aria-hidden',String(!open));}
  burger.addEventListener('click',toggle);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.body.classList.contains('menu-open'))toggle();});
})();

/* mobile prose folds: VIEW MORE / VIEW LESS (same pattern as index-H) */
(function(){
  if(!window.matchMedia('(max-width:900px)').matches) return;
  /* account types: tap the title to disclose (same as the homepage NO.01 directory) */
  [].slice.call(document.querySelectorAll('.acct3 .a')).forEach(function(d){
    var h=d.querySelector('h3'); if(!h) return;
    h.setAttribute('role','button'); h.setAttribute('tabindex','0'); h.setAttribute('aria-expanded','false');
    function toggle(){var open=d.classList.toggle('open'); h.setAttribute('aria-expanded',open?'true':'false');}
    h.addEventListener('click',toggle);
    h.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle();}});
  });
  [['.specimens .snote .smore','.snote'],
   ['.calcol .cmore','.calcol'],
   ['.devgrid .dmore','.devgrid']].forEach(function(pair){ /* .trust9 left the fold system 2026-07-31 */
    var btn=document.querySelector(pair[0]); if(!btn) return;
    btn.addEventListener('click',function(){
      var box=btn.closest(pair[1]);
      var open=box.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
      btn.textContent=open?'VIEW LESS':'VIEW MORE';
      if(open) box.querySelectorAll('.rv:not(.in)').forEach(function(el){el.classList.add('in');});
      /* newly-revealed .rv elements would otherwise sit at opacity 0 on motion-enabled devices */
    });
  });
})();
