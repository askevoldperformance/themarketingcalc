// ── Tab switching ────────────────────────────────────────────────────────────
document.querySelectorAll('.calc-tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.calc-tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.calc-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  });
});

// ── Mode toggle (find X / find Y) ────────────────────────────────────────────
document.querySelectorAll('.calc-mode-toggle .mode-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.closest('.calc-mode-toggle');
    group.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    setMode(btn.dataset.mode);
  });
});

function showFields(panel, show, hide) {
  show.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('hidden');
  });
  hide.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.add('hidden');
  });
}

function setMode(mode) {
  const modes = {
    'cpm-cpm':   [['cpm-field-cost','cpm-field-imp'], ['cpm-field-cpm']],
    'cpm-cost':  [['cpm-field-cpm','cpm-field-imp'], ['cpm-field-cost']],
    'cpm-imp':   [['cpm-field-cost','cpm-field-cpm'], ['cpm-field-imp']],
    'ctr-ctr':   [['ctr-field-clicks','ctr-field-imp'], ['ctr-field-ctr']],
    'ctr-clicks':[['ctr-field-ctr','ctr-field-imp'], ['ctr-field-clicks']],
    'ctr-imp':   [['ctr-field-clicks','ctr-field-ctr'], ['ctr-field-imp']],
    'cpc-cpc':   [['cpc-field-cost','cpc-field-clicks'], ['cpc-field-cpc']],
    'cpc-cost':  [['cpc-field-cpc','cpc-field-clicks'], ['cpc-field-cost']],
    'cpc-clicks':[['cpc-field-cost','cpc-field-cpc'], ['cpc-field-clicks']],
    'roas-roas': [['roas-field-rev','roas-field-spend'], ['roas-field-roas']],
    'roas-rev':  [['roas-field-roas','roas-field-spend'], ['roas-field-rev']],
    'roas-spend':[['roas-field-rev','roas-field-roas'], ['roas-field-spend']],
    'poas-poas': [['poas-field-profit','poas-field-spend'], ['poas-field-poas']],
    'poas-profit':[['poas-field-poas','poas-field-spend'], ['poas-field-profit']],
    'poas-spend':[['poas-field-profit','poas-field-poas'], ['poas-field-spend']],
    'cpl-cpl':   [['cpl-field-cost','cpl-field-leads'], ['cpl-field-cpl']],
    'cpl-cost':  [['cpl-field-cpl','cpl-field-leads'], ['cpl-field-cost']],
    'cpl-leads': [['cpl-field-cost','cpl-field-cpl'], ['cpl-field-leads']],
    'freq-freq': [['freq-field-imp','freq-field-reach'], ['freq-field-freq']],
    'freq-imp':  [['freq-field-freq','freq-field-reach'], ['freq-field-imp']],
    'freq-reach':[['freq-field-imp','freq-field-freq'], ['freq-field-reach']],
  };
  if (modes[mode]) showFields(null, modes[mode][0], modes[mode][1]);
}

// ── Result display ───────────────────────────────────────────────────────────
function showResult(id, label, value) {
  const el = document.getElementById(id);
  el.classList.remove('hidden');
  el.innerHTML = `<div class="result-label">${label}</div>${value}`;
}

function fmtNum(n, decimals = 2) {
  return n.toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
}
function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }

// ── Calculators ──────────────────────────────────────────────────────────────
function activeMode(prefix) {
  const btn = document.querySelector(`[data-mode^="${prefix}"].active`);
  return btn ? btn.dataset.mode : null;
}

function getVal(id) { return parseFloat(document.getElementById(id)?.value) || 0; }

function calcCPM() {
  const mode = activeMode('cpm');
  if (mode === 'cpm-cpm') {
    const cost = getVal('cpm-cost'), imp = getVal('cpm-impressions');
    if (!cost || !imp) return;
    showResult('cpm-result', 'CPM', `$${fmtNum(cost / imp * 1000)}`);
  } else if (mode === 'cpm-cost') {
    const cpm = getVal('cpm-cpm'), imp = getVal('cpm-impressions');
    if (!cpm || !imp) return;
    showResult('cpm-result', 'Total Cost', `$${fmtNum(cpm * imp / 1000)}`);
  } else {
    const cost = getVal('cpm-cost'), cpm = getVal('cpm-cpm');
    if (!cost || !cpm) return;
    showResult('cpm-result', 'Impressions', fmtInt(cost / cpm * 1000));
  }
}

function calcCTR() {
  const mode = activeMode('ctr');
  if (mode === 'ctr-ctr') {
    const clicks = getVal('ctr-clicks'), imp = getVal('ctr-impressions');
    if (!clicks || !imp) return;
    showResult('ctr-result', 'CTR', `${fmtNum(clicks / imp * 100)}%`);
  } else if (mode === 'ctr-clicks') {
    const ctr = getVal('ctr-ctr'), imp = getVal('ctr-impressions');
    if (!ctr || !imp) return;
    showResult('ctr-result', 'Clicks', fmtInt(ctr / 100 * imp));
  } else {
    const clicks = getVal('ctr-clicks'), ctr = getVal('ctr-ctr');
    if (!clicks || !ctr) return;
    showResult('ctr-result', 'Impressions', fmtInt(clicks / (ctr / 100)));
  }
}

function calcCPC() {
  const mode = activeMode('cpc');
  if (mode === 'cpc-cpc') {
    const cost = getVal('cpc-cost'), clicks = getVal('cpc-clicks');
    if (!cost || !clicks) return;
    showResult('cpc-result', 'CPC', `$${fmtNum(cost / clicks)}`);
  } else if (mode === 'cpc-cost') {
    const cpc = getVal('cpc-cpc'), clicks = getVal('cpc-clicks');
    if (!cpc || !clicks) return;
    showResult('cpc-result', 'Total Cost', `$${fmtNum(cpc * clicks)}`);
  } else {
    const cost = getVal('cpc-cost'), cpc = getVal('cpc-cpc');
    if (!cost || !cpc) return;
    showResult('cpc-result', 'Clicks', fmtInt(cost / cpc));
  }
}

function calcROAS() {
  const mode = activeMode('roas');
  if (mode === 'roas-roas') {
    const rev = getVal('roas-rev'), spend = getVal('roas-spend');
    if (!rev || !spend) return;
    showResult('roas-result', 'ROAS', `${fmtNum(rev / spend, 2)}×`);
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
    showResult('poas-result', 'POAS', `${fmtNum(profit / spend, 2)}×`);
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

function calcCPL() {
  const mode = activeMode('cpl');
  if (mode === 'cpl-cpl') {
    const cost = getVal('cpl-cost'), leads = getVal('cpl-leads');
    if (!cost || !leads) return;
    showResult('cpl-result', 'CPL', `$${fmtNum(cost / leads)}`);
  } else if (mode === 'cpl-cost') {
    const cpl = getVal('cpl-cpl'), leads = getVal('cpl-leads');
    if (!cpl || !leads) return;
    showResult('cpl-result', 'Total Cost', `$${fmtNum(cpl * leads)}`);
  } else {
    const cost = getVal('cpl-cost'), cpl = getVal('cpl-cpl');
    if (!cost || !cpl) return;
    showResult('cpl-result', 'Leads', fmtInt(cost / cpl));
  }
}

function calcFreq() {
  const mode = activeMode('freq');
  if (mode === 'freq-freq') {
    const imp = getVal('freq-imp'), reach = getVal('freq-reach');
    if (!imp || !reach) return;
    showResult('freq-result', 'Frequency', fmtNum(imp / reach, 2));
  } else if (mode === 'freq-imp') {
    const freq = getVal('freq-freq'), reach = getVal('freq-reach');
    if (!freq || !reach) return;
    showResult('freq-result', 'Impressions', fmtInt(freq * reach));
  } else {
    const imp = getVal('freq-imp'), freq = getVal('freq-freq');
    if (!imp || !freq) return;
    showResult('freq-result', 'Reach', fmtInt(imp / freq));
  }
}

function calcBEROAS() {
  const aov = getVal('be-aov'), cogs = getVal('be-cogs'), other = getVal('be-other');
  if (!aov || !cogs) return;
  const margin = aov - cogs - other;
  if (margin <= 0) {
    showResult('beroas-result', 'Error', 'COGS + other costs exceed AOV');
    return;
  }
  const beroas = aov / margin;
  showResult('beroas-result', 'Break-even ROAS',
    `${fmtNum(beroas, 2)}× <span style="font-size:0.85rem;color:#94A3B8;font-family:Inter,sans-serif;font-weight:400">(margin: ${fmtNum(margin / aov * 100, 1)}%)</span>`);
}

// ── Budget calculator ─────────────────────────────────────────────────────────
const BENCHMARKS = {
  US:  { meta: {cpm:10,cpc:0.8,ctr:1.2}, google: {cpm:null,cpc:3.5,ctr:3.8}, linkedin: {cpm:55,cpc:8,ctr:0.5}, tiktok: {cpm:11,cpc:0.5,ctr:0.8}, snapchat: {cpm:6,cpc:0.4,ctr:0.7}, reddit: {cpm:7,cpc:0.6,ctr:0.6}, x: {cpm:7,cpc:0.5,ctr:0.8} },
  UK:  { meta: {cpm:8,cpc:0.7,ctr:1.1}, google: {cpm:null,cpc:3.0,ctr:3.5}, linkedin: {cpm:50,cpc:7,ctr:0.5}, tiktok: {cpm:9,cpc:0.4,ctr:0.8}, snapchat: {cpm:5,cpc:0.35,ctr:0.7}, reddit: {cpm:6,cpc:0.5,ctr:0.6}, x: {cpm:6,cpc:0.4,ctr:0.7} },
  NO:  { meta: {cpm:12,cpc:0.9,ctr:1.1}, google: {cpm:null,cpc:4.0,ctr:3.5}, linkedin: {cpm:60,cpc:9,ctr:0.5}, tiktok: {cpm:10,cpc:0.5,ctr:0.8}, snapchat: {cpm:5,cpc:0.4,ctr:0.8}, reddit: {cpm:6,cpc:0.5,ctr:0.5}, x: {cpm:7,cpc:0.5,ctr:0.7} },
  SE:  { meta: {cpm:11,cpc:0.85,ctr:1.1}, google: {cpm:null,cpc:3.8,ctr:3.5}, linkedin: {cpm:58,cpc:8.5,ctr:0.5}, tiktok: {cpm:10,cpc:0.5,ctr:0.8}, snapchat: {cpm:5,cpc:0.4,ctr:0.7}, reddit: {cpm:6,cpc:0.5,ctr:0.5}, x: {cpm:7,cpc:0.5,ctr:0.7} },
  DK:  { meta: {cpm:11,cpc:0.85,ctr:1.1}, google: {cpm:null,cpc:3.8,ctr:3.5}, linkedin: {cpm:58,cpc:8.5,ctr:0.5}, tiktok: {cpm:10,cpc:0.5,ctr:0.8}, snapchat: {cpm:5,cpc:0.4,ctr:0.7}, reddit: {cpm:6,cpc:0.5,ctr:0.5}, x: {cpm:7,cpc:0.5,ctr:0.7} },
  EU:  { meta: {cpm:9,cpc:0.75,ctr:1.1}, google: {cpm:null,cpc:3.2,ctr:3.6}, linkedin: {cpm:52,cpc:7.5,ctr:0.5}, tiktok: {cpm:9,cpc:0.45,ctr:0.8}, snapchat: {cpm:5,cpc:0.38,ctr:0.7}, reddit: {cpm:6,cpc:0.5,ctr:0.5}, x: {cpm:6,cpc:0.45,ctr:0.7} },
  AU:  { meta: {cpm:9,cpc:0.75,ctr:1.1}, google: {cpm:null,cpc:3.0,ctr:3.6}, linkedin: {cpm:50,cpc:7,ctr:0.5}, tiktok: {cpm:9,cpc:0.45,ctr:0.8}, snapchat: {cpm:5,cpc:0.35,ctr:0.7}, reddit: {cpm:6,cpc:0.5,ctr:0.5}, x: {cpm:6,cpc:0.4,ctr:0.7} },
};
const SYMBOLS = { USD:'$', GBP:'£', NOK:'kr', SEK:'kr', DKK:'kr', EUR:'€', AUD:'A$' };
const CHANNEL_NAMES = { meta:'Meta', google:'Google Ads', linkedin:'LinkedIn', tiktok:'TikTok', snapchat:'Snapchat', reddit:'Reddit', x:'X (Twitter)' };

let selectedMarket = 'US', selectedCurrency = 'USD', selectedObjective = 'reach', selectedDirection = 'budget-to-results';
let selectedChannels = new Set(['meta']);

document.querySelectorAll('.market-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.market-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    selectedMarket = btn.dataset.market;
    selectedCurrency = btn.dataset.currency;
    document.querySelectorAll('.currency-label').forEach(el => el.textContent = selectedCurrency);
    document.getElementById('benchmark-market').textContent = selectedMarket;
    renderBenchmarks();
  });
});

document.querySelectorAll('.channel-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const ch = btn.dataset.channel;
    if (selectedChannels.has(ch) && selectedChannels.size > 1) {
      selectedChannels.delete(ch);
      btn.classList.remove('active');
    } else if (!selectedChannels.has(ch)) {
      selectedChannels.add(ch);
      btn.classList.add('active');
    }
    renderBenchmarks();
  });
});

document.querySelectorAll('.obj-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.obj-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    selectedObjective = btn.dataset.obj;
    updateGoalLabel();
  });
});

document.querySelectorAll('.dir-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.dir-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    selectedDirection = btn.dataset.dir;
    document.getElementById('budget-to-results-inputs').classList.toggle('hidden', selectedDirection !== 'budget-to-results');
    document.getElementById('goals-to-budget-inputs').classList.toggle('hidden', selectedDirection !== 'goals-to-budget');
  });
});

function updateGoalLabel() {
  const labels = { reach: 'Target Impressions', clicks: 'Target Clicks', conversions: 'Target Conversions' };
  const el = document.getElementById('goal-label');
  if (el) el.textContent = labels[selectedObjective] || 'Target';
}

function calcBudget() {
  const sym = SYMBOLS[selectedCurrency] || '$';
  const data = BENCHMARKS[selectedMarket];
  const channels = [...selectedChannels];
  const result = document.getElementById('budget-result');
  result.classList.remove('hidden');

  let html = '';
  channels.forEach(ch => {
    const b = data[ch];
    if (!b) return;
    if (selectedDirection === 'budget-to-results') {
      const budget = getVal('b2r-budget');
      if (!budget) return;
      const perChannel = budget / channels.length;
      if (selectedObjective === 'reach') {
        const imp = perChannel / b.cpm * 1000;
        html += `<div style="margin-bottom:10px"><strong>${CHANNEL_NAMES[ch]}:</strong> ~${fmtInt(imp)} impressions (CPM: ${sym}${fmtNum(b.cpm)})</div>`;
      } else if (selectedObjective === 'clicks') {
        const cpc = b.cpc;
        const clicks = perChannel / cpc;
        html += `<div style="margin-bottom:10px"><strong>${CHANNEL_NAMES[ch]}:</strong> ~${fmtInt(clicks)} clicks (CPC: ${sym}${fmtNum(cpc)})</div>`;
      } else {
        const cpc = b.cpc, cr = 0.02;
        const convs = (perChannel / cpc) * cr;
        html += `<div style="margin-bottom:10px"><strong>${CHANNEL_NAMES[ch]}:</strong> ~${fmtInt(convs)} conversions at 2% CVR (CPC: ${sym}${fmtNum(cpc)})</div>`;
      }
    } else {
      const goal = getVal('g2b-goal');
      if (!goal) return;
      let budgetNeeded = 0;
      if (selectedObjective === 'reach') budgetNeeded = goal / 1000 * b.cpm;
      else if (selectedObjective === 'clicks') budgetNeeded = goal * b.cpc;
      else budgetNeeded = goal / 0.02 * b.cpc;
      html += `<div style="margin-bottom:10px"><strong>${CHANNEL_NAMES[ch]}:</strong> ~${sym}${fmtNum(budgetNeeded)} required</div>`;
    }
  });
  result.innerHTML = `<div class="result-label">Estimated results</div>${html}<div style="font-size:0.78rem;color:#64748B;margin-top:8px">Estimates based on market benchmarks. Actual results depend on creative, audience, and bidding.</div>`;
}

function renderBenchmarks() {
  const data = BENCHMARKS[selectedMarket];
  const sym = SYMBOLS[selectedCurrency] || '$';
  const channels = Object.keys(CHANNEL_NAMES);
  let html = '<table><thead><tr><th>Channel</th><th>CPM</th><th>Avg CPC</th><th>Avg CTR</th></tr></thead><tbody>';
  channels.forEach(ch => {
    const b = data[ch];
    const active = selectedChannels.has(ch) ? 'style="color:var(--text)"' : 'style="color:var(--text-muted)"';
    html += `<tr ${active}><td>${CHANNEL_NAMES[ch]}</td><td>${b.cpm ? sym + fmtNum(b.cpm) : '—'}</td><td>${sym}${fmtNum(b.cpc)}</td><td>${fmtNum(b.ctr, 1)}%</td></tr>`;
  });
  html += '</tbody></table>';
  const el = document.getElementById('benchmark-table');
  if (el) el.innerHTML = html;
}

// ── Mobile nav ───────────────────────────────────────────────────────────────
const hamburger = document.querySelector('.nav-hamburger');
const navLinks = document.querySelector('.nav-links');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// ── Init ─────────────────────────────────────────────────────────────────────
if (document.getElementById('benchmark-table')) renderBenchmarks();
