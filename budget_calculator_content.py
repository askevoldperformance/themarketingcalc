"""
Budget Calculator v2 content module.
Contains the HTML body and is paired with budget_calculator.js for logic.
Benchmark data is embedded in the JS file (BENCHMARKS object) for runtime use.
"""

BUDGET_CALCULATOR_BODY = '''
<main>
  <section class="page-hero"><div class="container">
    <p class="hero-eyebrow">Advanced tool</p>
    <h1>Marketing <span class="accent">Budget Calculator</span></h1>
    <p class="hero-sub">Plan a realistic channel mix and budget split based on market penetration, population data, and your campaign objective - or override every benchmark with your own account data.</p>
  </div></section>

  <section class="budget-section"><div class="container">
    <div class="budget-card">

      <div class="budget-step">
        <h3>1. Market</h3>
        <div class="market-grid" id="market-grid"></div>
      </div>

      <div class="budget-step">
        <h3>2. Audience filter <span class="step-hint">optional - narrows population and reach estimates</span></h3>
        <div class="audience-filter-row">
          <div class="input-group">
            <label>Age range</label>
            <select id="age-filter">
              <option value="all">All ages (13+)</option>
              <option value="18-24">18-24</option>
              <option value="25-34">25-34</option>
              <option value="35-44">35-44</option>
              <option value="45-54">45-54</option>
              <option value="55-64">55-64</option>
              <option value="65+">65+</option>
            </select>
          </div>
          <div class="input-group">
            <label>Gender</label>
            <select id="gender-filter">
              <option value="all">All genders</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
          </div>
        </div>
        <p class="filter-disclaimer">Population and reach estimates use national demographic distribution averages. Your actual addressable audience may differ - especially once you apply customer lists, lookalikes, or interest-based targeting. Treat these numbers as a planning ceiling, not a guarantee.</p>
      </div>

      <div class="budget-step">
        <h3>3. Channels <span class="step-hint">select all that apply - budget will be split across them</span></h3>
        <div class="channel-grid" id="channel-grid"></div>
      </div>

      <div class="budget-step">
        <h3>4. Objective</h3>
        <div class="objective-toggle" id="objective-toggle"></div>
      </div>

      <div class="budget-step">
        <h3>5. Use your own metrics <span class="step-hint">optional - overrides benchmark data per channel</span></h3>
        <div class="custom-toggle-row">
          <label class="switch-label">
            <span class="switch-track" id="custom-toggle-track"><span class="switch-thumb" id="custom-toggle-thumb"></span></span>
            <span>Enable custom CPM / CPC / CTR</span>
          </label>
        </div>
        <div id="custom-metrics-panel" class="custom-metrics-panel hidden"></div>
      </div>

      <div class="budget-step">
        <h3>6. Calculate</h3>
        <div class="calc-direction-toggle">
          <button class="dir-btn active" data-dir="budget-to-results">Budget to Results</button>
          <button class="dir-btn" data-dir="goals-to-budget">Goals to Budget</button>
        </div>
        <div id="budget-to-results-inputs">
          <div class="input-group"><label>Total Budget (<span class="currency-label">USD</span>)</label><input type="number" id="b2r-budget" placeholder="e.g. 5000" min="0"></div>
        </div>
        <div id="goals-to-budget-inputs" class="hidden">
          <div class="input-group"><label id="goal-label">Target Impressions</label><input type="number" id="g2b-goal" placeholder="e.g. 500000" min="0"></div>
        </div>
        <button class="calc-btn" onclick="calcBudget()">Calculate channel mix</button>
      </div>

      <div id="budget-result-panel" class="budget-result-panel hidden"></div>

      <div class="budget-benchmarks">
        <h3>Reference benchmarks <span class="badge" id="benchmark-market">US</span></h3>
        <p class="benchmark-note">These are blended 2026 industry averages and will not match your account exactly. Use Step 5 to enter your own numbers per channel.</p>
        <div id="benchmark-table"></div>
      </div>

    </div>
  </div></section>
</main>'''
