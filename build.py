#!/usr/bin/env python3
"""Build script for themarketingcalc.com. Run: python3 build.py"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from poas_guide_content import POAS_GUIDE_CONTENT
from roas_guide_content import ROAS_GUIDE_CONTENT, ROAS_GUIDE_FAQ
from cpm_guide_content import CPM_GUIDE_CONTENT, CPM_GUIDE_FAQ
from ctr_guide_content import CTR_GUIDE_CONTENT, CTR_GUIDE_FAQ
from cpm_vs_ecpm_content import CPM_VS_ECPM_CONTENT, CPM_VS_ECPM_FAQ
from budget_guide_content import BUDGET_GUIDE_CONTENT, BUDGET_GUIDE_FAQ
from benchmarks_guide_content import BENCHMARKS_GUIDE_CONTENT, BENCHMARKS_GUIDE_FAQ
from rsa_guide_content import RSA_GUIDE_CONTENT, RSA_GUIDE_FAQ
from pmax_guide_content import PMAX_GUIDE_CONTENT, PMAX_GUIDE_FAQ
from budget_calculator_content import BUDGET_CALCULATOR_BODY
from marketing_tools_content import MARKETING_TOOLS_BODY, KEYWORD_TOOLS_BODY
from rsa_preview_content import RSA_PREVIEW_BODY
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

CALC_DROPDOWN = [
    ("CPM Calculator", "/cpm-calculator"),
    ("CTR Calculator", "/ctr-calculator"),
    ("CPC Calculator", "/cpc-calculator"),
    ("ROAS Calculator", "/roas-calculator"),
    ("CPL Calculator", "/cpl-calculator"),
    ("Frequency Calculator", "/frequency-calculator"),
]

GUIDES_DROPDOWN = [
    ("What is CPM?", "/guides/what-is-cpm"),
    ("What is ROAS?", "/guides/what-is-roas"),
    ("What is POAS?", "/guides/what-is-poas"),
    ("What is CTR?", "/guides/what-is-ctr"),
    ("CPM vs eCPM", "/guides/cpm-vs-ecpm"),
    ("How to Calculate Campaign Budget", "/guides/how-to-calculate-campaign-budget"),
    ("Marketing Budget Benchmarks", "/guides/marketing-budget-benchmarks"),
    ("Google Search Ads Guide", "/guides/responsive-search-ads-guide"),
    ("Performance Max Creative Specs", "/guides/performance-max-creative-specs"),
    ("All Guides", "/guides"),
]


def nav_html(active_path="/"):
    calc_active = any(href == active_path for _, href in CALC_DROPDOWN)
    guides_active = any(href == active_path for _, href in GUIDES_DROPDOWN)

    calc_items = "".join(
        f'<a href="{href}"{"class=\"active\"" if href == active_path else ""}>{label}</a>'
        for label, href in CALC_DROPDOWN
    )
    guides_items = "".join(
        f'<a href="{href}"{"class=\"active\"" if href == active_path else ""}>{label}</a>'
        for label, href in GUIDES_DROPDOWN
    )

    calc_class = "active" if calc_active else ""
    calc_dropdown = f'''<div class="nav-dropdown">
      <a href="/cpm-calculator" class="nav-calc-pill {calc_class}" onclick="return handleCalcNav(event)">Calculators</a>
      <div class="nav-dropdown-menu">{calc_items}</div>
    </div>'''

    guides_dropdown = f'''<div class="nav-dropdown">
      <a href="/guides" class="{"active" if guides_active else ""}">Guides</a>
      <div class="nav-dropdown-menu">{guides_items}</div>
    </div>'''

    budget_active = ' class="active"' if active_path == "/budget-calculator" else ""
    tools_active = ' class="active"' if active_path == "/marketing-tools" else ""
    home_active = ' class="active"' if active_path == "/" else ""

    return f'''
<nav class="site-nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo"><img src="/logo.png" alt="The Marketing Calc" width="36" height="36"><span>TheMarketingCalc</span></a>
    <ul class="nav-links">
      <li><a href="/" {home_active}>Home</a></li>
      <li>{calc_dropdown}</li>
      <li><a href="/budget-calculator"{budget_active}>Marketing Budget Calculator</a></li>
      <li><a href="/marketing-tools"{tools_active}>Marketing Tools</a></li>
      <li>{guides_dropdown}</li>
    </ul>
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
  <meta name="impact-site-verification" content="11b4deab-0282-498b-bf5a-89afaea16cf7">
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
<script src="/budget_calculator.js" defer></script>
<script src="/keyword_tools.js" defer></script>
<script src="/rsa_preview.js" defer></script>
</body>
</html>'''


def page(filepath, title, description, canonical_path, body_html):
    if os.path.dirname(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    content = head_html(title, description, canonical_path) + nav_html(canonical_path) + body_html + footer_html()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Built: {filepath}")


def calc_page(filepath, canonical_path, title, meta_desc, calc_html, editorial, faq_html, icon=None):
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


def calc_card(calc_id, title, desc, modes, fields, formula, icon=None):
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
    icon_html = f'<img src="/images/{icon}" alt="" class="calc-card-icon">' if icon else ''
    return f'''
<div class="calc-card">
  <div class="calc-header">
    <div class="calc-header-top">{icon_html}<h1>{title}</h1></div>
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
    [("cpm-cost","Total Cost","e.g. 500",False), ("cpm-impressions","Impressions","e.g. 100000",False), ("cpm-cpm-val","CPM","e.g. 5.00",True)],
    "CPM = (Cost / Impressions) x 1,000", icon="icon-cpm.png"
)

CTR_CALC = calc_card(
    "ctr", "CTR Calculator",
    "Calculate click-through rate, total clicks, or impressions. Enter any two values to find the third.",
    [("Find CTR", "ctr-ctr"), ("Find Clicks", "ctr-clicks"), ("Find Impressions", "ctr-imp")],
    [("ctr-clicks","Clicks","e.g. 250",False), ("ctr-impressions","Impressions","e.g. 10000",False), ("ctr-ctr-val","CTR (%)","e.g. 2.5",True)],
    "CTR = (Clicks / Impressions) x 100", icon="icon-ctr.png"
)

CPC_CALC = calc_card(
    "cpc", "CPC Calculator",
    "Calculate cost per click, total cost, or number of clicks. Enter any two values to find the third.",
    [("Find CPC", "cpc-cpc"), ("Find Cost", "cpc-cost"), ("Find Clicks", "cpc-clicks")],
    [("cpc-cost","Total Cost","e.g. 500",False), ("cpc-clicks","Clicks","e.g. 1000",False), ("cpc-cpc-val","CPC","e.g. 0.50",True)],
    "CPC = Cost / Clicks", icon="icon-cpc.png"
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
      <div class="input-group" id="roas-field-rev"><label>Revenue</label><input type="number" id="roas-rev" placeholder="e.g. 5000" min="0"></div>
      <div class="input-group" id="roas-field-spend"><label>Ad Spend</label><input type="number" id="roas-spend" placeholder="e.g. 1000" min="0"></div>
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
      <div class="input-group" id="poas-field-profit"><label>Gross Profit</label><input type="number" id="poas-profit" placeholder="e.g. 2000" min="0"></div>
      <div class="input-group" id="poas-field-spend"><label>Ad Spend</label><input type="number" id="poas-spend" placeholder="e.g. 1000" min="0"></div>
      <div class="input-group hidden" id="poas-field-poas"><label>POAS</label><input type="number" id="poas-poas" placeholder="e.g. 2" min="0"></div>
    </div>
    <button class="calc-btn" onclick="calcPOAS()">Calculate</button>
    <div class="calc-result hidden" id="poas-result"></div>
    <div class="calc-formula"><span class="formula-label">Formula</span><code>POAS = Gross Profit / Ad Spend</code></div>
  </div>
  <div class="calc-panel" id="tab-beroas">
    <div class="calc-header"><h2>Break-even ROAS Calculator</h2><p class="calc-desc">Find the minimum ROAS your campaigns need to cover costs and break even on ad spend.</p></div>
    <div class="calc-inputs">
      <div class="input-group"><label>Average Order Value</label><input type="number" id="be-aov" placeholder="e.g. 100" min="0"></div>
      <div class="input-group"><label>COGS per order</label><input type="number" id="be-cogs" placeholder="e.g. 40" min="0"></div>
      <div class="input-group"><label>Other variable costs per order <span class="input-hint">shipping, fulfillment etc.</span></label><input type="number" id="be-other" placeholder="e.g. 10" min="0" value="0"></div>
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
    [("cpl-cost","Total Cost","e.g. 1000",False), ("cpl-leads","Leads","e.g. 50",False), ("cpl-cpl-val","CPL","e.g. 20",True)],
    "CPL = Cost / Leads", icon="icon-cpl.png"
)

FREQ_CALC = calc_card(
    "freq", "Frequency Calculator",
    "Calculate ad frequency, total impressions, or unique reach. Enter any two values to find the third.",
    [("Find Frequency", "freq-freq"), ("Find Impressions", "freq-imp"), ("Find Reach", "freq-reach")],
    [("freq-imp","Impressions","e.g. 500000",False), ("freq-reach","Reach (unique people)","e.g. 100000",False), ("freq-freq-val","Frequency","e.g. 5",True)],
    "Frequency = Impressions / Reach", icon="icon-frequency.png"
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
          <a href="/cpm-calculator" class="metric-card"><img src="/images/icon-cpm.png" alt="" class="metric-card-icon"><span class="metric-abbr">CPM</span><span class="metric-name">Cost Per Mille</span><span class="metric-desc">Cost per 1,000 impressions. The standard buying unit for awareness campaigns.</span></a>
          <a href="/ctr-calculator" class="metric-card"><img src="/images/icon-ctr.png" alt="" class="metric-card-icon"><span class="metric-abbr">CTR</span><span class="metric-name">Click-Through Rate</span><span class="metric-desc">Percentage who clicked after seeing your ad. A direct signal of creative relevance.</span></a>
          <a href="/cpc-calculator" class="metric-card"><img src="/images/icon-cpc.png" alt="" class="metric-card-icon"><span class="metric-abbr">CPC</span><span class="metric-name">Cost Per Click</span><span class="metric-desc">What you pay per click. The core efficiency metric for traffic campaigns.</span></a>
          <a href="/roas-calculator" class="metric-card"><img src="/images/icon-roas.png" alt="" class="metric-card-icon"><span class="metric-abbr">ROAS</span><span class="metric-name">Return on Ad Spend</span><span class="metric-desc">Revenue per dollar spent. The primary KPI for e-commerce advertising.</span></a>
          <a href="/roas-calculator" class="metric-card"><img src="/images/icon-poas.png" alt="" class="metric-card-icon"><span class="metric-abbr">POAS</span><span class="metric-name">Profit on Ad Spend</span><span class="metric-desc">Profit per dollar spent. More accurate than ROAS for variable-margin businesses.</span></a>
          <a href="/cpl-calculator" class="metric-card"><img src="/images/icon-cpl.png" alt="" class="metric-card-icon"><span class="metric-abbr">CPL</span><span class="metric-name">Cost Per Lead</span><span class="metric-desc">What you pay per lead. The primary KPI for B2B and lead gen campaigns.</span></a>
          <a href="/frequency-calculator" class="metric-card"><img src="/images/icon-frequency.png" alt="" class="metric-card-icon"><span class="metric-abbr">Freq</span><span class="metric-name">Frequency</span><span class="metric-desc">Average times a person sees your ad. Too low means low recall. Too high means fatigue.</span></a>
          <a href="/roas-calculator" class="metric-card"><img src="/images/icon-roas.png" alt="" class="metric-card-icon"><span class="metric-abbr">BE</span><span class="metric-name">Break-even ROAS</span><span class="metric-desc">The minimum ROAS needed to cover costs. Every campaign needs a target floor.</span></a>
        </div>
      </div>
    </div>
  </section>
  <section class="guides-preview">
    <div class="container">
      <h2>Marketing Guides</h2>
      <div class="guide-grid">
        <a href="/guides/what-is-cpm" class="guide-card"><img src="/images/guides_cpm.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Understand cost per mille and when to optimise for it.</p></a>
        <a href="/guides/what-is-roas" class="guide-card"><img src="/images/guides_roas.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend explained - and how to benchmark it.</p></a>
        <a href="/guides/what-is-poas" class="guide-card"><img src="/images/guides_poas.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Why profit-based optimisation beats revenue ROAS.</p></a>
        <a href="/guides/what-is-ctr" class="guide-card"><img src="/images/guides_ctr.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by channel and ad format.</p></a>
        <a href="/guides/cpm-vs-ecpm" class="guide-card"><img src="/images/guides_cpm_vs_ecpm.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought and effective CPM.</p></a>
        <a href="/guides/marketing-budget-benchmarks" class="guide-card"><img src="/images/guides_budget_benchmarks.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>CPM, CPC, CTR and ROAS benchmarks by channel.</p></a>
      </div>
      <a href="/guides" class="btn-secondary">View all guides &rarr;</a>
    </div>
  </section>
  <section class="guides-preview">
    <div class="container">
      <h2>Free Marketing Tools</h2>
      <div class="guide-grid">
        <a href="/marketing-tools/rsa-preview-tool" class="guide-card">
          <img src="/images/icon-rsa-preview.png" alt="" class="guide-card-icon" loading="lazy">
          <span class="guide-tag">Google Ads</span>
          <h3>RSA Preview Tool</h3>
          <p>Visualize Responsive Search Ad combinations, lock headline positions, and test every variation before launch.</p>
        </a>
        <a href="/marketing-tools/free-keyword-tools" class="guide-card">
          <img src="/images/icon-keyword-match.png" alt="" class="guide-card-icon" loading="lazy">
          <span class="guide-tag">PPC &amp; SEO</span>
          <h3>Free Keyword Tools</h3>
          <p>Format keyword match types for Google Ads and Microsoft Ads, or combine word lists into long-tail keywords.</p>
        </a>
      </div>
      <a href="/marketing-tools" class="btn-secondary">View all tools &rarr;</a>
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
    <div class="guide-filter-tabs" id="guide-filter-tabs">
      <button class="guide-filter-btn active" data-filter="all">All</button>
      <button class="guide-filter-btn" data-filter="Google Ads">Google Ads</button>
      <button class="guide-filter-btn" data-filter="Marketing Metrics">Marketing Metrics</button>
      <button class="guide-filter-btn" data-filter="Budgets">Budgets</button>
    </div>
    <div class="guide-grid guide-grid-full" id="guide-grid-full">
      <a href="/guides/performance-max-creative-specs" class="guide-card" data-category="Google Ads"><img src="/images/guides_pmax_specs.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">Google Ads</span><h3>Performance Max Creative Specs</h3><p>Image sizes, video formats, character limits, and dead zones for PMax asset groups.</p></a>
      <a href="/guides/responsive-search-ads-guide" class="guide-card" data-category="Google Ads"><img src="/images/guides_search_ads_guide.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">Google Ads</span><h3>The Ultimate Google Search Ads Guide</h3><p>How to write winning responsive search ads using the science of the Messy Middle.</p></a>
      <a href="/guides/how-to-calculate-campaign-budget" class="guide-card" data-category="Budgets"><img src="/images/guides_campaign_budget.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">Budgets</span><h3>How to Calculate a Campaign Budget</h3><p>A step-by-step framework for estimating ad budgets across channels.</p></a>
      <a href="/guides/what-is-cpm" class="guide-card" data-category="Marketing Metrics"><img src="/images/guides_cpm.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Cost per mille explained - with channel benchmarks and examples.</p></a>
      <a href="/guides/what-is-roas" class="guide-card" data-category="Marketing Metrics"><img src="/images/guides_roas.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend: how to calculate, benchmark, and improve it.</p></a>
      <a href="/guides/cpm-vs-ecpm" class="guide-card" data-category="Marketing Metrics"><img src="/images/guides_cpm_vs_ecpm.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought CPM and effective CPM.</p></a>
      <a href="/guides/what-is-ctr" class="guide-card" data-category="Marketing Metrics"><img src="/images/guides_ctr.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by platform, format, and industry.</p></a>
      <a href="/guides/what-is-poas" class="guide-card" data-category="Marketing Metrics"><img src="/images/guides_poas.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Profit on Ad Spend - why it is more actionable than ROAS.</p></a>
      <a href="/guides/marketing-budget-benchmarks" class="guide-card" data-category="Budgets"><img src="/images/guides_budget_benchmarks.jpg" alt="" class="guide-card-img" loading="lazy"><span class="guide-tag">Budgets</span><h3>Marketing Budget Benchmarks</h3><p>CPM, CPC, CTR, and ROAS benchmarks across channels and markets.</p></a>
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


def guide_body(title, tag, content_html, h1=None, img=None):
    h1_text = h1 if h1 else title
    from datetime import date
    updated = date.today().strftime("%B %d, %Y")
    author_box = f'''
<div class="author-box">
  <img src="/images/robin-askevold.jpg" alt="Robin Askevold" class="author-avatar">
  <div class="author-meta">
    <span class="author-name">Robin Askevold</span>
    <span class="author-title">Performance Marketing Specialist</span>
    <span class="author-updated">Updated {updated}</span>
  </div>
</div>'''
    hero_img = f'<img src="/images/{img}" alt="{h1_text}" class="guide-hero-img">' if img else ''
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
    {hero_img}
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
         "/budget-calculator", BUDGET_CALCULATOR_BODY)

    page("marketing-tools.html",
         "Free Marketing Tools - Keyword Tools and More | TheMarketingCalc",
         "Free marketing tools for PPC and SEO professionals. Keyword match type formatting, keyword combination generators, and more practical tools for daily campaign work.",
         "/marketing-tools", MARKETING_TOOLS_BODY)

    page("marketing-tools/rsa-preview-tool.html",
         "Free RSA Preview Tool - Responsive Search Ad Generator and Mockup | TheMarketingCalc",
         "Free responsive search ad preview tool. Visualize Google Ads RSA combinations, lock headline positions, and test every variation before launch. No sign-up required.",
         "/marketing-tools/rsa-preview-tool", RSA_PREVIEW_BODY)

    page("marketing-tools/free-keyword-tools.html",
         "Free Keyword Tools - Match Type Formatter and Keyword Combiner | TheMarketingCalc",
         "Free keyword match type tool and keyword combiner for Google Ads and Microsoft Ads. Format Broad, Phrase, and Exact match keywords instantly, or combine word lists into long-tail keywords.",
         "/marketing-tools/free-keyword-tools", KEYWORD_TOOLS_BODY)

    page("guides.html",
         "Marketing Guides - CPM, ROAS, CTR, POAS Explained | TheMarketingCalc",
         "Practical guides explaining the marketing metrics that matter - with formulas, benchmarks, and examples.",
         "/guides", GUIDES_BODY)

    page("privacy-policy.html", "Privacy Policy | TheMarketingCalc",
         "Privacy policy for TheMarketingCalc.com.", "/privacy-policy", PRIVACY_BODY)

    guides = [
        ("guides/performance-max-creative-specs.html", "Performance Max Creative Specs - Image Sizes, Video Formats and Dead Zones", "Google Ads", "/guides/performance-max-creative-specs",
         PMAX_GUIDE_CONTENT + faq(PMAX_GUIDE_FAQ), "Mastering Google Ads Performance Max Formats: Specs, Dead Zones, and Creative Best Practices", "guides_pmax_specs.jpg"),
        ("guides/responsive-search-ads-guide.html", "The Ultimate Google Search Ads Guide - Writing Winning Responsive Search Ads", "Google Ads", "/guides/responsive-search-ads-guide",
         RSA_GUIDE_CONTENT + faq(RSA_GUIDE_FAQ), "The Ultimate Google Search Ads Guide: Learn How to Write Winning Responsive Search Ads", "guides_search_ads_guide.jpg"),
        ("guides/how-to-calculate-campaign-budget.html", "How to Calculate a Marketing Campaign Budget - Step-by-Step Guide", "Budgets", "/guides/how-to-calculate-campaign-budget",
         BUDGET_GUIDE_CONTENT + faq(BUDGET_GUIDE_FAQ), "How to Calculate a Marketing Campaign Budget: A Step-by-Step Guide", "guides_campaign_budget.jpg"),
        ("guides/what-is-cpm.html", "The Marketer's Guide to CPM - What It Means and Why It Drives Brand Growth", "CPM", "/guides/what-is-cpm",
         CPM_GUIDE_CONTENT + faq(CPM_GUIDE_FAQ), "The Marketer's Guide to CPM: What It Means and Why It Drives Brand Growth", "guides_cpm.jpg"),
        ("guides/what-is-roas.html", "The Ultimate Guide to ROAS - Measuring the True Efficiency of Your Ad Spend", "ROAS", "/guides/what-is-roas",
         ROAS_GUIDE_CONTENT + faq(ROAS_GUIDE_FAQ), "The Ultimate Guide to ROAS: Measuring the True Efficiency of Your Ad Spend", "guides_roas.jpg"),
        ("guides/cpm-vs-ecpm.html", "eCPM vs CPM - What is the Difference and How to Calculate Both", "CPM", "/guides/cpm-vs-ecpm",
         CPM_VS_ECPM_CONTENT + faq(CPM_VS_ECPM_FAQ), "eCPM vs CPM: Understanding the Differences and How to Calculate Both", "guides_cpm_vs_ecpm.jpg"),
        ("guides/what-is-ctr.html", "What is CTR? Click-Through Rate Meaning, Formula and Benchmarks", "CTR", "/guides/what-is-ctr",
         CTR_GUIDE_CONTENT + faq(CTR_GUIDE_FAQ), "The Ultimate Guide to CTR: Meaning, Formula, and How to Improve It", "guides_ctr.jpg"),
        ("guides/what-is-poas.html", "The Ultimate Guide to POAS - Why POAS Scales E-Commerce Profit", "POAS", "/guides/what-is-poas",
         POAS_GUIDE_CONTENT, "The Ultimate Guide to POAS: Why POAS is the Metric That Actually Scales E-Commerce Profit", "guides_poas.jpg"),
        ("guides/marketing-budget-benchmarks.html", "Marketing Budget Benchmarks by Channel 2025 - CTR, CPC, CPA and ROAS", "Budgets", "/guides/marketing-budget-benchmarks",
         BENCHMARKS_GUIDE_CONTENT + faq(BENCHMARKS_GUIDE_FAQ), "Marketing Budget Benchmarks by Channel: CTR, CPC, CVR, CPA and ROAS for 2025", "guides_budget_benchmarks.jpg"),
    ]

    for entry in guides:
        filepath, title, tag, canonical_path, content = entry[:5]
        h1 = entry[5] if len(entry) > 5 else None
        img = entry[6] if len(entry) > 6 else None
        page(filepath, f"{title} | TheMarketingCalc", title, canonical_path, guide_body(title, tag, content, h1=h1, img=img))

    print("Done.")
