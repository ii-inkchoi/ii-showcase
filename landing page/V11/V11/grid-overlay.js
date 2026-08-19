/* II site grid overlay — shared across all pages (canonical pattern, from Self-Directed).
   Press "g" / "ㅎ" to toggle a 12-column overlay. Reuses the page's own .container
   (max-width / frame padding) so it always matches the real content grid.
   Dev tool only: pointer-events:none, ignores typing in inputs. */
(function () {
  if (window.__iiGridOverlay) return;
  window.__iiGridOverlay = true;

  var STYLE =
    '.ii-grid-ov{position:fixed;inset:0;z-index:2000;pointer-events:none;display:none;}' +
    '.ii-grid-ov.on{display:block;}' +
    '.ii-grid-ov .container{height:100%;}' +
    '.ii-grid-ov .go-grid{display:grid;grid-template-columns:repeat(12,1fr);column-gap:var(--gutter);height:100%;}' +
    '.ii-grid-ov .go-grid span{background:var(--c-200);opacity:0.07;}';

  function init() {
    var st = document.createElement('style');
    st.textContent = STYLE;
    document.head.appendChild(st);

    var ov = document.createElement('div');
    ov.className = 'ii-grid-ov';
    ov.setAttribute('aria-hidden', 'true');
    var spans = '';
    for (var i = 0; i < 12; i++) spans += '<span></span>';
    ov.innerHTML = '<div class="container"><div class="go-grid">' + spans + '</div></div>';
    document.body.appendChild(ov);

    document.addEventListener('keydown', function (e) {
      var t = e.target, tag = (t && t.tagName || '').toLowerCase();
      if (tag === 'input' || tag === 'textarea' || tag === 'select' || (t && t.isContentEditable)) return;
      if ((e.key === 'g' || e.key === 'G' || e.key === 'ㅎ') && !e.metaKey && !e.ctrlKey && !e.altKey) {
        e.preventDefault();
        ov.classList.toggle('on');
      }
    });
  }

  if (document.body) init();
  else document.addEventListener('DOMContentLoaded', init);
})();
