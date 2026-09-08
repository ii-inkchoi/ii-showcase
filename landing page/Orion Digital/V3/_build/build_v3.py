# Builds V3/index.html. The nav logo SVG is lifted verbatim from V2 rather than retyped.
import io, os, re
ROOT = r"C:\Users\p0107\OneDrive\바탕 화면\II Work\Product Design_work files\Prototype\website\Orion Digital Website"
v2 = io.open(os.path.join(ROOT, "V2", "index.html"), encoding="utf-8").read()
nav = re.search(r'<nav class="nav">.*?</nav>', v2, re.S).group(0)
nav = nav.replace('shared/v2.css', 'shared/v3.css')
assert '    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">C$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>' in nav
nav = nav.replace('    <div class="qstrip">\n      <div class="qline"><span class="qlabel">TSX: ORIO</span><span class="qv unc">C$1.40</span><span class="qd">+0.03</span><span class="qp">+2.19%</span></div>\n      <div class="qline"><span class="qlabel">NASDAQ: ORIO</span><span class="qv unc">US$1.01</span><span class="qd">+0.02</span><span class="qp">+2.02%</span></div>\n      <div class="qasof">As of 2026-08-12</div>\n    </div>', '    <div class="qstrip">\n      <div class="qrows">\n        <div class="qrow"><span class="qex">TSX</span><span class="qv unc"><span class="qc">C$</span><span class="qn">1.40</span></span><span class="qp">+2.19%</span></div>\n        <div class="qrow"><span class="qex">NASDAQ</span><span class="qv unc"><span class="qc">US$</span><span class="qn">1.01</span></span><span class="qp">+2.02%</span></div>\n      </div>\n      <span class="qasof">As of 2026-08-12</span>\n    </div>', 1)


ARR = ('<svg class="arr" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
       '<path d="M4.5 11.5L11.5 4.5" stroke="currentColor" stroke-width="1.1"/>'
       '<path d="M5.5 4.5H11.5V10.5" stroke="currentColor" stroke-width="1.1"/></svg>')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orion Digital Corp. - Investor Overview (V3 role study)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="shared/v3.css">
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
<!-- 00 HERO — DECLARATION.
     The photograph is the ground. The title stands on it at full size, and one small cream
     plate at the lower right carries the paragraph. Two elements at opposite ends of the
     weight scale with the ground running uninterrupted between them.
     The title was boxed first, in a 6-column plate, and it failed: 43px display type in a
     369px measure broke into four lines and the plate had to grow until it was a band again.
     Either the type is large or it is boxed, not both, unless it takes the whole rail. -->
<section class="field photo hero" id="hero">
  <img class="bg" src="Images/hero-vessel.jpg" alt="" style="object-position:50% 50%">
  <div class="m11 hmark">ORION DIGITAL CORP. &nbsp;/&nbsp; NASDAQ &amp; TSX: ORIO</div>
  <div class="rail">
    <div class="grid12">
      <div class="htitle">
        <!-- No label over the headline. It read as furniture, and it was also the only tier
             on this hero that the ground's exposure had to be lowered for: a 9px label over
             the brightest part of the frame, measuring 4.23 against a 4.5 floor. Removing it
             put the window back up to 4-124 and the frame got its highlights back. -->
        <h1 class="h1">Building for an<span class="ind">AI-driven financial system.</span></h1>
      </div>
      <div class="hplate">
        <p class="p">Orion operates across Wealth, Payments and Consumer Lending, combining existing operating scale with multiple growth opportunities and disciplined capital allocation.</p>
      </div>
      <div class="hfoot">
        <div class="m13 lead">WEALTH &nbsp;&middot;&nbsp; PAYMENTS &nbsp;&middot;&nbsp; CONSUMER LENDING</div>
        <!-- "Figures as at June 30, 2026 unless stated" was here and is gone. The hero
             carries no figures, so it qualified nothing; every figure on the page already
             states its own date; and it was the only "as at" on a page that says "As of"
             everywhere else. -->
      </div>
    </div>
  </div>
</section>
'''

GLANCE = '''
<!-- 01 AT A GLANCE — EVIDENCE.
     Paper, grain, nothing else. No sheet, no rules, no photograph. The section is
     deliberately undesigned: it is the quiet between the hero and the businesses, and a
     page that composes everywhere composes nothing. Six figures on the 12-column grid,
     the second row inset by one column so the block does not settle into a table. -->
<section class="field paper secpad" id="at-a-glance">
  <div class="rail">
    <div class="eyeb"><span class="n">01</span><span>AT A GLANCE</span></div>
    <div class="grid12 gwrap">
      <div class="gcell p1 sp"><span class="m9 ix">[01.1]</span><span class="m11 lb">REVENUE</span><div class="v unc">C$67M</div><div class="m9">Annualized</div></div>
      <div class="gcell p2 dn sp"><span class="m9 ix">[01.2]</span><span class="m11 lb">SHARES OUTSTANDING</span><div class="v unc">23.8M</div><div class="m9">June 30, 2026</div></div>
      <div class="gcell p3 sp"><span class="m9 ix">[01.3]</span><span class="m11 lb">LTM ADJ. EBITDA<sup>1</sup></span><div class="v">C$8.9M</div><div class="m9">Twelve months ended June 30, 2026</div></div>
      <div class="gcell p4 dn sp"><span class="m9 ix">[01.4]</span><span class="m11 lb">INSIDER OWNERSHIP</span><div class="v unc">&gt;20%</div><div class="m9">Management and insiders</div></div>
      <div class="gcell p5 sp"><span class="m9 ix">[01.5]</span><span class="m11 lb">CASH &amp; INVESTMENTS<sup>2</sup></span><div class="v unc">C$34.8M</div><div class="m9">June 30, 2026</div></div>
      <div class="gcell p6 dn sp"><span class="m9 ix">[01.6]</span><span class="m11 lb">SHARES RETIRED</span><div class="v unc">~8%</div><div class="m9">Since 2022</div></div>
    </div>
  </div>
</section>
'''

BIZ = '''
<!-- 02 THREE OPERATING BUSINESSES / THE THREE.
     The ruled sheet, restored. The three horizontal registers built on 2026-09-05 were
     reviewed as worse than this and are gone; the register CSS is left in the stylesheet
     marked superseded so the attempt is on the record rather than repeated.
     This is the only sheet on the page. It spans 10 of 12 columns from column 2, so the
     photographic ground runs down both sides of it, which is the whole difference between
     an object standing on a ground and a band of different fill.
     One sheet split by hairlines, not three cards. Equal widths, unequal insides. The
     centre column is mostly empty on purpose: it is the breath that stops the row reading
     as tiles, and for Carta the emptiness is the subject, since the business carries other
     people's volume rather than its own balance sheet. -->
<section class="field photo mid secpad" id="businesses">
  <!-- Not wrapped for a sticky ground, though it was tried. A sticky ground can only travel
       the difference between its section and the viewport, and this section is 1030px tall
       against a 900px frame: 130px of travel for a 900px photograph, which is less than the
       lag it already has. The reference gets its overlap by pinning inside a document
       stretched to 8155px; on sections a viewport tall there is nothing to pin. -->
  <img class="bg" src="Images/ground-towers.jpg" alt="" style="object-position:50% 50%">
  <div class="rail">
    <div class="eyeb"><span class="n">02</span><span>THREE OPERATING BUSINESSES</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Three businesses.<span class="ind">Distinct roles.</span></h2>
    <div class="grid12">
      <div class="bsheet">
        <div class="bcell">
          <img class="cellbg" src="Images/cell-veil.jpg" alt="">
          <div class="bhead">
            <div class="bid">
              <div class="m9">[02.1]</div>
              <div class="t22 bname">Intelligent Investing</div>
              <div class="m9 bcat">CANADIAN WEALTH</div>
            </div>
            <span class="bmark"><svg viewBox="0 0 15 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Intelligent Investing"><path d="M5.59903 0H7.79315L2.19412 17.6523H0L5.59903 0Z" fill="currentColor"/><path d="M12.8061 0H15.0002L9.40115 17.6523H7.20703L12.8061 0Z" fill="currentColor"/></svg></span>
          </div>
          <div class="b-fig f1"><div class="m11">Assets under administration</div><div class="v">C$545.3M</div></div>
          <div class="b-note m9">+18% YoY</div>
          <div class="b-body">
            <p class="p b-desc">Built for an AI world where information is increasingly abundant and investment decision quality becomes more important.</p>
          <div class="m9" style="margin-top:calc(24 * var(--u))">Commercially launched July 2026</div>
          </div>
          <a class="link push" href="#"><!-- TODO stub -->EXPLORE WEALTH{ARR}</a>
        </div>
        <div class="bcell">
          <div class="bhead">
            <div class="bid">
              <div class="m9">[02.2]</div>
              <div class="t22 bname">Carta Worldwide</div>
              <div class="m9 bcat">EUROPEAN PAYMENTS INFRASTRUCTURE</div>
            </div>
            <span class="bmark carta"><img src="logos/carta-black.svg" alt="Carta Worldwide"></span>
          </div>
          <div class="b-fig f1"><div class="m11">Annual payments volume</div><div class="v">&gt;C$11B</div></div>
          <div class="b-fig f2"><div class="m11">End users through clients</div><div class="v unc">&gt;5M</div></div>
          <div class="b-body">
            <p class="p b-desc">Authorization technology supporting established payment programs across Europe.</p>
          </div>
          <a class="link push" href="#"><!-- TODO stub -->EXPLORE PAYMENTS{ARR}</a>
        </div>
        <div class="bcell">
          <div class="bhead">
            <div class="bid">
              <div class="m9">[02.3]</div>
              <div class="t22 bname">Mogo</div>
              <div class="m9 bcat">CANADIAN CONSUMER LENDING</div>
            </div>
            <span class="bmark"><img src="logos/mogo-black.svg" alt="Mogo"></span>
          </div>
          <div class="b-fig f1"><div class="m11">Gross loans receivable</div><div class="v">C$75.4M</div></div>
          <div class="b-sep"><div class="pairline"><span class="ln"></span><span class="gl">&#8597;</span><span class="ln"></span></div></div>
          <div class="b-fig f2"><div class="m11">Related lending facility</div><div class="v">C$49.8M</div></div>
          <div class="b-body">
            <p class="p b-desc">Established lending platform focused on risk-adjusted returns, capital efficiency and cash generation.</p>
          </div>
          <a class="link push" href="#"><!-- TODO stub -->EXPLORE LENDING{ARR}</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''.replace("{ARR}", ARR)

REST = """
<!-- 03 / 04 / 05 THE ARGUMENT RUN. Paper across all three, no photograph and no sheet.
     This is where the page puts nothing between the reader and the company. The order is
     Greg's and is load bearing: the balance sheet correction (04) has to land before the
     market's number (05) appears, because the point is that the juxtaposition does the work
     without the page ever saying the word. -->
<section class="field paper secpad" id="snapshot">
  <div class="rail">
    <div class="eyeb"><span class="n">03</span><span>OPERATING &amp; FINANCIAL SNAPSHOT</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Orion produces earnings<span class="ind">and cash. Not projections.</span></h2>
    <div class="grid12 split">
      <!-- The section's claim is earnings and cash rather than projections, so the picture
           is the record itself, accumulated: bundles of filed paper on shelves.
           Two frames were refused before it. An abstract concrete gap had no subject at all
           and needed brightness 1.62 to survive cream, which was the tell. A photograph of
           someone writing in a notebook had a subject but read as personal journaling, and
           it illustrated the sentence rather than standing beside it: a person performing
           the concept is the most literal move available.
           Not a card index or a drawer, though the library has better ones: 08's Wealth band
           is now filing drawers, and two pictures of the same subject on one page make it
           the page's motif rather than either section's point.
           No caption. It carried a stand-in note, and a picture that claims nothing needs no
           line under it: this is context, not Orion's own premises. -->
      <figure class="picwrap">
        <div class="pic"><img src="Images/pic-night.jpg" alt=""></div>
      </figure>
      <div class="stack">
        <div class="f sp"><span class="m9 ix">[03.1]</span><span class="m11 lb">LTM ADJUSTED EBITDA<sup>1</sup></span><div class="v">C$8.9M</div><div class="s15">Last twelve months ended June 30, 2026</div></div>
        <div class="f sp"><span class="m9 ix">[03.2]</span><span class="m11 lb">Q2 ADJUSTED EBITDA<sup>1</sup></span><div class="v">C$3.3M</div><div class="s15">+115% sequentially &middot; +70% YoY</div></div>
        <div class="f sp"><span class="m9 ix">[03.3]</span><span class="m11 lb">Q2 CORE CASH<sup>1</sup></span><div class="v">C$5.1M</div><div class="s15">+29% YoY excl. prior-year receipt</div></div>
        <div class="m9 foot">FY2026 Adjusted EBITDA guidance: C$6.0&ndash;7.0M. Q2 is not expected to represent a normalized earnings run rate.</div>
      </div>
    </div>
  </div>
</section>

<section class="field paper secpad" id="balance-sheet">
  <div class="rail">
    <div class="eyeb"><span class="n">04</span><span>BALANCE SHEET</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">The lending facility<span class="ind">is not corporate debt.</span></h2>
    <div class="grid12">
      <div class="quad">
        <div class="box">
          <div class="sp"><span class="m9 ix">[04.1]</span><span class="m11 lb">CASH, RESTRICTED CASH, SECURITIES &amp; INVESTMENTS<sup>2</sup></span><div class="v unc">C$34.8M</div><div class="s15">June 30, 2026</div></div>
        </div>
        <!-- the one reversal after the hero. The hero puts a cream plate on dark; this puts
             a dark box on cream. One each way is a rhyme, a third would be a pattern. -->
        <div class="box inv">
          <div class="m9">[04.2]</div>
          <div class="m11" style="margin-top:calc(14 * var(--u))">Gross loans receivable</div><div class="v">C$75.4M</div>
          <div class="pairline"><span class="ln"></span><span class="gl">&#8597;</span><span class="ln"></span></div>
          <div class="m11">Related lending facility</div><div class="v">C$49.8M</div>
          <div class="m9" style="margin-top:calc(16 * var(--u))">Directly finances the consumer loan portfolio</div>
        </div>
        <div class="box">
          <div class="sp"><span class="m9 ix">[04.3]</span><span class="m11 lb">CORPORATE DEBENTURES</span><div class="v">~C$31M</div><div class="s15">Corporate debt</div></div>
        </div>
      </div>
    </div>
    <div class="grid12 disc"><p class="p alignbox">The lending credit facility directly finances Orion's consumer loan portfolio. Management evaluates this portfolio funding separately from corporate obligations when assessing liquidity and leverage, while recognizing the facility's credit-performance, covenant and liquidity risks.</p></div>
  </div>
</section>

<!-- 05 MARKET VALUATION.
     Grey textured ground, a white sheet on the rail, and the half disc cut OUT of the sheet
     rather than drawn on it: at full resolution the reference's disc is the same grey as the
     ground around its sheet, and the white stops at its edge. It is a hole, so it is built as
     one, with a mask on the sheet's white layer.
     The two go together. A hole only reads if there is something behind the sheet, which is
     why the grey ground comes back with it.
     Title left on the pale distressed texture, every figure right on white. -->
<section class="field secpad" id="valuation">
  <div class="vbg"><img src="Images/vground-pale.jpg" alt=""></div>
  <div class="rail">
    <div class="vsheet2">
      <div class="vsheetbg" aria-hidden="true"></div>
      <div class="vleft">
        <img class="vtex" src="Images/vpic-pale.jpg" alt="">
        <div class="vtitle">
          <div class="eyeb"><span class="n">05</span><span>MARKET VALUATION</span></div>
          <h2 class="h2" style="margin-top:calc(48 * var(--u))">This is what the market<span class="ind">currently values it at.</span></h2>
        </div>
      </div>
      <div class="vright">
        <!-- two groups, not five items: the three readings in the first are one subject
             read three ways, and so are the two in the second. -->
        <div class="dgroup">
          <span class="m9 ix">[05.1]</span>
          <div class="gbody">
            <div class="m11 glabel">WHAT THE MARKET PAYS</div>
            <div class="greads">
              <div class="gread lead"><div class="v unc">~C$27M</div><div class="s15">Market capitalization &middot; As of 2026-08-12</div></div>
              <div class="gread"><div class="v unc">C$1.12</div><div class="s15">Share price &middot; TSX &middot; As of 2026-08-12</div></div>
              <div class="gread"><div class="v unc">~C$23M</div><div class="s15">Adjusted enterprise value<sup>3</sup> &middot; As of 2026-08-12</div></div>
            </div>
          </div>
        </div>
        <div class="dgroup dg2">
          <span class="m9 ix">[05.2]</span>
          <div class="gbody">
            <div class="m11 glabel">WHAT THE BUSINESS EARNS<sup>1</sup></div>
            <div class="greads">
              <div class="gread lead"><div class="v">C$8.9M</div><div class="s15">Adjusted EBITDA &middot; Last twelve months ended June 30, 2026</div></div>
              <div class="gread"><div class="v">C$6.0&ndash;7.0M</div><div class="s15">Adjusted EBITDA &middot; FY2026 guidance</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 06 THE TRANSITION. Black, no photograph. After three paper sections the page needs a
     breath, and a flat black field is the cheapest one available.
     The layout is a mirror. Every other section on this page is anchored left, so the
     horizontal axis is the one axis the page has never used, and it is the only one that can
     still carry meaning: past on the left, present on the right, and the thing that did not
     change on the seam between them. The four rows share that seam, which draws a centre line
     down the section without anything being drawn.
     Size says nothing here, colour says everything: both states sit at t22 and the past is
     --c-700 while the present is white. The arrows are gone; the position is the arrow.
     Not borrowed from the reference: its two large discs. Section 05 already cuts a disc out
     of its sheet, and a second circle would make circles a pattern of the page rather than a
     single event. The mirror is taken, the disc is not. -->
<section class="field blk secpad" id="transition">
  <div class="rail">
    <div class="eyeb"><span class="n">06</span><span>THE TRANSITION</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Then, and now.</h2>
    <div class="mirror">
      <!-- The two states are told apart by colour and by side, and neither of those says
           WHICH side is the past. These name them once, in the title's own two words, and
           each header carries the colour of the column under it so the rule is learned on
           the first row instead of assumed. Replace with dates when Greg confirms the two
           reference points; the labels are the only thing that would change. -->
      <div class="mrow mhead">
        <div class="m11 was">THEN</div>
        <div class="const" aria-hidden="true"></div>
        <div class="m11 is">NOW</div>
      </div>
      <div class="mrow">
        <div class="t22 was">Platform build</div>
        <div class="const"><span class="m9 cn">[06.1]</span><span class="m11">WEALTH</span></div>
        <div class="t22 is">Commercialization</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">Technology investment</div>
        <div class="const"><span class="m9 cn">[06.2]</span><span class="m11">PAYMENTS</span></div>
        <div class="t22 is">Growth</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">Volume</div>
        <div class="const"><span class="m9 cn">[06.3]</span><span class="m11">LENDING</span></div>
        <div class="t22 is">Returns</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
      <div class="mrow">
        <div class="t22 was">WonderFi</div>
        <div class="const"><span class="m9 cn">[06.4]</span><span class="m11">INVESTMENT PORTFOLIO</span></div>
        <div class="t22 is">Monetized</div>
        <span class="mrule" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</section>

<!-- 07 CAPITAL ALLOCATION. Paper, no photograph: principles are evidence of discipline,
     not atmosphere. Four pillars two up, the second row inset by one column. -->
<section class="field paper secpad" id="capital-allocation">
  <div class="rail">
    <div class="eyeb"><span class="n">07</span><span>DISCIPLINED CAPITAL ALLOCATION</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Capital is allocated<span class="ind">against evidence.</span></h2>
    <div class="rows">
      <div class="prow">
        <div class="m9 n">[07.1]</div>
        <div class="ttl"><div class="t22">Financial flexibility</div><div class="m11">PROTECT LIQUIDITY AND DOWNSIDE</div></div>
        <p class="p body">Maintain financial flexibility sufficient to meet corporate obligations and support operating requirements.</p>
      </div>
      <div class="prow">
        <div class="m9 n">[07.2]</div>
        <div class="ttl"><div class="t22">Return-based deployment</div><div class="m11">CAPITAL MUST EARN ITS WAY IN</div></div>
        <p class="p body">Deploy Mogo lending capital based on expected returns, capital payback, credit performance and liquidity requirements.</p>
      </div>
      <div class="prow">
        <div class="m9 n">[07.3]</div>
        <div class="ttl"><div class="t22">Invest behind evidence</div><div class="m11">SCALE GROWTH AGAINST DEMONSTRATED ECONOMICS</div></div>
        <p class="p body">Increase Intelligent Investing investment on demonstrated economics, and pursue Carta above return thresholds.</p>
      </div>
      <div class="prow">
        <div class="m9 n">[07.4]</div>
        <div class="ttl"><div class="t22">Long-term value per share</div><div class="m11">EVERY USE OF CAPITAL COMPETES</div></div>
        <p class="p body">Evaluate internal investment, debt reduction and share repurchases based on expected risk-adjusted long-term per-share returns.</p>
      </div>
    </div>
  </div>
</section>

<!-- 08 THREE SOURCES OF UPSIDE. The third and last photograph. This is a claim about what
     comes next rather than a statement of what already happened, so it gets a ground.
     Typography only, no sheet: the tiers used here are t22, m11 and p, all of which hold on
     a dark photographic ground. Nothing at the m9 tier sits on the picture. -->
<section class="field blk secpad" id="upside">
  <div class="rail">
    <div class="eyeb"><span class="n">08</span><span>THREE SOURCES OF UPSIDE</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Each business has something<span class="ind">today, and something more.</span></h2>
    <div class="bands">
      <div class="band">
        <img class="bg" src="Images/band-1.jpg" alt="">
        <div class="bd">
          <span class="m11 num">[08.1]</span>
          <div class="t22">Wealth</div>
          <div class="m11">SCALE + COMMERCIALIZATION</div>
          <p class="p">C$545M established wealth platform with Intelligent Investing now commercially launched.</p>
        </div>
      </div>
      <div class="band">
        <img class="bg" src="Images/band-2.jpg" alt="">
        <div class="bd">
          <span class="m11 num">[08.2]</span>
          <div class="t22">Payments</div>
          <div class="m11">INFRASTRUCTURE + EXPANSION</div>
          <p class="p">C$11B annual payment volume with selective commercial and infrastructure opportunities.</p>
        </div>
      </div>
      <div class="band">
        <img class="bg" src="Images/band-3.jpg" alt="">
        <div class="bd">
          <span class="m11 num">[08.3]</span>
          <div class="t22">Consumer lending</div>
          <div class="m11">CASH + CAPITAL EFFICIENCY</div>
          <p class="p">Established lending platform managed around returns, payback and disciplined deployment.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="field paper secpad" id="resources">
  <div class="rail">
    <div class="eyeb"><span class="n">09</span><span>INVESTOR RESOURCES</span></div>
    <h2 class="h2" style="margin-top:calc(48 * var(--u))">Diligence should be effortless.</h2>
    <div class="grid12 items">
      <div class="it c1-3"><span class="m9 num">[09.1]</span><div class="t22">Q2 2026 Results</div><a class="link" href="#"><!-- TODO stub -->EARNINGS RELEASE{ARR}</a></div>
      <div class="it c5-3 drop"><span class="m9 num">[09.2]</span><div class="t22">Q2 2026 Investor Presentation</div><a class="link" href="#"><!-- TODO stub -->VIEW PRESENTATION{ARR}</a></div>
      <div class="it c9-3"><span class="m9 num">[09.3]</span><div class="t22">Q2 2026 MD&amp;A &amp; Financial Statements</div><a class="link" href="#"><!-- TODO stub -->VIEW FILINGS{ARR}</a></div>
    </div>
    <div class="offer">
      <div><div class="m11">[09.4] INVESTOR CONTACT</div><div class="t22">Questions about the filings or the quarter.</div></div>
      <a class="cta" href="#"><!-- TODO stub -->GET IN TOUCH</a>
    </div>
  </div>
</section>

<footer class="field blk secpad" id="disclosures">
  <div class="rail">
    <div class="eyeb"><span class="n">10</span><span>DISCLOSURES</span></div>
    <div class="fn-list">
      <div class="fn-row" id="fn1"><div class="m9">1</div><div class="m9">Adjusted EBITDA and core operating cash generation are non-IFRS measures. Refer to Orion Digital&rsquo;s Q2 2026 MD&amp;A for definitions, reconciliations and additional information. LTM Adjusted EBITDA represents Adjusted EBITDA for the twelve months ended June 30, 2026.</div></div>
      <div class="fn-row" id="fn2"><div class="m9">2</div><div class="m9">Includes C$23.3M of cash, C$1.8M of restricted cash, C$4.2M of marketable securities and C$5.6M of investments at June 30, 2026. <span class="unc">Components sum to C$34.9M against the C$34.8M shown. Unresolved.</span></div></div>
      <div class="fn-row" id="fn3"><div class="m9">3</div><div class="m9">Adjusted Enterprise Value is calculated using market capitalization plus corporate debt, less cash, restricted cash, marketable securities and investments, and excludes the lending credit facility that directly finances the Company&rsquo;s consumer loan portfolio. <span class="unc">[Reconciliation to be linked]</span> <span class="unc">Wording is Greg&rsquo;s conceptual version, not counsel-approved.</span></div></div>
    </div>
    <div class="divider">
      <div class="m11">Forward-Looking Information <span class="unc draft">DRAFT &middot; REQUIRES SECURITIES COUNSEL REVIEW BEFORE PUBLICATION</span></div>
      <p class="m9" style="margin-top:calc(16 * var(--u))">Certain statements on this page constitute forward-looking information under Canadian securities legislation and forward-looking statements within the meaning of applicable United States securities laws. These include, without limitation, statements regarding the Company&rsquo;s FY2026 Adjusted EBITDA outlook, anticipated growth and commercial expansion across its operating businesses, and its capital allocation intentions. Forward-looking information reflects management&rsquo;s current expectations and assumptions and is subject to known and unknown risks and uncertainties that may cause actual results to differ materially from those expressed or implied. Readers should refer to the risk factors described in Orion Digital&rsquo;s most recent MD&amp;A and Annual Information Form. The Company undertakes no obligation to update forward-looking information except as required by applicable law.</p>
    </div>
    <div class="divider">
      <div class="m11">Market Data <span class="unc draft">DRAFT &middot; REQUIRES SECURITIES COUNSEL REVIEW</span></div>
      <p class="m9" style="margin-top:calc(16 * var(--u))">Share price, market capitalization and Adjusted Enterprise Value are stated as of the date shown and are not updated in real time. Market data may be delayed. Nothing on this page constitutes an offer to sell or a solicitation to buy any security.</p>
    </div>
    <div class="divider foot-id">
      <div class="m13">ORION DIGITAL CORP.</div>
      <div class="m9" style="margin-top:calc(8 * var(--u))">NASDAQ: ORIO &middot; TSX: ORIO</div>
      <div class="soc-row"><a class="soc" href="#" aria-label="Facebook"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><path d="M13 8a5 5 0 1 0-5.8 4.94v-3.5H5.9V8h1.3V6.87c0-1.28.76-1.99 1.93-1.99.56 0 1.14.1 1.14.1v1.26h-.64c-.64 0-.84.4-.84.8V8h1.43l-.23 1.44H9.5v3.5A5 5 0 0 0 13 8Z" fill="#000"/></svg></a><a class="soc" href="#" aria-label="Instagram"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="3.2" y="3.2" width="9.6" height="9.6" rx="2.6" fill="none" stroke="#000" stroke-width="1"/><circle cx="8" cy="8" r="2.3" fill="none" stroke="#000" stroke-width="1"/><circle cx="11.1" cy="4.9" r="0.6" fill="#000"/></svg></a><a class="soc" href="#" aria-label="X"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><path d="M4 4l8 8M12 4l-8 8" stroke="#000" stroke-width="1.1"/></svg></a><a class="soc" href="#" aria-label="LinkedIn"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="3.4" y="6.4" width="1.9" height="6.2" fill="#000"/><circle cx="4.35" cy="3.9" r="1.1" fill="#000"/><path d="M7.2 6.4h1.8v.95c.4-.6 1.1-1.05 2.1-1.05 1.7 0 2.5 1.1 2.5 2.9v3.4h-1.9V9.5c0-.9-.3-1.5-1.1-1.5-.7 0-1.1.5-1.3 1v3.6H7.2z" fill="#000"/></svg></a><a class="soc" href="#" aria-label="YouTube"><!-- TODO stub, needs real Orion social URL --><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="var(--c-white)"/><rect x="2.8" y="4.6" width="10.4" height="6.8" rx="2" fill="none" stroke="#000" stroke-width="1"/><path d="M7 6.7v3.6l3.2-1.8z" fill="#000"/></svg></a></div>
      <!-- Verbatim from orion-digital.com, 2026-09-06. This resolves the open question this
           file used to carry here: whether the footer needs its own subsidiary reference
           alongside 02 linking out to Intelligent Investing. It does, and the live site's own
           wording is that reference: a holding-company disclaimer naming the "not registered
           or licensed" status directly, rather than pointing to II's IISI/IIWMI paragraphs. -->
      <p class="m9" style="margin-top:calc(16 * var(--u));max-width:calc((100% + 30 * var(--u)) / 12 * 10 - 30 * var(--u))">&copy; 2026 Orion Digital Corp. (formerly Mogo Inc.). All rights reserved. Orion Digital Corp. is a holding company. Its subsidiaries operate independently and are each subject to their own regulatory requirements. Orion Digital Corp. itself is not registered or licensed under securities, lending, or other financial services laws and regulations. Certain subsidiaries of Orion Digital Corp. are separately registered and regulated in Canada and conduct business only through their respective legal entities. Information on this site is for general information only and does not constitute an offer or solicitation. For product-specific terms and regulatory disclosures, see the applicable subsidiary websites and terms of service.</p>
      <div class="foot-links m9"><a href="#"><!-- TODO stub -->Privacy Policy</a><a href="#"><!-- TODO stub -->Disclaimers</a><a href="#"><!-- TODO stub -->Terms of Use</a></div>
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
    ['#capital-allocation .prow',     'a-rise', 80, 'self'],
    ['#upside .band .p',              'a-rise', 90, 'self'],
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
    ['#upside .band > .bg', 40, 'element']
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
io.open(os.path.join(ROOT, "V3", "index.html"), "w", encoding="utf-8").write(out)
print("wrote V3/index.html", len(out), "bytes")
