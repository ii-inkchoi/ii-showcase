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

const FREQ_UNIT: Record<FreqType, string> = {
  weekly:    'per Week',
  'one-time': '',
  roundups:  'per Roundup',
}

function addCommas(s: string) {
  return s.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}

function normalize(digits: string) {
  return (parseInt(digits || '0', 10) || 0).toString()
}

// Find where in the formatted string (with commas) the cursor should appear
// given a cursorPos in the raw digits string
function findInsertAt(formatted: string, cursorPos: number): number {
  let digitCount = 0
  for (let i = 0; i < formatted.length; i++) {
    if (digitCount === cursorPos) return i
    if (/\d/.test(formatted[i])) digitCount++
  }
  return formatted.length
}

export default function App2() {
  const [digits,    setDigits]    = useState('')
  const [decDigits, setDecDigits] = useState('')
  const [hasDec,    setHasDec]    = useState(false)
  const [editing,   setEditing]   = useState(false)
  const [cursorPos, _setCursorPos] = useState(0)
  const cursorRef = useRef(0)
  const setCursorPos = (val: number) => { cursorRef.current = val; _setCursorPos(val) }

  // cursorInDec: cursor is in the decimal section (key presses go to decimal)
  const [cursorInDec, _setCursorInDec] = useState(false)
  const cursorInDecRef = useRef(false)
  const setCursorInDec = (val: boolean) => { cursorInDecRef.current = val; _setCursorInDec(val) }

  // decCursorPos: cursor position within decDigits (0=before first, 1=between, 2=after last)
  const [decCursorPos, _setDecCursorPos] = useState(0)
  const decCursorRef = useRef(0)
  const setDecCursorPos = (val: number) => { decCursorRef.current = val; _setDecCursorPos(val) }
  const [page,      setPage]      = useState<'input' | 'review'>('input')
  const [animKey,   setAnimKey]   = useState(0)

  const [freq,         setFreq]         = useState<FreqType>('weekly')
  const [showSheet,    setShowSheet]    = useState(false)
  const [sheetVisible, setSheetVisible] = useState(false)

  // ── Display strings ───────────────────────────────────────────────────────
  const normInt      = normalize(digits)
  const confirmedAmt = addCommas(normInt) + '.' + (hasDec ? decDigits.padEnd(2, '0') : '00')
  const newStr       = hasDec
    ? addCommas(digits || '0') + '.' + decDigits
    : addCommas(digits || '0')

  // ── Integer display with per-digit tappable spans + cursor ───────────────
  const buildIntSpans = () => {
    const formatted = addCommas(digits || '')
    // cursor in integer only when not in decimal section
    const insertAt = cursorInDec ? formatted.length : findInsertAt(formatted, cursorPos)
    const nodes: JSX.Element[] = []
    let rawIdx = 0

    for (let i = 0; i < formatted.length; i++) {
      if (i === insertAt) nodes.push(<span key="cur" className="amt-cursor" />)
      const ch = formatted[i]
      const isDigit = /\d/.test(ch)
      const capturedRaw = rawIdx
      if (isDigit) rawIdx++
      nodes.push(
        <span
          key={i}
          className="slot-lit"
          onPointerDown={isDigit ? (e) => {
            e.stopPropagation()
            setCursorInDec(false)        // cursor moves to integer
            setCursorPos(capturedRaw + 1) // decimal & hasDec preserved
          } : undefined}
        >
          {ch}
        </span>
      )
    }
    if (insertAt >= formatted.length && !cursorInDec) nodes.push(<span key="cur-end" className="amt-cursor" />)
    return nodes
  }

  // ── Bottom sheet ─────────────────────────────────────────────────────────
  const openSheet = () => {
    setShowSheet(true)
    requestAnimationFrame(() => requestAnimationFrame(() => setSheetVisible(true)))
  }
  const closeSheet = () => {
    setSheetVisible(false)
    setTimeout(() => setShowSheet(false), 330)
  }
  const selectFreq = (f: FreqType) => {
    setFreq(f); closeSheet()
    setDigits(''); setDecDigits(''); setHasDec(false)
    setEditing(false); setCursorPos(0); setCursorInDec(false); setDecCursorPos(0); setPage('input')
  }

  // ── Review ────────────────────────────────────────────────────────────────
  const handleReview = () => {
    if (!editing) return
    setDigits(normInt)
    setCursorPos(normInt.length)
    setPage('review')
  }

  // ── Keypad ────────────────────────────────────────────────────────────────
  const tap = useCallback((key: string) => {
    if ('vibrate' in navigator) navigator.vibrate(6)

    if (key === '←') {
      if (!editing) return
      if (cursorInDecRef.current) {
        const dp = decCursorRef.current
        if (dp === 0) { setCursorInDec(false); setAnimKey(k => k + 1) }
        else {
          setDecDigits(d => d.slice(0, dp - 1) + d.slice(dp))
          setDecCursorPos(dp - 1)
          setAnimKey(k => k + 1)
        }
      } else {
        const cp = cursorRef.current
        if (cp === 0) return
        setDigits(d => {
          const next = d.slice(0, cp - 1) + d.slice(cp)
          if (!next) { setEditing(false); setCursorPos(0); setHasDec(false); setDecDigits(''); setCursorInDec(false) }
          else       setCursorPos(cp - 1)
          return next
        })
        setAnimKey(k => k + 1)
      }
      return
    }

    if (key === '•') {
      if (cursorInDecRef.current) return
      if (!editing) { setEditing(true); setCursorPos(digits.length) }
      setHasDec(true); setCursorInDec(true); setDecCursorPos(decDigits.length); setAnimKey(k => k + 1); return
    }

    if (!editing) { setEditing(true); setCursorPos(digits.length) }

    if (cursorInDecRef.current) {
      const dp = decCursorRef.current
      const next = (decDigits.slice(0, dp) + key + decDigits.slice(dp)).slice(0, 2)
      setDecDigits(next)
      setDecCursorPos(Math.min(dp + 1, 2))
      setAnimKey(k => k + 1)
    } else {
      if (digits.length >= 9) return
      const cp = cursorRef.current
      setDigits(d => {
        const next = d.slice(0, cp) + key + d.slice(cp)
        setCursorPos(cp + 1)
        return next
      })
      setAnimKey(k => k + 1)
    }
  }, [editing, hasDec, digits, decDigits])

  // ── Review / Confirm page ─────────────────────────────────────────────────
  if (page === 'review') {
    return (
      <div className="screen">
        <div className="header">
          <button className="hbtn" aria-label="Back" onPointerDown={() => setPage('input')}>
            <svg width="11" height="19" viewBox="0 0 11 19" fill="none">
              <path d="M9.5 1.5L2 9.5L9.5 17.5" stroke="white" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
          <button className="hbtn hbtn-exit">Exit</button>
        </div>
        <hr className="divider" />

        <p className="confirm-title">Confirm Transfer Details</p>

        <div className="confirm-fields">
          <div className="confirm-field">
            <span className="confirm-label">From</span>
            <span className="confirm-value">RBC ****1234</span>
          </div>
          <div className="confirm-field">
            <span className="confirm-label">To</span>
            <span className="confirm-value">Become a Millionaire · TFSA</span>
          </div>
          <div className="confirm-field">
            <span className="confirm-label">Investment Type</span>
            <span className="confirm-value">{FREQ_LABELS[freq]}</span>
          </div>
          <div className="confirm-field">
            <span className="confirm-label">Amount</span>
            <span className="confirm-value">
              {confirmedAmt} {CURRENCY}{FREQ_UNIT[freq] ? ` ${FREQ_UNIT[freq]}` : ''}
            </span>
          </div>
          {freq !== 'one-time' && (
            <div className="confirm-field">
              <span className="confirm-label">Next Investment</span>
              <span className="confirm-value">Dec 15, 2025</span>
            </div>
          )}
        </div>

        <div style={{ flex: 1 }} />

        <div className="submit-bar">
          <button className="submit-btn">Submit</button>
        </div>
      </div>
    )
  }

  // ── Input page ────────────────────────────────────────────────────────────
  return (
    <div className="screen">

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

      <p className="title">Enter Amount</p>

      <div className="acct-row">
        <span className="icon-bank"><span className="icon-bank-s">$</span></span>
        <span className="acct-name">Chequing</span>
        <span className="acct-mask">****1234</span>
        <span className="acct-sep">→</span>
        <span className="icon-goal">//</span>
        <span className="acct-name">Become a Milliona...</span>
      </div>

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
          <span key={animKey} className={`amt-num${editing ? ' amt-num-anim' : ''}`}>
            {!editing ? (
              <>
                <span className="slot-dim">-</span>
                <span className="slot-dim">-</span>
                <span className="slot-dim">-</span>
              </>
            ) : !hasDec ? (
              buildIntSpans()
            ) : (
              <>
                {buildIntSpans()}
                <span
                  className="slot-lit"
                  onPointerDown={(e) => { e.stopPropagation(); setCursorInDec(true); setDecCursorPos(0) }}
                >.</span>
                {decDigits.split('').map((ch, i) => (
                  <>
                    {cursorInDec && decCursorPos === i && <span key={`dc${i}`} className="amt-cursor" />}
                    <span
                      key={i}
                      className="slot-lit"
                      onPointerDown={(e) => { e.stopPropagation(); setCursorInDec(true); setDecCursorPos(i) }}
                    >{ch}</span>
                  </>
                ))}
                {cursorInDec && decCursorPos >= decDigits.length && <span className="amt-cursor" />}
              </>
            )}
          </span>
          <span className="amt-cur">{CURRENCY}</span>
        </div>

        <button className="freq" onClick={openSheet}>
          {FREQ_LABELS[freq]}
          <svg className="freq-chevron" width="11" height="6" viewBox="0 0 11 6" fill="none">
            <path d="M1 1L5.5 5L10 1" stroke="#8E8E93" strokeWidth="1.4"
              strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </button>

        {freq === 'one-time' && (
          <p className="freq-microcopy">
            Weekly auto-invest remains active.<br />$300 will be invested every Monday,<br />separately from this transfer.
          </p>
        )}

      </div>

      <div style={{ flex: 1 }} />

      <div className="actions">
        <button className="act-btn">→ Cancel</button>
        <button
          className={`act-btn act-review${editing ? ' active' : ''}`}
          onPointerDown={handleReview}
        >
          → Review
        </button>
      </div>

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
