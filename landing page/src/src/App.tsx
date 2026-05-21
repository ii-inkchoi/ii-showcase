import { useState, useCallback, useRef } from 'react'

const CURRENT = 500
const CURRENCY = 'CAD'
const CUR_STR  = `${CURRENT}.00`

const ROWS = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9'],
  ['•', '0', '←'],
]

type FreqType = 'weekly' | 'one-time' | 'roundups'

const FREQ_LABELS: Record<FreqType, string> = {
  weekly:    'Weekly',
  'one-time':'One-Time',
  roundups:  'Roundups',
}

const FREQ_OPTIONS: { id: FreqType; label: string }[] = [
  { id: 'weekly',    label: 'Weekly'   },
  { id: 'one-time',  label: 'One-Time' },
  { id: 'roundups',  label: 'Roundups' },
]

function addCommas(s: string) {
  return s.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}

function buildSlots(int: string, dec: string, hasDec: boolean) {
  const slots: { ch: string; dim: boolean | 'mid'; key: string }[] = []

  const formatted = addCommas(int)
  for (let i = 0; i < formatted.length; i++)
    slots.push({ ch: formatted[i], dim: false, key: `i${i}` })

  const remaining = int.length === 0 ? 3 : 0
  for (let i = 0; i < remaining; i++)
    slots.push({ ch: '-', dim: true, key: `id${i}` })

  slots.push({ ch: '.', dim: hasDec ? false : 'mid', key: 'dot' })
  for (let i = 0; i < 2; i++) {
    if (hasDec && i < dec.length) slots.push({ ch: dec[i], dim: false, key: `d${i}`  })
    else                          slots.push({ ch: '0',    dim: true,  key: `dd${i}` })
  }

  return slots
}

export default function App() {
  const [int,    setInt]    = useState('')
  const [dec,    setDec]    = useState('')
  const [hasDec, setHasDec] = useState(false)
  const [editing,setEditing]= useState(false)

  const [freq,         setFreq]         = useState<FreqType>('weekly')
  const [showSheet,    setShowSheet]    = useState(false)
  const [sheetVisible, setSheetVisible] = useState(false)

  const numRef = useRef<HTMLSpanElement>(null)

  const slots  = buildSlots(int, dec, hasDec)
  const newStr = addCommas(int || '0') + '.' + (hasDec ? dec.padEnd(2, '0') : '00')

  // ── Bottom sheet open / close ────────────────────────────────────────────
  const openSheet = () => {
    setShowSheet(true)
    requestAnimationFrame(() => requestAnimationFrame(() => setSheetVisible(true)))
  }

  const closeSheet = () => {
    setSheetVisible(false)
    setTimeout(() => setShowSheet(false), 330)
  }

  const selectFreq = (f: FreqType) => {
    setFreq(f)
    closeSheet()
    // reset amount when switching type
    setInt(''); setDec(''); setHasDec(false); setEditing(false)
  }

  // ── Per-keystroke spring feedback ────────────────────────────────────────
  const pulse = useCallback(() => {
    const el = numRef.current
    if (!el) return
    el.style.transition = 'none'
    el.style.opacity    = '0.5'
    el.style.transform  = 'translateY(-2px)'
    void el.offsetHeight
    el.style.transition = 'opacity 0.4s cubic-bezier(0.16,1,0.3,1), transform 0.5s cubic-bezier(0.16,1,0.3,1)'
    el.style.opacity    = '1'
    el.style.transform  = 'translateY(0)'
  }, [])

  // ── Keypad logic ─────────────────────────────────────────────────────────
  const tap = useCallback((key: string) => {
    if ('vibrate' in navigator) navigator.vibrate(6)

    if (key === '←') {
      if (!editing) return
      if (hasDec) {
        if (dec.length > 0) { setDec(d => d.slice(0, -1)); pulse() }
        else                { setHasDec(false); pulse() }
      } else {
        const next = int.slice(0, -1)
        if (!next) { setEditing(false); setInt('') }
        else       { setInt(next); pulse() }
      }
      return
    }

    if (key === '•') {
      if (hasDec) return
      if (!editing) setEditing(true)
      setHasDec(true); pulse(); return
    }

    if (!editing) setEditing(true)

    if (hasDec) {
      if (dec.length < 2) { setDec(d => d + key); pulse() }
    } else {
      if (int.length >= 8) return
      const next = !int ? key : (int === '0' && key !== '0' ? key : int + key)
      setInt(next); pulse()
    }
  }, [editing, hasDec, int, dec, pulse])

  return (
    <div className="screen">

      {/* ── Header ── */}
      <div className="header">
        <button className="hbtn" aria-label="Back">
          <svg width="11" height="19" viewBox="0 0 11 19" fill="none">
            <path d="M9.5 1.5L2 9.5L9.5 17.5" stroke="white" strokeWidth="1.6"
              strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </button>
        <button className="hbtn hbtn-exit">Exit</button>
      </div>
      <hr className="divider" />

      {/* ── Title ── */}
      <p className="title">Enter Amount</p>

      {/* ── Account row ── */}
      <div className="acct-row">
        <span className="icon-bank"><span className="icon-bank-s">$</span></span>
        <span className="acct-name">Chequing</span>
        <span className="acct-mask">****1234</span>
        <span className="acct-sep">→</span>
        <span className="icon-goal">//</span>
        <span className="acct-name">Become a Milliona...</span>
      </div>

      {/* ── Amount section ── */}
      <div className="amount-section">

        <div className="label-wrap">
          <span className={`lbl lbl-default${editing ? ' out' : ''}`}>
            Current {CUR_STR} {CURRENCY}
          </span>
          <span className={`lbl lbl-edit${editing ? ' in' : ''}`}>
            Current {CUR_STR} {CURRENCY}
            <span className="lbl-sep"> → </span>
            <span className="lbl-new">New {newStr} {CURRENCY}</span>
          </span>
        </div>

        <div className="amt-row">
          <span ref={numRef} className="amt-num">
            {slots.map(s => (
              <span key={s.key} className={s.dim === 'mid' ? 'slot-mid' : s.dim ? 'slot-dim' : 'slot-lit'}>{s.ch}</span>
            ))}
          </span>
          <span className="amt-cur">{CURRENCY}</span>
        </div>

        {/* Frequency pill */}
        <button className="freq" onClick={openSheet}>
          {FREQ_LABELS[freq]}
          <svg className="freq-chevron" width="11" height="6" viewBox="0 0 11 6" fill="none">
            <path d="M1 1L5.5 5L10 1" stroke="#8E8E93" strokeWidth="1.4"
              strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </button>

        {/* Microcopy — only for One-Time */}
        {freq === 'one-time' && (
          <p className="freq-microcopy">
            Weekly auto-invest remains active.<br />$300 will be invested every Monday,<br />separately from this transfer.
          </p>
        )}

      </div>

      <div style={{ flex: 1 }} />

      {/* ── Actions ── */}
      <div className="actions">
        <button className="act-btn">→ Cancel</button>
        <button className={`act-btn act-review${editing ? ' active' : ''}`}>→ Review</button>
      </div>

      {/* ── Keypad ── */}
      <div className="keypad">
        {ROWS.map((row, i) => (
          <div key={i} className="key-row">
            {row.map(k => (
              <button key={k} className="key"
                onPointerDown={() => tap(k)}
                onContextMenu={e => e.preventDefault()}>
                {k}
              </button>
            ))}
          </div>
        ))}
      </div>

      {/* ── Investment Type Bottom Sheet ── */}
      {showSheet && (
        <div
          className={`sheet-overlay${sheetVisible ? ' visible' : ''}`}
          onClick={closeSheet}
        >
          <div
            className={`sheet${sheetVisible ? ' visible' : ''}`}
            onClick={e => e.stopPropagation()}
          >
            <div className="sheet-header">
              <span className="sheet-title">Investment Type</span>
              <button className="sheet-close" onClick={closeSheet} aria-label="Close">
                <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
                  <path d="M1.5 1.5L13.5 13.5M13.5 1.5L1.5 13.5"
                    stroke="#8E8E93" strokeWidth="1.6" strokeLinecap="round"/>
                </svg>
              </button>
            </div>

            {FREQ_OPTIONS.map((opt, i) => (
              <div key={opt.id}>
                {i > 0 && <hr className="sheet-divider" />}
                <button
                  className={`sheet-option${freq === opt.id ? ' selected' : ''}`}
                  onClick={() => selectFreq(opt.id)}
                >
                  <span>{opt.label}</span>
                  {freq === opt.id && (
                    <svg width="17" height="13" viewBox="0 0 17 13" fill="none">
                      <path d="M1.5 6.5L6.5 11.5L15.5 1.5"
                        stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  )}
                </button>
              </div>
            ))}

            <div className="sheet-bottom-gap" />
          </div>
        </div>
      )}

    </div>
  )
}
