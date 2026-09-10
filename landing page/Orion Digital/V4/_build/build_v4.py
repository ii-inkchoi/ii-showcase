# Builds V4/index.html. The nav logo SVG is lifted verbatim from V2 rather than retyped.
import io, os, re
ROOT = r"C:\Users\p0107\OneDrive\바탕 화면\II Work\Product Design_work files\Prototype\website\Orion Digital Website"
v2 = io.open(os.path.join(ROOT, "V2", "index.html"), encoding="utf-8").read()
nav = re.search(r'<nav class="nav">.*?</nav>', v2, re.S).group(0)
nav = nav.replace('shared/v2.css', 'shared/v4.css')
assert '    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">C$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>' in nav
nav = nav.replace('    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">C$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>', '    <div class="qstrip">\n      <div class="qrows">\n        <div class="qrow"><span class="qex">TSX</span><span class="qv unc"><span class="qc">C$</span><span class="qn">1.40</span></span><span class="qp">+2.19%</span></div>\n        <div class="qrow"><span class="qex">NASDAQ</span><span class="qv unc"><span class="qc">US$</span><span class="qn">1.01</span></span><span class="qp">+2.02%</span></div>\n      </div>\n      <span class="qasof">As of 2026-08-12</span>\n    </div>', 1)

# V4: the strip to the mockup. Full exchange labels, the point change beside the percent, and
# the date on one line as a third row. See v4.css for why it is a third row and not a column.
nav = nav.replace('''    <div class="qstrip">
      <div class="qrows">
        <div class="qrow"><span class="qex">TSX</span><span class="qv unc"><span class="qc">C$</span><span class="qn">1.40</span></span><span class="qp">+2.19%</span></div>
        <div class="qrow"><span class="qex">NASDAQ</span><span class="qv unc"><span class="qc">US$</span><span class="qn">1.01</span></span><span class="qp">+2.02%</span></div>
      </div>
      <span class="qasof">As of 2026-08-12</span>
    </div>''', '''    <div class="qstrip">
      <div class="qrows">
        <div class="qrow"><span class="qex"><span class="qxn">TSX:</span><span class="qtk">ORIO</span></span><span class="qv"><span class="qc">C$</span><span class="qn">1.40</span></span><span class="qp">+0.03 (+2.19%)</span></div>
        <div class="qrow"><span class="qex"><span class="qxn">NASDAQ:</span><span class="qtk">ORIO</span></span><span class="qv"><span class="qc">US$</span><span class="qn">1.01</span></span><span class="qp">+0.02 (+2.02%)</span></div>
        <div class="qasof">As of Aug 19, 2026 10:30 AM ET</div>
      </div>
    </div>''', 1)
assert 'class="qtk">ORIO<' in nav and 'As of Aug 19, 2026 10:30 AM ET' in nav
MAIL = ('<svg class="mail" viewBox="0 0 16 12" fill="none" aria-hidden="true">'
        '<rect x="0.5" y="0.5" width="15" height="11" stroke="currentColor"/>'
        '<path d="M0.5 0.5L8 6.5L15.5 0.5" stroke="currentColor"/></svg>')
assert nav.count('-->INVESTOR ALERTS</a>') == 1
nav = nav.replace('-->INVESTOR ALERTS</a>', '-->' + MAIL + 'INVESTOR ALERTS</a>', 1)


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
<link rel="stylesheet" href="shared/v4.css">
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
<!-- 00 HERO. Word for word the mockup's hero, which V3 already carried: the same headline,
     the same paragraph, the same three sector words. Nothing to reconcile here. -->
<section class="field photo hero" id="hero">
  <img class="bg" src="Images/hero-vessel.jpg" alt="" style="object-position:50% 50%">
  <div class="m11 hmark">ORION DIGITAL CORP. &nbsp;/&nbsp; NASDAQ &amp; TSX: ORIO</div>
  <div class="rail">
    <div class="grid12">
      <div class="htitle">
        <h1 class="h1">Building for an<span class="ind">AI-driven financial system.</span></h1>
      </div>
      <div class="hplate">
        <p class="p">Orion operates across Wealth, Payments and Consumer Lending, combining existing operating scale with multiple growth opportunities and disciplined capital allocation.</p>
      </div>
      <div class="hfoot">
        <div class="m13 lead">WEALTH &nbsp;&middot;&nbsp; PAYMENTS &nbsp;&middot;&nbsp; CONSUMER LENDING</div>
      </div>
    </div>
  </div>
</section>
'''

GLANCE = '''
<!-- 01 AT A GLANCE.
     The mockup puts its company paragraph in a band of its own between the hero and the
     figures. Here it is the lead of this section instead, because two paper bands with a
     hairline between them read as one section with a rule through it, not as two. The words
     are the mockup's, unchanged.
     Six figures, in the mockup's order. The grid classes place p1/p3/p5 on the top row and
     p2/p4/p6 on the row below, so the DOM order below is not the reading order: revenue,
     LTM EBITDA and cash read across the top, then shares, ownership and buyback beneath. -->
<section class="field paper secpad" id="at-a-glance">
  <div class="rail">
    <h2 class="h2">At a Glance</h2>
    <div class="grid12">
      <p class="p lead-intro">Orion Digital Corp. (NASDAQ: ORIO; TSX: ORIO) is emerging from a multi-year transition that has reshaped its businesses, capital allocation and financial profile. The Company is now entering a new phase focused on growth, cash generation and value realization across its three operating businesses.</p>
    </div>
    <div class="grid12 gwrap">
      <div class="gcell p1 sp"><span class="m11 lb">REVENUE</span><div class="v">C$67M</div><div class="m9">Annualized</div></div>
      <div class="gcell p2 dn sp"><span class="m11 lb">SHARES OUTSTANDING</span><div class="v">23.8M</div><div class="m9">June 30, 2026</div></div>
      <div class="gcell p3 sp"><span class="m11 lb">LTM ADJ. EBITDA<sup>1</sup></span><div class="v">C$8.9M</div><div class="m9">Twelve months ended June 30, 2026</div></div>
      <div class="gcell p4 dn sp"><span class="m11 lb">MANAGEMENT &amp; INSIDER OWNERSHIP <span class="tip">i</span></span><div class="v">&gt;20%</div></div>
      <div class="gcell p5 sp"><span class="m11 lb">CASH &amp; INVESTMENTS<sup>2</sup> <span class="tip">i</span></span><div class="v">C$35M</div><div class="m9">June 30, 2026</div></div>
      <div class="gcell p6 dn sp"><span class="m11 lb">SHARES RETIRED SINCE 2022 <span class="tip">i</span></span><div class="v">~8%</div></div>
    </div>
  </div>
</section>
'''

BIZ = '''
<!-- 02 THREE BUSINESSES. DISTINCT ROLES.
     The mockup's own section label, which V3 had carried as a display sentence under an
     eyebrow reading THREE OPERATING BUSINESSES. There is one label now, in the eyebrow,
     because the mockup has one.
     Two things the mockup adds to each cell: a role line (the business's job in the group)
     and a shorter description. Two things it removes: V3's longer written descriptions and,
     from the Mogo cell, the lending facility pair, which now lives behind the balance sheet
     card in 04. The role line sits at the top of the body rather than in a row of its own,
     so the cells keep the six-track subgrid they were aligned on.
     The role separator in the mockup is an em dash. The house rule bans it in copy, so it is
     a hyphen here; it is the one glyph on the page that is not the mockup's. -->
<section class="field photo mid secpad" id="businesses">
  <img class="bg" src="Images/ground-towers.jpg" alt="" style="object-position:50% 50%">
  <div class="rail">
    <h2 class="h2">Three Businesses. Distinct Roles.</h2>
    <div class="grid12">
      <div class="bsheet">
        <div class="bcell">
          <img class="cellbg" src="Images/cell-veil.jpg" alt="">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Intelligent Investing</div>
              <div class="m9 bcat">CANADIAN WEALTH</div>
            </div>
            <span class="bmark"><svg viewBox="0 0 15 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Intelligent Investing"><path d="M5.59903 0H7.79315L2.19412 17.6523H0L5.59903 0Z" fill="currentColor"/><path d="M12.8061 0H15.0002L9.40115 17.6523H7.20703L12.8061 0Z" fill="currentColor"/></svg></span>
          </div>
          <div class="b-fig f1"><div class="m11">Assets</div><div class="v">C$545M</div></div>
          <div class="b-note m9">+18% YoY</div>
          <div class="b-body">
            <div class="m11 brole">WEALTH - GROWTH</div>
            <p class="p b-desc">New investing platform commercially launched July 2026.</p>
          </div>
          <a class="link push" href="https://www.intelligentinvesting.ai/" target="_blank" rel="noopener">EXPLORE WEALTH{ARR}</a>
        </div>
        <div class="bcell">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Carta Worldwide</div>
              <div class="m9 bcat">EUROPEAN PAYMENTS INFRASTRUCTURE</div>
            </div>
            <span class="bmark carta"><img src="logos/carta-black.svg" alt="Carta Worldwide"></span>
          </div>
          <div class="b-fig f1"><div class="m11">Annual payments volume</div><div class="v">&gt;C$11B</div></div>
          <div class="b-fig f2"><div class="m11">End users through clients</div><div class="v">&gt;4M</div></div>
          <div class="b-body">
            <div class="m11 brole">PAYMENTS - GROWTH + STRATEGIC VALUE</div>
            <p class="p b-desc">Focused on growth following several years of technology investment.</p>
          </div>
          <a class="link push" href="https://cartaworldwide.com/" target="_blank" rel="noopener">EXPLORE PAYMENTS{ARR}</a>
        </div>
        <div class="bcell">
          <div class="bhead">
            <div class="bid">
              <div class="t22 bname">Mogo</div>
              <div class="m9 bcat">CANADIAN CONSUMER LENDING</div>
            </div>
            <span class="bmark"><img src="logos/mogo-black.svg" alt="Mogo"></span>
          </div>
          <div class="b-fig f1"><div class="m11">Gross loans receivable</div><div class="v">C$75.4M</div></div>
          <div class="b-body">
            <div class="m11 brole">LENDING - CASH + RETURNS</div>
            <p class="p b-desc">Managed around returns and capital payback.</p>
          </div>
          <a class="link push" href="https://www.mogo.ca/" target="_blank" rel="noopener">EXPLORE LENDING{ARR}</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''.replace("{ARR}", ARR)

REST = """
<!-- 03 DEMONSTRATING EARNINGS & CASH GENERATION.
     The same three figures V3 carried, in the mockup's order: the quarter first, then the
     quarter's cash, then the trailing year. The footnote on core operating cash moves from 1
     to 3, following the mockup's footnote scheme. -->
<section class="field paper secpad" id="snapshot">
  <div class="rail">
    <h2 class="h2">Demonstrating Earnings &amp; Cash Generation</h2>
    <div class="grid12 split">
      <figure class="picwrap">
        <div class="pic"><img src="Images/pic-night.jpg" alt=""></div>
      </figure>
      <div class="stack">
        <div class="f sp"><span class="m11 lb">Q2 ADJUSTED EBITDA<sup>1</sup></span><div class="v">C$3.3M</div><div class="s15">+115% Sequentially &middot; +70% YoY</div></div>
        <div class="f sp"><span class="m11 lb">Q2 CORE OPERATING CASH GENERATION<sup>3</sup></span><div class="v">C$5.1M</div><div class="s15">+29% YoY &middot; Excluding prior-year non-recurring receipt</div></div>
        <div class="f sp"><span class="m11 lb">LTM ADJUSTED EBITDA<sup>1</sup></span><div class="v">C$8.9M</div><div class="s15">Twelve months ended June 30, 2026</div></div>
        <div class="m9 foot">FY2026 Adjusted EBITDA guidance: C$6.0&ndash;7.0M. Q2 is not expected to represent a normalized earnings run rate.</div>
      </div>
    </div>
  </div>
</section>

<!-- 04 OPERATING SCALE VS. MARKET VALUE.
     This is the mockup's own juxtaposition and it is the same one V3 made: what the market
     pays, set beside what the business earns, with no multiple printed and the word
     undervalued never used. V3's two group labels are gone, because the mockup has none; the
     five readings sit in one run, the market capitalisation leading.
     The balance sheet is a card here rather than a section. That is the mockup's structure
     and it is a real change of argument: in V3 the correction was read before this number
     appeared. Recorded in RULES.md and on the confirmation list for Greg. -->
<section class="field secpad" id="valuation">
  <div class="vbg"><img src="Images/vground-pale.jpg" alt=""></div>
  <div class="rail">
    <div class="vsheet2">
      <div class="vsheetbg" aria-hidden="true"></div>
      <div class="vleft">
        <img class="vtex" src="Images/vpic-pale.jpg" alt="">
        <div class="vtitle">
          <h2 class="h2">Operating Scale vs. Market Value</h2>
          <div class="m9 asof">(as of Aug 19, 2026)</div>
        </div>
      </div>
      <div class="vright">
        <div class="dgroup">
          <div class="gbody">
            <div class="greads">
              <div class="gread lead"><div class="v">~C$33M</div><div class="s15">Market capitalization</div></div>
              <div class="gread"><div class="v">C$1.40</div><div class="s15">Share price &middot; TSX &middot; As of Aug 19, 2026</div></div>
              <div class="gread"><div class="v">~C$30M</div><div class="s15">Adjusted EV<sup>2</sup> <span class="tip">i</span> &middot; As of Aug 19, 2026</div></div>
              <div class="gread"><div class="v">C$8.9M</div><div class="s15">LTM Adj. EBITDA<sup>1</sup> &middot; Twelve months ended June 30, 2026</div></div>
              <div class="gread"><div class="v">C$6.0&ndash;7.0M</div><div class="s15">FY2026 Adj. EBITDA<sup>1</sup> guidance &middot; Outlook for fiscal year 2026</div></div>
            </div>
          </div>
        </div>
        <div class="cards one dg2">
          <div class="box line light">
            <a class="cardt" href="#"><!-- TODO stub --><span class="t22">Understand Our Balance Sheet</span>{ARR}</a>
            <p class="s15">Liquidity, lending facility<sup>1</sup> and capital structure.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 05 THE TRANSITION: THEN -> NOW.
     The mockup's four pairs are V3's four rows, unchanged, so the mirror stays: past on the
     left in --c-700, present on the right in white, the constant on the seam. The mockup adds
     a plus on each row that opens something; what it opens is not in the image, so the
     control is built and its content is marked unconfirmed rather than invented.
     Two cards follow, carrying what were sections 07 and 08 in V3. On black they are outlined
     rather than filled: the hero already puts a cream plate on dark and 04 puts a dark figure
     on white, and a third reversal would make it the page's pattern instead of its rhyme. -->
<section class="field blk secpad" id="transition">
  <div class="rail">
    <h2 class="h2">The Transition: Then &rarr; Now</h2>
    <div class="mirror">
      <div class="mrow mhead">
        <div class="m11 was">THEN</div>
        <div class="const" aria-hidden="true"></div>
        <div class="m11 is">NOW</div>
      </div>
      <div class="mrow">
        <div class="t22 was">Platform Build</div>
        <div class="const"><span class="m11">WEALTH</span></div>
        <div class="t22 is">Commercialization</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">Technology Investment</div>
        <div class="const"><span class="m11">PAYMENTS</span></div>
        <div class="t22 is">Growth</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">Volume</div>
        <div class="const"><span class="m11">LENDING</span></div>
        <div class="t22 is">Returns</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">WonderFi</div>
        <div class="const"><span class="m11">INVESTMENT PORTFOLIO</span></div>
        <div class="t22 is">Monetized</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
    </div>
    <div class="grid12">
      <div class="cards">
        <div class="box line">
          <a class="cardt" href="#"><!-- TODO stub --><span class="t22">What to Watch</span>{ARR}</a>
            <p class="s15">Key operating metrics and milestones across our businesses.</p>
        </div>
        <div class="box line">
          <a class="cardt" href="#"><!-- TODO stub --><span class="t22">Capital Allocation Framework</span>{ARR}</a>
            <p class="s15">Our approach to returns, evidence-based scaling and maximizing value per share.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 06 INVESTOR RESOURCES. Four documents and the contact, which is the mockup's five tiles.
     V3 carried three documents and offset the middle one; at four across the offset goes,
     because it was there to break a row of three. -->
<section class="field paper secpad" id="resources">
  <div class="rail">
    <h2 class="h2">Investor Resources</h2>
    <div class="items">
      <div class="it"><div class="t22">Q2 2026<br>Results</div><a class="link" href="#"><!-- TODO stub -->EARNINGS RELEASE{ARR}</a></div>
      <div class="it"><div class="t22">Q2 2026 Investor<br>Presentation</div><a class="link" href="#"><!-- TODO stub -->VIEW PRESENTATION{ARR}</a></div>
      <div class="it"><div class="t22">Q2 2026 MD&amp;A &amp;<br>Financial Statements</div><a class="link" href="#"><!-- TODO stub -->VIEW FILINGS{ARR}</a></div>
      <div class="it"><div class="t22">Latest Corporate<br>Presentation</div><a class="link" href="#"><!-- TODO stub -->VIEW PRESENTATION{ARR}</a></div>
      <div class="it"><div class="t22">Investor<br>Contact</div><a class="link" href="#"><!-- TODO stub -->GET IN TOUCH{ARR}</a></div>
    </div>
  </div>
</section>

<!-- 07 DISCLOSURES.
     Kept, though the mockup has none. Compliance outranks every other rule in this project and
     this content is frozen, so a mockup that omits the forward-looking, market data and
     holding-company paragraphs is read as a mockup that did not draw them, not as a decision
     to drop them.
     The footnote scheme is the mockup's: 1 non-IFRS measures, 2 Adjusted EV, 3 excluding the
     prior-year receipt. Two things the mockup leaves unresolved are marked rather than fixed
     silently: it prints a 2 on both Cash & Investments and Adjusted EV while listing only one
     note 2, and it dates the Adjusted EBITDA outlook to July 30, 2025 for a fiscal 2026
     guidance. -->
<footer class="field blk secpad" id="disclosures">
  <!-- The mockup's footer, and only that: one footnote line, the Non-IFRS link, the company
       block. Our own draft forward-looking and market-data paragraphs, and the live site's
       social row and legal paragraph, are not in the mockup and are not here.
       Two things the mockup leaves open are marked, not fixed: the outlook date reads 2025 for
       a fiscal 2026 guidance, and note 2 is printed on both Cash & Investments and Adjusted EV
       while the list defines it for Adjusted EV alone. -->
  <div class="rail">
    <div class="fstrip">
      <p class="m9 fnline"><sup>1</sup>Non-IFRS measures. &nbsp;<sup>2</sup>Adjusted EV is a non-IFRS measure. &nbsp;<sup>3</sup>Excluding prior-year non-recurring receipt.<br>Q2 2026 MD&amp;A for definitions, reconciliations and additional information. Adjusted EBITDA outlook provided July 30, 2025.</p>
      <a class="link" href="#"><!-- TODO stub -->NON-IFRS MEASURES &amp; RECONCILIATIONS <span class="tip">i</span></a>
      <div class="fid">
        <div class="m13">ORION DIGITAL CORP.</div>
        <div class="m9">TSX: ORIO &nbsp;&nbsp; NASDAQ: ORIO</div>
        <div class="m9"><a href="https://oriondigital.com">oriondigital.com</a></div>
      </div>
    </div>
    <!-- The live site's own footer block, verbatim from orion-digital.com. The mockup does
         not draw it; it is published wording rather than a draft, which is why it is here
         when the forward-looking and market-data paragraphs are not. -->
    <div class="fsite">
      <div class="soc-row"><a class="soc" href="#" aria-label="Facebook"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><path d="M13 8a5 5 0 1 0-5.8 4.94v-3.5H5.9V8h1.3V6.87c0-1.28.76-1.99 1.93-1.99.56 0 1.14.1 1.14.1v1.26h-.64c-.64 0-.84.4-.84.8V8h1.43l-.23 1.44H9.5v3.5A5 5 0 0 0 13 8Z" fill="#000"/></svg></a><a class="soc" href="#" aria-label="Instagram"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="3.2" y="3.2" width="9.6" height="9.6" rx="2.6" fill="none" stroke="#000" stroke-width="1"/><circle cx="8" cy="8" r="2.3" fill="none" stroke="#000" stroke-width="1"/><circle cx="11.1" cy="4.9" r="0.6" fill="#000"/></svg></a><a class="soc" href="#" aria-label="X"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><path d="M4 4l8 8M12 4l-8 8" stroke="#000" stroke-width="1.1"/></svg></a><a class="soc" href="#" aria-label="LinkedIn"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="3.4" y="6.4" width="1.9" height="6.2" fill="#000"/><circle cx="4.35" cy="3.9" r="1.1" fill="#000"/><path d="M7.2 6.4h1.8v.95c.4-.6 1.1-1.05 2.1-1.05 1.7 0 2.5 1.1 2.5 2.9v3.4h-1.9V9.5c0-.9-.3-1.5-1.1-1.5-.7 0-1.1.5-1.3 1v3.6H7.2z" fill="#000"/></svg></a><a class="soc" href="#" aria-label="YouTube"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="2.8" y="4.6" width="10.4" height="6.8" rx="2" fill="none" stroke="#000" stroke-width="1"/><path d="M7 6.7v3.6l3.2-1.8z" fill="#000"/></svg></a></div>
      <p class="m9 flegal">&copy; 2026 Orion Digital Corp. (formerly Mogo Inc.). All rights reserved. Orion Digital Corp. is a holding company. Its subsidiaries operate independently and are each subject to their own regulatory requirements. Orion Digital Corp. itself is not registered or licensed under securities, lending, or other financial services laws and regulations. Certain subsidiaries of Orion Digital Corp. are separately registered and regulated in Canada and conduct business only through their respective legal entities. Information on this site is for general information only and does not constitute an offer or solicitation. For product-specific terms and regulatory disclosures, see the applicable subsidiary websites and terms of service.</p>
    </div>
  </div>
</footer>

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
    ['#at-a-glance .gcell .v',        'a-val',  60, 'self'],
    ['#businesses .bcell .v',         'a-val',  80, 'section'],
    ['#snapshot .stack .f .v',        'a-val',  80, 'self'],
    ['#valuation .gread .v',          'a-val',  70, 'section'],
    ['#resources .it',                'a-rise', 60, 'self']
  ];
  var WIPE = [
    ['#businesses .bcell', 'down', 100],
    ['#valuation .vsheet2', 'left',  0]
  ];
  var LAG = [
    ['#hero > .bg',        160, 'page'],
    ['#businesses > .bg',   60, 'element'],
    ['#businesses .cellbg', 30, 'element'],
    ['#valuation .vbg img', 80, 'element'],
    ['#valuation .vtex',    34, 'element'],
    ];
  var ZOOM = [
    ['#snapshot .pic img', 1.05]
  ];

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
io.open(os.path.join(ROOT, "V4", "index.html"), "w", encoding="utf-8").write(out)
print("wrote V4/index.html", len(out), "bytes")
