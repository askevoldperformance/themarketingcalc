// ──────────────────────────────────────────────────────────────────────────
// Budget Calculator v2 - data and logic
// Benchmarks are blended 2026 estimates from public industry reports
// (WordStream, Triple Whale, Superads, AdAmigo, DigitalApplied, PPC Chief).
// They are reference points only - real performance varies by account,
// industry, creative, and bidding strategy.
// ──────────────────────────────────────────────────────────────────────────

const MARKETS = {
  US: { name: "United States", flag: "\u{1F1FA}\u{1F1F8}", currency: "USD", population: 341000000, internetPct: 0.92 },
  UK: { name: "United Kingdom", flag: "\u{1F1EC}\u{1F1E7}", currency: "GBP", population: 68500000, internetPct: 0.96 },
  NO: { name: "Norway", flag: "\u{1F1F3}\u{1F1F4}", currency: "NOK", population: 5550000, internetPct: 0.99 },
  SE: { name: "Sweden", flag: "\u{1F1F8}\u{1F1EA}", currency: "SEK", population: 10600000, internetPct: 0.98 },
  DK: { name: "Denmark", flag: "\u{1F1E9}\u{1F1F0}", currency: "DKK", population: 5950000, internetPct: 0.99 },
  DE: { name: "Germany", flag: "\u{1F1E9}\u{1F1EA}", currency: "EUR", population: 84500000, internetPct: 0.94 },
  AU: { name: "Australia", flag: "\u{1F1E6}\u{1F1FA}", currency: "AUD", population: 26600000, internetPct: 0.97 },
};

// Age distribution as % of total population (rough national averages, used to scale population estimates)
const AGE_DISTRIBUTION = {
  "all": 1.0,
  "18-24": 0.10,
  "25-34": 0.15,
  "35-44": 0.14,
  "45-54": 0.13,
  "55-64": 0.12,
  "65+":   0.17,
};
const GENDER_DISTRIBUTION = { "all": 1.0, "male": 0.495, "female": 0.505 };

// Channel penetration: % of each market's population reachable on that channel (ads manager potential reach / population)
// Sources: Meta Ads Manager reach data, LinkedIn/TikTok platform disclosures, blended 2026 estimates.
const CHANNEL_PENETRATION = {
  meta:        { US: 0.62, UK: 0.78, NO: 0.81, SE: 0.80, DK: 0.80, DE: 0.55, AU: 0.77 },
  google:      { US: 0.90, UK: 0.93, NO: 0.95, SE: 0.94, DK: 0.95, DE: 0.91, AU: 0.92 }, // search network reach via internet pop
  youtube:     { US: 0.85, UK: 0.88, NO: 0.90, SE: 0.89, DK: 0.90, DE: 0.84, AU: 0.87 },
  pmax:        { US: 0.85, UK: 0.88, NO: 0.90, SE: 0.89, DK: 0.90, DE: 0.84, AU: 0.87 }, // blended search+display+yt
  demandgen:   { US: 0.70, UK: 0.74, NO: 0.76, SE: 0.75, DK: 0.76, DE: 0.68, AU: 0.73 },
  linkedin:    { US: 0.31, UK: 0.36, NO: 0.42, SE: 0.40, DK: 0.41, DE: 0.28, AU: 0.33 },
  tiktok:      { US: 0.45, UK: 0.50, NO: 0.38, SE: 0.40, DK: 0.39, DE: 0.33, AU: 0.46 },
  snapchat:    { US: 0.38, UK: 0.34, NO: 0.30, SE: 0.29, DK: 0.30, DE: 0.18, AU: 0.32 },
  bing:        { US: 0.36, UK: 0.40, NO: 0.42, SE: 0.41, DK: 0.42, DE: 0.35, AU: 0.34 },
};

// Benchmark CPM / CPC / CTR per channel per market. Blended 2026 estimates, USD-normalised then converted.
// CPM null = not a CPM-buyable channel in this model (e.g. pure search CPC channels still get a notional CPM for reach math)
const BENCHMARKS = {
  meta: {
    US: { cpm: 14.19, cpc: 0.78, ctr: 1.55 },
    UK: { cpm: 10.80, cpc: 0.62, ctr: 1.50 },
    NO: { cpm: 14.00, cpc: 0.84, ctr: 1.40 },
    SE: { cpm: 9.10,  cpc: 0.60, ctr: 1.45 },
    DK: { cpm: 11.50, cpc: 0.65, ctr: 1.45 },
    DE: { cpm: 9.80,  cpc: 0.58, ctr: 1.35 },
    AU: { cpm: 12.50, cpc: 0.72, ctr: 1.50 },
  },
  google: {
    US: { cpm: 24.00, cpc: 4.22, ctr: 6.11 },
    UK: { cpm: 19.00, cpc: 2.55, ctr: 4.70 },
    NO: { cpm: 22.00, cpc: 3.10, ctr: 4.20 },
    SE: { cpm: 20.00, cpc: 2.80, ctr: 4.30 },
    DK: { cpm: 21.00, cpc: 2.90, ctr: 4.25 },
    DE: { cpm: 18.00, cpc: 2.10, ctr: 4.00 },
    AU: { cpm: 20.00, cpc: 2.95, ctr: 4.40 },
  },
  youtube: {
    US: { cpm: 11.00, cpc: 0.18, ctr: 0.65 },
    UK: { cpm: 8.50,  cpc: 0.14, ctr: 0.62 },
    NO: { cpm: 9.50,  cpc: 0.16, ctr: 0.58 },
    SE: { cpm: 8.00,  cpc: 0.13, ctr: 0.60 },
    DK: { cpm: 8.80,  cpc: 0.14, ctr: 0.59 },
    DE: { cpm: 7.80,  cpc: 0.12, ctr: 0.55 },
    AU: { cpm: 9.20,  cpc: 0.15, ctr: 0.61 },
  },
  pmax: {
    US: { cpm: 16.00, cpc: 1.20, ctr: 2.10 },
    UK: { cpm: 12.50, cpc: 0.85, ctr: 2.00 },
    NO: { cpm: 14.00, cpc: 1.00, ctr: 1.90 },
    SE: { cpm: 12.00, cpc: 0.90, ctr: 1.95 },
    DK: { cpm: 13.00, cpc: 0.95, ctr: 1.92 },
    DE: { cpm: 11.50, cpc: 0.80, ctr: 1.85 },
    AU: { cpm: 13.50, cpc: 0.95, ctr: 2.00 },
  },
  demandgen: {
    US: { cpm: 13.00, cpc: 0.55, ctr: 1.10 },
    UK: { cpm: 10.00, cpc: 0.45, ctr: 1.05 },
    NO: { cpm: 11.50, cpc: 0.50, ctr: 1.00 },
    SE: { cpm: 9.80,  cpc: 0.42, ctr: 1.02 },
    DK: { cpm: 10.80, cpc: 0.46, ctr: 1.01 },
    DE: { cpm: 9.50,  cpc: 0.40, ctr: 0.95 },
    AU: { cpm: 11.00, cpc: 0.48, ctr: 1.05 },
  },
  linkedin: {
    US: { cpm: 55.00, cpc: 8.00, ctr: 0.50 },
    UK: { cpm: 48.00, cpc: 6.80, ctr: 0.48 },
    NO: { cpm: 58.00, cpc: 9.00, ctr: 0.45 },
    SE: { cpm: 52.00, cpc: 8.20, ctr: 0.47 },
    DK: { cpm: 54.00, cpc: 8.50, ctr: 0.46 },
    DE: { cpm: 46.00, cpc: 6.50, ctr: 0.44 },
    AU: { cpm: 50.00, cpc: 7.20, ctr: 0.48 },
  },
  tiktok: {
    US: { cpm: 9.00,  cpc: 0.45, ctr: 0.95 },
    UK: { cpm: 7.50,  cpc: 0.38, ctr: 0.90 },
    NO: { cpm: 9.50,  cpc: 0.48, ctr: 0.85 },
    SE: { cpm: 8.00,  cpc: 0.40, ctr: 0.88 },
    DK: { cpm: 8.50,  cpc: 0.42, ctr: 0.87 },
    DE: { cpm: 7.20,  cpc: 0.36, ctr: 0.82 },
    AU: { cpm: 8.80,  cpc: 0.43, ctr: 0.90 },
  },
  snapchat: {
    US: { cpm: 6.50,  cpc: 0.40, ctr: 0.70 },
    UK: { cpm: 5.20,  cpc: 0.32, ctr: 0.68 },
    NO: { cpm: 6.00,  cpc: 0.38, ctr: 0.65 },
    SE: { cpm: 5.00,  cpc: 0.30, ctr: 0.67 },
    DK: { cpm: 5.50,  cpc: 0.34, ctr: 0.66 },
    DE: { cpm: 4.80,  cpc: 0.28, ctr: 0.60 },
    AU: { cpm: 5.80,  cpc: 0.35, ctr: 0.68 },
  },
  bing: {
    US: { cpm: 14.00, cpc: 1.80, ctr: 3.20 },
    UK: { cpm: 11.00, cpc: 1.30, ctr: 3.00 },
    NO: { cpm: 12.50, cpc: 1.50, ctr: 2.80 },
    SE: { cpm: 11.50, cpc: 1.40, ctr: 2.85 },
    DK: { cpm: 12.00, cpc: 1.45, ctr: 2.82 },
    DE: { cpm: 10.50, cpc: 1.20, ctr: 2.70 },
    AU: { cpm: 11.80, cpc: 1.35, ctr: 2.90 },
  },
};

// Currency conversion from USD (approximate, for display only)
const FX_FROM_USD = { USD: 1, GBP: 0.79, NOK: 10.85, SEK: 10.75, DKK: 6.95, EUR: 0.93, AUD: 1.54 };
const SYMBOLS = { USD: '$', GBP: '\u00a3', NOK: 'kr', SEK: 'kr', DKK: 'kr', EUR: '\u20ac', AUD: 'A$' };

const CHANNEL_META = {
  meta:      { name: 'Meta',          group: 'social',  type: 'cpm-cpc' },
  tiktok:    { name: 'TikTok',        group: 'social',  type: 'cpm-cpc' },
  snapchat:  { name: 'Snapchat',      group: 'social',  type: 'cpm-cpc' },
  linkedin:  { name: 'LinkedIn',      group: 'social',  type: 'cpm-cpc' },
  google:    { name: 'Google Search', group: 'search',  type: 'cpc' },
  bing:      { name: 'Bing Search',   group: 'search',  type: 'cpc' },
  youtube:   { name: 'YouTube',       group: 'push',    type: 'cpm-cpc' },
  pmax:      { name: 'Performance Max', group: 'push',  type: 'cpm-cpc' },
  demandgen: { name: 'Demand Gen',    group: 'push',    type: 'cpm-cpc' },
};

const OBJECTIVES = {
  reach:        { label: 'Reach / Awareness', favors: ['push', 'social'] },
  clicks:       { label: 'Traffic / Clicks',  favors: ['search', 'social'] },
  conversions:  { label: 'Conversions',       favors: ['search', 'push'] },
};

let state = {
  market: 'US',
  ageFilters: new Set(),
  genderFilter: 'all',
  channels: new Set(['meta', 'google']),
  objective: 'reach',
  direction: 'budget-to-results',
  customEnabled: false,
  customMetrics: {}, // { meta: {cpm: x, cpc: y, ctr: z}, ... }
};

function fmtNum(n, d = 2) { return n.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d }); }
function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }
function getVal(id) { const el = document.getElementById(id); return el ? parseFloat(el.value) || 0 : 0; }

// ── Render market buttons ──
function renderMarkets() {
  const grid = document.getElementById('market-grid');
  if (!grid) return;
  grid.innerHTML = Object.entries(MARKETS).map(([code, m]) =>
    `<button class="market-btn${code === state.market ? ' active' : ''}" data-market="${code}">${m.flag} ${m.name} <span>${m.currency}</span></button>`
  ).join('');
  grid.querySelectorAll('.market-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.market = btn.dataset.market;
      renderMarkets();
      document.querySelectorAll('.currency-label').forEach(el => el.textContent = MARKETS[state.market].currency);
      document.getElementById('benchmark-market').textContent = state.market;
      renderBenchmarkTable();
      renderCustomPanel();
    });
  });
}

// ── Render channel buttons ──
function renderChannels() {
  const grid = document.getElementById('channel-grid');
  if (!grid) return;
  const groups = { search: 'Search', social: 'Social', push: 'Push / Video' };
  let html = '';
  Object.entries(groups).forEach(([groupKey, groupLabel]) => {
    html += `<div class="channel-group"><span class="channel-group-label">${groupLabel}</span><div class="channel-group-btns">`;
    Object.entries(CHANNEL_META).filter(([k, v]) => v.group === groupKey).forEach(([key, meta]) => {
      html += `<button class="channel-btn${state.channels.has(key) ? ' active' : ''}" data-channel="${key}">${meta.name}</button>`;
    });
    html += `</div></div>`;
  });
  grid.innerHTML = html;
  grid.querySelectorAll('.channel-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const ch = btn.dataset.channel;
      if (state.channels.has(ch) && state.channels.size > 1) state.channels.delete(ch);
      else if (!state.channels.has(ch)) state.channels.add(ch);
      renderChannels();
      renderBenchmarkTable();
      renderCustomPanel();
    });
  });
}

// ── Render objective toggle ──
function renderObjectives() {
  const wrap = document.getElementById('objective-toggle');
  if (!wrap) return;
  wrap.innerHTML = Object.entries(OBJECTIVES).map(([key, o]) =>
    `<button class="obj-btn${key === state.objective ? ' active' : ''}" data-obj="${key}">${o.label}</button>`
  ).join('');
  wrap.querySelectorAll('.obj-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.objective = btn.dataset.obj;
      renderObjectives();
      updateGoalLabel();
    });
  });
}

function updateGoalLabel() {
  const labels = { reach: 'Target Impressions', clicks: 'Target Clicks', conversions: 'Target Conversions' };
  const el = document.getElementById('goal-label');
  if (el) el.textContent = labels[state.objective] || 'Target';
}

// ── Custom metrics panel ──
function renderCustomPanel() {
  const panel = document.getElementById('custom-metrics-panel');
  if (!panel) return;
  if (!state.customEnabled) { panel.classList.add('hidden'); return; }
  panel.classList.remove('hidden');
  const sym = SYMBOLS[MARKETS[state.market].currency];
  let html = '';
  [...state.channels].forEach(ch => {
    const meta = CHANNEL_META[ch];
    const existing = state.customMetrics[ch] || {};
    html += `<div class="custom-channel-row">
      <span class="custom-channel-name">${meta.name}</span>
      <div class="custom-channel-fields">
        <div class="input-group small"><label>CPM (${sym})</label><input type="number" class="custom-input" data-channel="${ch}" data-field="cpm" placeholder="benchmark" value="${existing.cpm || ''}" min="0"></div>
        <div class="input-group small"><label>CPC (${sym})</label><input type="number" class="custom-input" data-channel="${ch}" data-field="cpc" placeholder="benchmark" value="${existing.cpc || ''}" min="0"></div>
        <div class="input-group small"><label>CTR (%)</label><input type="number" class="custom-input" data-channel="${ch}" data-field="ctr" placeholder="benchmark" value="${existing.ctr || ''}" min="0"></div>
      </div>
    </div>`;
  });
  panel.innerHTML = html;
  panel.querySelectorAll('.custom-input').forEach(input => {
    input.addEventListener('input', () => {
      const ch = input.dataset.channel, field = input.dataset.field;
      if (!state.customMetrics[ch]) state.customMetrics[ch] = {};
      state.customMetrics[ch][field] = parseFloat(input.value) || null;
    });
  });
}

// Custom toggle switch
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

// Direction toggle
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

// Age / gender filter listeners
function initFilters() {
  document.querySelectorAll('#age-checkbox-group input[type=checkbox]').forEach(cb => {
    cb.addEventListener('change', () => {
      if (cb.checked) state.ageFilters.add(cb.value);
      else state.ageFilters.delete(cb.value);
    });
  });
  const genderEl = document.getElementById('gender-filter');
  if (genderEl) genderEl.addEventListener('change', () => { state.genderFilter = genderEl.value; });
}

// ── Get effective metric for a channel (custom override or benchmark) ──
function getMetric(channel, field) {
  const custom = state.customMetrics[channel];
  if (state.customEnabled && custom && custom[field]) return custom[field];
  const bench = BENCHMARKS[channel][state.market];
  return bench[field];
}

// ── Population ceiling for current filters ──
function getPopulationCeiling() {
  const market = MARKETS[state.market];
  const genderFactor = GENDER_DISTRIBUTION[state.genderFilter] || 1;
  let ageFactor;
  if (state.ageFilters.size === 0) {
    ageFactor = 1; // no age filter selected = all ages
  } else {
    ageFactor = [...state.ageFilters].reduce((sum, age) => sum + (AGE_DISTRIBUTION[age] || 0), 0);
  }
  return Math.round(market.population * market.internetPct * ageFactor * genderFactor);
}

// ── Channel mix weighting: penetration x objective favor ──
function computeChannelWeights() {
  const channels = [...state.channels];
  const weights = {};
  let total = 0;
  channels.forEach(ch => {
    const penetration = CHANNEL_PENETRATION[ch][state.market] || 0.3;
    const group = CHANNEL_META[ch].group;
    const objectiveBoost = OBJECTIVES[state.objective].favors.includes(group) ? 1.4 : 0.8;
    const weight = penetration * objectiveBoost;
    weights[ch] = weight;
    total += weight;
  });
  channels.forEach(ch => { weights[ch] = weights[ch] / total; });
  return weights;
}

// ── Main calculation ──
function calcBudget() {
  const channels = [...state.channels];
  if (channels.length === 0) return;

  const weights = computeChannelWeights();
  const sym = SYMBOLS[MARKETS[state.market].currency];
  const fx = FX_FROM_USD[MARKETS[state.market].currency];
  const popCeiling = getPopulationCeiling();
  const panel = document.getElementById('budget-result-panel');
  panel.classList.remove('hidden');

  let totalBudget = 0;
  let rows = [];

  if (state.direction === 'budget-to-results') {
    totalBudget = getVal('b2r-budget');
    if (!totalBudget) return;
  } else if (state.direction === 'goals-to-budget') {
    // goals-to-budget: distribute target across channels by weight, sum required budget
    const goal = getVal('g2b-goal');
    if (!goal) return;
    channels.forEach(ch => {
      const channelGoal = goal * weights[ch];
      const cpm = getMetric(ch, 'cpm');
      const cpc = getMetric(ch, 'cpc');
      let channelBudget = 0;
      if (state.objective === 'reach') channelBudget = (channelGoal / 1000) * cpm;
      else if (state.objective === 'clicks') channelBudget = channelGoal * cpc;
      else channelBudget = (channelGoal / 0.02) * cpc; // assume 2% CVR for conversions
      totalBudget += channelBudget;
    });
  } else if (state.direction === 'audience-to-budget') {
    // audience-to-budget: estimate cost to reach the full addressable population once per channel
    channels.forEach(ch => {
      const penetration = CHANNEL_PENETRATION[ch][state.market] || 0.3;
      const channelTargetReach = Math.round(popCeiling * penetration);
      const cpm = getMetric(ch, 'cpm');
      const cpc = getMetric(ch, 'cpc');
      const meta = CHANNEL_META[ch];
      let channelBudget = 0;
      if (meta.type === 'cpc') {
        const ctr = getMetric(ch, 'ctr');
        const impressionsNeeded = channelTargetReach; // 1x frequency assumption
        const clicksNeeded = impressionsNeeded * (ctr / 100);
        channelBudget = clicksNeeded * cpc;
      } else {
        channelBudget = (channelTargetReach / 1000) * cpm;
      }
      totalBudget += channelBudget;
    });
  }

  let totalImpressions = 0, totalReach = 0, totalClicks = 0;

  channels.forEach(ch => {
    const channelBudget = totalBudget * weights[ch];
    const cpm = getMetric(ch, 'cpm');
    const cpc = getMetric(ch, 'cpc');
    const ctr = getMetric(ch, 'ctr');
    const meta = CHANNEL_META[ch];

    let impressions, clicks;
    if (meta.type === 'cpc') {
      // pure CPC channel (Search): derive impressions from clicks / CTR
      clicks = channelBudget / cpc;
      impressions = clicks / (ctr / 100);
    } else {
      impressions = (channelBudget / cpm) * 1000;
      clicks = impressions * (ctr / 100);
    }

    const channelPenetration = CHANNEL_PENETRATION[ch][state.market] || 0.3;
    const channelPopCeiling = Math.round(popCeiling * channelPenetration);
    const reach = Math.min(impressions, channelPopCeiling);
    const frequency = reach > 0 ? impressions / reach : 0;

    totalImpressions += impressions;
    totalReach += reach; // note: not deduplicated across channels, shown per-channel
    totalClicks += clicks;

    rows.push({ ch, meta, channelBudget, impressions, clicks, reach, frequency, channelPopCeiling, cpm, cpc, ctr });
  });

  renderResults(rows, totalBudget, sym, popCeiling);
}

function renderResults(rows, totalBudget, sym, popCeiling) {
  const panel = document.getElementById('budget-result-panel');
  let html = `<div class="result-summary">
    <div class="result-summary-item"><span class="rs-label">Total budget</span><span class="rs-value">${sym}${fmtNum(totalBudget)}</span></div>
    <div class="result-summary-item"><span class="rs-label">Addressable population</span><span class="rs-value">${fmtInt(popCeiling)}</span></div>
  </div>
  <div class="mix-table-wrap">
  <table class="mix-table">
    <thead><tr>
      <th>Channel</th><th>Budget split</th><th>Spend</th><th>Impressions</th><th>Reach</th><th>Frequency</th><th>Clicks</th>
    </tr></thead>
    <tbody>`;

  rows.forEach(r => {
    const pctOfTotal = (r.channelBudget / totalBudget * 100).toFixed(0);
    const reachPctOfPop = r.channelPopCeiling > 0 ? (r.reach / r.channelPopCeiling * 100).toFixed(0) : 0;
    html += `<tr>
      <td><strong>${r.meta.name}</strong></td>
      <td>${pctOfTotal}%</td>
      <td>${sym}${fmtNum(r.channelBudget)}</td>
      <td>${fmtInt(r.impressions)}</td>
      <td>${fmtInt(r.reach)} <span class="reach-pct">(${reachPctOfPop}% of pop)</span></td>
      <td>${fmtNum(r.frequency, 1)}x</td>
      <td>${fmtInt(r.clicks)}</td>
    </tr>`;
  });

  html += `</tbody></table></div>
  <p class="mix-disclaimer">Budget split is weighted by each channel's market penetration and fit for your selected objective. Reach is capped by addressable population per channel and is not deduplicated across channels - someone reached on Meta may also be reached on YouTube. Frequency above ${fmtNum(5,0)}x within a 7-day window often signals audience saturation. Treat these as planning estimates - validate against your own account data once live.</p>`;

  panel.innerHTML = html;
}

// ── Benchmark table ──
function renderBenchmarkTable() {
  const el = document.getElementById('benchmark-table');
  if (!el) return;
  const sym = SYMBOLS[MARKETS[state.market].currency];
  const fx = FX_FROM_USD[MARKETS[state.market].currency];
  let html = '<table><thead><tr><th>Channel</th><th>CPM</th><th>CPC</th><th>CTR</th><th>Market reach</th></tr></thead><tbody>';
  Object.entries(CHANNEL_META).forEach(([key, meta]) => {
    const b = BENCHMARKS[key][state.market];
    const pen = CHANNEL_PENETRATION[key][state.market];
    const active = state.channels.has(key) ? 'style="color:var(--text)"' : 'style="color:var(--text-muted)"';
    const cpmDisplay = meta.type === 'cpc' ? '-' : `${sym}${fmtNum(b.cpm)}`;
    html += `<tr ${active}><td>${meta.name}</td><td>${cpmDisplay}</td><td>${sym}${fmtNum(b.cpc)}</td><td>${fmtNum(b.ctr, 1)}%</td><td>${(pen*100).toFixed(0)}%</td></tr>`;
  });
  html += '</tbody></table>';
  el.innerHTML = html;
}

// ── Init ──
function initBudgetCalculator() {
  if (!document.getElementById('market-grid')) return;
  renderMarkets();
  renderChannels();
  renderObjectives();
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
