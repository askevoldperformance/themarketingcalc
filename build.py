#!/usr/bin/env python3
"""
Build script for themarketingcalc.com
Run: python build.py
Outputs static HTML files.
"""

import os

GTM_ID = "GTM-XXXXXXXXX"  # Replace with real GTM ID
ADSENSE_PUB = "ca-pub-4789906927045850"
SITE_URL = "https://themarketingcalc.com"

NAV_LINKS = [
    ("Marketing Calculators", "/"),
    ("Budget Calculator", "/budget-calculator"),
    ("Guides ▾", "#", [
        ("All Guides", "/guides"),
        ("How to Calculate Campaign Budget", "/guides/how-to-calculate-campaign-budget"),
        ("What is CPM?", "/guides/what-is-cpm"),
        ("What is ROAS?", "/guides/what-is-roas"),
        ("CPM vs eCPM", "/guides/cpm-vs-ecpm"),
        ("What is CTR?", "/guides/what-is-ctr"),
        ("What is POAS?", "/guides/what-is-poas"),
        ("Marketing Budget Benchmarks", "/guides/marketing-budget-benchmarks"),
    ]),
]


def nav_html(active_path="/"):
    links = ""
    for item in NAV_LINKS:
        if len(item) == 3:
            label, _, children = item
            sub = "".join(
                f'<a href="{c[1]}">{c[0]}</a>' for c in children
            )
            links += f'<div class="nav-dropdown"><button class="nav-btn">{label}</button><div class="nav-dropdown-menu">{sub}</div></div>'
        else:
            label, href = item
            active = ' class="active"' if href == active_path else ""
            links += f'<a href="{href}"{active}>{label}</a>'
    return f'''
<nav class="site-nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo"><img src="/logo.png" alt="The Marketing Calc" width="36" height="36"><span>TheMarketingCalc</span></a>
    <div class="nav-links">{links}</div>
    <button class="nav-hamburger" aria-label="Menu">&#9776;</button>
  </div>
</nav>'''


def head_html(title, description, canonical_path, og_image="/logo.png"):
    canonical = SITE_URL + canonical_path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}{og_image}">
  <meta name="google-adsense-account" content="{ADSENSE_PUB}">
  <link rel="icon" href="/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'''


def footer_html():
    return '''
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="/logo.png" alt="The Marketing Calc" width="28" height="28">
      <span>TheMarketingCalc.com</span>
    </div>
    <nav class="footer-links">
      <a href="/guides">Guides</a>
      <a href="/budget-calculator">Budget Calculator</a>
      <a href="/privacy-policy">Privacy Policy</a>
    </nav>
    <p class="footer-copy">&copy; 2025 TheMarketingCalc.com</p>
  </div>
</footer>
<script src="/cookie_banner.js" defer></script>
<script src="/main.js" defer></script>
</body>
</html>'''


def page(filepath, title, description, canonical_path, body_html):
    """Generate a full HTML page and write it to filepath."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True) if os.path.dirname(filepath) else None
    active = canonical_path if canonical_path else "/"
    content = (
        head_html(title, description, canonical_path)
        + nav_html(active)
        + body_html
        + footer_html()
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Built: {filepath}")


# ─── PAGE BODIES ──────────────────────────────────────────────────────────────

INDEX_BODY = '''
<main>
  <section class="hero">
    <div class="hero-inner">
      <p class="hero-eyebrow">Free marketing calculators</p>
      <h1>Calculate Any<br><span class="accent">Marketing Metric</span><br>Instantly</h1>
      <p class="hero-sub">CPM, CTR, CPC, ROAS, POAS, CPL, Frequency, Break-even — all in one place.</p>
    </div>
  </section>

  <section class="calcs-section" id="calculators">
    <div class="container">
      <div class="calc-tabs-nav" role="tablist">
        <button class="calc-tab active" data-tab="cpm" role="tab">CPM</button>
        <button class="calc-tab" data-tab="ctr" role="tab">CTR</button>
        <button class="calc-tab" data-tab="cpc" role="tab">CPC</button>
        <button class="calc-tab" data-tab="roas" role="tab">ROAS</button>
        <button class="calc-tab" data-tab="poas" role="tab">POAS</button>
        <button class="calc-tab" data-tab="cpl" role="tab">CPL</button>
        <button class="calc-tab" data-tab="freq" role="tab">Frequency</button>
        <button class="calc-tab" data-tab="beroas" role="tab">Break-even ROAS</button>
      </div>

      <!-- CPM -->
      <div class="calc-panel active" id="tab-cpm">
        <div class="calc-card">
          <div class="calc-header">
            <h2>CPM Calculator</h2>
            <p class="calc-desc">Cost Per Mille — cost per 1,000 impressions. Solve for CPM, Cost, or Impressions.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="cpm-cpm">Find CPM</button>
            <button class="mode-btn" data-mode="cpm-cost">Find Cost</button>
            <button class="mode-btn" data-mode="cpm-imp">Find Impressions</button>
          </div>
          <div class="calc-inputs" id="cpm-inputs">
            <div class="input-group" id="cpm-field-cost"><label>Total Cost ($)</label><input type="number" id="cpm-cost" placeholder="e.g. 500" min="0"></div>
            <div class="input-group" id="cpm-field-imp"><label>Impressions</label><input type="number" id="cpm-impressions" placeholder="e.g. 100000" min="0"></div>
            <div class="input-group hidden" id="cpm-field-cpm"><label>CPM ($)</label><input type="number" id="cpm-cpm" placeholder="e.g. 5.00" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcCPM()">Calculate</button>
          <div class="calc-result hidden" id="cpm-result"></div>
          <div class="calc-formula">
            <span class="formula-label">Formula</span>
            <code>CPM = (Cost / Impressions) × 1,000</code>
          </div>
        </div>
      </div>

      <!-- CTR -->
      <div class="calc-panel" id="tab-ctr">
        <div class="calc-card">
          <div class="calc-header">
            <h2>CTR Calculator</h2>
            <p class="calc-desc">Click-Through Rate. Solve for CTR, Clicks, or Impressions.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="ctr-ctr">Find CTR</button>
            <button class="mode-btn" data-mode="ctr-clicks">Find Clicks</button>
            <button class="mode-btn" data-mode="ctr-imp">Find Impressions</button>
          </div>
          <div class="calc-inputs" id="ctr-inputs">
            <div class="input-group" id="ctr-field-clicks"><label>Clicks</label><input type="number" id="ctr-clicks" placeholder="e.g. 250" min="0"></div>
            <div class="input-group" id="ctr-field-imp"><label>Impressions</label><input type="number" id="ctr-impressions" placeholder="e.g. 10000" min="0"></div>
            <div class="input-group hidden" id="ctr-field-ctr"><label>CTR (%)</label><input type="number" id="ctr-ctr" placeholder="e.g. 2.5" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcCTR()">Calculate</button>
          <div class="calc-result hidden" id="ctr-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>CTR = (Clicks / Impressions) × 100</code></div>
        </div>
      </div>

      <!-- CPC -->
      <div class="calc-panel" id="tab-cpc">
        <div class="calc-card">
          <div class="calc-header">
            <h2>CPC Calculator</h2>
            <p class="calc-desc">Cost Per Click. Solve for CPC, Cost, or Clicks.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="cpc-cpc">Find CPC</button>
            <button class="mode-btn" data-mode="cpc-cost">Find Cost</button>
            <button class="mode-btn" data-mode="cpc-clicks">Find Clicks</button>
          </div>
          <div class="calc-inputs" id="cpc-inputs">
            <div class="input-group" id="cpc-field-cost"><label>Total Cost ($)</label><input type="number" id="cpc-cost" placeholder="e.g. 500" min="0"></div>
            <div class="input-group" id="cpc-field-clicks"><label>Clicks</label><input type="number" id="cpc-clicks" placeholder="e.g. 1000" min="0"></div>
            <div class="input-group hidden" id="cpc-field-cpc"><label>CPC ($)</label><input type="number" id="cpc-cpc" placeholder="e.g. 0.50" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcCPC()">Calculate</button>
          <div class="calc-result hidden" id="cpc-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>CPC = Cost / Clicks</code></div>
        </div>
      </div>

      <!-- ROAS -->
      <div class="calc-panel" id="tab-roas">
        <div class="calc-card">
          <div class="calc-header">
            <h2>ROAS Calculator</h2>
            <p class="calc-desc">Return on Ad Spend. Solve for ROAS, Revenue, or Ad Spend.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="roas-roas">Find ROAS</button>
            <button class="mode-btn" data-mode="roas-rev">Find Revenue</button>
            <button class="mode-btn" data-mode="roas-spend">Find Ad Spend</button>
          </div>
          <div class="calc-inputs" id="roas-inputs">
            <div class="input-group" id="roas-field-rev"><label>Revenue ($)</label><input type="number" id="roas-rev" placeholder="e.g. 5000" min="0"></div>
            <div class="input-group" id="roas-field-spend"><label>Ad Spend ($)</label><input type="number" id="roas-spend" placeholder="e.g. 1000" min="0"></div>
            <div class="input-group hidden" id="roas-field-roas"><label>ROAS</label><input type="number" id="roas-roas" placeholder="e.g. 4" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcROAS()">Calculate</button>
          <div class="calc-result hidden" id="roas-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>ROAS = Revenue / Ad Spend</code></div>
        </div>
      </div>

      <!-- POAS -->
      <div class="calc-panel" id="tab-poas">
        <div class="calc-card">
          <div class="calc-header">
            <h2>POAS Calculator</h2>
            <p class="calc-desc">Profit on Ad Spend — like ROAS but uses profit instead of revenue. Solve for POAS, Profit, or Ad Spend.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="poas-poas">Find POAS</button>
            <button class="mode-btn" data-mode="poas-profit">Find Profit</button>
            <button class="mode-btn" data-mode="poas-spend">Find Ad Spend</button>
          </div>
          <div class="calc-inputs" id="poas-inputs">
            <div class="input-group" id="poas-field-profit"><label>Gross Profit ($)</label><input type="number" id="poas-profit" placeholder="e.g. 2000" min="0"></div>
            <div class="input-group" id="poas-field-spend"><label>Ad Spend ($)</label><input type="number" id="poas-spend" placeholder="e.g. 1000" min="0"></div>
            <div class="input-group hidden" id="poas-field-poas"><label>POAS</label><input type="number" id="poas-poas" placeholder="e.g. 2" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcPOAS()">Calculate</button>
          <div class="calc-result hidden" id="poas-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>POAS = Gross Profit / Ad Spend</code></div>
        </div>
      </div>

      <!-- CPL -->
      <div class="calc-panel" id="tab-cpl">
        <div class="calc-card">
          <div class="calc-header">
            <h2>CPL Calculator</h2>
            <p class="calc-desc">Cost Per Lead. Solve for CPL, Cost, or Number of Leads.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="cpl-cpl">Find CPL</button>
            <button class="mode-btn" data-mode="cpl-cost">Find Cost</button>
            <button class="mode-btn" data-mode="cpl-leads">Find Leads</button>
          </div>
          <div class="calc-inputs" id="cpl-inputs">
            <div class="input-group" id="cpl-field-cost"><label>Total Cost ($)</label><input type="number" id="cpl-cost" placeholder="e.g. 1000" min="0"></div>
            <div class="input-group" id="cpl-field-leads"><label>Leads</label><input type="number" id="cpl-leads" placeholder="e.g. 50" min="0"></div>
            <div class="input-group hidden" id="cpl-field-cpl"><label>CPL ($)</label><input type="number" id="cpl-cpl" placeholder="e.g. 20" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcCPL()">Calculate</button>
          <div class="calc-result hidden" id="cpl-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>CPL = Cost / Leads</code></div>
        </div>
      </div>

      <!-- Frequency -->
      <div class="calc-panel" id="tab-freq">
        <div class="calc-card">
          <div class="calc-header">
            <h2>Frequency Calculator</h2>
            <p class="calc-desc">Average number of times a person sees your ad. Solve for Frequency, Impressions, or Reach.</p>
          </div>
          <div class="calc-mode-toggle">
            <button class="mode-btn active" data-mode="freq-freq">Find Frequency</button>
            <button class="mode-btn" data-mode="freq-imp">Find Impressions</button>
            <button class="mode-btn" data-mode="freq-reach">Find Reach</button>
          </div>
          <div class="calc-inputs" id="freq-inputs">
            <div class="input-group" id="freq-field-imp"><label>Impressions</label><input type="number" id="freq-imp" placeholder="e.g. 500000" min="0"></div>
            <div class="input-group" id="freq-field-reach"><label>Reach (unique people)</label><input type="number" id="freq-reach" placeholder="e.g. 100000" min="0"></div>
            <div class="input-group hidden" id="freq-field-freq"><label>Frequency</label><input type="number" id="freq-freq" placeholder="e.g. 5" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcFreq()">Calculate</button>
          <div class="calc-result hidden" id="freq-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>Frequency = Impressions / Reach</code></div>
        </div>
      </div>

      <!-- Break-even ROAS -->
      <div class="calc-panel" id="tab-beroas">
        <div class="calc-card">
          <div class="calc-header">
            <h2>Break-even ROAS Calculator</h2>
            <p class="calc-desc">Find the minimum ROAS needed to cover your costs and break even on ad spend.</p>
          </div>
          <div class="calc-inputs" id="beroas-inputs">
            <div class="input-group"><label>Average Order Value ($)</label><input type="number" id="be-aov" placeholder="e.g. 100" min="0"></div>
            <div class="input-group"><label>COGS per order ($)</label><input type="number" id="be-cogs" placeholder="e.g. 40" min="0"></div>
            <div class="input-group"><label>Other variable costs per order ($) <span class="input-hint">shipping, fulfillment etc.</span></label><input type="number" id="be-other" placeholder="e.g. 10" min="0" value="0"></div>
          </div>
          <button class="calc-btn" onclick="calcBEROAS()">Calculate</button>
          <div class="calc-result hidden" id="beroas-result"></div>
          <div class="calc-formula"><span class="formula-label">Formula</span><code>Break-even ROAS = AOV / (AOV − COGS − Other Costs)</code></div>
        </div>
      </div>

    </div>
  </section>

  <section class="tools-cta">
    <div class="container">
      <h2>Need to plan a full campaign budget?</h2>
      <p>Use our advanced Budget Calculator to estimate results across Meta, Google Ads, LinkedIn and more — with benchmarks per channel and market.</p>
      <a href="/budget-calculator" class="btn-primary">Open Budget Calculator &rarr;</a>
    </div>
  </section>

  <section class="guides-preview">
    <div class="container">
      <h2>Marketing Guides</h2>
      <div class="guide-grid">
        <a href="/guides/what-is-cpm" class="guide-card"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Understand cost per mille and when to optimise for it.</p></a>
        <a href="/guides/what-is-roas" class="guide-card"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend explained — and how to benchmark it.</p></a>
        <a href="/guides/what-is-poas" class="guide-card"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Why profit-based optimisation beats revenue ROAS.</p></a>
        <a href="/guides/what-is-ctr" class="guide-card"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by channel and ad format.</p></a>
        <a href="/guides/cpm-vs-ecpm" class="guide-card"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought and effective CPM.</p></a>
        <a href="/guides/marketing-budget-benchmarks" class="guide-card"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>Industry benchmarks for CPM, CPC, CTR and ROAS by channel.</p></a>
      </div>
      <a href="/guides" class="btn-secondary">View all guides &rarr;</a>
    </div>
  </section>
</main>
'''

BUDGET_BODY = '''
<main>
  <section class="page-hero">
    <div class="container">
      <p class="hero-eyebrow">Advanced tool</p>
      <h1>Marketing <span class="accent">Budget Calculator</span></h1>
      <p class="hero-sub">Estimate campaign results or required budget across channels — with benchmarks per market.</p>
    </div>
  </section>

  <section class="budget-section">
    <div class="container">
      <div class="budget-card">
        <div class="budget-step">
          <h3>1. Select market &amp; currency</h3>
          <div class="market-grid">
            <button class="market-btn active" data-market="US" data-currency="USD">🇺🇸 US <span>USD</span></button>
            <button class="market-btn" data-market="UK" data-currency="GBP">🇬🇧 UK <span>GBP</span></button>
            <button class="market-btn" data-market="NO" data-currency="NOK">🇳🇴 Norway <span>NOK</span></button>
            <button class="market-btn" data-market="SE" data-currency="SEK">🇸🇪 Sweden <span>SEK</span></button>
            <button class="market-btn" data-market="DK" data-currency="DKK">🇩🇰 Denmark <span>DKK</span></button>
            <button class="market-btn" data-market="EU" data-currency="EUR">🇪🇺 EU <span>EUR</span></button>
            <button class="market-btn" data-market="AU" data-currency="AUD">🇦🇺 Australia <span>AUD</span></button>
          </div>
        </div>

        <div class="budget-step">
          <h3>2. Select channel(s)</h3>
          <div class="channel-grid">
            <button class="channel-btn active" data-channel="meta">Meta</button>
            <button class="channel-btn" data-channel="google">Google Ads</button>
            <button class="channel-btn" data-channel="linkedin">LinkedIn</button>
            <button class="channel-btn" data-channel="tiktok">TikTok</button>
            <button class="channel-btn" data-channel="snapchat">Snapchat</button>
            <button class="channel-btn" data-channel="reddit">Reddit</button>
            <button class="channel-btn" data-channel="x">X (Twitter)</button>
          </div>
        </div>

        <div class="budget-step">
          <h3>3. Objective</h3>
          <div class="objective-toggle">
            <button class="obj-btn active" data-obj="reach">Reach / Awareness</button>
            <button class="obj-btn" data-obj="clicks">Traffic / Clicks</button>
            <button class="obj-btn" data-obj="conversions">Conversions</button>
          </div>
        </div>

        <div class="budget-step">
          <h3>4. Calculate</h3>
          <div class="calc-direction-toggle">
            <button class="dir-btn active" data-dir="budget-to-results">Budget → Results</button>
            <button class="dir-btn" data-dir="goals-to-budget">Goals → Budget</button>
          </div>
          <div id="budget-to-results-inputs">
            <div class="input-group"><label>Total Budget (<span class="currency-label">USD</span>)</label><input type="number" id="b2r-budget" placeholder="e.g. 5000" min="0"></div>
          </div>
          <div id="goals-to-budget-inputs" class="hidden">
            <div class="input-group"><label id="goal-label">Target Impressions</label><input type="number" id="g2b-goal" placeholder="e.g. 500000" min="0"></div>
          </div>
          <button class="calc-btn" onclick="calcBudget()">Estimate</button>
          <div class="calc-result hidden" id="budget-result"></div>
        </div>

        <div class="budget-benchmarks">
          <h3>Channel benchmarks <span class="badge" id="benchmark-market">US</span></h3>
          <div id="benchmark-table"></div>
        </div>
      </div>
    </div>
  </section>
</main>
'''

GUIDES_BODY = '''
<main>
  <section class="page-hero">
    <div class="container">
      <h1>Marketing <span class="accent">Guides</span></h1>
      <p class="hero-sub">Practical explanations of the metrics that matter — with formulas, benchmarks, and examples.</p>
    </div>
  </section>
  <section class="guides-full">
    <div class="container">
      <div class="guide-grid guide-grid-full">
        <a href="/guides/how-to-calculate-campaign-budget" class="guide-card"><span class="guide-tag">Budgets</span><h3>How to Calculate Campaign Budget</h3><p>A step-by-step framework for estimating ad budgets across channels.</p></a>
        <a href="/guides/what-is-cpm" class="guide-card"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Cost per mille explained — with channel benchmarks and examples.</p></a>
        <a href="/guides/what-is-roas" class="guide-card"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend: how to calculate, benchmark, and improve it.</p></a>
        <a href="/guides/cpm-vs-ecpm" class="guide-card"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought CPM and effective CPM.</p></a>
        <a href="/guides/what-is-ctr" class="guide-card"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by platform, format, and industry.</p></a>
        <a href="/guides/what-is-poas" class="guide-card"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Profit on Ad Spend — why it\'s more actionable than ROAS.</p></a>
        <a href="/guides/marketing-budget-benchmarks" class="guide-card"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>CPM, CPC, CTR, and ROAS benchmarks across channels and markets.</p></a>
      </div>
    </div>
  </section>
</main>
'''

PRIVACY_BODY = '''
<main>
  <section class="page-hero">
    <div class="container">
      <h1>Privacy <span class="accent">Policy</span></h1>
    </div>
  </section>
  <section class="prose-section">
    <div class="container prose">
      <p>Last updated: January 2025</p>
      <h2>1. Who we are</h2>
      <p>TheMarketingCalc.com is a free marketing calculator and resource site. We do not sell products or collect personal data for commercial purposes.</p>
      <h2>2. Cookies and tracking</h2>
      <p>We use Google Analytics 4 (statistics) and Google AdSense (marketing) cookies. These are only activated with your consent via our cookie banner. We implement Google Consent Mode v2.</p>
      <h2>3. Data collected</h2>
      <p>If you accept statistics cookies: anonymised page views, session data, and device type via GA4. If you accept marketing cookies: ad interaction data via Google AdSense.</p>
      <h2>4. Third parties</h2>
      <p>Google Analytics and Google AdSense are operated by Google LLC. You can review Google\'s privacy policy at <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a>.</p>
      <h2>5. Your rights</h2>
      <p>You can withdraw consent at any time by clearing your browser\'s localStorage (key: <code>cookie_consent_v1</code>) or clearing cookies and revisiting the site.</p>
      <h2>6. Contact</h2>
      <p>Questions about this policy can be sent to: privacy@themarketingcalc.com</p>
    </div>
  </section>
</main>
'''


def guide_body(title, tag, content_html):
    return f'''
<main>
  <section class="page-hero">
    <div class="container">
      <span class="guide-tag">{tag}</span>
      <h1>{title}</h1>
    </div>
  </section>
  <section class="prose-section">
    <div class="container prose">
      {content_html}
    </div>
  </section>
  <section class="tools-cta">
    <div class="container">
      <h2>Try the calculators</h2>
      <p>Put these formulas to work instantly.</p>
      <a href="/" class="btn-primary">Open Calculators &rarr;</a>
    </div>
  </section>
</main>
'''


# ─── BUILD ALL PAGES ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building themarketingcalc.com...")

    page("index.html",
         "Free Marketing Calculators — CPM, CTR, ROAS, POAS & More | TheMarketingCalc",
         "Calculate CPM, CTR, CPC, ROAS, POAS, CPL, Frequency and Break-even ROAS instantly. Free marketing calculators for digital advertisers.",
         "/",
         INDEX_BODY)

    page("budget-calculator.html",
         "Marketing Budget Calculator — Estimate Reach, Clicks & Conversions | TheMarketingCalc",
         "Advanced marketing budget calculator. Select market, channel mix, and objective to estimate campaign results or required budget.",
         "/budget-calculator",
         BUDGET_BODY)

    page("guides.html",
         "Marketing Guides — CPM, ROAS, CTR, POAS Explained | TheMarketingCalc",
         "Practical guides explaining the marketing metrics that matter — with formulas, benchmarks, and examples.",
         "/guides",
         GUIDES_BODY)

    page("privacy-policy.html",
         "Privacy Policy | TheMarketingCalc",
         "Privacy policy for TheMarketingCalc.com.",
         "/privacy-policy",
         PRIVACY_BODY)

    # Guides
    guides = [
        ("guides/how-to-calculate-campaign-budget.html",
         "How to Calculate a Campaign Budget", "Budgets", "/guides/how-to-calculate-campaign-budget",
         "<h2>The framework</h2><p>Start with your objective and work backwards from a target metric. If your goal is 500,000 impressions and your expected CPM is $5, your budget is <strong>500,000 / 1,000 × $5 = $2,500</strong>.</p><h2>Step 1 — Choose your objective</h2><p>Reach/Awareness → use CPM. Traffic → use CPC. Conversions → use CPL or target CPA.</p><h2>Step 2 — Benchmark your metric</h2><p>Use platform averages as a starting point, then adjust for your industry, creative quality, and audience size. See our <a href='/guides/marketing-budget-benchmarks'>benchmark guide</a>.</p><h2>Step 3 — Calculate</h2><p>Budget = Target Volume / 1,000 × CPM (for impressions)<br>Budget = Target Clicks × CPC<br>Budget = Target Leads × CPL</p><h2>Step 4 — Sanity-check with ROAS</h2><p>If running e-commerce, verify your budget makes sense with break-even ROAS. Use our <a href='/'>Break-even ROAS calculator</a>.</p>"),

        ("guides/what-is-cpm.html",
         "What is CPM? Cost Per Mille Explained", "CPM", "/guides/what-is-cpm",
         "<h2>Definition</h2><p>CPM (Cost Per Mille) is the price you pay per 1,000 ad impressions. It is the standard buying unit for awareness and reach campaigns.</p><h2>Formula</h2><p><code>CPM = (Total Cost / Impressions) × 1,000</code></p><h2>Example</h2><p>You spend $500 and receive 200,000 impressions. CPM = ($500 / 200,000) × 1,000 = <strong>$2.50</strong>.</p><h2>Benchmarks (2024–2025)</h2><p>Meta Ads: $6–$14 · Google Display: $2–$5 · LinkedIn: $30–$80 · TikTok: $8–$15. These vary significantly by audience, creative, and objective.</p><h2>CPM vs eCPM</h2><p>CPM is what you pay. eCPM (effective CPM) is calculated from actual results and used to compare campaigns with different buying models. <a href='/guides/cpm-vs-ecpm'>Read more →</a></p>"),

        ("guides/what-is-roas.html",
         "What is ROAS? Return on Ad Spend Explained", "ROAS", "/guides/what-is-roas",
         "<h2>Definition</h2><p>ROAS (Return on Ad Spend) measures revenue generated per dollar spent on advertising.</p><h2>Formula</h2><p><code>ROAS = Revenue / Ad Spend</code></p><h2>Example</h2><p>Revenue: $10,000. Ad Spend: $2,000. ROAS = 10,000 / 2,000 = <strong>5×</strong> (or 500%).</p><h2>What is a good ROAS?</h2><p>Depends entirely on your margins. A product with 70% gross margin can sustain a lower ROAS than one with 30% margin. Use the Break-even ROAS calculator to find your floor.</p><h2>ROAS vs POAS</h2><p>ROAS uses revenue. POAS uses gross profit — making it more actionable for businesses where margins vary across products. <a href='/guides/what-is-poas'>Read more →</a></p>"),

        ("guides/cpm-vs-ecpm.html",
         "CPM vs eCPM — What is the Difference?", "CPM", "/guides/cpm-vs-ecpm",
         "<h2>CPM — what you pay</h2><p>CPM is the rate you agreed to pay per 1,000 impressions. It is set at auction or negotiated directly.</p><h2>eCPM — what you effectively pay</h2><p>eCPM (effective CPM) normalises performance across different buying models. It is calculated retroactively: <code>eCPM = (Total Cost / Impressions) × 1,000</code>.</p><h2>Why the distinction matters</h2><p>If you run a CPC campaign and get 500,000 impressions at a cost of $1,500, your eCPM is $3. This lets you compare the efficiency of a CPC buy against a CPM buy for the same audience.</p><h2>Publisher vs advertiser</h2><p>Publishers use eCPM to compare yield across ad units and demand sources. Advertisers use it to benchmark campaign efficiency regardless of buying model.</p>"),

        ("guides/what-is-ctr.html",
         "What is CTR? Click-Through Rate Explained", "CTR", "/guides/what-is-ctr",
         "<h2>Definition</h2><p>CTR (Click-Through Rate) is the percentage of people who clicked your ad after seeing it.</p><h2>Formula</h2><p><code>CTR = (Clicks / Impressions) × 100</code></p><h2>Example</h2><p>1,000 clicks from 200,000 impressions. CTR = (1,000 / 200,000) × 100 = <strong>0.5%</strong>.</p><h2>Benchmarks by channel</h2><p>Google Search: 3–6% · Google Display: 0.1–0.3% · Meta Feed: 0.5–1.5% · LinkedIn: 0.3–0.7% · TikTok: 0.5–1.2%.</p><h2>CTR as a signal</h2><p>High CTR indicates strong creative-audience fit. But CTR alone does not determine campaign success — pair it with conversion rate and CPC to get the full picture.</p>"),

        ("guides/what-is-poas.html",
         "What is POAS? Profit on Ad Spend Explained", "POAS", "/guides/what-is-poas",
         "<h2>Definition</h2><p>POAS (Profit on Ad Spend) measures gross profit generated per dollar of ad spend, making it a more accurate performance metric than revenue-based ROAS.</p><h2>Formula</h2><p><code>POAS = Gross Profit / Ad Spend</code></p><h2>Example</h2><p>Gross Profit: $4,000. Ad Spend: $1,000. POAS = 4,000 / 1,000 = <strong>4×</strong>.</p><h2>Why POAS beats ROAS</h2><p>ROAS ignores COGS. A 5× ROAS on a 15% margin product loses money. POAS forces profitability into the optimisation signal. Break-even POAS is always 1 — making targets universal across products.</p><h2>Implementing POAS</h2><p>Pass gross profit (not order value) as your conversion value in Meta or Google Ads. This can be done via a server-side event or a dynamic conversion value in your checkout.</p>"),

        ("guides/marketing-budget-benchmarks.html",
         "Marketing Budget Benchmarks — CPM, CPC, CTR & ROAS by Channel", "Budgets", "/guides/marketing-budget-benchmarks",
         "<h2>How to use these benchmarks</h2><p>These are industry averages for 2024–2025. Treat them as starting points — your actual numbers will vary by audience, creative quality, industry, and bidding strategy.</p><h2>CPM benchmarks</h2><p>Meta: $6–$14 · Google Search (not applicable) · Google Display: $2–$5 · LinkedIn: $30–$80 · TikTok: $8–$15 · Snapchat: $3–$8 · Reddit: $3–$10 · X: $4–$9.</p><h2>CPC benchmarks</h2><p>Google Search: $1–$6 (varies widely by industry) · Meta: $0.30–$1.50 · LinkedIn: $5–$15 · TikTok: $0.20–$0.80.</p><h2>CTR benchmarks</h2><p>Google Search: 3–6% · Google Display: 0.1–0.3% · Meta Feed: 0.5–1.5% · LinkedIn: 0.3–0.7%.</p><h2>ROAS benchmarks</h2><p>E-commerce average: 3–5×. But the only ROAS that matters is your break-even ROAS, which depends on your margins. Use our <a href='/'>Break-even ROAS calculator</a> to find your target.</p>"),
    ]

    for filepath, title, tag, canonical_path, content in guides:
        page(filepath,
             f"{title} | TheMarketingCalc",
             title,
             canonical_path,
             guide_body(title, tag, content))

    print("Done.")
