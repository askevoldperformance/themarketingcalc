#!/usr/bin/env python3
"""
Build script for themarketingcalc.com
Run: python build.py
"""

import os

GTM_ID = "GTM-XXXXXXXXX"
ADSENSE_PUB = "ca-pub-4789906927045850"
SITE_URL = "https://themarketingcalc.com"

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
      <a href="/cpm-calculator">CPM Calculator</a>
      <a href="/ctr-calculator">CTR Calculator</a>
      <a href="/roas-calculator">ROAS Calculator</a>
      <a href="/budget-calculator">Budget Calculator</a>
      <a href="/guides">Guides</a>
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
    if os.path.dirname(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    content = (
        head_html(title, description, canonical_path)
        + nav_html(canonical_path)
        + body_html
        + footer_html()
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Built: {filepath}")


# ── CALC CARD COMPONENTS ──────────────────────────────────────────────────────

def calc_card(calc_id, title, desc, modes, fields, formula, extra_fields=""):
    mode_btns = ""
    for i, (label, mode) in enumerate(modes):
        active = " active" if i == 0 else ""
        mode_btns += f'<button class="mode-btn{active}" data-mode="{mode}">{label}</button>'

    field_html = ""
    for fid, flabel, placeholder, hidden in fields:
        h = " hidden" if hidden else ""
        hint = ""
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
  <div class="calc-inputs">{field_html}{extra_fields}</div>
  <button class="calc-btn" onclick="calc_{calc_id}()">Calculate</button>
  <div class="calc-result hidden" id="{calc_id}-result"></div>
  <div class="calc-formula">
    <span class="formula-label">Formula</span>
    <code>{formula}</code>
  </div>
</div>'''


def calc_page(filepath, canonical_path, title, meta_desc, calc_html, content_html):
    body = f'''
<main>
  <section class="calc-hero">
    <div class="container">
      {calc_html}
    </div>
  </section>
  <section class="calc-content">
    <div class="container prose">
      {content_html}
    </div>
  </section>
</main>'''
    page(filepath, title, meta_desc, canonical_path, body)


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
        <a href="/cpm-calculator" class="calc-tab">CPM</a>
        <a href="/ctr-calculator" class="calc-tab">CTR</a>
        <a href="/cpc-calculator" class="calc-tab">CPC</a>
        <a href="/roas-calculator" class="calc-tab">ROAS</a>
        <a href="/roas-calculator" class="calc-tab">POAS</a>
        <a href="/cpl-calculator" class="calc-tab">CPL</a>
        <a href="/frequency-calculator" class="calc-tab">Frequency</a>
        <a href="/roas-calculator" class="calc-tab">Break-even ROAS</a>
      </div>

      <div class="index-content">
        <h2>Marketing metrics, calculated instantly</h2>
        <p>Digital advertising runs on numbers. CPM tells you what you are paying for attention. CTR tells you how compelling your creative is. ROAS tells you whether your campaigns are profitable. POAS goes one step further and measures profitability directly. Every metric answers a specific question, and understanding all of them together is what separates good media buyers from great ones.</p>
        <p>This site gives you free calculators for every core paid media metric - CPM, CTR, CPC, ROAS, POAS, CPL, Frequency and Break-even ROAS. Each calculator works in all directions: give it any two values and it will find the third. No accounts, no paywalls, no limits.</p>

        <div class="metric-grid">
          <a href="/cpm-calculator" class="metric-card">
            <span class="metric-abbr">CPM</span>
            <span class="metric-name">Cost Per Mille</span>
            <span class="metric-desc">Cost per 1,000 impressions. The standard buying unit for awareness campaigns.</span>
          </a>
          <a href="/ctr-calculator" class="metric-card">
            <span class="metric-abbr">CTR</span>
            <span class="metric-name">Click-Through Rate</span>
            <span class="metric-desc">Percentage of people who clicked after seeing your ad. A signal of creative quality.</span>
          </a>
          <a href="/cpc-calculator" class="metric-card">
            <span class="metric-abbr">CPC</span>
            <span class="metric-name">Cost Per Click</span>
            <span class="metric-desc">What you pay for each click. Essential for traffic and conversion campaigns.</span>
          </a>
          <a href="/roas-calculator" class="metric-card">
            <span class="metric-abbr">ROAS</span>
            <span class="metric-name">Return on Ad Spend</span>
            <span class="metric-desc">Revenue generated per dollar spent. The primary KPI for e-commerce advertising.</span>
          </a>
          <a href="/roas-calculator" class="metric-card">
            <span class="metric-abbr">POAS</span>
            <span class="metric-name">Profit on Ad Spend</span>
            <span class="metric-desc">Profit generated per dollar spent. More accurate than ROAS for variable-margin businesses.</span>
          </a>
          <a href="/cpl-calculator" class="metric-card">
            <span class="metric-abbr">CPL</span>
            <span class="metric-name">Cost Per Lead</span>
            <span class="metric-desc">What you pay per lead generated. The primary KPI for B2B and lead gen campaigns.</span>
          </a>
          <a href="/frequency-calculator" class="metric-card">
            <span class="metric-abbr">Freq</span>
            <span class="metric-name">Frequency</span>
            <span class="metric-desc">Average times a person sees your ad. Too low means low brand recall. Too high means ad fatigue.</span>
          </a>
          <a href="/roas-calculator" class="metric-card">
            <span class="metric-abbr">BE</span>
            <span class="metric-name">Break-even ROAS</span>
            <span class="metric-desc">The minimum ROAS needed to cover your costs. Every campaign needs a target floor.</span>
          </a>
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
</main>
'''

# ── CPM CALCULATOR ────────────────────────────────────────────────────────────

CPM_CALC = calc_card(
    "cpm", "CPM Calculator",
    "Calculate CPM, total cost, or impressions. Enter any two values to find the third.",
    [("Find CPM", "cpm-cpm"), ("Find Cost", "cpm-cost"), ("Find Impressions", "cpm-imp")],
    [
        ("cpm-cost", "Total Cost ($)", "e.g. 500", False),
        ("cpm-impressions", "Impressions", "e.g. 100000", False),
        ("cpm-cpm-val", "CPM ($)", "e.g. 5.00", True),
    ],
    "CPM = (Cost / Impressions) x 1,000"
)

CPM_CONTENT = '''
<h2>What is CPM and how is it calculated?</h2>
<p>CPM stands for Cost Per Mille, where "mille" is Latin for thousand. It is the price an advertiser pays for 1,000 impressions of an ad. CPM is the standard pricing model for display advertising, social media reach campaigns, and programmatic buying.</p>
<p>The formula is straightforward: CPM = (Total Cost / Impressions) x 1,000. If you spend $500 and receive 200,000 impressions, your CPM is $2.50.</p>

<h2>How do I calculate how many impressions I will get for my budget?</h2>
<p>Rearrange the CPM formula: Impressions = (Budget / CPM) x 1,000. With a $1,000 budget and a $10 CPM, you can expect 100,000 impressions. Use the calculator above in "Find Impressions" mode to do this instantly.</p>

<h2>How do I calculate the cost of a campaign from a CPM rate?</h2>
<p>Cost = (CPM / 1,000) x Impressions. If your CPM is $8 and you want 500,000 impressions, your campaign cost will be $4,000. Switch the calculator to "Find Cost" mode and enter your CPM and target impressions.</p>

<h2>What is a good CPM?</h2>
<p>CPM benchmarks vary significantly by platform, audience, and objective. As rough reference points for 2024 to 2025: Meta Ads typically range from $6 to $14, Google Display from $2 to $5, LinkedIn from $30 to $80, and TikTok from $8 to $15. Niche B2B audiences and retargeting audiences will always command higher CPMs than broad prospecting.</p>

<h2>Why is my CPM high?</h2>
<p>Several factors push CPM up: a small, competitive audience (like senior decision-makers on LinkedIn), a high-demand period (Q4, holidays), low relevance scores or quality scores on your creative, aggressive bidding from competitors in the same auction, and narrow geographic targeting. Broad audiences, strong creative quality scores, and avoiding peak seasons all help reduce CPM.</p>

<h2>What is the difference between CPM and eCPM?</h2>
<p>CPM is the rate you agreed to pay when buying media. eCPM (effective CPM) is calculated retroactively from actual spend and impressions, and is used to compare efficiency across campaigns or ad units that may have been bought on different models - CPC, CPA, or CPM. See our <a href="/guides/cpm-vs-ecpm">CPM vs eCPM guide</a> for a full breakdown.</p>

<h2>Does a lower CPM always mean a better campaign?</h2>
<p>Not necessarily. A very low CPM usually means a broad, low-quality audience. What matters is cost per outcome - whether that is a click, a lead, or a purchase. A $20 CPM that delivers a 3% CTR is more efficient than a $5 CPM with a 0.3% CTR if your goal is traffic. Always evaluate CPM in context with CTR and conversion rate.</p>

<h2>How do CPM campaigns compare to CPC campaigns?</h2>
<p>CPM campaigns charge per impression regardless of whether anyone clicks. CPC campaigns charge only when someone clicks. CPM is typically better for awareness and reach goals where broad exposure matters. CPC is better when you want to pay only for engaged users. You can compare the two by calculating eCPM: if your CPC is $0.50 and your CTR is 1%, your effective CPM is $5. Use our <a href="/cpc-calculator">CPC calculator</a> alongside this one to model both scenarios.</p>

<h2>What CPM should I use when planning a campaign budget?</h2>
<p>Use platform benchmark data as a starting point, then adjust based on your own historical data. If you have run similar campaigns before, your actual CPM is the best predictor. If you are planning a new campaign, use the conservative end of the benchmark range to avoid overestimating reach. Our <a href="/budget-calculator">budget calculator</a> uses channel-specific benchmarks to estimate reach from a given budget.</p>

<h2>How does audience size affect CPM?</h2>
<p>Smaller audiences tend to have higher CPMs because more advertisers are competing for fewer impressions. A retargeting audience of 10,000 people will almost always have a higher CPM than a prospecting audience of 2 million. This is why scaling a retargeting campaign is disproportionately expensive compared to top-of-funnel reach campaigns.</p>

<h2>Can CPM be used to compare performance across channels?</h2>
<p>Yes, but with caution. A LinkedIn impression and a TikTok impression are not the same thing in terms of attention or context. CPM is useful for comparing efficiency within a channel or between similar placements. Cross-channel CPM comparisons are best used as a rough efficiency indicator, not a definitive ranking.</p>
'''

# ── CTR CALCULATOR ────────────────────────────────────────────────────────────

CTR_CALC = calc_card(
    "ctr", "CTR Calculator",
    "Calculate click-through rate, total clicks, or impressions. Enter any two values to find the third.",
    [("Find CTR", "ctr-ctr"), ("Find Clicks", "ctr-clicks"), ("Find Impressions", "ctr-imp")],
    [
        ("ctr-clicks", "Clicks", "e.g. 250", False),
        ("ctr-impressions", "Impressions", "e.g. 10000", False),
        ("ctr-ctr-val", "CTR (%)", "e.g. 2.5", True),
    ],
    "CTR = (Clicks / Impressions) x 100"
)

CTR_CONTENT = '''
<h2>What is CTR and how is it calculated?</h2>
<p>CTR (Click-Through Rate) is the percentage of people who clicked your ad after seeing it. It is calculated as: CTR = (Clicks / Impressions) x 100. If your ad received 300 clicks from 20,000 impressions, your CTR is 1.5%.</p>

<h2>How do I calculate how many clicks I will get from a campaign?</h2>
<p>Clicks = CTR% x Impressions / 100. If you expect 500,000 impressions and a 1% CTR, you will get approximately 5,000 clicks. Use the "Find Clicks" mode in the calculator above and enter your expected impressions and CTR benchmark.</p>

<h2>What is a good CTR for paid social ads?</h2>
<p>For Meta (Facebook and Instagram) feed ads, a CTR between 0.5% and 1.5% is typical for cold audiences. Story and Reels formats tend to run lower at 0.3% to 0.8%. Retargeting campaigns often see 1.5% to 3% or higher. For TikTok, 0.5% to 1.2% is a common range. LinkedIn typically runs 0.3% to 0.7% due to the professional context and higher costs.</p>

<h2>What is a good CTR for Google Search ads?</h2>
<p>Google Search typically has the highest CTR of any ad channel because ads appear in response to active searches. Average CTR across industries ranges from 3% to 6%, but high-intent branded or product keywords can exceed 10%. Display and YouTube ads are much lower, closer to 0.1% to 0.5%.</p>

<h2>Why is my CTR low?</h2>
<p>Low CTR usually points to one of three issues: the wrong audience (your ad is reaching people with no interest in what you are offering), a weak creative or headline (the ad does not give a reason to click), or a mismatch between the ad and the placement (a text-heavy ad in a fast-scroll environment like Reels). Test different creatives, headlines, and audience segments to diagnose the issue.</p>

<h2>Does a high CTR always mean a successful campaign?</h2>
<p>No. CTR measures interest, not outcomes. An ad can have a 5% CTR but a 0.1% conversion rate, making it expensive and ineffective. Always pair CTR with post-click metrics - conversion rate, cost per acquisition, and ROAS. A lower CTR with a higher-quality audience often outperforms a high CTR from a broad, unqualified audience.</p>

<h2>How does CTR affect my CPC?</h2>
<p>On platforms like Google Ads and Meta, CTR directly affects your quality score or relevance score. A higher CTR signals to the platform that your ad is relevant, which can lower your CPC through better auction positioning. This means improving creative quality is not just about getting more clicks - it also makes every click cheaper. Use our <a href="/cpc-calculator">CPC calculator</a> to model the impact.</p>

<h2>What is the relationship between CTR and CPM?</h2>
<p>CTR and CPM together determine your effective CPC. If your CPM is $10 and your CTR is 1%, your effective CPC is $1. If your CTR drops to 0.5% with the same CPM, your effective CPC doubles to $2. This is why creative quality has a compounding effect on campaign economics.</p>

<h2>How do I improve CTR on Meta ads?</h2>
<p>The single biggest lever is the first second of video or the first frame of an image - it needs to stop the scroll. Beyond that: use faces in creative (strong performer for most audiences), make the value proposition explicit in the headline, test multiple creative formats (single image, carousel, video, Reels), and ensure your audience targeting is tight enough that the ad feels relevant to the person seeing it.</p>

<h2>How do I use CTR data to forecast campaign performance?</h2>
<p>Start with your expected impressions (from your CPM and budget), apply your historical or benchmark CTR to get estimated clicks, then apply your landing page conversion rate to get conversions. This simple funnel model - Impressions x CTR x CVR - is the foundation of any campaign forecast. Use our <a href="/budget-calculator">budget calculator</a> to model full campaigns across channels.</p>
'''

# ── CPC CALCULATOR ────────────────────────────────────────────────────────────

CPC_CALC = calc_card(
    "cpc", "CPC Calculator",
    "Calculate cost per click, total cost, or number of clicks. Enter any two values to find the third.",
    [("Find CPC", "cpc-cpc"), ("Find Cost", "cpc-cost"), ("Find Clicks", "cpc-clicks")],
    [
        ("cpc-cost", "Total Cost ($)", "e.g. 500", False),
        ("cpc-clicks", "Clicks", "e.g. 1000", False),
        ("cpc-cpc-val", "CPC ($)", "e.g. 0.50", True),
    ],
    "CPC = Cost / Clicks"
)

CPC_CONTENT = '''
<h2>What is CPC and how is it calculated?</h2>
<p>CPC (Cost Per Click) is the amount you pay each time someone clicks your ad. It is calculated as: CPC = Total Cost / Clicks. If you spend $400 and receive 800 clicks, your CPC is $0.50.</p>

<h2>How do I calculate how many clicks I can get from my budget?</h2>
<p>Clicks = Budget / CPC. With a $1,000 budget and a $2 CPC, you can expect 500 clicks. Use the "Find Clicks" mode in the calculator above to model this instantly.</p>

<h2>What is a good CPC for paid search?</h2>
<p>Google Search CPC varies enormously by industry. Legal, finance, and insurance keywords can exceed $50 per click for competitive terms. E-commerce and retail typically see $0.50 to $3. SaaS and B2B software ranges from $3 to $15. The only benchmark that matters for your business is the maximum CPC you can afford given your conversion rate and customer value.</p>

<h2>What is a good CPC for paid social?</h2>
<p>Meta Ads typically deliver CPC between $0.30 and $1.50 for most e-commerce verticals. LinkedIn is significantly higher at $5 to $15 due to the professional audience. TikTok ranges from $0.20 to $0.80. These are averages - your actual CPC depends heavily on audience size, creative quality, and bidding strategy.</p>

<h2>What is the maximum CPC I should bid?</h2>
<p>Max CPC = (Average Order Value x Conversion Rate) / Target ROAS. If your AOV is $100, your site converts at 2%, and you need a 3x ROAS, your max CPC is ($100 x 0.02) / 3 = $0.67. Bidding above this means you are paying more per click than your economics support. Use our <a href="/roas-calculator">ROAS calculator</a> alongside this to model break-even points.</p>

<h2>Why is my CPC increasing?</h2>
<p>CPC increases when auction competition rises. Common causes: competitors increasing budgets, seasonal demand spikes (Q4, peak retail periods), audience size shrinking due to narrow targeting, or declining relevance scores from stale creative. If your CTR drops while CPM stays flat, your effective CPC will rise even without a bid change.</p>

<h2>How does CPC relate to CPM and CTR?</h2>
<p>CPC = CPM / (CTR x 10). This means CPC is directly determined by how much you pay per impression and how often people click. Improving CTR is the most efficient way to reduce CPC without reducing bids. A creative with double the CTR effectively halves your CPC at the same CPM.</p>

<h2>Should I use CPC or CPM bidding?</h2>
<p>CPC bidding makes sense when you want to pay only for engaged users and your goal is traffic or conversions. CPM bidding is better for reach and awareness goals where you want maximum exposure regardless of clicks. Most modern platforms use automated bidding that optimises for your stated objective, making the manual CPC vs CPM choice less relevant - but understanding both helps you audit performance and set realistic targets.</p>

<h2>How do I reduce my CPC?</h2>
<p>The most effective levers are: improving creative quality to increase CTR (higher CTR = lower effective CPC), broadening audience targeting to reduce auction competition, testing landing page quality to improve quality scores, running campaigns outside peak demand windows, and using broad match or broad audiences to let platform algorithms find efficient traffic.</p>

<h2>How do I forecast campaign cost from a CPC?</h2>
<p>Total Cost = Target Clicks x CPC. If you need 2,000 clicks to hit your conversion target and your expected CPC is $1.20, budget $2,400. Always add a 15% to 20% buffer for CPC volatility, especially in competitive or seasonal categories. Use our <a href="/budget-calculator">budget calculator</a> to build full channel forecasts.</p>
'''

# ── ROAS/POAS/BE-ROAS CALCULATOR ──────────────────────────────────────────────

ROAS_CALC = '''
<div class="calc-card">
  <div class="calc-tabs-nav calc-tabs-inner" role="tablist">
    <button class="calc-tab active" data-tab="roas">ROAS</button>
    <button class="calc-tab" data-tab="poas">POAS</button>
    <button class="calc-tab" data-tab="beroas">Break-even ROAS</button>
  </div>

  <div class="calc-panel active" id="tab-roas">
    <div class="calc-header">
      <h1>ROAS Calculator</h1>
      <p class="calc-desc">Return on Ad Spend. Calculate ROAS, revenue, or ad spend - enter any two values to find the third.</p>
    </div>
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
    <div class="calc-header">
      <h2>POAS Calculator</h2>
      <p class="calc-desc">Profit on Ad Spend. Uses gross profit instead of revenue - a more accurate measure of true campaign profitability.</p>
    </div>
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
    <div class="calc-header">
      <h2>Break-even ROAS Calculator</h2>
      <p class="calc-desc">Find the minimum ROAS your campaigns need to cover costs and break even on ad spend.</p>
    </div>
    <div class="calc-inputs">
      <div class="input-group"><label>Average Order Value ($)</label><input type="number" id="be-aov" placeholder="e.g. 100" min="0"></div>
      <div class="input-group"><label>COGS per order ($)</label><input type="number" id="be-cogs" placeholder="e.g. 40" min="0"></div>
      <div class="input-group"><label>Other variable costs per order ($) <span class="input-hint">shipping, fulfillment etc.</span></label><input type="number" id="be-other" placeholder="e.g. 10" min="0" value="0"></div>
    </div>
    <button class="calc-btn" onclick="calcBEROAS()">Calculate</button>
    <div class="calc-result hidden" id="beroas-result"></div>
    <div class="calc-formula"><span class="formula-label">Formula</span><code>Break-even ROAS = AOV / (AOV - COGS - Other Costs)</code></div>
  </div>
</div>
'''

ROAS_CONTENT = '''
<h2>What is ROAS and how is it calculated?</h2>
<p>ROAS (Return on Ad Spend) measures how much revenue you generate for every dollar spent on advertising. The formula is: ROAS = Revenue / Ad Spend. If you spend $2,000 and generate $10,000 in revenue, your ROAS is 5x (or 500%).</p>

<h2>What is POAS and how is it different from ROAS?</h2>
<p>POAS (Profit on Ad Spend) uses gross profit instead of revenue: POAS = Gross Profit / Ad Spend. If you generate $10,000 in revenue with a 40% gross margin, your gross profit is $4,000. With $2,000 in ad spend, your POAS is 2x. ROAS would show 5x on the same campaign, which looks much better - but POAS tells you what actually matters: are you making money?</p>

<h2>When should I use POAS instead of ROAS?</h2>
<p>Use POAS when your product margins vary. If you sell products ranging from 15% to 60% gross margin, a high ROAS on low-margin products can still lose money. POAS forces this reality into your optimisation signal. It is especially important for e-commerce businesses with wide product catalogues, bundle deals, and promotional pricing. A campaign with ROAS 4x on a 20% margin product is losing money. The same ROAS on a 60% margin product is highly profitable.</p>

<h2>What is a good ROAS?</h2>
<p>There is no universal answer. The only ROAS that matters is your break-even ROAS, which depends entirely on your margins. An e-commerce business with 60% gross margin can be profitable at ROAS 2x. A business with 15% margin needs ROAS 8x or higher just to break even. Use the Break-even ROAS calculator above to find your specific floor.</p>

<h2>What is break-even ROAS?</h2>
<p>Break-even ROAS is the minimum return needed for a campaign to cover its costs and neither make nor lose money. The formula is: Break-even ROAS = AOV / (AOV - COGS - Other Variable Costs). If your average order value is $100, COGS is $40, and shipping costs $10, your margin is $50 and your break-even ROAS is 100/50 = 2x. Any campaign above 2x ROAS is profitable. Any campaign below it is losing money even if the absolute ROAS number looks acceptable.</p>

<h2>How do I improve ROAS?</h2>
<p>ROAS can be improved from either side of the formula. On the revenue side: improve conversion rate on your landing page, increase average order value through upsells and bundles, improve product feed quality for shopping campaigns. On the cost side: cut spend on underperforming ad sets, tighten audience targeting, pause low-quality placements, and improve creative to reduce CPCs. The most sustainable ROAS improvements come from better post-click experience, not just bid adjustments.</p>

<h2>What is the difference between ROAS and ROI?</h2>
<p>ROAS measures revenue relative to ad spend only. ROI measures profit relative to all costs - including COGS, operations, and overhead - not just ad spend. ROAS = Revenue / Ad Spend. ROI = (Net Profit / Total Investment) x 100. ROAS is useful for comparing campaign efficiency. ROI tells you whether the entire business activity is profitable. POAS bridges the gap by factoring margins into the ad-spend calculation.</p>

<h2>How does attribution affect ROAS?</h2>
<p>ROAS is only as accurate as your attribution model. Last-click attribution over-credits the final touchpoint and under-credits awareness and consideration channels. Data-driven attribution distributes credit across touchpoints but depends on volume to work well. iOS privacy changes and cookie restrictions have made ROAS figures less reliable across Meta and Google. This is one reason POAS is increasingly preferred - it focuses on actual profit outcomes rather than attributed revenue figures that may be inflated.</p>

<h2>Can I set a ROAS target in Meta and Google Ads?</h2>
<p>Yes. Meta calls it "Minimum ROAS" in Advantage+ and manual campaign setups. Google Ads calls it "Target ROAS" (tROAS). Both work by telling the platform's algorithm to only bid on users it predicts will deliver your target return. Setting the target too high can cause under-delivery as the algorithm becomes too selective. The break-even ROAS is your floor - set your target above it with enough headroom for the algorithm to find volume.</p>

<h2>How do I implement POAS in Meta and Google Ads?</h2>
<p>Pass gross profit as your conversion value instead of order value. In Google Ads, this is done via a dynamic conversion value in your checkout or via the conversion API. In Meta, use the Conversions API to send a custom revenue value equal to the gross profit per order. Once you are passing profit as conversion value, set your target ROAS to 1x - because POAS break-even is always 1.</p>
'''

# ── CPL CALCULATOR ────────────────────────────────────────────────────────────

CPL_CALC = calc_card(
    "cpl", "CPL Calculator",
    "Calculate cost per lead, total cost, or number of leads. Enter any two values to find the third.",
    [("Find CPL", "cpl-cpl"), ("Find Cost", "cpl-cost"), ("Find Leads", "cpl-leads")],
    [
        ("cpl-cost", "Total Cost ($)", "e.g. 1000", False),
        ("cpl-leads", "Leads", "e.g. 50", False),
        ("cpl-cpl-val", "CPL ($)", "e.g. 20", True),
    ],
    "CPL = Cost / Leads"
)

CPL_CONTENT = '''
<h2>What is CPL and how is it calculated?</h2>
<p>CPL (Cost Per Lead) is the amount you pay to acquire a single lead - a person who has shown interest by filling in a form, requesting a callback, signing up for a trial, or taking another qualifying action. CPL = Total Cost / Number of Leads. Spending $2,000 to generate 80 leads gives a CPL of $25.</p>

<h2>How do I calculate how many leads I can get from my budget?</h2>
<p>Leads = Budget / CPL. With a $5,000 budget and a target CPL of $40, you can expect approximately 125 leads. Use the "Find Leads" mode in the calculator above to model this. Note that CPL targets should be informed by your close rate and customer lifetime value, not just historical averages.</p>

<h2>What is a good CPL?</h2>
<p>It depends entirely on what a lead is worth to your business. A B2B SaaS company with a $50,000 annual contract value can afford a CPL of $500 or more if the close rate is reasonable. A local service business generating $300 jobs might need a CPL below $30 to be profitable. Calculate your maximum CPL as: Max CPL = (Average Contract Value x Close Rate x Gross Margin).</p>

<h2>What is CPL for different channels?</h2>
<p>CPL benchmarks vary widely by industry and channel. LinkedIn Lead Gen Forms often see CPL between $50 and $200 for B2B audiences. Meta lead generation campaigns typically range from $5 to $50 depending on the industry and form complexity. Google Search lead campaigns range from $20 to $100 for most service categories. High-intent keywords in legal, finance, and medical can produce CPLs of $100 to $500.</p>

<h2>How do I reduce CPL?</h2>
<p>CPL has two components: CPC and conversion rate. To lower CPL you need to either pay less per click (improve creative CTR, tighten audience, improve quality scores) or convert more of those clicks into leads (improve landing page, reduce form friction, strengthen the offer). The fastest wins usually come from landing page optimisation - small improvements in conversion rate have a large impact on CPL.</p>

<h2>What is the difference between CPL and CPA?</h2>
<p>CPL specifically measures the cost of acquiring a lead - a person who has expressed interest but not yet converted into a customer. CPA (Cost Per Acquisition) measures the cost of a completed conversion, which could be a purchase, a subscription, or a signed contract. In lead gen funnels, CPA = CPL / Close Rate. If your CPL is $40 and you close 20% of leads, your CPA is $200.</p>

<h2>How does lead quality affect CPL benchmarks?</h2>
<p>A low CPL is meaningless if the leads do not convert. Optimising purely for CPL often leads to low-quality leads - people who filled in a form without real intent. The better metric is cost per qualified lead or cost per opportunity. When reporting CPL, always pair it with lead-to-opportunity rate to give a complete picture of funnel efficiency.</p>

<h2>Should I use lead gen forms or landing pages for CPL campaigns?</h2>
<p>Native lead gen forms (Meta Lead Ads, LinkedIn Lead Gen Forms) typically produce lower CPL because they reduce friction - the user never leaves the platform. However, the lead quality is often lower because the bar to submit is lower. Landing pages produce fewer but higher-quality leads because the person actively navigated to a new page and completed a form. The right choice depends on your sales process and how quickly you can qualify leads.</p>

<h2>How do I forecast CPL for a new campaign?</h2>
<p>Use this chain: estimated CPC from benchmarks, estimated landing page conversion rate (typically 2% to 8% for lead gen), then CPL = CPC / Conversion Rate. A $2 CPC with a 4% conversion rate gives a $50 CPL. Use our <a href="/budget-calculator">budget calculator</a> to build full channel forecasts including CPL estimates.</p>
'''

# ── FREQUENCY CALCULATOR ──────────────────────────────────────────────────────

FREQ_CALC = calc_card(
    "freq", "Frequency Calculator",
    "Calculate ad frequency, total impressions, or reach. Enter any two values to find the third.",
    [("Find Frequency", "freq-freq"), ("Find Impressions", "freq-imp"), ("Find Reach", "freq-reach")],
    [
        ("freq-imp", "Impressions", "e.g. 500000", False),
        ("freq-reach", "Reach (unique people)", "e.g. 100000", False),
        ("freq-freq-val", "Frequency", "e.g. 5", True),
    ],
    "Frequency = Impressions / Reach"
)

FREQ_CONTENT = '''
<h2>What is frequency in advertising and how is it calculated?</h2>
<p>Frequency is the average number of times a unique person sees your ad within a given time period. Frequency = Impressions / Reach. If your campaign reaches 100,000 unique people with 400,000 impressions, the average frequency is 4. This means each person saw your ad four times on average.</p>

<h2>How do I calculate total impressions from reach and frequency?</h2>
<p>Impressions = Reach x Frequency. If you want to reach 200,000 people at a frequency of 5, you need 1,000,000 impressions. Use the "Find Impressions" mode in the calculator above to plan campaign scale. This is especially useful when forecasting reach campaign delivery from a fixed budget.</p>

<h2>What is a good frequency for Facebook and Instagram ads?</h2>
<p>For cold prospecting campaigns, a frequency of 1.5 to 3 over a 7-day period is typically healthy. Above 4 to 5, ad fatigue begins to show up as rising CPMs and falling CTR. For retargeting campaigns, slightly higher frequency is acceptable - 3 to 6 over a 14-day window - because the audience is warmer and more receptive. For brand awareness campaigns with strong creative, 3 to 7 over a month can work without fatigue.</p>

<h2>What is ad frequency fatigue?</h2>
<p>Ad fatigue occurs when the same audience sees the same ad too many times. The symptoms are predictable: CTR starts declining, CPM starts rising (because the algorithm needs to work harder to deliver to a saturated audience), and conversion rate drops. Fatigue is not always about the absolute frequency number - it is about creative wear-out. Refreshing creative can reset fatigue even without changing the audience.</p>

<h2>How do I control frequency on Meta?</h2>
<p>In Reach and Frequency buying (available to larger accounts), you can set a frequency cap directly. In auction-based buying, you control frequency indirectly through audience size (larger audiences = lower frequency at the same budget), budget size relative to audience, and campaign duration. Shorter flight dates with larger budgets will always produce higher frequency than the same budget over a longer period.</p>

<h2>What is the minimum effective frequency?</h2>
<p>The concept of minimum effective frequency comes from traditional media - the idea that a brand message needs to be seen a certain number of times before it registers. Research varies widely, but 3 to 5 exposures is often cited as a baseline for new brand messages. For performance campaigns focused on direct response, even a single high-quality exposure can drive action if the creative and audience match is strong.</p>

<h2>How does frequency relate to reach?</h2>
<p>Reach and frequency are inversely related at a fixed impression volume. At 1,000,000 impressions: reaching 1,000,000 people = frequency 1, reaching 500,000 people = frequency 2, reaching 200,000 people = frequency 5. Broad targeting maximises reach at low frequency. Narrow targeting concentrates impressions on fewer people, increasing frequency. Neither is inherently better - it depends on your objective.</p>

<h2>What is the difference between reach and impressions?</h2>
<p>Reach counts unique people. Impressions count total ad views, including multiple views by the same person. A campaign with 500,000 impressions and 200,000 reach has a frequency of 2.5 - each person saw the ad 2.5 times on average. Reach is the more important metric for awareness campaigns. Impressions matter more when you are trying to increase message repetition or frequency.</p>

<h2>How does frequency affect CPM?</h2>
<p>As frequency rises within a fixed audience, CPM typically increases because the algorithm must serve the same people repeatedly rather than finding fresh audiences. This is sometimes called "audience saturation premium." When you see CPM rising over the course of a campaign without changes to targeting or creative, increasing frequency is usually the first thing to check.</p>

<h2>How do I balance reach and frequency for a brand awareness campaign?</h2>
<p>A common framework: maximise reach first (get your message to as many people as possible at frequency 1 to 2), then build frequency selectively with retargeting or lookalike audiences to reinforce the message among people most likely to engage. This two-stage approach is more efficient than trying to achieve both high reach and high frequency with a single campaign structure.</p>
'''

# ── GUIDES PAGE ───────────────────────────────────────────────────────────────

GUIDES_BODY = '''
<main>
  <section class="page-hero">
    <div class="container">
      <h1>Marketing <span class="accent">Guides</span></h1>
      <p class="hero-sub">Practical explanations of the metrics that matter - with formulas, benchmarks, and examples.</p>
    </div>
  </section>
  <section class="guides-full">
    <div class="container">
      <div class="guide-grid guide-grid-full">
        <a href="/guides/how-to-calculate-campaign-budget" class="guide-card"><span class="guide-tag">Budgets</span><h3>How to Calculate a Campaign Budget</h3><p>A step-by-step framework for estimating ad budgets across channels.</p></a>
        <a href="/guides/what-is-cpm" class="guide-card"><span class="guide-tag">CPM</span><h3>What is CPM?</h3><p>Cost per mille explained - with channel benchmarks and examples.</p></a>
        <a href="/guides/what-is-roas" class="guide-card"><span class="guide-tag">ROAS</span><h3>What is ROAS?</h3><p>Return on Ad Spend: how to calculate, benchmark, and improve it.</p></a>
        <a href="/guides/cpm-vs-ecpm" class="guide-card"><span class="guide-tag">CPM</span><h3>CPM vs eCPM</h3><p>The difference between bought CPM and effective CPM.</p></a>
        <a href="/guides/what-is-ctr" class="guide-card"><span class="guide-tag">CTR</span><h3>What is CTR?</h3><p>Click-through rate benchmarks by platform, format, and industry.</p></a>
        <a href="/guides/what-is-poas" class="guide-card"><span class="guide-tag">POAS</span><h3>What is POAS?</h3><p>Profit on Ad Spend - why it is more actionable than ROAS.</p></a>
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
      <p>Google Analytics and Google AdSense are operated by Google LLC. You can review Google's privacy policy at <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a>.</p>
      <h2>5. Your rights</h2>
      <p>You can withdraw consent at any time by clearing your browser's localStorage (key: cookie_consent_v1) or clearing cookies and revisiting the site.</p>
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


# ── BUILD ALL PAGES ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building themarketingcalc.com...")

    page("index.html",
         "Free Marketing Calculators - CPM, CTR, ROAS, POAS and More | TheMarketingCalc",
         "Free calculators for every core paid media metric. CPM, CTR, CPC, ROAS, POAS, CPL, Frequency and Break-even ROAS. No sign-up required.",
         "/", INDEX_BODY)

    calc_page("cpm-calculator.html", "/cpm-calculator",
              "CPM Calculator - Calculate Cost Per Mille, Impressions and Budget | TheMarketingCalc",
              "Free CPM calculator. Calculate CPM, total campaign cost, or impressions from any two values. Includes benchmarks, formulas, and answers to the most common CPM questions.",
              CPM_CALC, CPM_CONTENT)

    calc_page("ctr-calculator.html", "/ctr-calculator",
              "CTR Calculator - Calculate Click-Through Rate, Clicks and Impressions | TheMarketingCalc",
              "Free CTR calculator. Calculate click-through rate, total clicks, or impressions. Includes benchmarks by channel and answers to common CTR questions.",
              CTR_CALC, CTR_CONTENT)

    calc_page("cpc-calculator.html", "/cpc-calculator",
              "CPC Calculator - Calculate Cost Per Click, Budget and Clicks | TheMarketingCalc",
              "Free CPC calculator. Calculate cost per click, total campaign cost, or number of clicks. Includes channel benchmarks and max CPC guidance.",
              CPC_CALC, CPC_CONTENT)

    calc_page("roas-calculator.html", "/roas-calculator",
              "ROAS Calculator - Calculate Return on Ad Spend, POAS and Break-even ROAS | TheMarketingCalc",
              "Free ROAS, POAS and break-even ROAS calculator. Understand the difference between revenue-based and profit-based optimisation, and find your campaign floor.",
              ROAS_CALC, ROAS_CONTENT)

    calc_page("cpl-calculator.html", "/cpl-calculator",
              "CPL Calculator - Calculate Cost Per Lead, Budget and Leads | TheMarketingCalc",
              "Free CPL calculator. Calculate cost per lead, total budget, or number of leads. Includes benchmarks by channel and guidance on max CPL targets.",
              CPL_CALC, CPL_CONTENT)

    calc_page("frequency-calculator.html", "/frequency-calculator",
              "Frequency Calculator - Calculate Ad Frequency, Reach and Impressions | TheMarketingCalc",
              "Free ad frequency calculator. Calculate frequency, total impressions, or reach. Includes guidance on optimal frequency ranges and how to avoid ad fatigue.",
              FREQ_CALC, FREQ_CONTENT)

    page("budget-calculator.html",
         "Marketing Budget Calculator - Estimate Reach, Clicks and Conversions | TheMarketingCalc",
         "Advanced marketing budget calculator. Select market, channel mix, and objective to estimate campaign results or required budget.",
         "/budget-calculator",
         '''<main>
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
</main>''')

    page("guides.html",
         "Marketing Guides - CPM, ROAS, CTR, POAS Explained | TheMarketingCalc",
         "Practical guides explaining the marketing metrics that matter - with formulas, benchmarks, and examples.",
         "/guides", GUIDES_BODY)

    page("privacy-policy.html",
         "Privacy Policy | TheMarketingCalc",
         "Privacy policy for TheMarketingCalc.com.",
         "/privacy-policy", PRIVACY_BODY)

    guides = [
        ("guides/how-to-calculate-campaign-budget.html",
         "How to Calculate a Campaign Budget", "Budgets", "/guides/how-to-calculate-campaign-budget",
         "<h2>The framework</h2><p>Start with your objective and work backwards from a target metric. If your goal is 500,000 impressions and your expected CPM is $5, your budget is 500,000 / 1,000 x $5 = $2,500.</p><h2>Step 1 - Choose your objective</h2><p>Reach/Awareness: use CPM. Traffic: use CPC. Conversions: use CPL or target CPA.</p><h2>Step 2 - Benchmark your metric</h2><p>Use platform averages as a starting point, then adjust for your industry, creative quality, and audience size. See our <a href='/guides/marketing-budget-benchmarks'>benchmark guide</a>.</p><h2>Step 3 - Calculate</h2><p>Budget = Target Volume / 1,000 x CPM for impressions. Budget = Target Clicks x CPC. Budget = Target Leads x CPL.</p><h2>Step 4 - Sanity-check with ROAS</h2><p>If running e-commerce, verify your budget makes sense against your break-even ROAS. Use our <a href='/roas-calculator'>Break-even ROAS calculator</a> to find your floor before committing spend.</p>"),

        ("guides/what-is-cpm.html",
         "What is CPM? Cost Per Mille Explained", "CPM", "/guides/what-is-cpm",
         "<h2>Definition</h2><p>CPM (Cost Per Mille) is the price you pay per 1,000 ad impressions. It is the standard buying unit for awareness and reach campaigns across all major ad platforms.</p><h2>Formula</h2><p><code>CPM = (Total Cost / Impressions) x 1,000</code></p><h2>Example</h2><p>You spend $500 and receive 200,000 impressions. CPM = ($500 / 200,000) x 1,000 = $2.50.</p><h2>Benchmarks (2024-2025)</h2><p>Meta Ads: $6 to $14. Google Display: $2 to $5. LinkedIn: $30 to $80. TikTok: $8 to $15. These vary significantly by audience, creative, and objective.</p><h2>CPM vs eCPM</h2><p>CPM is what you pay. eCPM (effective CPM) is calculated from actual results and used to compare campaigns with different buying models. <a href='/guides/cpm-vs-ecpm'>Read more</a></p><p>Use our <a href='/cpm-calculator'>CPM calculator</a> to calculate CPM, total cost, or impressions from any two values.</p>"),

        ("guides/what-is-roas.html",
         "What is ROAS? Return on Ad Spend Explained", "ROAS", "/guides/what-is-roas",
         "<h2>Definition</h2><p>ROAS (Return on Ad Spend) measures revenue generated per dollar spent on advertising.</p><h2>Formula</h2><p><code>ROAS = Revenue / Ad Spend</code></p><h2>Example</h2><p>Revenue: $10,000. Ad Spend: $2,000. ROAS = 10,000 / 2,000 = 5x (or 500%).</p><h2>What is a good ROAS?</h2><p>Depends entirely on your margins. A product with 70% gross margin can sustain a lower ROAS than one with 30% margin. Use the Break-even ROAS calculator to find your floor before setting targets.</p><h2>ROAS vs POAS</h2><p>ROAS uses revenue. POAS uses gross profit - making it more actionable for businesses where margins vary across products. <a href='/guides/what-is-poas'>Read more</a></p><p>Use our <a href='/roas-calculator'>ROAS calculator</a> to calculate ROAS, revenue, or ad spend - and find your break-even ROAS.</p>"),

        ("guides/cpm-vs-ecpm.html",
         "CPM vs eCPM - What is the Difference?", "CPM", "/guides/cpm-vs-ecpm",
         "<h2>CPM - what you pay</h2><p>CPM is the rate you agreed to pay per 1,000 impressions. It is set at auction or negotiated directly with a publisher.</p><h2>eCPM - what you effectively pay</h2><p>eCPM (effective CPM) normalises performance across different buying models. It is calculated retroactively: eCPM = (Total Cost / Impressions) x 1,000.</p><h2>Why the distinction matters</h2><p>If you run a CPC campaign and get 500,000 impressions at a cost of $1,500, your eCPM is $3. This lets you compare the efficiency of a CPC buy against a CPM buy for the same audience - something you cannot do by looking at CPC or CPM alone.</p><h2>Publisher vs advertiser</h2><p>Publishers use eCPM to compare yield across ad units and demand sources. Advertisers use it to benchmark campaign efficiency regardless of buying model. Use our <a href='/cpm-calculator'>CPM calculator</a> to calculate eCPM from any campaign.</p>"),

        ("guides/what-is-ctr.html",
         "What is CTR? Click-Through Rate Explained", "CTR", "/guides/what-is-ctr",
         "<h2>Definition</h2><p>CTR (Click-Through Rate) is the percentage of people who clicked your ad after seeing it.</p><h2>Formula</h2><p><code>CTR = (Clicks / Impressions) x 100</code></p><h2>Example</h2><p>1,000 clicks from 200,000 impressions. CTR = (1,000 / 200,000) x 100 = 0.5%.</p><h2>Benchmarks by channel</h2><p>Google Search: 3 to 6%. Google Display: 0.1 to 0.3%. Meta Feed: 0.5 to 1.5%. LinkedIn: 0.3 to 0.7%. TikTok: 0.5 to 1.2%.</p><h2>CTR as a signal</h2><p>High CTR indicates strong creative-audience fit. But CTR alone does not determine campaign success - pair it with conversion rate and CPC to get the full picture. Use our <a href='/ctr-calculator'>CTR calculator</a> to model all three scenarios.</p>"),

        ("guides/what-is-poas.html",
         "What is POAS? Profit on Ad Spend Explained", "POAS", "/guides/what-is-poas",
         "<h2>Definition</h2><p>POAS (Profit on Ad Spend) measures gross profit generated per dollar of ad spend, making it a more accurate performance metric than revenue-based ROAS.</p><h2>Formula</h2><p><code>POAS = Gross Profit / Ad Spend</code></p><h2>Example</h2><p>Gross Profit: $4,000. Ad Spend: $1,000. POAS = 4,000 / 1,000 = 4x.</p><h2>Why POAS beats ROAS</h2><p>ROAS ignores COGS. A 5x ROAS on a 15% margin product loses money. POAS forces profitability into the optimisation signal. Break-even POAS is always 1 - making targets universal across products regardless of price point.</p><h2>Implementing POAS</h2><p>Pass gross profit (not order value) as your conversion value in Meta or Google Ads. This is done via a server-side event or a dynamic conversion value in your checkout. Use our <a href='/roas-calculator'>POAS calculator</a> to model campaigns before and after the switch.</p>"),

        ("guides/marketing-budget-benchmarks.html",
         "Marketing Budget Benchmarks - CPM, CPC, CTR and ROAS by Channel", "Budgets", "/guides/marketing-budget-benchmarks",
         "<h2>How to use these benchmarks</h2><p>These are industry averages for 2024 to 2025. Treat them as starting points - your actual numbers will vary by audience, creative quality, industry, and bidding strategy.</p><h2>CPM benchmarks</h2><p>Meta: $6 to $14. Google Display: $2 to $5. LinkedIn: $30 to $80. TikTok: $8 to $15. Snapchat: $3 to $8. Reddit: $3 to $10. X: $4 to $9.</p><h2>CPC benchmarks</h2><p>Google Search: $1 to $6 (varies widely by industry). Meta: $0.30 to $1.50. LinkedIn: $5 to $15. TikTok: $0.20 to $0.80.</p><h2>CTR benchmarks</h2><p>Google Search: 3 to 6%. Google Display: 0.1 to 0.3%. Meta Feed: 0.5 to 1.5%. LinkedIn: 0.3 to 0.7%.</p><h2>ROAS benchmarks</h2><p>E-commerce average: 3 to 5x. But the only ROAS that matters is your break-even ROAS, which depends on your margins. Use our <a href='/roas-calculator'>Break-even ROAS calculator</a> to find your specific target.</p>"),
    ]

    for filepath, title, tag, canonical_path, content in guides:
        page(filepath,
             f"{title} | TheMarketingCalc",
             title,
             canonical_path,
             guide_body(title, tag, content))

    print("Done.")
