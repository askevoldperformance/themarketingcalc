// ──────────────────────────────────────────────────────────────────────────
// Budget Calculator v3 - data and logic
// Benchmarks are blended 2026 estimates, already in local currency per market.
// Baseline = Reach/Awareness objective (multipliers applied for other objectives).
// ──────────────────────────────────────────────────────────────────────────

const MARKETS = {
  US: { name: "United States", flag: "\u{1F1FA}\u{1F1F8}", currency: "USD", population: 341000000, internetPct: 0.92 },
  UK: { name: "United Kingdom", flag: "\u{1F1EC}\u{1F1E7}", currency: "GBP", population: 68500000, internetPct: 0.96 },
  NO: { name: "Norway",         flag: "\u{1F1F3}\u{1F1F4}", currency: "NOK", population: 5550000,  internetPct: 0.99 },
  SE: { name: "Sweden",         flag: "\u{1F1F8}\u{1F1EA}", currency: "SEK", population: 10600000, internetPct: 0.98 },
  DK: { name: "Denmark",        flag: "\u{1F1E9}\u{1F1F0}", currency: "DKK", population: 5950000,  internetPct: 0.99 },
  DE: { name: "Germany",        flag: "\u{1F1E9}\u{1F1EA}", currency: "EUR", population: 84500000, internetPct: 0.94 },
  AU: { name: "Australia",      flag: "\u{1F1E6}\u{1F1FA}", currency: "AUD", population: 26600000, internetPct: 0.97 },
};

// Age distribution as % of total population
const AGE_DISTRIBUTION = {
  "18-24": 0.10, "25-34": 0.15, "35-44": 0.14,
  "45-54": 0.13, "55-64": 0.12, "65+": 0.17,
};
const GENDER_DISTRIBUTION = { all: 1.0, male: 0.495, female: 0.505 };

// Benchmarks per currency - baseline = Reach/Awareness objective
// CTR stored as decimal (0.014 = 1.4%)
const BENCHMARKS = {
  USD: {
    meta:      { cpm: 14.5,  cpc: 1.65,  ctr: 0.014, reach: 0.80 },
    linkedin:  { cpm: 75.0,  cpc: 11.0,  ctr: 0.005, reach: 0.35 },
    tiktok:    { cpm: 9.5,   cpc: 0.95,  ctr: 0.009, reach: 0.45 },
    snapchat:  { cpm: 7.0,   cpc: 0.80,  ctr: 0.007, reach: 0.38 },
    google:    { cpm: 0,     cpc: 4.5,   ctr: 0.045, reach: 0.92 },
    youtube:   { cpm: 12.0,  cpc: 0.45,  ctr: 0.006, reach: 0.88 },
    pmax:      { cpm: 18.0,  cpc: 2.80,  ctr: 0.019, reach: 0.88 },
    demandgen: { cpm: 12.5,  cpc: 1.10,  ctr: 0.010, reach: 0.70 },
    bing:      { cpm: 0,     cpc: 2.20,  ctr: 0.032, reach: 0.36 },
  },
  GBP: {
    meta:      { cpm: 7.5,   cpc: 0.85,  ctr: 0.014, reach: 0.82 },
    linkedin:  { cpm: 48.0,  cpc: 7.00,  ctr: 0.005, reach: 0.38 },
    tiktok:    { cpm: 5.0,   cpc: 0.55,  ctr: 0.009, reach: 0.42 },
    snapchat:  { cpm: 4.0,   cpc: 0.45,  ctr: 0.007, reach: 0.32 },
    google:    { cpm: 0,     cpc: 2.40,  ctr: 0.045, reach: 0.94 },
    youtube:   { cpm: 8.0,   cpc: 0.28,  ctr: 0.006, reach: 0.90 },
    pmax:      { cpm: 9.5,   cpc: 1.60,  ctr: 0.019, reach: 0.90 },
    demandgen: { cpm: 6.0,   cpc: 0.60,  ctr: 0.010, reach: 0.74 },
    bing:      { cpm: 0,     cpc: 1.20,  ctr: 0.030, reach: 0.38 },
  },
  NOK: {
    meta:      { cpm: 50.0,  cpc: 5.50,  ctr: 0.014, reach: 0.81 },
    linkedin:  { cpm: 450.0, cpc: 65.0,  ctr: 0.005, reach: 0.42 },
    tiktok:    { cpm: 35.0,  cpc: 4.00,  ctr: 0.009, reach: 0.38 },
    snapchat:  { cpm: 28.0,  cpc: 3.20,  ctr: 0.007, reach: 0.30 },
    google:    { cpm: 0,     cpc: 18.0,  ctr: 0.045, reach: 0.95 },
    youtube:   { cpm: 55.0,  cpc: 2.20,  ctr: 0.006, reach: 0.90 },
    pmax:      { cpm: 65.0,  cpc: 12.0,  ctr: 0.019, reach: 0.90 },
    demandgen: { cpm: 40.0,  cpc: 4.50,  ctr: 0.010, reach: 0.76 },
    bing:      { cpm: 0,     cpc: 8.00,  ctr: 0.028, reach: 0.42 },
  },
  SEK: {
    meta:      { cpm: 45.0,  cpc: 5.00,  ctr: 0.014, reach: 0.83 },
    linkedin:  { cpm: 420.0, cpc: 60.0,  ctr: 0.005, reach: 0.45 },
    tiktok:    { cpm: 32.0,  cpc: 3.80,  ctr: 0.009, reach: 0.40 },
    snapchat:  { cpm: 25.0,  cpc: 3.00,  ctr: 0.007, reach: 0.32 },
    google:    { cpm: 0,     cpc: 16.0,  ctr: 0.045, reach: 0.95 },
    youtube:   { cpm: 50.0,  cpc: 2.00,  ctr: 0.006, reach: 0.90 },
    pmax:      { cpm: 60.0,  cpc: 11.0,  ctr: 0.019, reach: 0.90 },
    demandgen: { cpm: 38.0,  cpc: 4.20,  ctr: 0.010, reach: 0.75 },
    bing:      { cpm: 0,     cpc: 7.50,  ctr: 0.028, reach: 0.38 },
  },
  DKK: {
    meta:      { cpm: 38.0,  cpc: 4.20,  ctr: 0.014, reach: 0.80 },
    linkedin:  { cpm: 320.0, cpc: 45.0,  ctr: 0.005, reach: 0.40 },
    tiktok:    { cpm: 26.0,  cpc: 3.00,  ctr: 0.009, reach: 0.36 },
    snapchat:  { cpm: 20.0,  cpc: 2.40,  ctr: 0.007, reach: 0.28 },
    google:    { cpm: 0,     cpc: 14.0,  ctr: 0.045, reach: 0.95 },
    youtube:   { cpm: 42.0,  cpc: 1.60,  ctr: 0.006, reach: 0.88 },
    pmax:      { cpm: 50.0,  cpc: 9.50,  ctr: 0.019, reach: 0.88 },
    demandgen: { cpm: 30.0,  cpc: 3.40,  ctr: 0.010, reach: 0.72 },
    bing:      { cpm: 0,     cpc: 6.00,  ctr: 0.028, reach: 0.35 },
  },
  EUR: {
    meta:      { cpm: 6.5,   cpc: 0.75,  ctr: 0.013, reach: 0.78 },
    linkedin:  { cpm: 45.0,  cpc: 6.50,  ctr: 0.005, reach: 0.32 },
    tiktok:    { cpm: 4.5,   cpc: 0.50,  ctr: 0.009, reach: 0.35 },
    snapchat:  { cpm: 3.5,   cpc: 0.40,  ctr: 0.007, reach: 0.25 },
    google:    { cpm: 0,     cpc: 2.20,  ctr: 0.042, reach: 0.92 },
    youtube:   { cpm: 7.0,   cpc: 0.25,  ctr: 0.006, reach: 0.88 },
    pmax:      { cpm: 8.5,   cpc: 1.50,  ctr: 0.018, reach: 0.88 },
    demandgen: { cpm: 5.5,   cpc: 0.55,  ctr: 0.010, reach: 0.70 },
    bing:      { cpm: 0,     cpc: 1.10,  ctr: 0.025, reach: 0.30 },
  },
  AUD: {
    meta:      { cpm: 18.0,  cpc: 1.90,  ctr: 0.014, reach: 0.82 },
    linkedin:  { cpm: 85.0,  cpc: 12.5,  ctr: 0.005, reach: 0.36 },
    tiktok:    { cpm: 11.0,  cpc: 1.10,  ctr: 0.009, reach: 0.42 },
    snapchat:  { cpm: 8.5,   cpc: 0.90,  ctr: 0.007, reach: 0.34 },
    google:    { cpm: 0,     cpc: 5.00,  ctr: 0.045, reach: 0.94 },
    youtube:   { cpm: 14.0,  cpc: 0.50,  ctr: 0.006, reach: 0.90 },
    pmax:      { cpm: 20.0,  cpc: 3.10,  ctr: 0.019, reach: 0.90 },
    demandgen: { cpm: 14.0,  cpc: 1.30,  ctr: 0.010, reach: 0.72 },
    bing:      { cpm: 0,     cpc: 2.50,  ctr: 0.028, reach: 0.32 },
  },
};

// Objective multipliers applied to CPM and CPC
const OBJECTIVE_MULTIPLIER = { reach: 1.0, clicks: 1.35, conversions: 1.80 };

// Auto-select channels per objective (user can override)
const OBJECTIVE_CHANNELS = {
  reach:       new Set(['meta', 'tiktok', 'snapchat', 'youtube']),
  clicks:      new Set(['meta', 'google', 'linkedin', 'demandgen']),
  conversions: new Set(['google', 'pmax', 'meta']),
};

const CHANNEL_META = {
  meta:      { name: 'Meta',            group: 'social',  type: 'cpm' },
  linkedin:  { name: 'LinkedIn',        group: 'social',  type: 'cpm' },
  tiktok:    { name: 'TikTok',          group: 'social',  type: 'cpm' },
  snapchat:  { name: 'Snapchat',        group: 'social',  type: 'cpm' },
  google:    { name: 'Google Search',   group: 'search',  type: 'cpc' },
  bing:      { name: 'Bing Search',     group: 'search',  type: 'cpc' },
  youtube:   { name: 'YouTube',         group: 'push',    type: 'cpm' },
  pmax:      { name: 'Performance Max', group: 'push',    type: 'cpm' },
  demandgen: { name: 'Demand Gen',      group: 'push',    type: 'cpm' },
};

const OBJECTIVES = {
  reach:       { label: 'Reach / Awareness' },
  clicks:      { label: 'Traffic / Clicks'  },
  conversions: { label: 'Conversions'       },
};

const SYMBOLS = { USD: '$', GBP: '£', NOK: 'kr ', SEK: 'kr ', DKK: 'kr ', EUR: '€', AUD: 'A$' };

let state = {
  market: 'US',
  ageFilters: new Set(),
  genderFilter: 'all',
  channels: new Set(['meta', 'tiktok', 'snapchat', 'youtube']),
  objective: 'reach',
  direction: 'budget-to-results',
  customEnabled: false,
  customMetrics: {},
};

function fmtNum(n, d = 2) { return n.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d }); }
function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }
function getVal(id) { const el = document.getElementById(id); return el ? parseFloat(el.value) || 0 : 0; }

function getCurrency() { return MARKETS[state.market].currency; }
function getBenchmarks() { return BENCHMARKS[getCurrency()]; }

// Get effective metric applying objective multiplier and custom override
function getMetric(channel, field) {
  const custom = state.customMetrics[channel];
  if (state.customEnabled && custom && custom[field] != null) return custom[field];
  const bench = getBenchmarks()[channel];
  if (!bench) return 0;
  const mult = (field === 'cpm' || field === 'cpc') ? OBJECTIVE_MULTIPLIER[state.objective] : 1.0;
  return bench[field] * mult;
}

// Population ceiling based on market + age + gender filters
function getPopulationCeiling() {
  const market = MARKETS[state.market];
  const genderFactor = GENDER_DISTRIBUTION[state.genderFilter] || 1;
  let ageFactor = state.ageFilters.size === 0 ? 1 :
    [...state.ageFilters].reduce((s, a) => s + (AGE_DISTRIBUTION[a] || 0), 0);
  return Math.round(market.population * market.internetPct * ageFactor * genderFactor);
}

// Channel weights: reach penetration only (objective already baked into cost via multiplier)
function computeChannelWeights() {
  const channels = [...state.channels];
  const bench = getBenchmarks();
  let total = 0;
  const raw = {};
  channels.forEach(ch => {
    const pen = bench[ch] ? bench[ch].reach : 0.3;
    raw[ch] = pen;
    total += pen;
  });
  const weights = {};
  channels.forEach(ch => { weights[ch] = total > 0 ? raw[ch] / total : 1 / channels.length; });
  return weights;
}

// ── Render markets ──
function renderMarkets() {
  const grid = document.getElementById('market-grid');
  if (!grid) return;
  grid.innerHTML = Object.entries(MARKETS).map(([code, m]) =>
    `<button class="market-btn${code === state.market ? ' active' : ''}" data-market="${code}">${m.flag} ${m.name} <span>${m.currency}</span></button>`
  ).join('');
  grid.querySelectorAll('.market-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.market = btn.dataset.market;
      state.customMetrics = {};
      renderMarkets();
      document.querySelectorAll('.currency-label').forEach(el => el.textContent = getCurrency());
      document.getElementById('benchmark-market').textContent = state.market;
      renderBenchmarkTable();
      renderCustomPanel();
      updateAudienceDisplay();
    });
  });
}

// ── Render objectives ──
function renderObjectives() {
  const el = document.getElementById('objective-toggle');
  if (!el) return;
  el.innerHTML = Object.entries(OBJECTIVES).map(([key, obj]) =>
    `<button class="obj-btn${key === state.objective ? ' active' : ''}" data-obj="${key}">${obj.label}</button>`
  ).join('');
  el.querySelectorAll('.obj-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.objective = btn.dataset.obj;
      // Auto-select channels for this objective
      state.channels = new Set(OBJECTIVE_CHANNELS[state.objective]);
      renderObjectives();
      renderChannels();
      renderBenchmarkTable();
      renderCustomPanel();
      const convExtra = document.getElementById('conversions-extra');
      if (convExtra) convExtra.classList.toggle('hidden', state.objective !== 'conversions');
    });
  });
  const convExtra = document.getElementById('conversions-extra');
  if (convExtra) convExtra.classList.toggle('hidden', state.objective !== 'conversions');
}

// ── Render channels ──
function renderChannels() {
  const grid = document.getElementById('channel-grid');
  if (!grid) return;
  const groups = { social: 'Social', search: 'Search', push: 'Push / Video' };
  let html = '';
  Object.entries(groups).forEach(([groupKey, groupLabel]) => {
    html += `<div class="channel-group"><span class="channel-group-label">${groupLabel}</span><div class="channel-group-btns">`;
    Object.entries(CHANNEL_META).filter(([, v]) => v.group === groupKey).forEach(([key, meta]) => {
      html += `<button class="channel-btn${state.channels.has(key) ? ' active' : ''}" data-channel="${key}">${meta.name}</button>`;
    });
    html += `</div></div>`;
  });
  grid.innerHTML = html;
  grid.querySelectorAll('.channel-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const ch = btn.dataset.channel;
      if (state.channels.has(ch)) { state.channels.delete(ch); btn.classList.remove('active'); }
      else { state.channels.add(ch); btn.classList.add('active'); }
      renderBenchmarkTable();
      renderCustomPanel();
    });
  });
}

// ── Custom metrics panel - prefilled with objective-adjusted benchmarks ──
function renderCustomPanel() {
  const panel = document.getElementById('custom-metrics-panel');
  if (!panel) return;
  if (!state.customEnabled) { panel.classList.add('hidden'); return; }
  panel.classList.remove('hidden');
  const sym = SYMBOLS[getCurrency()];
  const mult = OBJECTIVE_MULTIPLIER[state.objective];
  const bench = getBenchmarks();
  let html = `<p class="step-hint" style="margin-bottom:12px;">Values shown are baseline benchmarks × ${mult}x (${OBJECTIVES[state.objective].label} multiplier). Edit to use your own account data.</p>`;
  [...state.channels].forEach(ch => {
    const meta = CHANNEL_META[ch];
    const b = bench[ch];
    if (!b) return;
    const cur = state.customMetrics[ch] || {};
    const cpmAdj = (b.cpm * mult).toFixed(2);
    const cpcAdj = (b.cpc * mult).toFixed(2);
    const ctrPct = (b.ctr * 100).toFixed(1);
    const cpmVal = cur.cpm != null ? cur.cpm : cpmAdj;
    const cpcVal = cur.cpc != null ? cur.cpc : cpcAdj;
    const ctrVal = cur.ctr != null ? (cur.ctr * 100).toFixed(1) : ctrPct;
    const cpmField = meta.type === 'cpc' ? '' :
      `<div class="input-group"><label>CPM (${sym})</label><input type="number" data-ch="${ch}" data-field="cpm" value="${cpmVal}" min="0" step="0.01"></div>`;
    html += `<div class="custom-channel-row">
      <div class="custom-channel-name">${meta.name}</div>
      ${cpmField}
      <div class="input-group"><label>CPC (${sym})</label><input type="number" data-ch="${ch}" data-field="cpc" value="${cpcVal}" min="0" step="0.01"></div>
      <div class="input-group"><label>CTR (%)</label><input type="number" data-ch="${ch}" data-field="ctr" value="${ctrVal}" min="0" step="0.01"></div>
    </div>`;
  });
  panel.innerHTML = html;
  panel.querySelectorAll('input[data-ch]').forEach(input => {
    input.addEventListener('input', () => {
      const ch = input.dataset.ch;
      const field = input.dataset.field;
      if (!state.customMetrics[ch]) state.customMetrics[ch] = {};
      const val = parseFloat(input.value);
      // CTR stored as decimal internally
      state.customMetrics[ch][field] = field === 'ctr' ? val / 100 : val;
    });
  });
}

// ── Custom toggle ──
function initCustomToggle() {
  const track = document.getElementById('custom-toggle-track');
  const thumb = document.getElementById('custom-toggle-thumb');
  if (!track) return;
  track.addEventListener('click', () => {
    state.customEnabled = !state.customEnabled;
    track.style.background = state.customEnabled ? '#6366F1' : '';
    thumb.style.transform = state.customEnabled ? 'translateX(20px)' : 'translateX(0)';
    renderCustomPanel();
  });
}

// ── Direction toggle ──
function initDirectionToggle() {
  document.querySelectorAll('.dir-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.dir-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.direction = btn.dataset.dir;
      document.getElementById('budget-to-results-inputs').classList.toggle('hidden', state.direction !== 'budget-to-results');
      document.getElementById('goals-to-budget-inputs').classList.toggle('hidden', state.direction !== 'goals-to-budget');
      document.getElementById('audience-to-budget-inputs').classList.toggle('hidden', state.direction !== 'audience-to-budget');
    });
  });
}

// ── Age / gender filters ──
function initFilters() {
  document.querySelectorAll('#age-checkbox-group input[type=checkbox]').forEach(cb => {
    cb.addEventListener('change', () => {
      if (cb.checked) state.ageFilters.add(cb.value);
      else state.ageFilters.delete(cb.value);
      updateAudienceDisplay();
    });
  });
  const genderEl = document.getElementById('gender-filter');
  if (genderEl) genderEl.addEventListener('change', () => {
    state.genderFilter = genderEl.value;
    updateAudienceDisplay();
  });
  updateAudienceDisplay();
}

function updateAudienceDisplay() {
  const el = document.getElementById('audience-size-display');
  if (!el) return;
  const pop = getPopulationCeiling();
  el.innerHTML = '<span class="audience-size-label">Estimated addressable audience:</span> <strong>' + fmtInt(pop) + '</strong> people';
  el.classList.add('visible');
}

// ── Main calculation ──
function calcBudget() {
  const channels = [...state.channels];
  if (channels.length === 0) { alert('Please select at least one channel.'); return; }

  const weights = computeChannelWeights();
  const sym = SYMBOLS[getCurrency()];
  const popCeiling = getPopulationCeiling();
  const panel = document.getElementById('budget-result-panel');
  panel.classList.remove('hidden');

  let totalBudget = 0;

  if (state.direction === 'budget-to-results') {
    totalBudget = getVal('b2r-budget');
    if (!totalBudget) { panel.innerHTML = '<p class="mix-disclaimer">Enter a budget amount to calculate.</p>'; return; }

  } else if (state.direction === 'goals-to-budget') {
    const goal = getVal('g2b-goal');
    if (!goal) { panel.innerHTML = '<p class="mix-disclaimer">Enter a target to calculate.</p>'; return; }
    channels.forEach(ch => {
      const channelGoal = goal * weights[ch];
      const cpc = getMetric(ch, 'cpc');
      const cpm = getMetric(ch, 'cpm');
      const meta = CHANNEL_META[ch];
      let channelBudget = 0;
      if (state.objective === 'reach') channelBudget = (channelGoal / 1000) * cpm;
      else if (state.objective === 'clicks') channelBudget = channelGoal * cpc;
      else channelBudget = channelGoal * cpc / 0.02;
      totalBudget += channelBudget;
    });

  } else if (state.direction === 'audience-to-budget') {
    const targetFreq = parseFloat(document.getElementById('target-frequency')?.value) || 3;
    channels.forEach(ch => {
      const bench = getBenchmarks()[ch];
      if (!bench) return;
      const channelReach = Math.round(popCeiling * bench.reach);
      const totalImpressions = channelReach * targetFreq;
      const cpm = getMetric(ch, 'cpm');
      const cpc = getMetric(ch, 'cpc');
      const ctr = getMetric(ch, 'ctr');
      const meta = CHANNEL_META[ch];
      let channelBudget = 0;
      if (meta.type === 'cpc') {
        channelBudget = totalImpressions * ctr * cpc;
      } else {
        channelBudget = (totalImpressions / 1000) * cpm;
      }
      totalBudget += channelBudget;
    });
  }

  // Per-channel delivery
  let rows = [];
  let totalImpressions = 0, totalClicks = 0, totalReach = 0;

  channels.forEach(ch => {
    const channelBudget = totalBudget * weights[ch];
    const cpm = getMetric(ch, 'cpm');
    const cpc = getMetric(ch, 'cpc');
    const ctr = getMetric(ch, 'ctr');
    const bench = getBenchmarks()[ch];
    const meta = CHANNEL_META[ch];

    let impressions, clicks;
    if (meta.type === 'cpc') {
      clicks = channelBudget / cpc;
      impressions = ctr > 0 ? clicks / ctr : 0;
    } else {
      impressions = cpm > 0 ? (channelBudget / cpm) * 1000 : 0;
      clicks = impressions * ctr;
    }

    const channelPopCeiling = Math.round(popCeiling * (bench ? bench.reach : 0.5));
    const reach = Math.min(impressions, channelPopCeiling);
    const frequency = reach > 0 ? impressions / reach : 0;

    totalImpressions += impressions;
    totalClicks += clicks;
    totalReach += reach;

    rows.push({ ch, meta, channelBudget, impressions, clicks, reach, frequency, channelPopCeiling, cpm, cpc, ctr });
  });

  renderResults(rows, totalBudget, sym, popCeiling, totalClicks);
}

function renderResults(rows, totalBudget, sym, popCeiling, totalClicks) {
  const panel = document.getElementById('budget-result-panel');
  const mult = OBJECTIVE_MULTIPLIER[state.objective];

  // ROAS calculation if conversions objective with AOV + CVR
  const aov = getVal('aov-input');
  const cvr = getVal('cvr-input');
  let roasHtml = '';
  if (state.objective === 'conversions' && aov > 0 && cvr > 0) {
    const conversions = totalClicks * (cvr / 100);
    const revenue = conversions * aov;
    const roas = totalBudget > 0 ? revenue / totalBudget : 0;
    roasHtml = `
    <div class="result-summary-item"><span class="rs-label">Est. conversions</span><span class="rs-value">${fmtInt(conversions)}</span></div>
    <div class="result-summary-item"><span class="rs-label">Est. revenue</span><span class="rs-value">${sym}${fmtNum(revenue)}</span></div>
    <div class="result-summary-item"><span class="rs-label">Est. ROAS</span><span class="rs-value">${fmtNum(roas, 2)}x</span></div>`;
  }

  let html = `<div class="result-summary">
    <div class="result-summary-item"><span class="rs-label">Total budget</span><span class="rs-value">${sym}${fmtNum(totalBudget)}</span></div>
    <div class="result-summary-item"><span class="rs-label">Addressable population</span><span class="rs-value">${fmtInt(popCeiling)}</span></div>
    <div class="result-summary-item"><span class="rs-label">Pricing multiplier</span><span class="rs-value">${mult}x <span style="font-size:0.78rem;color:var(--text-muted);">(${OBJECTIVES[state.objective].label})</span></span></div>
    ${roasHtml}
  </div>
  <div class="mix-table-wrap">
  <table class="mix-table">
    <thead><tr>
      <th>Channel</th><th>Split</th><th>Spend</th><th>Impressions</th><th>Reach</th><th>Frequency</th><th>Clicks</th>
    </tr></thead>
    <tbody>`;

  rows.forEach(r => {
    const pct = (r.channelBudget / totalBudget * 100).toFixed(0);
    const reachPct = r.channelPopCeiling > 0 ? (r.reach / r.channelPopCeiling * 100).toFixed(0) : 0;
    html += `<tr>
      <td><strong>${r.meta.name}</strong></td>
      <td>${pct}%</td>
      <td>${sym}${fmtNum(r.channelBudget)}</td>
      <td>${fmtInt(r.impressions)}</td>
      <td>${fmtInt(r.reach)} <span class="reach-pct">(${reachPct}% of pop)</span></td>
      <td>${fmtNum(r.frequency, 1)}x</td>
      <td>${fmtInt(r.clicks)}</td>
    </tr>`;
  });

  html += `</tbody></table></div>
  <p class="mix-disclaimer">Budget split is weighted by each channel's market reach penetration. CPM and CPC benchmarks are adjusted by ${mult}x for the <strong>${OBJECTIVES[state.objective].label}</strong> objective (higher objectives attract more auction competition). Reach is capped by addressable population per channel and is not deduplicated across channels. Treat as planning estimates.</p>`;

  panel.innerHTML = html;
}

// ── Benchmark table ──
function renderBenchmarkTable() {
  const el = document.getElementById('benchmark-table');
  if (!el) return;
  const sym = SYMBOLS[getCurrency()];
  const bench = getBenchmarks();
  const mult = OBJECTIVE_MULTIPLIER[state.objective];
  let html = `<table><thead><tr><th>Channel</th><th>CPM (${mult}x)</th><th>CPC (${mult}x)</th><th>CTR</th><th>Market reach</th></tr></thead><tbody>`;
  Object.entries(CHANNEL_META).forEach(([key, meta]) => {
    const b = bench[key];
    if (!b) return;
    const active = state.channels.has(key) ? 'style="color:var(--text)"' : 'style="color:var(--text-muted)"';
    const cpmDisplay = meta.type === 'cpc' ? '-' : `${sym}${fmtNum(b.cpm * mult)}`;
    html += `<tr ${active}><td>${meta.name}</td><td>${cpmDisplay}</td><td>${sym}${fmtNum(b.cpc * mult)}</td><td>${(b.ctr * 100).toFixed(1)}%</td><td>${(b.reach * 100).toFixed(0)}%</td></tr>`;
  });
  html += '</tbody></table>';
  el.innerHTML = html;
}

// ── FAQ accordion ──
document.addEventListener('click', e => {
  const q = e.target.closest('.faq-q');
  if (!q) return;
  q.closest('.faq-item').classList.toggle('open');
});

// ── Init ──
function initBudgetCalculator() {
  if (!document.getElementById('market-grid')) return;
  renderObjectives();
  renderMarkets();
  renderChannels();
  initCustomToggle();
  initDirectionToggle();
  initFilters();
  renderBenchmarkTable();
  document.getElementById('benchmark-market').textContent = state.market;
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initBudgetCalculator);
} else {
  initBudgetCalculator();
}
