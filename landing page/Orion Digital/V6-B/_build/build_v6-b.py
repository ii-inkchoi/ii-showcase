# Builds V5/index.html. The nav logo SVG is lifted verbatim from V2 rather than retyped.
import io, os, re
ROOT = r"C:\Users\p0107\OneDrive\바탕 화면\II Work\Product Design_work files\Prototype\website\Orion Digital Website"
v2 = io.open(os.path.join(ROOT, "V2", "index.html"), encoding="utf-8").read()
nav = re.search(r'<nav class="nav">.*?</nav>', v2, re.S).group(0)
nav = nav.replace('shared/v2.css', 'shared/v6-b.css')
assert '    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>' in nav
nav = nav.replace('    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>', '    <div class="qstrip">\n      <div class="qrows">\n        <div class="qrow"><span class="qex">TSX</span><span class="qv unc"><span class="qc">$</span><span class="qn">1.40</span></span><span class="qp">+2.19%</span></div>\n        <div class="qrow"><span class="qex">NASDAQ</span><span class="qv unc"><span class="qc">US$</span><span class="qn">1.01</span></span><span class="qp">+2.02%</span></div>\n      </div>\n      <span class="qasof">As of 2026-08-12</span>\n    </div>', 1)

# V5: the live IR site's menu, the quote strip out of the bar, and the mockup's tagline
# beside the logo. INVESTOR ALERTS goes with the strip: the IR nav is five links and the
# new mockup puts a search icon in that corner, so neither reference carries that button.
_om = '  <div class="navmenu">\n    <a href="#" class="on"><!-- TODO stub -->Overview</a>\n    <a href="#"><!-- TODO stub -->Businesses</a>\n    <a href="#"><!-- TODO stub -->Investors</a>\n    <a href="#"><!-- TODO stub -->News</a>\n    <a href="#"><!-- TODO stub -->About</a>\n    <a href="#"><!-- TODO stub -->Contact</a>\n  </div>'
_nm = '  <div class="navmenu">\n    <a href="https://www.orion-digital.com/investor-relations" class="on">Overview</a>\n    <a href="https://www.orion-digital.com/press-release">Press Releases</a>\n    <a href="https://www.orion-digital.com/financial-reports">Financial Reports</a>\n    <a href="https://www.orion-digital.com/events">Events</a>\n    <a href="https://www.orion-digital.com/corporate-governance">Governance</a>\n  </div>'
assert nav.count(_om) == 1
nav = nav.replace(_om, _nm, 1)
_i = nav.index('<div class="navright">')
_j = nav.index('</div>\n</nav>')
nav = nav[:_i] + nav[_j:]
assert 'qstrip' not in nav and 'INVESTOR ALERTS' not in nav
nav = nav.replace('</a>\n  <div class="navmenu">',
                  '</a>\n  <div class="m9 navtag">A FINANCIAL TECHNOLOGY COMPANY</div>\n  <div class="navmenu">', 1)
nav = nav.replace('  <div class="m9 navtag">A FINANCIAL TECHNOLOGY COMPANY</div>\n', '', 1)


ARR = ('<svg class="arr" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
       '<path d="M4.5 11.5L11.5 4.5" stroke="currentColor" stroke-width="1.1"/>'
       '<path d="M5.5 4.5H11.5V10.5" stroke="currentColor" stroke-width="1.1"/></svg>')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orion Digital Corp. - Investor Overview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="shared/v6-b.css">
</head>
<body>

<!-- V3, a role study. Three sections only: the two composed moments and the quiet one
     between them. V1 and V2 are untouched.
     What is being judged here is whether the page says which moment matters. V2 gave all
     ten sections a device and the review was "난잡해"; the fix is subtraction, not more
     variation. Content, figures and compliance obligations are unchanged from V1, whose
     PLAN.md remains the specification. Figures are inline; rewiring to data.js waits for
     a settled direction. -->
'''

HERO = '''
<!-- 00 HERO. The mockup's words, on our ground. The sector line moves above the headline, where
     the mockup puts it, and the four-line claim sits at the lower right in the plate the hero
     already had. -->
<section class="field photo hero" id="hero">
  <img class="bg" src="Images/hero-b.jpg" alt="" style="object-position:50% 50%">
  <div class="rail">
    <div class="grid12">
      <div class="htitle">
        <div class="m13 heyeb">WEALTH. PAYMENTS. CONSUMER LENDING.<br><span class="hsol">DISCIPLINED REAL-WORLD FINANCIAL SOLUTIONS FOR AN AI-DRIVEN ECONOMY.</span></div>
        <h1 class="h1">Building for an<span class="ind">AI-Driven Financial System.</span></h1>
        <p class="p hsub">Real businesses. Disciplined capital allocation.<br>A more intelligent and connected financial future.</p>
      </div>
    </div>
  </div>
</section>
'''

GLANCE = '''
<!-- 01 LIVE SHARE PRICE.
     Its own band, black, between the hero and the page. In V4 this lived in the nav and had to
     be crushed beside a button; the mockup gives it a band of its own and there is room in one
     for the exchange, the price, the change and the timestamp on one line. -->
<section class="field blk pband" id="price">
  <div class="rail">
    <div class="grid12 pgrid">
      <div class="plabel">
        <div class="m13">LIVE SHARE PRICE</div>
        <div class="m11 pasof">As of September 9, 2026 (15 min. delay)</div>
      </div>
      <div class="pq pq1" data-sim="0.72" data-prev="0.70" data-cur="$" title="Simulated for the prototype, not a live quote">
        <div class="m11 pex">TSX: ORIO</div>
        <div class="pquote">
          <div class="v">$0.72</div>
          <div class="m13 pch up">+0.02 (+2.9%) &#9650;</div>
        </div>
      </div>
      <div class="pq pq2" data-sim="0.52" data-prev="0.51" data-cur="US$" title="Simulated for the prototype, not a live quote">
        <div class="m11 pex">NASDAQ: ORIO</div>
        <div class="pquote">
          <div class="v">US$0.52</div>
          <div class="m13 pch up">+0.01 (+2.0%) &#9650;</div>
        </div>
      </div>
    </div>
  </div>

<script>
/* Demo tick. The quotes are simulated, not live: a random walk around the quoted price,
   with the change, the percentage and the direction recomputed from the previous close so
   the line always agrees with itself. A live page swaps this for the IR vendor's feed. */
(function () {
  var quotes = [].slice.call(document.querySelectorAll('#price .pq[data-sim]'));
  if (!quotes.length) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  quotes.forEach(function (q) {
    q._price = parseFloat(q.getAttribute('data-sim'));
    q._prev = parseFloat(q.getAttribute('data-prev'));
    q._cur = q.getAttribute('data-cur');
  });

  function draw(q) {
    var d = q._price - q._prev;
    var pct = (d / q._prev) * 100;
    var up = d >= 0;
    q.querySelector('.v').textContent = q._cur + q._price.toFixed(2);
    var ch = q.querySelector('.pch');
    ch.textContent = (up ? '+' : '−') + Math.abs(d).toFixed(2)
      + ' (' + (up ? '+' : '−') + Math.abs(pct).toFixed(1) + '%) '
      + (up ? '▲' : '▼');
    ch.classList.toggle('up', up);
    ch.classList.toggle('dn', !up);
  }

  function tick() {
    quotes.forEach(function (q) {
      var step = (Math.random() - 0.5) * 0.02;          /* about a cent either way */
      var next = q._price + step;
      var floor = q._prev * 0.9, ceil = q._prev * 1.12; /* it wanders, it does not run */
      q._price = Math.min(ceil, Math.max(floor, Math.round(next * 100) / 100));
      draw(q);
    });
    setTimeout(tick, 2600 + Math.random() * 2200);
  }
  setTimeout(tick, 2000);
})();
</script>
</section>

<!-- 02 ORION TODAY.
     The mockup's own section, and it absorbs what V4 carried as At a Glance. The market
     capitalisation sits beside the paragraph rather than in a valuation section of its own,
     which is the mockup's structure; what it costs is the juxtaposition V3 was built around,
     since Adjusted EV is gone with that section. Recorded for Greg. -->
<section class="field paper secpad" id="today">
  <div class="rail">
    <div class="grid12 tgrid">
      <div class="tleft">
        <div class="m13 teyeb">ORION TODAY</div>
        <h2 class="h2">Emerging from transition.<br>Focused on execution and value creation.</h2>
        <p class="p">Orion is emerging from a multi-year transition that has reshaped its businesses, capital allocation and financial profile. We are now entering a new phase, focused on execution, disciplined growth and long-term value creation.</p>
      </div>
      <div class="tright panel">
        <div class="m13 teyeb">CURRENT MARKET CAPITALIZATION</div>
        <div class="v mcap">~$37M</div>
        <div class="m11 mcapex">TSX: ORIO &nbsp;|&nbsp; NASDAQ: ORIO</div>
        <div class="m9">As of September 9, 2026</div>
      </div>
    </div>
    <div class="figrow">
      <div class="fig"><div class="v">$67M</div><div class="s15">Annual Revenue<br><span class="m9">(FY2025)</span></div></div>
      <div class="fig"><div class="v">$8.9M</div><div class="s15">LTM Adjusted EBITDA<br><span class="m9">(Q2 2026)</span></div></div>
      <div class="fig"><div class="v">$35M</div><div class="s15">Cash &amp; Investments<br><span class="m9">(Jun 30, 2026)</span></div></div>
      <div class="fig"><div class="v">&gt;20%</div><div class="s15">Insider Ownership</div></div>
      <div class="fig"><div class="v">~8%</div><div class="s15">Shares Retired<br><span class="m9">(Since 2022)</span></div></div>
    </div>
    <p class="m9 curnote">All figures in Canadian dollars unless otherwise noted.</p>
  </div>
</section>
'''

BIZ = '''
<!-- 03 WEALTH. PAYMENTS. CONSUMER LENDING.
     The mockup's label and its standfirst. The cells are inverted against the mockup on the
     team's instruction: the company name leads and the division is its label, because the
     section title already names the three divisions and saying them twice makes the companies
     the smaller fact on their own card.
     Each cell carries an image. The mockup uses a phone, a Carta card and a road; none of the
     three exists in our library, so the register approved instead is muted urban photography,
     one subject each so no two cells share a frame. -->
<section class="field photo mid secpad" id="businesses">
  <img class="bg" src="Images/ground-pattern.jpg" alt="" style="object-position:50% 50%">
  <div class="rail">
    <div class="m13 beyeb">WEALTH. PAYMENTS. CONSUMER LENDING.</div>
    <h2 class="h2 bstand">Three financial businesses managed through a disciplined capital allocation framework.</h2>
    <div class="grid12">
      <div class="bsheet">
        <div class="bcell">
          <img class="bpic" src="Images/prod-wealth.jpg" alt="">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Intelligent Investing</div>
              <div class="m13 bcat">WEALTH</div>
            </div>
            <span class="bmark"><svg viewBox="0 0 15 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Intelligent Investing"><path d="M5.59903 0H7.79315L2.19412 17.6523H0L5.59903 0Z" fill="currentColor"/><path d="M12.8061 0H15.0002L9.40115 17.6523H7.20703L12.8061 0Z" fill="currentColor"/></svg></span>
          </div>
          <div class="b-body">
            <p class="p b-desc">A differentiated investing platform built for an AI world.</p>
          </div>
          <div class="b-fig f1"><div class="v">~$545M</div><div class="m11">Client Assets (AUA/AUM)</div></div>
          <a class="link push" href="https://www.intelligentinvesting.ai/" target="_blank" rel="noopener">LEARN MORE{ARR}</a>
        </div>
        <div class="bcell">
          <img class="bpic" src="Images/prod-payments.jpg" alt="">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Carta Worldwide</div>
              <div class="m13 bcat">PAYMENTS</div>
            </div>
            <span class="bmark carta"><img src="logos/carta-black.svg" alt="Carta Worldwide"></span>
          </div>
          <div class="b-body">
            <p class="p b-desc">European payments infrastructure for a digital economy.</p>
          </div>
          <div class="b-fig f1"><div class="v">&gt;$11B</div><div class="m11">Annual Processing Volume (FY2025)</div></div>
          <a class="link push" href="https://cartaworldwide.com/" target="_blank" rel="noopener">LEARN MORE{ARR}</a>
        </div>
        <div class="bcell">
          <img class="bpic" src="Images/prod-lending.jpg" alt="">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Mogo</div>
              <div class="m13 bcat">CONSUMER LENDING</div>
            </div>
            <span class="bmark"><img src="logos/mogo-black.svg" alt="Mogo"></span>
          </div>
          <div class="b-body">
            <p class="p b-desc">An established Canadian lending business.</p>
          </div>
          <div class="b-fig f1"><div class="v">~$75M</div><div class="m11">Gross Loans (Jun 30, 2026)</div></div>
          <a class="link push" href="https://www.mogo.ca/" target="_blank" rel="noopener">LEARN MORE{ARR}</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''.replace("{ARR}", ARR)

REST = """
<!-- 04 Q2 DEMONSTRATED EARNINGS & CASH-GENERATING CAPACITY.
     Three figures and the one button on the page. The mockup draws that button outlined, which
     is also what our system does with a chrome CTA, so it is the same component. -->
<section class="field paper secpad" id="snapshot">
  <div class="rail">
    <div class="q2panel">
      <div class="q2head">
        <div class="m13 beyeb">Q2 DEMONSTRATED EARNINGS &amp; CASH-GENERATING CAPACITY.</div>
        <a class="link q2link" href="https://www.orion-digital.com/financial-reports">VIEW Q2 RESULTS{ARR}</a>
      </div>
      <div class="q2row">
        <div class="fig"><div class="v">$3.3M</div><div class="s15">Q2 Adjusted EBITDA <span class="m9">(+115% q/q)</span></div></div>
        <div class="fig"><div class="v">$5.1M</div><div class="s15">Q2 Core Operating Cash Generation</div></div>
        <div class="fig"><div class="v">$6.0M &ndash; $7.0M</div><div class="s15">FY2026 Adjusted EBITDA Guidance</div></div>
      </div>
    </div>
  </div>
</section>

<!-- 05 LATEST NEWS.
     Three releases and a way out to the rest. Dates and headlines are the mockup's; they need
     checking against the real newsroom, and the order it shows is not chronological. -->
<section class="field white secpad" id="news">
  <div class="rail">
    <div class="nhead">
      <div class="m13 beyeb">LATEST NEWS</div>
      <a class="link" href="https://www.orion-digital.com/press-release">VIEW ALL NEWS{ARR}</a>
    </div>
    <div class="nrows">
      <div class="nrow grid12">
        <div class="nmeta"><div class="m11">Press Release</div><div class="m11 ndate">JUL 27, 2026</div></div>
        <div class="t22 ntitle">Orion Launches Intelligent Investing Platform for an AI World</div>
        <a class="link nread" href="#"><!-- TODO stub, needs the release URL -->READ MORE{ARR}</a>
      </div>
      <div class="nrow grid12">
        <div class="nmeta"><div class="m11">Press Release</div><div class="m11 ndate">AUG 10, 2026</div></div>
        <div class="t22 ntitle">Orion Reports Strong Q2 2026 Results</div>
        <a class="link nread" href="#"><!-- TODO stub, needs the release URL -->READ MORE{ARR}</a>
      </div>
      <div class="nrow grid12">
        <div class="nmeta"><div class="m11">Press Release</div><div class="m11 ndate">MAR 12, 2026</div></div>
        <div class="t22 ntitle">Mogo Inc. Completes Name Change to Orion Digital Corp.</div>
        <a class="link nread" href="#"><!-- TODO stub, needs the release URL -->READ MORE{ARR}</a>
      </div>
    </div>
  </div>
</section>

<!-- 06 DISCLOSURES.
     Held as it was pending the separate review of the disclaimer language. The mockup's own
     footer row, the identity and the three links, sits under it. -->
<footer class="field blk secpad" id="disclosures">
  <div class="rail">
    <div class="fsite">
      <div class="soc-row"><a class="soc" href="#" aria-label="Facebook"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M14 8h2.5V4.5H14c-2.2 0-3.5 1.6-3.5 3.7V10H8v3.5h2.5V21H14v-7.5h2.6l.4-3.5h-3V8.4c0-.3.1-.4.4-.4z"/></svg></a><a class="soc" href="#" aria-label="Instagram"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a><a class="soc" href="#" aria-label="X"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.9 2H22l-7.6 8.7L23 22h-7l-5.5-7.2L4.2 22H1l8.1-9.3L1 2h7.2l5 6.6L18.9 2zm-1.2 18h1.9L7.4 4H5.5l12.2 16z"/></svg></a><a class="soc" href="#" aria-label="LinkedIn"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7.5 10.5V17M7.5 7.6v.1M11.5 17v-4a2.5 2.5 0 015 0v4M11.5 10.5V17"/></svg></a><a class="soc" href="#" aria-label="YouTube"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.5c-.3-1-1-1.8-2-2C19 5 12 5 12 5s-7 0-9 .5c-1 .3-1.8 1-2 2C.5 9.3.5 12 .5 12s0 2.7.5 4.5c.3 1 1 1.8 2 2C5 19 12 19 12 19s7 0 9-.5c1-.3 1.8-1 2-2 .5-1.8.5-4.5.5-4.5s0-2.7-.5-4.5zM9.8 15.3V8.7l5.7 3.3-5.7 3.3z"/></svg></a></div>
      <p class="m9 flegal">&copy; 2026 Orion Digital Corp. (formerly Mogo Inc.). All rights reserved. Orion Digital Corp. is a holding company. Its subsidiaries operate independently and are each subject to their own regulatory requirements. Orion Digital Corp. itself is not registered or licensed under securities, lending, or other financial services laws and regulations. Certain subsidiaries of Orion Digital Corp. are separately registered and regulated in Canada and conduct business only through their respective legal entities. Information on this site is for general information only and does not constitute an offer or solicitation. For product-specific terms and regulatory disclosures, see the applicable subsidiary websites and terms of service.</p>
    </div>
  </div>
</footer>
<script>
/* The mobile menu, on the II site's pattern: the burger toggles body.menu-open, a black overlay
   carries the same five links at display size, Escape closes it, and the page behind it is
   locked. Desktop never shows either piece. */
(function () {
  var nav = document.querySelector('.nav');
  if (!nav || nav.querySelector('.burger')) return;

  var b = document.createElement('button');
  b.className = 'burger';
  b.type = 'button';
  b.setAttribute('aria-label', 'Menu');
  b.setAttribute('aria-expanded', 'false');
  b.innerHTML = '<span></span><span></span>';
  nav.appendChild(b);

  var ov = document.createElement('div');
  ov.className = 'menuov';
  ov.setAttribute('aria-hidden', 'true');
  var list = document.createElement('div');
  list.className = 'mlist';
  var src = nav.querySelectorAll('.navmenu a');
  for (var i = 0; i < src.length; i++) {
    var a = document.createElement('a');
    a.href = src[i].getAttribute('href') || '#';
    a.textContent = src[i].textContent;
    if (src[i].className.indexOf('on') > -1) a.className = 'cur';
    list.appendChild(a);
  }
  ov.appendChild(list);
  var mfoot = document.createElement('div');
  mfoot.className = 'm13 mfoot';
  mfoot.textContent = 'WEALTH. PAYMENTS. CONSUMER LENDING.';
  ov.appendChild(mfoot);
  document.body.appendChild(ov);

  function toggle(open) {
    document.body.classList.toggle('menu-open', open);
    ov.classList.toggle('open', open);
    ov.setAttribute('aria-hidden', String(!open));
    b.setAttribute('aria-expanded', String(open));
  }
  b.addEventListener('click', function () {
    toggle(!document.body.classList.contains('menu-open'));
  });
  ov.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') toggle(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('menu-open')) toggle(false);
  });
  addEventListener('resize', function () {
    if (innerWidth > 900 && document.body.classList.contains('menu-open')) toggle(false);
  });
})();
</script>

""".replace("{ARR}", ARR)

TAIL = '''
<div class="gridov" id="gridov" aria-hidden="true"><div class="rail"><div class="grid12">
  <i class="col"></i><i class="col"></i><i class="col"></i><i class="col"></i>
  <i class="col"></i><i class="col"></i><i class="col"></i><i class="col"></i>
  <i class="col"></i><i class="col"></i><i class="col"></i><i class="col"></i>
</div></div></div>

<script>
// The nav turns opaque once the hero is behind it. Same behaviour as V1 and V2.
(function(){
  var nav = document.querySelector('.nav');
  function onScroll(){ nav.classList.toggle('scrolled', window.scrollY > window.innerHeight * 0.72); }
  onScroll(); window.addEventListener('scroll', onScroll, {passive:true});
})();
// g toggles the 12-column overlay, the same key used on the II site pages. Ignored while a
// field has focus so it never eats a keystroke.
(function(){
  var ov = document.getElementById('gridov');
  document.addEventListener('keydown', function(e){
    if (e.key !== 'g' && e.key !== 'G') return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    ov.classList.toggle('on');
  });
})();
// 06's leader lines draw from the rail's edges inward as each row arrives. The only motion
// on the page, in the only section that is about change.
// The .motion class is added by script, so the animated state exists only once JS has run:
// with JS off the lines are simply drawn, rather than sitting at scaleX(0) forever.
// Not animated: the type. The reference scales its word up because it has one word per
// frame; eight phrases growing at once would move the layout while it is being read, and on
// an issuer's page figures that shift while you look at them cost more than they buy.
(function(){
  var sec = document.getElementById('transition');
  if (!sec) return;
  var rows = sec.querySelectorAll('.mrow:not(.mhead)');
  if (!rows.length || !('IntersectionObserver' in window)) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  sec.classList.add('motion');
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      io.unobserve(en.target);
    });
  }, {threshold: 0.6});
  rows.forEach(function(r){ io.observe(r); });
})();
// 04's pair arrives in order: portfolio, rule, facility. Same .motion gate as 06, so the
// section is complete without script and under prefers-reduced-motion.
(function(){
  var sec = document.getElementById('balance-sheet');
  if (!sec) return;
  var box = sec.querySelector('.box.inv');
  if (!box || !('IntersectionObserver' in window)) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  sec.classList.add('motion');
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      io.unobserve(en.target);
    });
  }, {threshold: 0.2});
  io.observe(box);
})();
// The page's motion, all of it, from one table.
//
// ARRIVE: [selector, primitive, stagger ms, trigger]. The trigger decides WHEN. 'self' means
// the element watches for itself; 'section' means its section does, which is a requirement
// wherever a wipe is involved rather than a preference: a wipe clips its element to nothing,
// and an element clipped to nothing never intersects the viewport, so it cannot trigger
// itself and neither can anything inside it.
// LAG: [selector, travel px, clock]. 'page' measures against the first viewport, 'element'
// against the whole time the ground is on screen. The hero takes 'page' because a ground
// already in frame is half travelled before the reader has touched the wheel.
//
// 04 and 06's pair sequence are absent: each has a bespoke sequence saying something only
// that section says. 10 DISCLOSURES is absent for another reason, that legal copy appearing
// on scroll looks like copy that was being withheld.
(function(){
  var ARRIVE = [
    ['#today .figrow .fig .v',   'a-val',  60, 'section'],
    ['#today .mcap',             'a-val',   0, 'section'],
    ['#businesses .bcell .v',    'a-val',  80, 'section'],
    ['#snapshot .q2row .fig .v', 'a-val',  70, 'section'],
    ['#news .nitem',             'a-rise', 60, 'self']
  ];
  var WIPE = [
    ['#businesses .bcell', 'down', 100]
  ];
  var LAG = [
    ['#hero > .bg',        160, 'page'],
    ['#businesses > .bg',   60, 'element']
  ];
  var ZOOM = [];

  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;

  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      io.unobserve(en.target);
    });
  }, {threshold: 0.2});

  function openWith(section, els){
    if (!section) return;
    var so = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (!en.isIntersecting) return;
        Array.prototype.forEach.call(els, function(el){ el.classList.add('in'); });
        so.unobserve(en.target);
      });
    }, {threshold: 0.15});
    so.observe(section);
  }

  function mark(els, cls, step, extra){
    Array.prototype.forEach.call(els, function(el, i){
      el.classList.add(cls);
      if (extra) el.classList.add(extra);
      if (step) el.style.transitionDelay = (i * step) + 'ms';
    });
  }

  WIPE.forEach(function(r){
    var els = document.querySelectorAll(r[0]);
    if (!els.length) return;
    mark(els, 'a-wipe', r[2], r[1] === 'left' ? 'wl' : null);
    openWith(els[0].closest('section'), els);
  });

  ARRIVE.forEach(function(r){
    var els = document.querySelectorAll(r[0]);
    if (!els.length) return;
    mark(els, r[1], r[2], null);
    if (r[3] === 'section') {
      openWith(els[0].closest('section'), els);
    } else {
      Array.prototype.forEach.call(els, function(el){ io.observe(el); });
    }
  });

  // 06's rows: each draws its own rule as it arrives
  Array.prototype.forEach.call(
    document.querySelectorAll('#transition .mrow:not(.mhead)'),
    function(row){ io.observe(row); });

  // grounds and the one picture that scales, both written inline per frame
  var moving = [];
  LAG.forEach(function(r){
    Array.prototype.forEach.call(document.querySelectorAll(r[0]), function(el){
      el.classList.add('a-lag');
      // top only moves a positioned element, and 05's ground image is static inside its
      // wrapper. That is declared in the stylesheet now, on #valuation > .vbg img, and is
      // deliberately NOT inferred here: reading getComputedStyle at this moment asks a
      // question the page cannot yet answer. If the stylesheet has not arrived, every ground
      // reads static and gets an inline position:relative that permanently beats the
      // absolute in the stylesheet, which leaves the background images in flow carrying the
      // inline height below and blows the hero up from 880px to 1852px.
      el.style.top = (-r[1]) + 'px';
      el.style.height = 'calc(100% + ' + r[1] + 'px)';
      moving.push({el: el, kind: 'lag', amount: r[1], clock: r[2]});
    });
  });
  ZOOM.forEach(function(r){
    Array.prototype.forEach.call(document.querySelectorAll(r[0]), function(el){
      el.classList.add('a-zoom');
      moving.push({el: el, kind: 'zoom', amount: r[1], clock: 'element'});
    });
  });

  // Only now is hiding allowed. Everything above is additive; the class that lets CSS hide
  // anything goes on last, so a failure before this point leaves the page finished.
  document.documentElement.classList.add('js-anim');

  var lastY = -1;
  function apply(){
    var vh = window.innerHeight;
    moving.forEach(function(m){
      var p;
      if (m.clock === 'page') {
        p = window.scrollY / vh;
      } else {
        var bb = m.el.getBoundingClientRect();
        p = (vh - bb.top) / (vh + bb.height);
      }
      if (p < 0) p = 0; else if (p > 1) p = 1;
      if (m.kind === 'lag') {
        m.el.style.transform = 'translate3d(0,' + (p * m.amount).toFixed(1) + 'px,0)';
      } else {
        m.el.style.transform = 'scale(' + (1 + (m.amount - 1) * p).toFixed(4) + ')';
      }
    });
  }
  function onScroll(){
    var y = window.scrollY;
    if (y === lastY) return;
    lastY = y;
    apply();
  }
  apply();
  window.addEventListener('scroll', onScroll, {passive:true});
  window.addEventListener('resize', onScroll, {passive:true});
})();
</script>
</body>
</html>
'''

out = HEAD + "\n" + nav + "\n" + HERO + GLANCE + BIZ + REST + TAIL
io.open(os.path.join(ROOT, "V5", "index.html"), "w", encoding="utf-8").write(out)
print("wrote V5/index.html", len(out), "bytes")
