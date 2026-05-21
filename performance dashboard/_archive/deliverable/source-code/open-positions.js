const holdingsContainer = document.querySelector('.holdings');
    const allRows = Array.from(holdingsContainer.querySelectorAll('.hold-row'));
    const allGroupLabels = Array.from(holdingsContainer.querySelectorAll('.group-label'));
    const originalChildren = Array.from(holdingsContainer.children);

    // Hold-row drill-down to Stock Page v2
    allRows.forEach(row => {
      row.style.cursor = 'pointer';
      row.addEventListener('click', () => {
        window.location.href = '../../Stock%20Pages/Post%20MVP/Stock%20Page%20v2.html';
      });
    });

    const sortNotes = {
      discipline: 'Rule violations first (kill line, past horizon, overdue review), then worst alpha.',
      impact: 'Biggest absolute dollar moves first.',
      alpha: 'Worst alpha first — biggest underperformers vs S&P 500 at the top.'
    };
    const sortNoteEl = document.getElementById('sortNote');

    function applySort(sortKey) {
      // Update note
      if (sortNoteEl && sortNotes[sortKey]) sortNoteEl.textContent = sortNotes[sortKey];

      // Clear container
      while (holdingsContainer.firstChild) holdingsContainer.removeChild(holdingsContainer.firstChild);

      if (sortKey === 'discipline') {
        // Restore original order with group labels
        originalChildren.forEach(el => holdingsContainer.appendChild(el));
        return;
      }

      // Hide group labels for non-discipline sorts — flat list
      let sorted = [...allRows];
      if (sortKey === 'impact') {
        sorted.sort((a, b) => Math.abs(parseFloat(b.dataset.alpha)) - Math.abs(parseFloat(a.dataset.alpha)));
      } else if (sortKey === 'alpha') {
        sorted.sort((a, b) => parseFloat(a.dataset.alpha) - parseFloat(b.dataset.alpha));
      }
      sorted.forEach(row => holdingsContainer.appendChild(row));
    }

    const sortOpts = document.querySelectorAll('.sort-opt');
    sortOpts.forEach(opt => {
      opt.addEventListener('click', e => {
        e.stopPropagation();
        if (opt.classList.contains('active')) return;
        sortOpts.forEach(o => { o.classList.remove('active'); o.setAttribute('aria-selected','false'); });
        opt.classList.add('active');
        opt.setAttribute('aria-selected','true');
        applySort(opt.dataset.sort);
      });
    });
