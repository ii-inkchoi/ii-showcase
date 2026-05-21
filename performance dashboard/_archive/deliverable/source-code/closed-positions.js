const holdingsContainer = document.querySelector('.holdings');
    let allRows = Array.from(holdingsContainer.querySelectorAll('.hold-row'));

    // URL parameter filter: ?filter=winners or ?filter=losers
    const urlParams = new URLSearchParams(window.location.search);
    const filter = urlParams.get('filter');

    function parseSignedDollar(text) {
      const m = text.match(/([+−-])\s*([\d,]+\.?\d*)/);
      if (!m) return 0;
      let v = parseFloat(m[2].replace(/,/g, ''));
      if (m[1] === '−' || m[1] === '-') v = -v;
      return v;
    }

    function fmtMoney(v) {
      const sign = v > 0 ? '+' : (v < 0 ? '−' : '');
      const abs = Math.abs(v);
      return sign + abs.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function parseHoldingMonths(metaText) {
      // Parses things like "1y 8m" or "11m" or "2y" — returns total months
      const m = metaText.match(/(?:(\d+)y)?\s*(?:(\d+)m)?/);
      if (!m) return 0;
      const y = parseInt(m[1] || '0');
      const mo = parseInt(m[2] || '0');
      return y * 12 + mo;
    }

    function recalculateSummary(rows) {
      let capital = 0, returnSum = 0, spSum = 0, alphaSum = 0, holdMonths = 0;
      rows.forEach(row => {
        const capText = row.querySelector('.h-cap-lbl').textContent;
        const capMatch = capText.match(/Capital\s+([\d,]+\.?\d*)/);
        if (capMatch) capital += parseFloat(capMatch[1].replace(/,/g, ''));
        returnSum += parseSignedDollar(row.querySelector('.h-return').textContent);
        const spText = row.querySelector('.h-sp').textContent.replace(/^S&P\s+/, '');
        spSum += parseSignedDollar(spText);
        alphaSum += parseSignedDollar(row.querySelector('.h-alpha').textContent.replace(/^Alpha\s+/, ''));
        holdMonths += parseHoldingMonths(row.querySelector('.h-meta').textContent);
      });
      const winRate = rows.length > 0 ? (rows.filter(r => parseSignedDollar(r.querySelector('.h-alpha').textContent.replace(/^Alpha\s+/, '')) > 0).length / rows.length * 100).toFixed(1) + '%' : '0%';
      const avgHold = rows.length > 0 ? Math.round(holdMonths / rows.length) : 0;
      const avgHoldStr = avgHold >= 12 ? Math.floor(avgHold / 12) + 'y ' + (avgHold % 12) + 'm' : avgHold + 'm';

      const summaryRows = document.querySelectorAll('.summary-row');
      if (summaryRows[0]) summaryRows[0].querySelector('.val').textContent = rows.length;
      if (summaryRows[1]) summaryRows[1].querySelector('.val').textContent = winRate;
      if (summaryRows[2]) summaryRows[2].querySelector('.val').textContent = capital.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      if (summaryRows[3]) summaryRows[3].querySelector('.val').textContent = fmtMoney(returnSum);
      if (summaryRows[4]) summaryRows[4].querySelector('.val').textContent = fmtMoney(spSum);
      if (summaryRows[5]) summaryRows[5].querySelector('.val').textContent = fmtMoney(alphaSum);
      if (summaryRows[6]) summaryRows[6].querySelector('.val').textContent = avgHoldStr;
    }

    if (filter === 'winners' || filter === 'losers') {
      // Update title to reflect filter
      const titlePrimary = document.querySelector('.t-primary');
      if (titlePrimary) {
        titlePrimary.textContent = filter === 'winners' ? 'Winners' : 'Losers';
      }
      // Update first summary row label
      const firstSummaryLabel = document.querySelector('.summary-row .lbl');
      if (firstSummaryLabel) firstSummaryLabel.textContent = filter === 'winners' ? 'Total Winners' : 'Total Losers';

      // Update section label
      const sectionLabel = document.querySelector('.section-label');
      if (sectionLabel) sectionLabel.textContent = filter === 'winners' ? 'Winners (Alpha+)' : 'Losers (Alpha−)';

      // Filter rows
      allRows = allRows.filter(row => {
        const v = parseSignedDollar(row.querySelector('.h-alpha').textContent.replace(/^Alpha\s+/, ''));
        if (filter === 'winners') return v > 0;
        else return v < 0;
      });
      // Rebuild container with filtered rows
      while (holdingsContainer.firstChild) holdingsContainer.removeChild(holdingsContainer.firstChild);
      allRows.forEach(r => holdingsContainer.appendChild(r));

      // Recalculate ALL summary stats from filtered rows
      recalculateSummary(allRows);
    }

    // Parse alpha + date from each row's DOM content (cache for sort)
    const months = { Jan:1, Feb:2, Mar:3, Apr:4, May:5, Jun:6, Jul:7, Aug:8, Sep:9, Oct:10, Nov:11, Dec:12 };
    allRows.forEach((row, i) => {
      const alphaText = row.querySelector('.h-alpha').textContent;
      const am = alphaText.match(/([+−-])\s*([\d,]+\.?\d*)/);
      let alpha = 0;
      if (am) {
        alpha = parseFloat(am[2].replace(/,/g, ''));
        if (am[1] === '−' || am[1] === '-') alpha = -alpha;
      }
      row.dataset.alpha = alpha;

      const metaText = row.querySelector('.h-meta').textContent;
      const dm = metaText.match(/Closed\s+(\w+)\s+(\d{4})/);
      let dateNum = 0;
      if (dm) {
        const m = months[dm[1]] || 0;
        const y = parseInt(dm[2]);
        dateNum = y * 100 + m;
      }
      row.dataset.date = dateNum;
      row.dataset.origIdx = i;
    });

    // Drill-down to Stock Page v2
    allRows.forEach(row => {
      row.style.cursor = 'pointer';
      row.addEventListener('click', () => {
        window.location.href = '../../Stock%20Pages/Post%20MVP/Stock%20Page%20v2.html';
      });
    });

    const sortNotes = {
      'alpha-asc': 'Worst alpha first — biggest underperformers vs S&P 500 at the top.',
      'impact': 'Biggest absolute dollar moves first.',
      'recent': 'Most recently closed first.'
    };
    const sortNoteEl = document.getElementById('sortNote');

    function applySort(sortKey) {
      if (sortNoteEl && sortNotes[sortKey]) sortNoteEl.textContent = sortNotes[sortKey];

      let sorted = [...allRows];
      if (sortKey === 'alpha-asc') {
        sorted.sort((a, b) => parseFloat(a.dataset.alpha) - parseFloat(b.dataset.alpha));
      } else if (sortKey === 'impact') {
        sorted.sort((a, b) => Math.abs(parseFloat(b.dataset.alpha)) - Math.abs(parseFloat(a.dataset.alpha)));
      } else if (sortKey === 'recent') {
        sorted.sort((a, b) => parseInt(b.dataset.date) - parseInt(a.dataset.date));
      }
      while (holdingsContainer.firstChild) holdingsContainer.removeChild(holdingsContainer.firstChild);
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
