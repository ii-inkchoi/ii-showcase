# Stock Page · Notes Feature · Dev Handoff

**Date:** 2026-06-04
**Source:** v10 prototype
**Phase:** Phase 1 (single note per stock, BE-persisted)

---

## Summary

Phase 1 of the memo feature. Users can add **one note per stock**. Notes are stored at the **stock level** (not order/position level). Notes persist across app reinstall via **backend**.

---

## Functional spec

### Data model
- **One note per (user, stock)** — single text string, V1
- **Plain text** (no rich formatting in V1)
- **Persistence:** backend (survives logout / reinstall)
- Prototype uses `localStorage` key `atz-memo-notes`

### Behavior
1. User opens Stock Page (any state — first-time, with memo, with position)
2. Notes section visible with placeholder: `Add a note. Capture a thought, a thesis, a question.`
3. Tap textarea → focus, auto-expand height
4. Type → `Save Note` button becomes active (color shifts to brighter)
5. Tap `Save Note` → text saved to BE, button label briefly changes to `Saved` (1.2s), then back to `Save Note`
6. Textarea blurs after save
7. On revisit, saved note pre-fills the textarea
8. Long notes (>100px height) auto-collapse with `Read more` button
9. Re-edit → textarea grows again, `Save Note` re-enables on diff vs saved value

### States
| State | Behavior |
|---|---|
| Empty | Placeholder visible, Save button inactive (faint color) |
| Typing | Save button activates when content differs from saved value |
| Saved | Button briefly shows `Saved`, then returns to `Save Note` |
| Loaded (revisit) | Saved text shown in textarea (slightly grey via `.is-saved` class) |
| Long content (blurred) | Collapsed with `Read more` button |

---

## UI placement on Stock Page

| Stock Page state | Notes position |
|---|---|
| **First-time** (no memo) | **TOP of memo block** — primary "scratchpad" entry |
| **With memo** (Active or Core) | **BOTTOM of memo block** — secondary artifact below memo fields |

Chairman directive: "memo as hero, notes as secondary" → notes bottom when memo exists.

---

## Reference files (prototype HTML)

### Locked / canonical implementations:
- **`Stock Page Firsttime User.html`** — blank state, Notes at TOP
- **`Stock Page Memo Only.html`** — filled Active, Notes at BOTTOM
- **`Stock Page Memo Only (Core).html`** — filled Core, Notes at BOTTOM

### CSS classes / selectors
```css
.memo-block-notes-section { display: flex; flex-direction: column; gap: 6px; }
.memo-block-notes-input {
  width: 100%; min-height: 44px;
  resize: none; overflow: hidden;
  background: transparent; border: none; padding: 0; outline: none;
  color: var(--c-200);  /* #E3E2E2 */
  font-size: 13px; line-height: 1.55; letter-spacing: -0.02em;
}
.memo-block-notes-input::placeholder { color: var(--c-800); }  /* #565B5E */
.memo-block-notes-input.is-saved { color: var(--c-700); }  /* #929292 — darker after save */
.memo-block-notes-input.is-collapsed {
  max-height: 100px; overflow: hidden;
  mask-image: linear-gradient(to bottom, #000 60%, transparent 100%);
}

.memo-notes-eyebrow { font-size: 11px; color: var(--c-700); }  /* "Notes" label */

.notes-save-btn {
  font-size: 11px; color: var(--c-800);  /* faint when not ready */
  padding: 4px 0; border: none; background: transparent;
  cursor: default; pointer-events: none;
}
.notes-save-btn.is-ready { color: var(--c-200); cursor: pointer; pointer-events: auto; }
.notes-save-btn.is-saved { color: var(--c-white); cursor: default; pointer-events: none; }

.notes-read-more {
  font-size: 11px; color: var(--c-700);
  background: transparent; border: none; cursor: pointer;
}
```

### HTML structure
```html
<div class="memo-block-notes-section">
  <div class="memo-notes-eyebrow">Notes</div>
  <textarea
    class="memo-block-notes-input"
    id="memoNotesInput"
    rows="2"
    placeholder="Add a note. Capture a thought, a thesis, a question."
    oninput="onMemoNotesInput(this)"
    onfocus="onMemoNotesFocus(this)"
    onblur="onMemoNotesBlur(this)"></textarea>
  <button type="button" class="notes-read-more" id="memoNotesReadMore" onclick="expandMemoNotes()" hidden>Read more</button>
  <div class="memo-block-notes-toolbar">
    <button type="button" class="notes-save-btn" id="memoNotesSaveBtn" onclick="saveMemoNote()">Save Note</button>
  </div>
</div>
```

### JS behavior (prototype)
```javascript
var NOTES_KEY = 'atz-memo-notes';  // BE: GET/PUT note for {user, stock}

function autoExpand(el) {
  if (!el) return;
  el.style.height = 'auto';
  el.style.height = el.scrollHeight + 'px';
}

function onMemoNotesInput(el) {
  autoExpand(el);
  var saved = localStorage.getItem(NOTES_KEY) || '';
  var btn = document.getElementById('memoNotesSaveBtn');
  btn.classList.remove('is-saved');
  btn.textContent = 'Save Note';
  if (el.value !== saved) btn.classList.add('is-ready');
  else btn.classList.remove('is-ready');
}

function saveMemoNote() {
  var el = document.getElementById('memoNotesInput');
  var text = el.value || '';
  localStorage.setItem(NOTES_KEY, text);  // ← Replace with BE PUT
  el.classList.add('is-saved');
  var btn = document.getElementById('memoNotesSaveBtn');
  btn.classList.remove('is-ready');
  btn.classList.add('is-saved');
  btn.textContent = 'Saved';
  el.blur();
  setTimeout(function() {
    btn.classList.remove('is-saved');
    btn.textContent = 'Save Note';
  }, 1200);
}

function onMemoNotesFocus(el) {
  el.classList.remove('is-saved');
  el.classList.remove('is-collapsed');
  autoExpand(el);
}

function onMemoNotesBlur(el) {
  autoExpand(el);
  var btn = document.getElementById('memoNotesReadMore');
  if (el.scrollHeight > 100) {
    el.classList.add('is-collapsed');
    if (btn) btn.hidden = false;
  } else {
    el.classList.remove('is-collapsed');
    if (btn) btn.hidden = true;
  }
}

// On page load: hydrate from BE
function renderNotes() {
  var text = localStorage.getItem(NOTES_KEY) || '';  // ← Replace with BE GET
  var el = document.getElementById('memoNotesInput');
  el.value = text;
  autoExpand(el);
  if (text) el.classList.add('is-saved');
}
```

---

## Backend integration

### Endpoints
- **GET** `/users/{userId}/stocks/{symbol}/note` → returns `{ text: string, updatedAt: timestamp }` or 404
- **PUT** `/users/{userId}/stocks/{symbol}/note` body: `{ text: string }` → saves note, returns `{ text, updatedAt }`
- **DELETE** `/users/{userId}/stocks/{symbol}/note` → clears note

### Data model
```
table: stock_notes
  user_id      string    (FK to users)
  symbol       string    (e.g., "ATZ")
  text         text      (the note content)
  created_at   timestamp
  updated_at   timestamp
  unique(user_id, symbol)
```

### Validation
- `text` max length: e.g., 5,000 chars (TBD)
- Plain text only — strip HTML / markdown rendering on FE
- Empty string saves as cleared note (DELETE semantics OK too)

---

## Edge cases

1. **Save when text identical to last saved** → no-op (Save button stays inactive)
2. **Save empty string after having content** → BE saves empty (or DELETE)
3. **Network failure on save** → show error, retain Save button as ready, don't apply `is-saved` state
4. **Concurrent edit on another device** → V1: last write wins. Reload pulls fresh on page load.
5. **App reinstall / logout-login** → note re-hydrates from BE on Stock Page load

---

## Phase 2 considerations (out of scope)
- Multiple notes per stock (note list with timestamps)
- Rich formatting (markdown / bold / lists)
- Note categorization / tags
- Notes search

---

## Open questions for BE team
- Max text length policy?
- Empty save = DELETE or empty record? (suggest: empty PUT keeps record but with empty text)
- Soft-delete vs hard-delete?
- Audit log of edits (for Phase 2 timeline view)?

---

## Files referenced (prototype)
- `Stock Page Firsttime User.html` — Notes TOP (blank memo state)
- `Stock Page Memo Only.html` — Notes BOTTOM (Active memo, no position)
- `Stock Page Memo Only (Core).html` — Notes BOTTOM (Core memo, no position)
- `Stock Page Return User.html` — Notes BOTTOM (Active V1 + held position)
- `Stock Page Return User - History.html` — Notes BOTTOM (V50, multi-version)
- `Stock Page Multi-Quarter Alerts.html` — Notes BOTTOM (with earnings alert)

→ All share same Notes pattern: textarea + Save Note button + auto-expand + collapse for long content.
