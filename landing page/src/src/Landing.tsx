import { useEffect, useRef, useState } from 'react'
import appMockup from './assets/app-mockup.png'

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
    title: 'People who:',
    body: [
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
          <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#c7c7c7', letterSpacing: '1px', lineHeight: 1.25 }}>
            {title}
          </span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
          {body.map((text, i) => (
            <p key={i} className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#929292', margin: 0, letterSpacing: '1px', lineHeight: 1.35, whiteSpace: 'pre-line', opacity: 0.9 }}>
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
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.259 5.63 5.905-5.63zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z" fill="#929292" />
    </svg>
  )
}

function InstagramIcon() {
  return (
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
      <rect x="2" y="2" width="20" height="20" rx="5" stroke="#929292" strokeWidth="1.5" fill="none" />
      <circle cx="12" cy="12" r="4.5" stroke="#929292" strokeWidth="1.5" fill="none" />
      <circle cx="17.5" cy="6.5" r="1.5" fill="#929292" />
    </svg>
  )
}

// ── Page ──────────────────────────────────────────────────────────────────────
export default function Landing() {
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
      <div style={{ display: 'flex', flexDirection: 'column', gap: 165, paddingTop: '48vh', paddingBottom: 300, paddingLeft: '5%', paddingRight: '5%' }}>

        {/* ── HERO ── */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 30, maxWidth: 650 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 15 }}>
            <span style={{ fontFamily: "'Inter', sans-serif", fontSize: 18, color: '#5c5c5c', ...heroStyle(120) }}>
              Intelligent Investing
            </span>
            <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', letterSpacing: '1px', lineHeight: 1.25, ...heroStyle(260) }}>
              Reality does not reward confidence.<br />It rewards discipline.
            </span>
          </div>
          <p className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#929292', margin: 0, letterSpacing: '1px', lineHeight: 1.35, opacity: loaded ? 0.9 : 0, transform: loaded ? 'translateY(0)' : 'translateY(18px)', transition: 'opacity 1.1s cubic-bezier(0.16,1,0.3,1) 420ms, transform 1.1s cubic-bezier(0.16,1,0.3,1) 420ms' }}>
            Most people confuse activity with progress.<br />
            Markets punish that mistake relentlessly.<br />
            This system was built for people who prefer truth over comfort.
          </p>
        </div>

        {/* ── SECTIONS 001–003 ── */}
        {allSections.slice(0, 3).map((s) => <Section key={s.number} {...s} />)}

        {/* ── SECTION 004 ── */}
        <Reveal>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 28, maxWidth: 650 }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
              <span style={{ fontFamily: "'Chakra Petch', sans-serif", fontSize: 18, fontWeight: 400, color: '#5c5c5c' }}>{allSections[3].number}</span>
              <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#c7c7c7', letterSpacing: '1px', lineHeight: 1.25 }}>{allSections[3].title}</span>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
              {allSections[3].body.map((text, i) => (
                <p key={i} className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, fontWeight: 400, color: '#929292', margin: 0, letterSpacing: '1px', lineHeight: 1.35, whiteSpace: 'pre-line', opacity: 0.9 }}>{text}</p>
              ))}
            </div>
          </div>
        </Reveal>

        {/* ── APP IMAGE ── */}
        <Reveal>
          <div style={{ overflow: 'hidden', maxWidth: 900 }}>
            <img src={appMockup} alt="" style={{ width: '100%', display: 'block', opacity: 0.2 }} />
          </div>
        </Reveal>

        {/* ── SYSTEM IN PRACTICE ── */}
        <Reveal>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 30, maxWidth: 650, paddingLeft: 127 }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 15 }}>
              <span style={{ fontFamily: "'Inter', sans-serif", fontSize: 18, color: '#5c5c5c' }}>System in practice</span>
              <span className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', letterSpacing: '1px', lineHeight: 1.25 }}>
                A calm environment for deliberate capital allocation.
              </span>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
              <p className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#929292', margin: 0, letterSpacing: '1px', lineHeight: 1.35, opacity: 0.9 }}>No noise. No urgency. No distraction.</p>
              <p className="landing-body-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#929292', margin: 0, letterSpacing: '1px', lineHeight: 1.35, opacity: 0.9 }}>This is where decisions are made,<br />not reactions.</p>
            </div>
          </div>
        </Reveal>

        {/* ── SECTIONS 005–014 ── */}
        {allSections.slice(4).map((s) => <Section key={s.number} {...s} />)}

        {/* ── CTA ── */}
        <Reveal>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 165, maxWidth: 650 }}>
            <p className="landing-title-text" style={{ fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', margin: 0, letterSpacing: '1px', lineHeight: 1.35 }}>
              We are not building an investing app. We are building better investors.
            </p>
            <button style={{ background: 'none', border: 'none', padding: 0, cursor: 'pointer', fontFamily: "'Inter', sans-serif", fontSize: 21, color: '#c7c7c7', letterSpacing: '1px', textAlign: 'left', display: 'flex', alignItems: 'center', gap: 12 }}>
              <span>→</span><span>Proceed Deliberately</span>
            </button>
          </div>
        </Reveal>

        {/* ── FOOTER ── */}
        <Reveal>
          <footer style={{ display: 'flex', flexDirection: 'column', gap: 30 }}>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 18, color: '#929292', margin: 0 }}>©2026 Orion Digital Corp. All rights reserved.</p>
            <div style={{ display: 'flex', gap: 30 }}><InstagramIcon /><TwitterIcon /></div>
            <p style={{ fontFamily: "'Inter', sans-serif", fontSize: 14, color: '#929292', margin: 0, maxWidth: 650, lineHeight: 1.7, opacity: 0.8 }}>
              If you're interested in diving into the sources for information on our website, research process, and investment methodology, you can find them linked below. We believe transparency is foundational to trust—so rather than citing selectively, we make our references available in full.
            </p>
          </footer>
        </Reveal>

      </div>
    </div>
  )
}
