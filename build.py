#!/usr/bin/env python3
"""Build script for themarketingcalc.com. Run: python3 build.py"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from poas_guide_content import POAS_GUIDE_CONTENT
from roas_guide_content import ROAS_GUIDE_CONTENT, ROAS_GUIDE_FAQ
from cpm_guide_content import CPM_GUIDE_CONTENT, CPM_GUIDE_FAQ
from rsa_guide_content import RSA_GUIDE_CONTENT, RSA_GUIDE_FAQ
from build_helpers import AD_LEADERBOARD, AD_SIDEBAR_L, AD_SIDEBAR_R, affiliate, faq, AFFILIATES
from content import (
    CPM_EDITORIAL, CPM_FAQ,
    CTR_EDITORIAL, CTR_FAQ,
    CPC_EDITORIAL, CPC_FAQ,
    ROAS_EDITORIAL, ROAS_FAQ,
    CPL_EDITORIAL, CPL_FAQ,
    FREQ_EDITORIAL, FREQ_FAQ,
)

GTM_ID      = "GTM-546VKQVR"
ADSENSE_PUB = "ca-pub-4789906927045850"
SITE_URL    = "https://themarketingcalc.com"

NAV_LINKS = [
    ("Home", "/"),
    ("CPM Calculator", "/cpm-calculator"),
    ("CTR Calculator", "/ctr-calculator"),
    ("CPC Calculator", "/cpc-calculator"),
    ("ROAS Calculator", "/roas-calculator"),
    ("CPL Calculator", "/cpl-calculator"),
    ("Frequency Calculator", "/frequency-calculator"),
    ("Budget Calculator", "/budget-calculator"),
    ("Guides", "/guides"),
]


def nav_html(active_path="/"):
    links = ""
    for label, href in NAV_LINKS:
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


def head_html(title, description, canonical_path):
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
  <meta property="og:image" content="{SITE_URL}/logo.png">
  <meta name="google-adsense-account" content="{ADSENSE_PUB}">
  <link rel="icon" href="/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
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
      <a href="/cpm-calculator">CPM</a>
      <a href="/ctr-calculator">CTR</a>
      <a href="/cpc-calculator">CPC</a>
      <a href="/roas-calculator">ROAS</a>
      <a href="/cpl-calculator">CPL</a>
      <a href="/frequency-calculator">Frequency</a>
      <a href="/budget-calculator">Budget Calculator</a>
      <a href="/guides">Guides</a>
      <a href="/privacy-policy">Privacy Policy</a>
    </nav>
    <p class="footer-copy">&copy; 2026 TheMarketingCalc.com</p>
  </div>
</footer>
<script src="/cookie_banner.js" defer></script>
<script src="/main.js" defer></script>
</body>
</html>'''


def page(filepath, title, description, canonical_path, body_html):
    if os.path.dirname(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    content = head_html(title, description, canonical_path) + nav_html(canonical_path) + body_html + footer_html()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Built: {filepath}")


def calc_page(filepath, canonical_path, title, meta_desc, calc_html, editorial, faq_html):
    body = f'''
<main>
  <section class="calc-hero">
    <div class="container">
      {AD_LEADERBOARD}
      {calc_html}
    </div>
  </section>
  <section class="calc-content">
    <div class="container">
      <div class="page-with-sidebar">
        {AD_SIDEBAR_L}
        <div class="main-col prose">
          {editorial}
          {faq_html}
        </div>
        {AD_SIDEBAR_R}
      </div>
    </div>
  </section>
</main>'''
    page(filepath, title, meta_desc, canonical_path, body)


def calc_card(calc_id, title, desc, modes, fields, formula):
    mode_btns = ""
    for i, (label, mode) in enumerate(modes):
        active = " active" if i == 0 else ""
        mode_btns += f'<button class="mode-btn{active}" data-mode="{mode}">{label}</button>'
    field_html = ""
    for fid, flabel, placeholder, hidden in fields:
        h = " hidden" if hidden else ""
        field_html += f'''
        <div class="input-group{h}" id="field-{fid}">
          <label>{flabel}</label>
          <input type="number" id="{fid}" placeholder="{placeholder}" min="0">
        </div>'''
    return f'''
<div class="calc-card">
  <div class="calc-header">
    <h1>{title}</h1>
    <p class="calc-desc">{desc}</p>
  </div>
  <div class="calc-mode-toggle">{mode_btns}</div>
  <div class="calc-inputs">{field_html}</div>
  <button class="calc-btn" onclick="calc_{calc_id}()">Calculate</button>
  <div class="calc-result hidden" id="{calc_id}-result"></div>
  <div class="calc-formula">
    <span class="formula-label">Formula</span>
    <code>{formula}</code>
  </div>
</div>'''


# ── CALCULATOR HTML ───────────────────────────────────────────────────────────

CPM_CALC = calc_card(
    "cpm", "CPM Calculator",
    "Calculate CPM, total cost, or impressions. Enter any two values to find the third.",
    [("Find CPM", "cpm-cpm"), ("Find Cost", "cpm-cost"), ("Find Impressions", "cpm-imp")],
    [("cpm-cost","Total Cost ($)","e.g. 500",False), ("cpm-impressions","Impressions","e.g. 100000",False), ("cpm-cpm-val","CPM ($)","e.g. 5.00",True)],
    "CPM = (Cost / Impressions) x 1,000"
)

CTR_CALC = calc_card(
    "ctr", "CTR Calculator",
    "Calculate click-through rate, total clicks, or impressions. Enter any two values to find the third.",
    [("Find CTR", "ctr-ctr"), ("Find Clicks", "ctr-clicks"), ("Find Impressions", "ctr-imp")],
    [("ctr-clicks","Clicks","e.g. 250",False), ("ctr-impressions","Impressions","e.g. 10000",False), ("ctr-ctr-val","CTR (%)","e.g. 2.5",True)],
    "CTR = (Clicks / Impressions) x 100"
)

CPC_CALC = calc_card(
    "cpc", "CPC Calculator",
    "Calculate cost per click, total cost, or number of clicks. Enter any two values to find the third.",
    [("Find CPC", "cpc-cpc"), ("Find Cost", "cpc-cost"), ("Find Clicks", "cpc-clicks")],
    [("cpc-cost","Total Cost ($)","e.g. 500",False), ("cpc-clicks","Clicks","e.g. 1000",False), ("cpc-cpc-val","CPC ($)","e.g. 0.50",True)],
    "CPC = Cost / Clicks"
)

ROAS_CALC = '''
<div class="calc-card">
  <div class="calc-tabs-nav calc-tabs-inner" role="tablist">
    <button class="calc-tab active" data-tab="roas">ROAS</button>
    <button class="calc-tab" data-tab="poas">POAS</button>
    <button class="calc-tab" data-tab="beroas">Break-even ROAS</button>
  </div>
  <div class="calc-panel active" id="tab-roas">
    <div class="calc-header"><h1>ROAS Calculator</h1><p class="calc-desc">Return on Ad Spend. Calculate ROAS, revenue, or ad spend from any two values.</p></div>
    <div class="calc-mode-toggle">
      <button class="mode-btn active" data-mode="roas-roas">Find ROAS</button>
      <button class="mode-btn" data-mode="roas-rev">Find Revenue</button>
      <button class="mode-btn" data-mode="roas-spend">Find Ad Spend</button>
    </div>
    <div class="calc-inputs">
      <div class="input-group" id="roas-field-rev"><label>Revenue ($)</label><input type="number" id="roas-rev" placeholder="e.g. 5000" min="0"></div>
      <div class="input-group" id="roas-field-spend"><label>Ad Spend ($)</label><input type="number" id="roas-spend" placeholder="e.g. 1000" min="0"></div>
      <div class="input-group hidden" id="roas-field-roas"><label>ROAS</label><input type="number" id="roas-roas" placeholder="e.g. 4" min="0"></div>
    </div>
    <button class="calc-btn" onclick="calcROAS()">Calculate</button>
    <div class="calc-result hidden" id="roas-result"></div>
    <div class="calc-formula"><span class="formula-label">Formula</span><code>ROAS = Revenue / Ad Spend</code></div>
  </div>
  <div class="calc-panel" id="tab-poas">
    <div class="calc-header"><h2>POAS Calculator</h2><p class="calc-desc">Profit on Ad Spend - uses gross profit instead of revenue for a more accurate picture of campaign profitability.</p></div>
    <div class="calc-mode-toggle">
      <button class="mode-btn active" data-mode="poas-poas">Find POAS</button>
      <button class="mode-btn" data-mode="poas-profit">Find Profit</button>
      <button class="mode-btn" data-mode="poas-spend">Find Ad Spend</button>
    </div>
    <div class="calc-inputs">
      <div class="input-group" id="poas-field-profit"><label>Gross Profit ($)</label><input type="number" id="poas-profit" placeholder="e.g. 2000" min="0"></div>
      <div class="input-group" id="poas-field-spend"><label>Ad Spend ($)</label><input type="number" id="poas-spend" placeholder="e.g. 1000" min="0"></div>
      <div class="input-group hidden" id="poas-field-poas"><label>POAS</label><input type="number" id="poas-poas" placeholder="e.g. 2" min="0"></div>
    </div>
    <button class="calc-btn" onclick="calcPOAS()">Calculate</button>
    <div class="calc-result hidden" id="poas-result"></div>
    <div class="calc-formula"><span class="formula-label">Formula</span><code>POAS = Gross Profit / Ad Spend</code></div>
  </div>
  <div class="calc-panel" id="tab-beroas">
    <div class="calc-header"><h2>Break-even ROAS Calculator</h2><p class="calc-desc">Find the minimum ROAS your campaigns need to cover costs and break even on ad spend.</p></div>
    <div class="calc-inputs">
      <div class="input-group"><label>Average Order Value ($)</label><input type="number" id="be-aov" placeholder="e.g. 100" min="0"></div>
      <div class="input-group"><label>COGS per order ($)</label><input type="number" id="be-cogs" placeholder="e.g. 40" min="0"></div>
      <div class="input-group"><label>Other variable costs per order ($) <span class="input-hint">shipping, fulfillment etc.</span></label><input type="number" id="be-other" placeholder="e.g. 10" min="0" value="0"></div>
    </div>
    <button class="calc-btn" onclick="calcBEROAS()">Calculate</button>
    <div class="calc-result hidden" id="beroas-result"></div>
    <div class="calc-formula"><span class="formula-label">Formula</span><code>Break-even ROAS = AOV / (AOV - COGS - Other Costs)</code></div>
  </div>
</div>'''

CPL_CALC = calc_card(
    "cpl", "CPL Calculator",
    "Calculate cost per lead, total budget, or number of leads. Enter any two values to find the third.",
    [("Find CPL", "cpl-cpl"), ("Find Cost", "cpl-cost"), ("Find Leads", "cpl-leads")],
    [("cpl-cost","Total Cost ($)","e.g. 1000",False), ("cpl-leads","Leads","e.g. 50",False), ("cpl-cpl-val","CPL ($)","e.g. 20",True)],
    "CPL = Cost / Leads"
)

FREQ_CALC = calc_card(
    "freq", "Frequency Calculator",
    "Calculate ad frequency, total impressions, or unique reach. Enter any two values to find the third.",
    [("Find Frequency", "freq-freq"), ("Find Impressions", "freq-imp"), ("Find Reach", "freq-reach")],
    [("freq-imp","Impressions","e.g. 500000",False), ("freq-reach","Reach (unique people)","e.g. 100000",False), ("freq-freq-val","Frequency","e.g. 5",True)],
    "Frequency = Impressions / Reach"
)

# ── INDEX ─────────────────────────────────────────────────────────────────────

INDEX_BODY = '''
<main>
  <section class="hero">
    <div class="hero-inner">
      <p class="hero-eyebrow">Free marketing calculators</p>
      <h1>Calculate Any<br><span class="accent">Marketing Metric</span><br>Instantly</h1>
      <p class="hero-sub">CPM, CTR, CPC, ROAS, POAS, CPL, Frequency, Break-even ROAS - all free, no sign-up required.</p>
    </div>
  </section>
  <section class="calcs-section" id="calculators">
    <div class="container">
      <div class="calc-tabs-nav" role="tablist">
        <a href="/cpm-calculator" class="calc-tab">CPM Calculator</a>
        <a href="/ctr-calculator" class="calc-tab">CTR Calculator</a>
        <a href="/cpc-calculator" class="calc-tab">CPC Calculator</a>
        <a href="/roas-calculator" class="calc-tab">ROAS Calculator</a>
        <a href="/roas-calculator" class="calc-tab">POAS Calculator</a>
        <a href="/cpl-calculator" class="calc-tab">CPL Calculator</a>
        <a href="/frequency-calculator" class="calc-tab">Frequency Calculator</a>
        <a href="/roas-calculator" class="calc-tab">Break-even ROAS</a>
      </div>
      <div class="index-content">
        <h2>Marketing metrics, calculated instantly</h2>
        <p>Digital advertising runs on numbers. CPM tells you what you are paying for attention. CTR tells you how compelling your creative is. ROAS tells you whether your campaigns are profitable. POAS goes one step further and measures profitability directly. Every metric answers a specific question, and understanding all of them together is what separates good media buyers from great ones.</p>
        <p>This site gives you free calculators for every core paid media metric - CPM, CTR, CPC, ROAS, POAS, CPL, Frequency and Break-even ROAS. Each calculator works in all directions: give it any two values and it will find the third. No accounts, no paywalls, no limits.</p>
        <div class="metric-grid">
          <a href="/cpm-calculator" class="metric-card"><span class="metric-abbr">CPM</span><span class="metric-name">Cost Per Mille</span><span class="metric-desc">Cost per 1,000 impressions. The standard buying unit for awareness campaigns.</span></a>
          <a href="/ctr-calculator" class="metric-card"><span class="metric-abbr">CTR</span><span class="metric-name">Click-Through Rate</span><span class="metric-desc">Percentage who clicked after seeing your ad. A direct signal of creative relevance.</span></a>
          <a href="/cpc-calculator" class="metric-card"><span class="metric-abbr">CPC</span><span class="metric-name">Cost Per Click</span><span class="metric-desc">What you pay per click. The core efficiency metric for traffic campaigns.</span></a>
          <a href="/roas-calculator" class="metric-card"><span class="metric-abbr">ROAS</span><span class="metric-name">Return on Ad Spend</span><span class="metric-desc">Revenue per dollar spent. The primary KPI for e-commerce advertising.</span></a>
          <a href="/roas-calculator" class="metric-card"><span class="metric-abbr">POAS</span><span class="metric-name">Profit on Ad Spend</span><span class="metric-desc">Profit per dollar spent. More accurate than ROAS for variable-margin businesses.</span></a>
          <a href="/cpl-calculator" class="metric-card"><span class="metric-abbr">CPL</span><span class="metric-name">Cost Per Lead</span><span class="metric-desc">What you pay per lead. The primary KPI for B2B and lead gen campaigns.</span></a>
          <a href="/frequency-calculator" class="metric-card"><span class="metric-abbr">Freq</span><span class="metric-name">Frequency</span><span class="metric-desc">Average times a person sees your ad. Too low means low recall. Too high means fatigue.</span></a>
          <a href="/roas-calculator" class="metric-card"><span class="metric-abbr">BE</span><span class="metric-name">Break-even ROAS</span><span class="metric-desc">The minimum ROAS needed to cover costs. Every campaign needs a target floor.</span></a>
        </div>
      </div>
    </div>
  </section>
  <section class="guides-preview">
    <div class="container">
      <h2>Marketing Guides</h2>
      <div class="guide-grid">
        <a href="/guides/what-is-cpm" class="guide-card"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Understand cost per mille and when to optimise for it.</p></a>
        <a href="/guides/what-is-roas" class="guide-card"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend explained - and how to benchmark it.</p></a>
        <a href="/guides/what-is-poas" class="guide-card"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Why profit-based optimisation beats revenue ROAS.</p></a>
        <a href="/guides/what-is-ctr" class="guide-card"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by channel and ad format.</p></a>
        <a href="/guides/cpm-vs-ecpm" class="guide-card"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought and effective CPM.</p></a>
        <a href="/guides/marketing-budget-benchmarks" class="guide-card"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>CPM, CPC, CTR and ROAS benchmarks by channel.</p></a>
      </div>
      <a href="/guides" class="btn-secondary">View all guides &rarr;</a>
    </div>
  </section>
</main>'''

GUIDES_BODY = '''
<main>
  <section class="page-hero"><div class="container">
    <h1>Marketing <span class="accent">Guides</span></h1>
    <p class="hero-sub">Practical explanations of the metrics that matter - with formulas, benchmarks, and examples.</p>
  </div></section>
  <section class="guides-full"><div class="container">
    <div class="guide-grid guide-grid-full">
      <a href="/guides/responsive-search-ads-guide" class="guide-card"><span class="guide-tag">Google Ads</span><h3>The Ultimate Google Search Ads Guide</h3><p>How to write winning responsive search ads using the science of the Messy Middle.</p></a>
      <a href="/guides/how-to-calculate-campaign-budget" class="guide-card"><span class="guide-tag">Budgets</span><h3>How to Calculate a Campaign Budget</h3><p>A step-by-step framework for estimating ad budgets across channels.</p></a>
      <a href="/guides/what-is-cpm" class="guide-card"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Cost per mille explained - with channel benchmarks and examples.</p></a>
      <a href="/guides/what-is-roas" class="guide-card"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend: how to calculate, benchmark, and improve it.</p></a>
      <a href="/guides/cpm-vs-ecpm" class="guide-card"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought CPM and effective CPM.</p></a>
      <a href="/guides/what-is-ctr" class="guide-card"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by platform, format, and industry.</p></a>
      <a href="/guides/what-is-poas" class="guide-card"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Profit on Ad Spend - why it is more actionable than ROAS.</p></a>
      <a href="/guides/marketing-budget-benchmarks" class="guide-card"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>CPM, CPC, CTR, and ROAS benchmarks across channels and markets.</p></a>
    </div>
  </div></section>
</main>'''

PRIVACY_BODY = '''
<main>
  <section class="page-hero"><div class="container"><h1>Privacy <span class="accent">Policy</span></h1></div></section>
  <section class="prose-section"><div class="container prose">
    <p>Last updated: January 2025</p>
    <h2>1. Who we are</h2>
    <p>TheMarketingCalc.com is a free marketing calculator and resource site. We do not sell products or collect personal data for commercial purposes.</p>
    <h2>2. Cookies and tracking</h2>
    <p>We use Google Analytics 4 (statistics) and Google AdSense (marketing) cookies. These are only activated with your consent via our cookie banner. We implement Google Consent Mode v2.</p>
    <h2>3. Data collected</h2>
    <p>If you accept statistics cookies: anonymised page views, session data, and device type via GA4. If you accept marketing cookies: ad interaction data via Google AdSense.</p>
    <h2>4. Third parties</h2>
    <p>Google Analytics and Google AdSense are operated by Google LLC. See <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a>.</p>
    <h2>5. Your rights</h2>
    <p>Withdraw consent at any time by clearing localStorage key <code>cookie_consent_v1</code> and revisiting the site.</p>
    <h2>6. Contact</h2>
    <p>privacy@themarketingcalc.com</p>
  </div></section>
</main>'''


def guide_body(title, tag, content_html, h1=None):
    h1_text = h1 if h1 else title
    from datetime import date
    updated = date.today().strftime("%B %d, %Y")
    author_box = f'''
<div class="author-box">
  <img src="/images/peter-jensen.jpg" alt="Peter Jensen" class="author-avatar">
  <div class="author-meta">
    <span class="author-name">Peter Jensen</span>
    <span class="author-title">Marketing Specialist</span>
    <span class="author-updated">Updated {updated}</span>
  </div>
</div>'''
    breadcrumb = f'''<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="/">Home</a><span class="bc-sep">/</span><a href="/guides">Guides</a><span class="bc-sep">/</span><span class="bc-current">{h1_text}</span>
</nav>'''
    return f'''
<main>
  <section class="page-hero"><div class="container">
    {breadcrumb}
    <span class="guide-tag">{tag}</span>
    <h1>{h1_text}</h1>
    {author_box}
  </div></section>
  <section class="prose-section"><div class="container">
    <div class="page-with-sidebar">
      {AD_SIDEBAR_L}
      <div class="main-col prose">{content_html}</div>
      {AD_SIDEBAR_R}
    </div>
  </div></section>
  <section class="tools-cta"><div class="container">
    <h2>Try the calculators</h2>
    <p>Put these formulas to work instantly.</p>
    <a href="/" class="btn-primary">Open Calculators &rarr;</a>
  </div></section>
</main>'''


BUDGET_BODY = '''
<main>
  <section class="page-hero"><div class="container">
    <p class="hero-eyebrow">Advanced tool</p>
    <h1>Marketing <span class="accent">Budget Calculator</span></h1>
    <p class="hero-sub">Estimate campaign results or required budget across channels - with benchmarks per market.</p>
  </div></section>
  <section class="budget-section"><div class="container">
    <div class="budget-card">
      <div class="budget-step"><h3>1. Select market and currency</h3>
        <div class="market-grid">
          <button class="market-btn active" data-market="US" data-currency="USD">US <span>USD</span></button>
          <button class="market-btn" data-market="UK" data-currency="GBP">UK <span>GBP</span></button>
          <button class="market-btn" data-market="NO" data-currency="NOK">Norway <span>NOK</span></button>
          <button class="market-btn" data-market="SE" data-currency="SEK">Sweden <span>SEK</span></button>
          <button class="market-btn" data-market="DK" data-currency="DKK">Denmark <span>DKK</span></button>
          <button class="market-btn" data-market="EU" data-currency="EUR">EU <span>EUR</span></button>
          <button class="market-btn" data-market="AU" data-currency="AUD">Australia <span>AUD</span></button>
        </div>
      </div>
      <div class="budget-step"><h3>2. Select channel(s)</h3>
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
      <div class="budget-step"><h3>3. Objective</h3>
        <div class="objective-toggle">
          <button class="obj-btn active" data-obj="reach">Reach / Awareness</button>
          <button class="obj-btn" data-obj="clicks">Traffic / Clicks</button>
          <button class="obj-btn" data-obj="conversions">Conversions</button>
        </div>
      </div>
      <div class="budget-step"><h3>4. Calculate</h3>
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
        <button class="calc-btn" onclick="calcBudget()">Estimate</button>
        <div class="calc-result hidden" id="budget-result"></div>
      </div>
      <div class="budget-benchmarks">
        <h3>Channel benchmarks <span class="badge" id="benchmark-market">US</span></h3>
        <div id="benchmark-table"></div>
      </div>
    </div>
  </div></section>
</main>'''


# ── BUILD ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building themarketingcalc.com...")

    page("index.html",
         "Free Marketing Calculators - CPM, CTR, ROAS, POAS and More | TheMarketingCalc",
         "Free calculators for every core paid media metric. CPM, CTR, CPC, ROAS, POAS, CPL, Frequency and Break-even ROAS. No sign-up required.",
         "/", INDEX_BODY)

    calc_page("cpm-calculator.html", "/cpm-calculator",
              "CPM Calculator - Calculate Cost Per Mille, Impressions and Budget | TheMarketingCalc",
              "Free CPM calculator. Calculate CPM, total campaign cost, or impressions from any two values. Benchmarks, formulas, and FAQs.",
              CPM_CALC, CPM_EDITORIAL, CPM_FAQ)

    calc_page("ctr-calculator.html", "/ctr-calculator",
              "CTR Calculator - Calculate Click-Through Rate, Clicks and Impressions | TheMarketingCalc",
              "Free CTR calculator. Calculate click-through rate, total clicks, or impressions. Benchmarks by channel and practical guidance.",
              CTR_CALC, CTR_EDITORIAL, CTR_FAQ)

    calc_page("cpc-calculator.html", "/cpc-calculator",
              "CPC Calculator - Calculate Cost Per Click, Budget and Clicks | TheMarketingCalc",
              "Free CPC calculator. Calculate cost per click, total campaign cost, or number of clicks. Channel benchmarks and max CPC guidance.",
              CPC_CALC, CPC_EDITORIAL, CPC_FAQ)

    calc_page("roas-calculator.html", "/roas-calculator",
              "ROAS Calculator - ROAS, POAS and Break-even ROAS | TheMarketingCalc",
              "Free ROAS, POAS and break-even ROAS calculator. Understand the difference between revenue and profit-based optimisation.",
              ROAS_CALC, ROAS_EDITORIAL, ROAS_FAQ)

    calc_page("cpl-calculator.html", "/cpl-calculator",
              "CPL Calculator - Calculate Cost Per Lead, Budget and Leads | TheMarketingCalc",
              "Free CPL calculator. Calculate cost per lead, total budget, or number of leads. Benchmarks by channel and max CPL guidance.",
              CPL_CALC, CPL_EDITORIAL, CPL_FAQ)

    calc_page("frequency-calculator.html", "/frequency-calculator",
              "Frequency Calculator - Calculate Ad Frequency, Reach and Impressions | TheMarketingCalc",
              "Free ad frequency calculator. Calculate frequency, impressions, or reach. Guidance on optimal frequency and avoiding ad fatigue.",
              FREQ_CALC, FREQ_EDITORIAL, FREQ_FAQ)

    page("budget-calculator.html",
         "Marketing Budget Calculator - Estimate Reach, Clicks and Conversions | TheMarketingCalc",
         "Advanced marketing budget calculator. Select market, channel mix, and objective to estimate results or required budget.",
         "/budget-calculator", BUDGET_BODY)

    page("guides.html",
         "Marketing Guides - CPM, ROAS, CTR, POAS Explained | TheMarketingCalc",
         "Practical guides explaining the marketing metrics that matter - with formulas, benchmarks, and examples.",
         "/guides", GUIDES_BODY)

    page("privacy-policy.html", "Privacy Policy | TheMarketingCalc",
         "Privacy policy for TheMarketingCalc.com.", "/privacy-policy", PRIVACY_BODY)

    guides = [
        ("guides/responsive-search-ads-guide.html", "The Ultimate Google Search Ads Guide - Writing Winning Responsive Search Ads", "Google Ads", "/guides/responsive-search-ads-guide",
         RSA_GUIDE_CONTENT + faq(RSA_GUIDE_FAQ), "The Ultimate Google Search Ads Guide: Learn How to Write Winning Responsive Search Ads"),
        ("guides/how-to-calculate-campaign-budget.html", "How to Calculate a Campaign Budget", "Budgets", "/guides/how-to-calculate-campaign-budget",
         "<h2>The framework</h2><p>Start with your objective and work backwards from a target metric. If your goal is 500,000 impressions and your expected CPM is $5, your budget is 500,000 / 1,000 x $5 = $2,500.</p><h2>Step 1 - Choose your objective</h2><p>Reach/Awareness: use CPM. Traffic: use CPC. Conversions: use CPL or target CPA.</p><h2>Step 2 - Benchmark your metric</h2><p>Use platform averages as a starting point, then adjust for your industry, creative quality, and audience size. See our <a href='/guides/marketing-budget-benchmarks'>benchmark guide</a>.</p><h2>Step 3 - Calculate</h2><p>Budget = Target Impressions / 1,000 x CPM. Budget = Target Clicks x CPC. Budget = Target Leads x CPL.</p><h2>Step 4 - Sanity-check with break-even ROAS</h2><p>If running e-commerce, verify your budget makes sense against your margin floor before committing spend. Use our <a href='/roas-calculator'>Break-even ROAS calculator</a>."),
        ("guides/what-is-cpm.html", "The Marketer's Guide to CPM - What It Means and Why It Drives Brand Growth", "CPM", "/guides/what-is-cpm",
         CPM_GUIDE_CONTENT + faq(CPM_GUIDE_FAQ), "The Marketer's Guide to CPM: What It Means and Why It Drives Brand Growth"),
        ("guides/what-is-roas.html", "The Ultimate Guide to ROAS - Measuring the True Efficiency of Your Ad Spend", "ROAS", "/guides/what-is-roas",
         ROAS_GUIDE_CONTENT + faq(ROAS_GUIDE_FAQ), "The Ultimate Guide to ROAS: Measuring the True Efficiency of Your Ad Spend"),
        ("guides/cpm-vs-ecpm.html", "CPM vs eCPM - What is the Difference?", "CPM", "/guides/cpm-vs-ecpm",
         "<h2>CPM - what you pay</h2><p>CPM is the rate you agreed to pay per 1,000 impressions.</p><h2>eCPM - what you effectively pay</h2><p>eCPM normalises performance across buying models: eCPM = (Total Cost / Impressions) x 1,000. Use it to compare CPC and CPM buys on equal footing.</p><p>Use our <a href='/cpm-calculator'>CPM calculator</a> to calculate eCPM from any campaign spend and impression data.</p>"),
        ("guides/what-is-ctr.html", "What is CTR? Click-Through Rate Explained", "CTR", "/guides/what-is-ctr",
         "<h2>Definition</h2><p>CTR = (Clicks / Impressions) x 100. A direct signal of creative and audience relevance.</p><h2>Benchmarks</h2><p>Google Search: 3 to 6%. Google Display: 0.1 to 0.3%. Meta Feed: 0.5 to 1.5%. LinkedIn: 0.3 to 0.7%.</p><p>Use our <a href='/ctr-calculator'>CTR calculator</a> to calculate CTR, clicks, or impressions from any two values.</p>"),
        ("guides/what-is-poas.html", "The Ultimate Guide to POAS - Why POAS Scales E-Commerce Profit", "POAS", "/guides/what-is-poas",
         POAS_GUIDE_CONTENT, "The Ultimate Guide to POAS: Why POAS is the Metric That Actually Scales E-Commerce Profit"),
        ("guides/marketing-budget-benchmarks.html", "Marketing Budget Benchmarks by Channel", "Budgets", "/guides/marketing-budget-benchmarks",
         "<h2>CPM benchmarks (2024-2025)</h2><p>Meta: $6 to $14. Google Display: $2 to $5. LinkedIn: $30 to $80. TikTok: $8 to $15. Snapchat: $3 to $8. Reddit: $3 to $10. X: $4 to $9.</p><h2>CPC benchmarks</h2><p>Google Search: $1 to $6. Meta: $0.30 to $1.50. LinkedIn: $5 to $15. TikTok: $0.20 to $0.80.</p><h2>CTR benchmarks</h2><p>Google Search: 3 to 6%. Google Display: 0.1 to 0.3%. Meta Feed: 0.5 to 1.5%. LinkedIn: 0.3 to 0.7%.</p><h2>Note on benchmarks</h2><p>These are averages. Your numbers depend on audience, creative, industry, and bidding strategy. Use our <a href='/budget-calculator'>budget calculator</a> to model full campaigns with channel-specific benchmarks.</p>"),
    ]

    for entry in guides:
        filepath, title, tag, canonical_path, content = entry[:5]
        h1 = entry[5] if len(entry) > 5 else None
        page(filepath, f"{title} | TheMarketingCalc", title, canonical_path, guide_body(title, tag, content, h1=h1))

    print("Done.")
