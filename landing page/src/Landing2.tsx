import { useEffect, useRef, useState } from 'react'

// ── Animation hook ────────────────────────────────────────────────────────────
function useInView(threshold = 0.15) {
  const ref = useRef<HTMLDivElement>(null)
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) { setVisible(true); obs.disconnect() } },
      { threshold }
    )
    obs.observe(el)
    return () => obs.disconnect()
  }, [threshold])

  return { ref, visible }
}

// ── Animated block ────────────────────────────────────────────────────────────
function Reveal({
  children,
  delay = 0,
  style,
}: {
  children: React.ReactNode
  delay?: number
  style?: React.CSSProperties
}) {
  const { ref, visible } = useInView()
  return (
    <div
      ref={ref}
      style={{
        opacity: visible ? 1 : 0,
        transform: visible ? 'translateY(0)' : 'translateY(22px)',
        transition: `opacity 0.9s cubic-bezier(0.16,1,0.3,1) ${delay}ms, transform 0.9s cubic-bezier(0.16,1,0.3,1) ${delay}ms`,
        ...style,
      }}
    >
      {children}
    </div>
  )
}


// ── Animated number matrix ────────────────────────────────────────────────────
function NumberMatrix({ height = 600 }: { height?: number }) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const rafRef = useRef<number>(0)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    const W = canvas.width
    const H = canvas.height
    const FONT_SIZE = 11
    const LINE_H = 17
    const COL_W = 115          // width of each data column block
    const NUM_COLS = Math.ceil(W / COL_W) + 1

    // Generate a repeating sequence of numbers per column (looks like price/tick data)
    function makeSequence(seed: number): string[] {
      const rows: string[] = []
      let v = 1000 + (seed * 137) % 9000
      for (let i = 0; i < 40; i++) {
        v = v + Math.floor(Math.sin(seed * 0.3 + i * 0.7) * 23)
        const digits = v.toString().split('').join(' ')
        rows.push(digits)
      }
      return rows
    }

    const columns = Array.from({ length: NUM_COLS }, (_, i) => ({
      seq: makeSequence(i * 7 + 3),
      // each column scrolls at a slightly different speed
      speed: 0.18 + (i % 5) * 0.06,
      offset: (i * 47) % (LINE_H * 40),
    }))

    let running = true

    function draw(ts: number) {
      if (!running) return
      ctx.clearRect(0, 0, W, H)
      ctx.font = `${FONT_SIZE}px 'Courier New', monospace`

      for (let ci = 0; ci < NUM_COLS; ci++) {
        const col = columns[ci]
        col.offset = (col.offset + col.speed) % (LINE_H * col.seq.length)
        const x = ci * COL_W

        for (let ri = 0; ri < col.seq.length + 2; ri++) {
          const y = ri * LINE_H - col.offset
          if (y < -LINE_H || y > H + LINE_H) continue

          const seqIdx = ri % col.seq.length
          const text = col.seq[seqIdx]

          // fade at top and bottom edges
          const fade = Math.min(y / 60, 1) * Math.min((H - y) / 60, 1)
          const alpha = Math.max(0, Math.min(1, fade)) * 0.8

          ctx.fillStyle = `rgba(140, 140, 140, ${alpha})`
          ctx.fillText(text, x, y)
        }
      }

      rafRef.current = requestAnimationFrame(draw)
    }

    rafRef.current = requestAnimationFrame(draw)
    return () => { running = false; cancelAnimationFrame(rafRef.current) }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      width={1440}
      height={height}
      style={{ display: 'block', width: '100%', height: '100%' }}
    />
  )
}

// ── Data ──────────────────────────────────────────────────────────────────────
const allSections: { number: string; title: string; body: string[]; indent: boolean }[] = [
  {
    number: 'NO. 001',
    title: 'A statement of position',
    body: [
      'We are not here to make investing feel easy.\nEasy is what produces delusion.\nDelusion is what produces losses.\nIntelligent Investing exists to remove illusion, not replace it with a better story.',
    ],
    indent: false,
  },
  {
    number: 'NO. 002',
    title: 'The shift',
    body: [
      'Investing is not trading. It is capital allocation.',
      'The difference is not semantic.',
      'It is the difference between: reacting and deciding',
    ],
    indent: false,
  },
  {
    number: 'NO. 003',
    title: 'What this is',
    body: [
      'Intelligent Investing is a discipline-first capital allocation system. Designed to compound capital over decades.',
      'It is not a tool. It is a system you operate inside.',
      'Reduce behavioral error. Enforce long-term thinking. Slow decision-making where speed destroys outcomes. Align structure with compounding.',
    ],
    indent: false,
  },
  {
    number: 'NO. 004',
    title: 'The system',
    body: [
      'This is not a collection of features.',
      'It is a structured environment for allocating capital deliberately.',
      'Inside it:',
      'A disciplined core portfolio\nA structured decision process\nA professional research environment\nBehavioral design that enforces discipline',
      'Each element exists for one reason: to support long-term compounding.',
    ],
    indent: true,
  },
  {
    number: 'NO. 005',
    title: 'How it works',
    body: [
      'Capital can be allocated in different ways within the system.',
      'A disciplined, market-based portfolio can be implemented directly. It exists as a default—because most investors do not outperform over time.',
      'Active positions can be built alongside it. Treated as a craft, not a shortcut.',
      'Every decision is expected to be:',
      'thought through\ndocumented\nand understood in terms of risk',
      'The system does not restrict action. It makes the consequences of action visible.',
    ],
    indent: false,
  },
  {
    number: 'NO. 006',
    title: 'The environment you are operating in',
    body: [
      'Markets are not fair.',
      'Narrative\nIncentives\nOverconfidence\nShort-term feedback loops',
      'Most participants are reacting. A small minority is allocating.',
      'This platform is designed for the latter.',
    ],
    indent: false,
  },
  {
    number: 'NO. 007',
    title: 'Core system principles',
    body: [
      'Discipline over prediction. Outcomes improve when error is reduced, not when forecasts multiply.',
      'Structure over willpower. Good intentions fail without constraints.',
      'Time as the primary edge. Compounding requires duration most cannot tolerate.',
      'Friction as intelligence. If a decision feels too easy, it usually is.',
    ],
    indent: false,
  },
  {
    number: 'NO. 008',
    title: 'The behavioral layer',
    body: [
      'Most underperformance is not analytical. It is behavioural.',
      'This system is built to surface:',
      'Overconfidence\nImpatience\nNarrative chasing\nInconsistent decision-making',
      'And to apply pressure in the opposite direction.',
      'Not through motivation. Through design.',
    ],
    indent: true,
  },
  {
    number: 'NO. 009',
    title: 'Research & analysis',
    body: [
      'Every membership includes access to Fiscal.ai, a professional-grade research environment.',
      'Most investors trade based on price and headlines. Serious investors analyze businesses.',
      'The AI supports analysis. It does not make decisions.',
    ],
    indent: false,
  },
  {
    number: 'NO. 010',
    title: 'Compounding',
    body: [
      'Compounding is not driven by activity.',
      'It is the result of disciplined capital allocation sustained over time.',
      'Few investors can maintain that discipline.',
      'This system exists to make it possible.',
    ],
    indent: false,
  },
  {
    number: 'NO. 011',
    title: 'Mastery over moments',
    body: [
      'This platform is built around long arcs, not short wins.',
      'Learning compounds. Judgment compounds. Character compounds.',
      'The investor improves. The portfolio follows.',
    ],
    indent: false,
  },
  {
    number: 'NO. 012',
    title: 'Who this is for',
    body: [
      'People who:',
      'Think in decades\nDistrust easy answers\nValue restraint\nPrefer being right over being entertained',
    ],
    indent: true,
  },
  {
    number: 'NO. 013',
    title: 'Who this is not for',
    body: [
      'People looking for:',
      'Excitement\nShortcuts\nConstant validation\nSomeone to blame',
      'If you are looking for reassurance, this is not the place.',
      'If you value clarity, welcome.',
    ],
    indent: true,
  },
  {
    number: 'NO. 014',
    title: 'Aligned incentives',
    body: [
      '$20 per month\nCancel anytime',
      '0.10% annual fee on managed portfolios',
      'No commissions\nNo FX markup',
      'Your success is our retention model.',
    ],
    indent: false,
  },
]

// ── Section component ─────────────────────────────────────────────────────────
function Section({ number, title, body, indent }: {
  number: string; title: string; body: string[]; indent: boolean
}) {
  return (
    <Reveal>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 28, maxWidth: 650, paddingLeft: indent ? 127 : 0 }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
          <span style={{ fontFamily: "'Chakra Petch', sans-serif", fontSize: 18, fontWeight: 400, color: '#5c5c5c' }}>
            {number}
          </span>
          <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#c7c7c7', letterSpacing: '0px', lineHeight: 1.4 }}>
            {title}
          </span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
          {body.map((text, i) => (
            <p key={i} className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#929292', margin: 0, letterSpacing: '0px', lineHeight: 1.55, whiteSpace: 'pre-line', opacity: 0.9 }}>
              {text}
            </p>
          ))}
        </div>
      </div>
    </Reveal>
  )
}

// ── Icons ─────────────────────────────────────────────────────────────────────
function Logo() {
  return (
    <svg width="17" height="20" viewBox="0 0 17 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M6.34371 0H8.82965L2.48594 20H0L6.34371 0Z" fill="white"/>
      <path d="M14.5097 0H16.9957L10.652 20H8.16602L14.5097 0Z" fill="white"/>
    </svg>
  )
}

function HamburgerIcon() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10, cursor: 'pointer', padding: '10px 0' }}>
      <div style={{ width: 68, height: 0.5, background: '#929292' }} />
      <div style={{ width: 68, height: 0.5, background: '#929292' }} />
    </div>
  )
}

function TwitterIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.259 5.63 5.905-5.63zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z" fill="#565B5E" />
    </svg>
  )
}

function InstagramIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
      <rect x="2" y="2" width="20" height="20" rx="5" stroke="#565B5E" strokeWidth="1.5" fill="none" />
      <circle cx="12" cy="12" r="4.5" stroke="#565B5E" strokeWidth="1.5" fill="none" />
      <circle cx="17.5" cy="6.5" r="1.5" fill="#565B5E" />
    </svg>
  )
}

function TikTokIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
      <path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.18 8.18 0 004.78 1.52V6.75a4.85 4.85 0 01-1.01-.06z" fill="#565B5E" />
    </svg>
  )
}

function YouTubeIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
      <path d="M22.54 6.42a2.78 2.78 0 00-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 001.46 6.42 29 29 0 001 12a29 29 0 00.46 5.58 2.78 2.78 0 001.95 1.96C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 001.95-1.96A29 29 0 0023 12a29 29 0 00-.46-5.58zM9.75 15.02V8.98L15.5 12l-5.75 3.02z" fill="#565B5E" />
    </svg>
  )
}

// ── Page ──────────────────────────────────────────────────────────────────────
export default function Landing2() {
  // Hero initial load animation
  const [loaded, setLoaded] = useState(false)
  useEffect(() => { const t = setTimeout(() => setLoaded(true), 80); return () => clearTimeout(t) }, [])

  const heroStyle = (delay: number): React.CSSProperties => ({
    opacity: loaded ? 1 : 0,
    transform: loaded ? 'translateY(0)' : 'translateY(18px)',
    transition: `opacity 1.1s cubic-bezier(0.16,1,0.3,1) ${delay}ms, transform 1.1s cubic-bezier(0.16,1,0.3,1) ${delay}ms`,
  })

  return (
    <div style={{ background: '#000000', minHeight: '100vh', fontFamily: "'Inter', sans-serif", color: '#929292', overflowX: 'hidden' }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Chakra+Petch:wght@400&display=swap');
        *, *::before, *::after { box-sizing: border-box; }
        body { margin:0!important; background:#000!important; overflow-x:hidden!important; display:block!important; align-items:unset!important; justify-content:unset!important; min-height:unset!important; }
        #root { display:block!important; min-height:unset!important; align-items:unset!important; }
        .landing-body-text { font-size: 21px; }
        .landing-title-text { font-size: 21px; }
        @media (max-width: 768px) {
          .landing-body-text { font-size: 16px !important; }
          .landing-title-text { font-size: 16px !important; }
          .screen-grid { flex-direction: column !important; align-self: stretch !important; }
          .screen-grid > div { margin-top: 0 !important; }
          .screen-grid > div > div { margin-top: 0 !important; }
          .screen-panel { width: 100% !important; max-width: 100% !important; }
          .main-content { padding-top: 32vh !important; }
        }
      `}</style>

      {/* ── NAV ── */}
      <nav style={{
        position: 'fixed', top: 0, left: 0, right: 0, zIndex: 100,
        background: '#000', display: 'flex', alignItems: 'center',
        justifyContent: 'space-between', padding: '60px 5% 36px',
        ...heroStyle(0),
      }}>
        <Logo />
        <HamburgerIcon />
      </nav>

      {/* ── CONTENT ── */}
      <div className="main-content" style={{ display: 'flex', flexDirection: 'column', gap: 165, paddingTop: '48vh', paddingBottom: 300, paddingLeft: '5%', paddingRight: '5%' }}>

        {/* ── HERO ── */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 30, maxWidth: 650 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 15 }}>
            <span style={{ fontFamily: "'Inter', sans-serif", fontSize: 18, color: '#5c5c5c', ...heroStyle(120) }}>
              Intelligent Investing
            </span>
            <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', letterSpacing: '0px', lineHeight: 1.4, ...heroStyle(260) }}>
              Reality does not reward confidence.<br />It rewards discipline.
            </span>
          </div>
          <p className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#929292', margin: 0, letterSpacing: '0px', lineHeight: 1.55, opacity: loaded ? 0.9 : 0, transform: loaded ? 'translateY(0)' : 'translateY(18px)', transition: 'opacity 1.1s cubic-bezier(0.16,1,0.3,1) 420ms, transform 1.1s cubic-bezier(0.16,1,0.3,1) 420ms' }}>
            Most people confuse activity with progress.<br />
            Markets punish that mistake relentlessly.<br />
            This system was built for people who prefer truth over comfort.
          </p>
        </div>

        {/* ── SECTIONS 001–003 ── */}
        {allSections.slice(0, 3).map((s) => <Section key={s.number} {...s} />)}

        {/* ── SECTION 004 ── */}
        <Reveal>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 28, maxWidth: 650, paddingLeft: 127 }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
              <span style={{ fontFamily: "'Chakra Petch', sans-serif", fontSize: 18, fontWeight: 400, color: '#5c5c5c' }}>{allSections[3].number}</span>
              <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#c7c7c7', letterSpacing: '0px', lineHeight: 1.4 }}>{allSections[3].title}</span>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
              {allSections[3].body.map((text, i) => (
                <p key={i} className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#929292', margin: 0, letterSpacing: '0px', lineHeight: 1.55, whiteSpace: 'pre-line', opacity: 0.9 }}>{text}</p>
              ))}
            </div>
          </div>
        </Reveal>




        {/* ── SECTIONS 005–014 ── */}
        {allSections.slice(4).map((s) => <Section key={s.number} {...s} />)}

        {/* ── CTA ── */}
        <Reveal>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 165, maxWidth: 650 }}>
            <p className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', margin: 0, letterSpacing: '0px', lineHeight: 1.55 }}>
              We are not building an investing app. We are building better investors.
            </p>
            <button style={{ background: 'none', border: 'none', padding: 0, cursor: 'pointer', fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', letterSpacing: '0px', textAlign: 'left', display: 'flex', alignItems: 'center', gap: 12 }}>
              <span>→</span><span>Proceed Deliberately</span>
            </button>
          </div>
        </Reveal>

        {/* ── FOOTER ── */}
        <Reveal>
          <footer style={{ display: 'flex', flexDirection: 'column', gap: 24, paddingBottom: 80 }}>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 13, color: '#929292', margin: 0 }}>
              ©2026 <a href="#" style={{ color: '#929292' }}>Orion Digital Corp.</a> All rights reserved.
            </p>
            <div style={{ display: 'flex', gap: 24, alignItems: 'center' }}>
              <InstagramIcon /><TikTokIcon /><TwitterIcon /><YouTubeIcon />
            </div>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>Past returns are no guarantee of future performance.</p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>
              Managed investing accounts are opened with IntelligentInvesting Wealth Management Inc., a registered portfolio manager. IntelligentInvesting Wealth Management Inc. accounts that are held with CI Investment Services Inc., a custodian, are protected by CIPF in accordance with its coverage policy. CI Investment Services Inc. is a CIRO member. Self-directed investing accounts are opened by IntelligentInvesting Securities Inc., an investment dealer regulated by the Canadian Investment Regulatory Organization (CIRO). IntelligentInvesting Securities Inc. is a CIPF member. IntelligentInvesting Securities Inc. accounts are covered by CIPF. A brochure describing the scope and nature of coverage, as well as the limitations and exclusions of coverage, is available upon request or at <a href="https://www.cipf.ca" style={{ color: '#565B5E' }}>www.cipf.ca</a>.
            </p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>IntelligentInvesting Wealth Management Inc. and IntelligentInvesting Securities Inc. are subsidiaries of Orion Digital Corp. Orion Digital Corp. is not an investment adviser or dealer and does not provide investment advice or deal in securities.</p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>Nothing herein should be considered an offer, solicitation of an offer, or advice to buy or sell securities. Account holdings are for illustrative purposes only. Actual products may differ from those depicted and images contained herein. The Intelligent Investing app incorporates the investing principles of Warren Buffett in its features, design, and content. Neither Orion Digital Corp. nor its affiliates are endorsed by or affiliated with Warren Buffett. All images, names, logos, and brands are the property of their respective owners.</p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>The information contained on this website is provided for informational purposes only and does not constitute a promise of specific results or future performance. Certain statements may contain opinions, assumptions, or forward-looking information that are subject to change and may not reflect actual outcomes. No representation or warranty, express or implied, is made as to the accuracy, completeness, or timeliness of the information presented. Statistics, examples, and projections, where provided, are for illustrative purposes only and should not be relied upon as guarantees of future results.</p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>Investing involves risk, including the potential loss of capital. The risks associated with any investment strategy, product, or service should be carefully considered before making any investment decision.</p>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 12, color: '#565B5E', margin: 0, lineHeight: 1.7 }}>
              <a href="#" style={{ color: '#565B5E' }}>Fiscal.ai</a>, an AI investment research tool powered by Fiscal.ai, is a third-party product provided "as is" without warranties on accuracy, completeness, quality, or timeliness. Verify information independently. Fiscal.ai outputs are not investment advice or recommendations and should not be used for investment decisions. By using Fiscal.ai, you agree to our <a href="#" style={{ color: '#565B5E' }}>Privacy Policy</a> and <a href="#" style={{ color: '#565B5E' }}>Terms of Use</a>.
            </p>
          </footer>
        </Reveal>

      </div>
    </div>
  )
}
