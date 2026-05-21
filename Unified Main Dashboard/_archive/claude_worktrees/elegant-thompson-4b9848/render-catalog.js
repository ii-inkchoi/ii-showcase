const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FINAL_DIR = path.join(__dirname, 'Final');

// Order follows the Gallery/Figma file order
const SCENARIOS = [
  // --- Unified Dashboard (base) ---
  { cat: 'Unified Dashboard', id: 'unified-dashboard', file: 'Unified Dashboard.html', param: '',
    title: 'Unified Dashboard — Fully Active',
    desc: 'Combined view with Managed (126,471.77) and Self-Directed (46,777.23) both active. Total 173,249.00 CAD.',
    target: true },

  // --- Managed (8) ---
  { cat: 'Managed', id: 'm-core-open-no-investment', file: 'Managed.html', param: 's=core-open-no-investment',
    title: 'Core Account · No Investment', desc: 'Core account open but no investment scheduled.' },
  { cat: 'Managed', id: 'm-no-managed-accounts', file: 'Managed.html', param: 's=no-managed-accounts',
    title: 'No Managed Accounts', desc: 'No managed accounts exist.' },
  { cat: 'Managed', id: 'm-no-capital-active-unscheduled', file: 'Managed.html', param: 's=no-capital-active-unscheduled',
    title: 'No Capital · Active · No Schedule', desc: 'Account exists · no capital · no scheduled investments · portfolio active.' },
  { cat: 'Managed', id: 'm-no-capital-active-scheduled', file: 'Managed.html', param: 's=no-capital-active-scheduled',
    title: 'No Capital · Active · Scheduled', desc: 'Account exists · no capital · scheduled investments · portfolio active.' },
  { cat: 'Managed', id: 'm-no-capital-inactive-unscheduled', file: 'Managed.html', param: 's=no-capital-inactive-unscheduled',
    title: 'No Capital · Inactive · No Schedule', desc: 'Account exists · no capital · no scheduled investments · portfolio inactive.' },
  { cat: 'Managed', id: 'm-no-capital-inactive-scheduled', file: 'Managed.html', param: 's=no-capital-inactive-scheduled',
    title: 'No Capital · Inactive · Scheduled', desc: 'Account exists · no capital · scheduled investments · portfolio inactive.' },
  { cat: 'Managed', id: 'm-capital-inactive', file: 'Managed.html', param: 's=capital-inactive',
    title: 'Capital · Inactive', desc: 'Has capital · portfolio inactive (most existing managed users).' },
  { cat: 'Managed', id: 'm-capital-active', file: 'Managed.html', param: 's=capital-active',
    title: 'Capital · Active', desc: 'Has capital · portfolio active (target state). Total 173,249.00 CAD.', target: true },

  // --- Self-Directed (10) ---
  { cat: 'Self-Directed', id: 'sd-no-accounts', file: 'SelfDirected.html', param: 's=no-accounts',
    title: 'No Accounts', desc: 'No self-directed accounts · open account CTA.' },
  { cat: 'Self-Directed', id: 'sd-no-capital-add-funds', file: 'SelfDirected.html', param: 's=no-capital-add-funds',
    title: 'No Capital · Add Funds', desc: '0.00 · no capital deployed · add funds · under review 4.' },
  { cat: 'Self-Directed', id: 'sd-tfsa-transfer-pending', file: 'SelfDirected.html', param: 's=tfsa-transfer-pending',
    title: 'TFSA · Transfer Pending', desc: 'TFSA · 0.00 · no capital deployed · transfer pending.' },
  { cat: 'Self-Directed', id: 'sd-core-inactive-tfsa', file: 'SelfDirected.html', param: 's=core-inactive-tfsa',
    title: 'All Inactive · TFSA', desc: 'Total 0 · Core Portfolio inactive · TFSA add funds.' },
  { cat: 'Self-Directed', id: 'sd-active-rrsp', file: 'SelfDirected.html', param: 's=active-rrsp',
    title: 'Active · RRSP', desc: 'Full active state · RRSP settlement message. Total 173,249.00 CAD.', target: true },
  { cat: 'Self-Directed', id: 'sd-tfsa-opening', file: 'SelfDirected.html', param: 's=tfsa-opening',
    title: 'TFSA · Opening', desc: 'Account opening message · ID in review.' },
  { cat: 'Self-Directed', id: 'sd-rrsp-opening', file: 'SelfDirected.html', param: 's=rrsp-opening',
    title: 'RRSP · Opening', desc: 'Account opening message · ID in review.' },
  { cat: 'Self-Directed', id: 'sd-nonreg-opening', file: 'SelfDirected.html', param: 's=nonreg-opening',
    title: 'Non-Registered · Opening', desc: 'Account opening message · ID in review.' },
  { cat: 'Self-Directed', id: 'sd-identity-in-review', file: 'SelfDirected.html', param: 's=identity-in-review',
    title: 'Identity · In Review', desc: 'ID under review · verification in progress · transfers unavailable.' },
  { cat: 'Self-Directed', id: 'sd-identity-failed', file: 'SelfDirected.html', param: 's=identity-failed',
    title: 'Identity · Failed', desc: 'ID verification failed · try again.' },

  // --- Managed + Self-Directed (6 — splitting "fully-active" into with/without orders) ---
  { cat: 'Managed + Self-Directed', id: 'umd-fully-active-orders', file: 'ManagedSelfDirected.html', param: 's=fully-active-orders',
    title: 'Fully Active · With Orders', desc: 'Both Managed + Self-Directed fully active with pending orders. Total 173,249.00 CAD.', target: true },
  { cat: 'Managed + Self-Directed', id: 'umd-fully-active-no-orders', file: 'ManagedSelfDirected.html', param: 's=fully-active-no-orders',
    title: 'Fully Active · No Orders', desc: 'Both Managed + Self-Directed fully active with no orders. Total 173,249.00 CAD.', target: true },
  { cat: 'Managed + Self-Directed', id: 'umd-no-capital', file: 'ManagedSelfDirected.html', param: 's=no-capital',
    title: 'No Capital', desc: 'Core inactive · Self-directed 0.00 · Add Funds.' },
  { cat: 'Managed + Self-Directed', id: 'umd-no-accounts', file: 'ManagedSelfDirected.html', param: 's=no-accounts',
    title: 'No Accounts', desc: 'Core inactive · no Self-directed accounts.' },
  { cat: 'Managed + Self-Directed', id: 'umd-no-managed-sched-no-sd', file: 'ManagedSelfDirected.html', param: 's=no-managed-sched-no-sd',
    title: 'No Managed Schedule · No SD Accounts', desc: 'Core inactive · no capital deployed · no Self-directed accounts.' },
  { cat: 'Managed + Self-Directed', id: 'umd-managed-sched-no-accts', file: 'ManagedSelfDirected.html', param: 's=managed-sched-no-accts',
    title: 'Managed Scheduled · No SD Accounts', desc: 'Managed first investment scheduled · no Self-directed accounts.' },

  // --- Account Sheet (reference) ---
  { cat: 'Account Sheet', id: 'account-sheet', file: 'Account_Sheet.html', param: '',
    title: 'Account Sheet', desc: 'Configuration reference for Managed, Self-Directed, and combined accounts.' },
];

const CATEGORY_INFO = {
  'Unified Dashboard': 'Combined view of Managed + Self-Directed portfolios in the fully-active target state.',
  'Managed': 'Managed-only prototype states. Covers every combination of capital, activity, and scheduling.',
  'Self-Directed': 'Self-Directed-only states — onboarding, identity verification, funding, and the active trading state.',
  'Managed + Self-Directed': 'Mixed-product states for users on both Managed and Self-Directed.',
  'Account Sheet': 'Internal reference sheet for account configurations across the prototypes.',
};

// Inline all computed styles so each rendered DOM is self-contained (no CSS conflict)
async function renderScenario(browser, s) {
  const context = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2 });
  const page = await context.newPage();
  const fileUrl = 'file:///' + path.join(FINAL_DIR, s.file).replace(/\\/g, '/').replace(/ /g, '%20') + (s.param ? '?' + s.param : '');

  await page.goto(fileUrl, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(1200); // let animations settle

  const html = await page.evaluate(() => {
    // Clone document, inline computed styles on every element
    const clone = document.body.cloneNode(true);
    const srcEls = document.body.querySelectorAll('*');
    const cloneEls = clone.querySelectorAll('*');
    const IGNORED_PROPS = new Set(['transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'animation', 'animation-delay', 'animation-duration', 'animation-iteration-count', 'animation-name', 'animation-timing-function', 'animation-fill-mode']);
    for (let i = 0; i < srcEls.length; i++) {
      const comp = getComputedStyle(srcEls[i]);
      let style = '';
      for (let j = 0; j < comp.length; j++) {
        const prop = comp[j];
        if (IGNORED_PROPS.has(prop)) continue;
        const val = comp.getPropertyValue(prop);
        if (val) style += `${prop}:${val};`;
      }
      cloneEls[i].setAttribute('style', style);
    }
    // Remove scripts so they don't re-run
    clone.querySelectorAll('script').forEach(el => el.remove());
    return clone.innerHTML;
  });

  await page.close();
  await context.close();
  return html;
}

function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

(async () => {
  const browser = await chromium.launch();
  console.log('Rendering', SCENARIOS.length, 'scenarios...');
  const rendered = [];
  for (const s of SCENARIOS) {
    process.stdout.write(`  - ${s.id} ... `);
    try {
      const html = await renderScenario(browser, s);
      rendered.push({ ...s, html });
      console.log('ok (', html.length, 'chars)');
    } catch (err) {
      console.log('FAILED:', err.message);
      rendered.push({ ...s, html: `<div style="color:red;padding:16px;">Failed to render: ${esc(err.message)}</div>` });
    }
  }
  await browser.close();

  // Build catalog
  const seenCats = new Set();
  let body = '';
  for (const r of rendered) {
    if (!seenCats.has(r.cat)) {
      seenCats.add(r.cat);
      body += `
  <section class="category" id="cat-${r.cat.replace(/[^a-z0-9]+/gi, '-').toLowerCase()}">
    <div class="cat-head">
      <div class="eyebrow">${esc(r.cat)}</div>
      <h2>${esc(r.cat)}</h2>
      <p class="cat-desc">${esc(CATEGORY_INFO[r.cat] || '')}</p>
    </div>
    <div class="cat-grid">`;
    }
    const isLastInCat = rendered[rendered.indexOf(r) + 1]?.cat !== r.cat;
    body += `
      <article class="card${r.target ? ' target' : ''}" id="${r.id}">
        <div class="card-head">
          <div class="tag-row">
            <span class="tag">${esc(r.param ? r.param.replace('s=', '') : 'default')}</span>
            ${r.target ? '<span class="tag target">Target</span>' : ''}
          </div>
          <h3>${esc(r.title)}</h3>
          <p>${esc(r.desc)}</p>
        </div>
        <div class="mobile-frame">${r.html}</div>
      </article>`;
    if (isLastInCat) body += `\n    </div>\n  </section>`;
  }

  const out = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Unified Main Dashboard — Figma Export Catalog (Flat)</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0a; --surface: #111; --border: rgba(255,255,255,0.08);
    --text: #e8e8e8; --text-dim: rgba(255,255,255,0.55); --text-faint: rgba(255,255,255,0.35);
    --accent: #c9a96e;
  }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; }
  body { padding: 48px 32px 96px; max-width: 1680px; margin: 0 auto; }
  .doc-head { margin-bottom: 56px; padding-bottom: 32px; border-bottom: 1px solid var(--border); }
  .doc-head h1 { font-size: 32px; font-weight: 600; margin: 0 0 12px; letter-spacing: -0.02em; }
  .doc-head p { color: var(--text-dim); font-size: 15px; line-height: 1.6; max-width: 820px; margin: 0 0 12px; }
  .doc-head .meta { font-size: 13px; color: var(--text-faint); }
  .doc-head .meta strong { color: var(--text-dim); font-weight: 500; }
  .category { margin-bottom: 72px; }
  .cat-head { margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
  .cat-head .eyebrow { font-size: 11px; letter-spacing: 0.18em; color: var(--accent); text-transform: uppercase; margin-bottom: 8px; font-weight: 500; }
  .cat-head h2 { font-size: 22px; font-weight: 600; margin: 0 0 10px; letter-spacing: -0.01em; }
  .cat-head .cat-desc { color: var(--text-dim); font-size: 14px; line-height: 1.65; max-width: 820px; margin: 0; }
  .cat-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); gap: 28px; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
  .card.target { border-color: rgba(201,169,110,0.3); }
  .card-head { padding: 18px 20px 16px; border-bottom: 1px solid var(--border); }
  .card-head .tag-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }
  .card-head .tag { font-size: 10.5px; letter-spacing: 0.1em; text-transform: uppercase; padding: 3px 8px; border: 1px solid var(--border); border-radius: 4px; color: var(--text-faint); font-weight: 500; }
  .card-head .tag.target { color: var(--accent); border-color: rgba(201,169,110,0.35); }
  .card-head h3 { font-size: 16px; font-weight: 600; margin: 0 0 6px; letter-spacing: -0.005em; }
  .card-head p { font-size: 13px; line-height: 1.6; color: var(--text-dim); margin: 0; }
  .mobile-frame { background: #000; padding: 16px; display: flex; justify-content: center; }
  .mobile-frame > div, .mobile-frame { all: initial; }
  .mobile-frame { background: #000; padding: 16px; display: flex; justify-content: center; font-family: 'Inter', sans-serif; }
  .scene { width: 390px; height: 780px; overflow: hidden; background: #000; border-radius: 8px; position: relative; }
</style>
</head>
<body>
  <header class="doc-head">
    <h1>Unified Main Dashboard — Figma Export Catalog</h1>
    <p>Fully-rendered, self-contained snapshot of every prototype state. Designed to be imported into Figma via the <strong>html.to.design</strong> plugin — no iframes, all content inline.</p>
    <div class="meta"><strong>Surface:</strong> Mobile (390 × 780) &nbsp;·&nbsp; <strong>Total Value (fully-active):</strong> 173,249.00 CAD</div>
  </header>
${body}
</body>
</html>`;

  // Wrap each rendered html in .scene
  const finalOut = out.replace(/<div class="mobile-frame">([\s\S]*?)<\/div>\s*<\/article>/g, (_, inner) => {
    return `<div class="mobile-frame"><div class="scene">${inner}</div></div></article>`;
  });

  const outPath = path.join(FINAL_DIR, 'Figma_Catalog_Flat.html');
  fs.writeFileSync(outPath, finalOut, 'utf8');
  console.log('\nWritten:', outPath);
  console.log('Size:', (finalOut.length / 1024).toFixed(1), 'KB');
})();
