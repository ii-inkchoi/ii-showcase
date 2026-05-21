const STAGGER = 700;
const STATE_KEY = 'sdo_state';

function loadState() {
  try { return JSON.parse(sessionStorage.getItem(STATE_KEY)) || {}; }
  catch { return {}; }
}
function saveState(patch) {
  const s = loadState();
  Object.assign(s, patch);
  sessionStorage.setItem(STATE_KEY, JSON.stringify(s));
}

function goTo(page) { window.location.href = page; }
function goBack() { history.length > 1 ? history.back() : null; }

function getAnimEls(screen) {
  const els = Array.from(screen.querySelectorAll(
    '.fig-col > p, .fig-col > .fig-line-group, .fig-col > .prompt-block, .fig-col > .choice-list, ' +
    '.fig-col > .reflect-block, .fig-col > .t14-800, ' +
    '.t18-w, .check-list, ' +
    '.post-headline, .research-btn'
  ));
  const arrow = screen.querySelector('.arrow-btn');
  if (arrow) els.push(arrow);
  const enterBtn = screen.querySelector('.enter-btn');
  if (enterBtn) els.push(enterBtn);
  return els;
}

function resetScreen(screen) {
  getAnimEls(screen).forEach(el => {
    el.style.transition = 'none';
    el.classList.remove('anim-in');
    el.classList.add('anim-ready');
    void el.offsetHeight;
    el.style.transition = '';
  });
}

function animateScreen(screen) {
  getAnimEls(screen).forEach((el, i) => {
    setTimeout(() => el.classList.add('anim-in'), i * STAGGER);
  });
}

function checkTextInput(inputId, btnId) {
  const val = document.getElementById(inputId).value.trim();
  const btn = document.getElementById(btnId);
  if (btn) btn.disabled = val.length === 0;
}

function autoResizeTextInput(el) {
  el.style.height = 'auto';
  el.style.height = el.scrollHeight + 'px';
}

function updateSingleItemClass(listEl, rowSelector) {
  if (!listEl) return;
  const count = listEl.querySelectorAll(rowSelector).length;
  listEl.classList.toggle('single-item', count <= 1);
}

function updateInputCount(el) {
  const counter = document.querySelector('.input-count[data-for="' + el.id + '"]');
  if (!counter) return;
  const max = el.maxLength > 0 ? el.maxLength : 0;
  counter.textContent = max ? (el.value.length + '/' + max) : String(el.value.length);
}

function toggleCheck(el, listId, btnId) {
  el.classList.toggle('sel');
  const list = document.getElementById(listId);
  const anySelected = list.querySelectorAll('.check-row.sel').length > 0;
  updateSingleItemClass(list, '.check-row');
  document.getElementById(btnId).disabled = !anySelected;
}

function selectRadio(btn, screenId, btnId) {
  const screen = document.getElementById(screenId);
  screen.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('sel'));
  btn.classList.add('sel');
  updateSingleItemClass(screen.querySelector('.choice-list'), '.choice-btn');
  document.getElementById(btnId).disabled = false;
}

function getCheckedLabels(listId) {
  return Array.from(document.querySelectorAll('#' + listId + ' .check-row.sel .check-label'))
    .map(el => el.textContent.trim());
}

function getSelectedChoiceLabel(screenId) {
  const btn = document.querySelector('#' + screenId + ' .choice-btn.sel .choice-label');
  return btn ? btn.textContent.trim() : '';
}

function initScreen(screenId) {
  const screen = document.getElementById(screenId);
  if (!screen) return;
  resetScreen(screen);
  setTimeout(() => animateScreen(screen), 80);

  document.querySelectorAll('.text-input').forEach(el => {
    autoResizeTextInput(el);
    updateInputCount(el);
    el.addEventListener('input', () => {
      autoResizeTextInput(el);
      updateInputCount(el);
    });
  });
  document.querySelectorAll('.check-list').forEach(list => updateSingleItemClass(list, '.check-row'));
  document.querySelectorAll('.choice-list').forEach(list => updateSingleItemClass(list, '.choice-btn'));

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') {
      const btn = screen.querySelector('.arrow-btn');
      if (btn && !btn.disabled) btn.click();
    }
    if (e.key === 'ArrowLeft') goBack();
  });
}
