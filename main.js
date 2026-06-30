// ── Inner tab switching (ROAS page) ──────────────────────────────────────────
document.querySelectorAll('.calc-tabs-inner .calc-tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.calc-tabs-inner .calc-tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.calc-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  });
});

// ── Mode toggle ───────────────────────────────────────────────────────────────
document.querySelectorAll('.calc-mode-toggle .mode-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.closest('.calc-mode-toggle');
    group.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    setMode(btn.dataset.mode);
  });
});

function showFields(show, hide) {
  show.forEach(id => { const el = document.getElementById(id); if (el) el.classList.remove('hidden'); });
  hide.forEach(id => { const el = document.getElementById(id); if (el) el.classList.add('hidden'); });
}

function setMode(mode) {
  const map = {
    'cpm-cpm':    [['field-cpm-cost','field-cpm-impressions'], ['field-cpm-cpm-val']],
    'cpm-cost':   [['field-cpm-cpm-val','field-cpm-impressions'], ['field-cpm-cost']],
    'cpm-imp':    [['field-cpm-cost','field-cpm-cpm-val'], ['field-cpm-impressions']],
    'ctr-ctr':    [['field-ctr-clicks','field-ctr-impressions'], ['field-ctr-ctr-val']],
    'ctr-clicks': [['field-ctr-ctr-val','field-ctr-impressions'], ['field-ctr-clicks']],
    'ctr-imp':    [['field-ctr-clicks','field-ctr-ctr-val'], ['field-ctr-impressions']],
    'cpc-cpc':    [['field-cpc-cost','field-cpc-clicks'], ['field-cpc-cpc-val']],
    'cpc-cost':   [['field-cpc-cpc-val','field-cpc-clicks'], ['field-cpc-cost']],
    'cpc-clicks': [['field-cpc-cost','field-cpc-cpc-val'], ['field-cpc-clicks']],
    'roas-roas':  [['roas-field-rev','roas-field-spend'], ['roas-field-roas']],
    'roas-rev':   [['roas-field-roas','roas-field-spend'], ['roas-field-rev']],
    'roas-spend': [['roas-field-rev','roas-field-roas'], ['roas-field-spend']],
    'poas-poas':  [['poas-field-profit','poas-field-spend'], ['poas-field-poas']],
    'poas-profit':[['poas-field-poas','poas-field-spend'], ['poas-field-profit']],
    'poas-spend': [['poas-field-profit','poas-field-poas'], ['poas-field-spend']],
    'cpl-cpl':    [['field-cpl-cost','field-cpl-leads'], ['field-cpl-cpl-val']],
    'cpl-cost':   [['field-cpl-cpl-val','field-cpl-leads'], ['field-cpl-cost']],
    'cpl-leads':  [['field-cpl-cost','field-cpl-cpl-val'], ['field-cpl-leads']],
    'freq-freq':  [['field-freq-imp','field-freq-reach'], ['field-freq-freq-val']],
    'freq-imp':   [['field-freq-freq-val','field-freq-reach'], ['field-freq-imp']],
    'freq-reach': [['field-freq-imp','field-freq-freq-val'], ['field-freq-reach']],
  };
  if (map[mode]) showFields(map[mode][0], map[mode][1]);
}

// ── Helpers ───────────────────────────────────────────────────────────────────
function getVal(id) { return parseFloat(document.getElementById(id)?.value) || 0; }
function fmtNum(n, d=2) { return n.toLocaleString('en-US', {minimumFractionDigits:d, maximumFractionDigits:d}); }
function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }

function showResult(id, label, value) {
  const el = document.getElementById(id);
  if (!el) return;
  el.classList.remove('hidden');
  el.innerHTML = `<div class="result-label">${label}</div>${value}`;
}

function activeMode(prefix) {
  const btn = document.querySelector(`[data-mode^="${prefix}"].active`);
  return btn ? btn.dataset.mode : null;
}

// ── Calculators ───────────────────────────────────────────────────────────────
function calc_cpm() {
  const mode = activeMode('cpm');
  if (mode === 'cpm-cpm') {
    const cost = getVal('cpm-cost'), imp = getVal('cpm-impressions');
    if (!cost || !imp) return;
    showResult('cpm-result', 'CPM', `$${fmtNum(cost / imp * 1000)}`);
  } else if (mode === 'cpm-cost') {
    const cpm = getVal('cpm-cpm-val'), imp = getVal('cpm-impressions');
    if (!cpm || !imp) return;
    showResult('cpm-result', 'Total Cost', `$${fmtNum(cpm * imp / 1000)}`);
  } else {
    const cost = getVal('cpm-cost'), cpm = getVal('cpm-cpm-val');
    if (!cost || !cpm) return;
    showResult('cpm-result', 'Impressions', fmtInt(cost / cpm * 1000));
  }
}

function calc_ctr() {
  const mode = activeMode('ctr');
  if (mode === 'ctr-ctr') {
    const clicks = getVal('ctr-clicks'), imp = getVal('ctr-impressions');
    if (!clicks || !imp) return;
    showResult('ctr-result', 'CTR', `${fmtNum(clicks / imp * 100)}%`);
  } else if (mode === 'ctr-clicks') {
    const ctr = getVal('ctr-ctr-val'), imp = getVal('ctr-impressions');
    if (!ctr || !imp) return;
    showResult('ctr-result', 'Clicks', fmtInt(ctr / 100 * imp));
  } else {
    const clicks = getVal('ctr-clicks'), ctr = getVal('ctr-ctr-val');
    if (!clicks || !ctr) return;
    showResult('ctr-result', 'Impressions', fmtInt(clicks / (ctr / 100)));
  }
}

function calc_cpc() {
  const mode = activeMode('cpc');
  if (mode === 'cpc-cpc') {
    const cost = getVal('cpc-cost'), clicks = getVal('cpc-clicks');
    if (!cost || !clicks) return;
    showResult('cpc-result', 'CPC', `$${fmtNum(cost / clicks)}`);
  } else if (mode === 'cpc-cost') {
    const cpc = getVal('cpc-cpc-val'), clicks = getVal('cpc-clicks');
    if (!cpc || !clicks) return;
    showResult('cpc-result', 'Total Cost', `$${fmtNum(cpc * clicks)}`);
  } else {
    const cost = getVal('cpc-cost'), cpc = getVal('cpc-cpc-val');
    if (!cost || !cpc) return;
    showResult('cpc-result', 'Clicks', fmtInt(cost / cpc));
  }
}

function calcROAS() {
  const mode = activeMode('roas');
  if (mode === 'roas-roas') {
    const rev = getVal('roas-rev'), spend = getVal('roas-spend');
    if (!rev || !spend) return;
    showResult('roas-result', 'ROAS', `${fmtNum(rev / spend, 2)}x`);
  } else if (mode === 'roas-rev') {
    const roas = getVal('roas-roas'), spend = getVal('roas-spend');
    if (!roas || !spend) return;
    showResult('roas-result', 'Revenue', `$${fmtNum(roas * spend)}`);
  } else {
    const rev = getVal('roas-rev'), roas = getVal('roas-roas');
    if (!rev || !roas) return;
    showResult('roas-result', 'Ad Spend', `$${fmtNum(rev / roas)}`);
  }
}

function calcPOAS() {
  const mode = activeMode('poas');
  if (mode === 'poas-poas') {
    const profit = getVal('poas-profit'), spend = getVal('poas-spend');
    if (!profit || !spend) return;
    showResult('poas-result', 'POAS', `${fmtNum(profit / spend, 2)}x`);
  } else if (mode === 'poas-profit') {
    const poas = getVal('poas-poas'), spend = getVal('poas-spend');
    if (!poas || !spend) return;
    showResult('poas-result', 'Gross Profit', `$${fmtNum(poas * spend)}`);
  } else {
    const profit = getVal('poas-profit'), poas = getVal('poas-poas');
    if (!profit || !poas) return;
    showResult('poas-result', 'Ad Spend', `$${fmtNum(profit / poas)}`);
  }
}

function calc_cpl() {
  const mode = activeMode('cpl');
  if (mode === 'cpl-cpl') {
    const cost = getVal('cpl-cost'), leads = getVal('cpl-leads');
    if (!cost || !leads) return;
    showResult('cpl-result', 'CPL', `$${fmtNum(cost / leads)}`);
  } else if (mode === 'cpl-cost') {
    const cpl = getVal('cpl-cpl-val'), leads = getVal('cpl-leads');
    if (!cpl || !leads) return;
    showResult('cpl-result', 'Total Cost', `$${fmtNum(cpl * leads)}`);
  } else {
    const cost = getVal('cpl-cost'), cpl = getVal('cpl-cpl-val');
    if (!cost || !cpl) return;
    showResult('cpl-result', 'Leads', fmtInt(cost / cpl));
  }
}

function calc_freq() {
  const mode = activeMode('freq');
  if (mode === 'freq-freq') {
    const imp = getVal('freq-imp'), reach = getVal('freq-reach');
    if (!imp || !reach) return;
    showResult('freq-result', 'Frequency', fmtNum(imp / reach, 2));
  } else if (mode === 'freq-imp') {
    const freq = getVal('freq-freq-val'), reach = getVal('freq-reach');
    if (!freq || !reach) return;
    showResult('freq-result', 'Impressions', fmtInt(freq * reach));
  } else {
    const imp = getVal('freq-imp'), freq = getVal('freq-freq-val');
    if (!imp || !freq) return;
    showResult('freq-result', 'Reach', fmtInt(imp / freq));
  }
}

function calcBEROAS() {
  const aov = getVal('be-aov'), cogs = getVal('be-cogs'), other = getVal('be-other');
  if (!aov || !cogs) return;
  const margin = aov - cogs - other;
  if (margin <= 0) { showResult('beroas-result', 'Error', 'COGS + costs exceed AOV'); return; }
  const beroas = aov / margin;
  showResult('beroas-result', 'Break-even ROAS',
    `${fmtNum(beroas, 2)}x <span style="font-size:0.85rem;color:#94A3B8;font-family:Inter,sans-serif;font-weight:400">(margin: ${fmtNum(margin / aov * 100, 1)}%)</span>`);
}


// ── FAQ accordion ─────────────────────────────────────────────────────────────
document.addEventListener('click', e => {
  const q = e.target.closest('.faq-q');
  if (!q) return;
  q.closest('.faq-item').classList.toggle('open');
});
