from build_helpers import faq, AD_INLINE, AFFILIATES

BENCHMARKS_GUIDE_CONTENT = """
<p style="font-size:1.05rem;color:var(--text-muted);margin-bottom:32px;line-height:1.7;">Media fragmentation means every platform behaves differently. High-intent environments like search capture existing demand. Visual, algorithmically-driven platforms like short-form video excel at generating net-new demand. These cross-industry benchmarks provide the performance baselines needed to structure, evaluate, and scale paid media budgets. All figures are global averages converted to EUR.</p>

<p>Use the <a href="/budget-calculator">Marketing Budget Calculator</a> to model your campaign spend across these channels, or jump directly to the individual calculators - <a href="/cpm-calculator">CPM</a>, <a href="/ctr-calculator">CTR</a>, <a href="/cpc-calculator">CPC</a>, <a href="/roas-calculator">ROAS</a>, <a href="/cpl-calculator">CPL</a> - to work with your own live account data.</p>

<h2>At a glance: cross-channel advertising benchmarks</h2>
<p>This master matrix standardises performance metrics across the major ad networks for quick benchmarking and cross-channel comparison.</p>

<div style="overflow-x:auto;margin:24px 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.82rem;">
  <thead>
    <tr style="border-bottom:2px solid var(--border);">
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Channel / Format</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">CTR</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">CPC</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">CVR</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">CPA / CPL</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">ROAS</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Google Paid Search</td>
      <td style="padding:10px 12px;color:var(--text-muted);">3.5% - 6.0%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">~EUR 2.75</td>
      <td style="padding:10px 12px;color:var(--text-muted);">3.2% - 5.0%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 42-60 / EUR 75+</td>
      <td style="padding:10px 12px;color:var(--accent);font-weight:600;">3.5:1 - 4.5:1</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Google PMax</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.2% - 2.5%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 0.55 - 1.10</td>
      <td style="padding:10px 12px;color:var(--text-muted);">2.5% - 4.2%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">~8% below Search</td>
      <td style="padding:10px 12px;color:var(--accent);font-weight:600;">4.0:1+</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Google Demand Gen</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.8% - 1.5%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 0.37 - 0.80</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.0% - 2.2%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 37 - 65</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.8:1 - 2.5:1</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">YouTube Video</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.5% - 1.2%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 0.11 - 0.17 (CPV)</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.2% - 2.5%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 55 - 93</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.2:1 - 2.0:1</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Google Display</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.4% - 0.6%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">~EUR 0.41</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.5% - 0.9%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 84 - 130+</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.2:1 - 2.0:1</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Meta (Facebook / IG)</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.5% - 2.2%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">~EUR 1.60</td>
      <td style="padding:10px 12px;color:var(--text-muted);">2.35% (7.5%+ lead forms)</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 36 / EUR 21</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.86:1 median</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">TikTok</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.5% - 0.8%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 0.42 - 0.79</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.5% - 2.1%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 30 (EUR 13-20 with UGC)</td>
      <td style="padding:10px 12px;color:var(--text-muted);">2.21:1</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Snapchat</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.6% - 1.0%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 0.14 - 0.37</td>
      <td style="padding:10px 12px;color:var(--text-muted);">0.4% - 0.95%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 14 - 33</td>
      <td style="padding:10px 12px;color:var(--text-muted);">1.3:1 - 2.1:1</td>
    </tr>
    <tr>
      <td style="padding:10px 12px;font-weight:600;color:var(--text);">Microsoft / Bing Search</td>
      <td style="padding:10px 12px;color:var(--text-muted);">2.5% - 3.5%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 1.16 - 1.95</td>
      <td style="padding:10px 12px;color:var(--text-muted);">2.8% - 4.0%</td>
      <td style="padding:10px 12px;color:var(--text-muted);">EUR 33 - 51</td>
      <td style="padding:10px 12px;color:var(--accent);font-weight:600;">3.0:1 - 4.0:1</td>
    </tr>
  </tbody>
</table>
</div>

""" + AD_INLINE + """

<h2>Google Ads ecosystem</h2>
<p>Google remains the cornerstone of capture-based marketing, but its network inventory varies widely depending on placement intent.</p>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge google">G</div>
    <div>
      <div class="channel-name">Google Paid Search</div>
      <div class="channel-desc">High-intent text ads - captures users actively looking for a solution</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">3.5% - 6.0%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">~EUR 2.75</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">3.2% - 5.0%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 42-60 (E-com)<br>EUR 75+ (B2B)</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">3.5:1 - 4.5:1</div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">This intent rewards advertisers with strong conversion rates, though hyper-competitive niches easily push costs above the EUR 2.75 average. Use the <a href="/cpc-calculator">CPC Calculator</a> to forecast spend from your target click volume.</p>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge google">G</div>
    <div>
      <div class="channel-name">Google Performance Max</div>
      <div class="channel-desc">AI-optimised cross-channel architecture spanning Search, Shopping, YouTube, Display, Discover, Gmail and Maps</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">1.2% - 2.5%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">EUR 0.55 - 1.10</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">2.5% - 4.2%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">~8% below Search</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">4.0:1+</div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">Achieves high revenue efficiency by dynamically blending inventory tiers. See our <a href="/guides/performance-max-creative-specs">Performance Max creative specs guide</a> for asset requirements.</p>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge google">G</div>
    <div>
      <div class="channel-name">Google Demand Gen</div>
      <div class="channel-desc">Visual, feed-native placements across YouTube and Discover - mid-funnel consideration</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">0.8% - 1.5%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">EUR 0.37 - 0.80</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">1.0% - 2.2%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 37 - 65</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">1.8:1 - 2.5:1</div></div>
  </div>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge youtube">YT</div>
    <div>
      <div class="channel-name">YouTube Video</div>
      <div class="channel-desc">In-stream and in-feed video - primarily top-of-funnel. CPC measured as cost-per-view (CPV)</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">0.5% - 1.2%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPV</div><div class="benchmark-value">EUR 0.11 - 0.17</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">1.2% - 2.5%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 55 - 93</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">1.2:1 - 2.0:1</div></div>
  </div>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge google">G</div>
    <div>
      <div class="channel-name">Google Display Network</div>
      <div class="channel-desc">Banner and responsive display ads across 3M+ partner sites - affordable reach over immediate intent</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">0.4% - 0.6%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">~EUR 0.41</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">0.5% - 0.9%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 84 - 130+</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">1.2:1 - 2.0:1</div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">Display ads appear passively while users browse. Lower intent means lower conversion rates - but also very low CPCs. Best used for retargeting and brand awareness rather than direct acquisition. Use the <a href="/cpm-calculator">CPM Calculator</a> to plan reach-based display budgets.</p>
</div>

<h2>Social platforms</h2>
<p>Paid social operates on discovery algorithms. Success depends heavily on matching your creative format to user behaviour on each platform.</p>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge meta">M</div>
    <div>
      <div class="channel-name">Meta (Facebook and Instagram)</div>
      <div class="channel-desc">Feed, Stories, Reels and native lead gen forms - highly stable cross-industry performance</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">1.5% - 2.2%<br><span style="font-size:0.75rem;color:var(--text-muted);">Lead forms: 2.5%+</span></div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">~EUR 1.60</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">2.35% (feed)<br><span style="font-size:0.75rem;color:var(--text-muted);">7.5-8.5% (lead forms)</span></div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 36 (E-com)<br>EUR 21 (Lead forms)</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">1.86:1 median<br><span style="font-size:0.75rem;color:var(--text-muted);">Top quartile: 4.2:1</span></div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">Meta's standout feature is its native Lead Generation Forms. By keeping users inside the app, conversion rates jump to 7.5% to 8.5%, reducing the average CPL to EUR 21. Note that native form leads sometimes require additional qualification compared to website form leads.</p>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge tiktok">TT</div>
    <div>
      <div class="channel-name">TikTok</div>
      <div class="channel-desc">Entertainment-first platform - standard polished ads underperform, native UGC-style content wins</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">0.5% - 0.8%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">EUR 0.42 - 0.79</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">1.5% - 2.1%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 30 median<br><span style="font-size:0.75rem;color:var(--text-muted);">EUR 13-20 with UGC</span></div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">2.21:1</div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">Brands using native user-generated content (UGC) see acquisition costs slashed to EUR 13 to EUR 20, compared to the EUR 30 platform median. Works best for consumer products with a strong visual story and a young-to-mid-age audience.</p>
</div>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge snap">SC</div>
    <div>
      <div class="channel-name">Snapchat</div>
      <div class="channel-desc">High-volume play - strongest for app installs and low-friction consumer offers</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">Swipe-up rate</div><div class="benchmark-value">0.6% - 1.0%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">EUR 0.14 - 0.37</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">0.4% - 0.95%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 14 - 33</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">1.3:1 - 2.1:1</div></div>
  </div>
</div>

<h2>Microsoft Advertising</h2>

<div class="channel-benchmark-card">
  <div class="channel-benchmark-header">
    <div class="channel-badge bing">B</div>
    <div>
      <div class="channel-name">Microsoft / Bing Search</div>
      <div class="channel-desc">High-intent search at a discount - slightly older demographic with higher average household income</div>
    </div>
  </div>
  <div class="benchmark-grid">
    <div class="benchmark-stat"><div class="benchmark-label">CTR</div><div class="benchmark-value">2.5% - 3.5%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPC</div><div class="benchmark-value">EUR 1.16 - 1.95</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CVR</div><div class="benchmark-value">2.8% - 4.0%</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">CPA / CPL</div><div class="benchmark-value">EUR 33 - 51</div></div>
    <div class="benchmark-stat"><div class="benchmark-label">ROAS</div><div class="benchmark-value">3.0:1 - 4.0:1</div></div>
  </div>
  <p style="margin:14px 0 0;font-size:0.875rem;color:var(--text-muted);">Bing captures high-intent search traffic at a significant discount compared to Google. The demographic trends slightly older with higher average household income, delivering very predictable ROAS and strong conversion rates. Often the first channel to add after Google Search is performing.</p>
</div>

<h2>How to apply benchmarks to your forecasting</h2>
<p>Cross-industry averages provide a starting point for initial planning - your actual numbers will vary based on your vertical, creative quality, landing page experience, and audience targeting. Once your campaigns are live, replace these benchmarks with your own historical data using the formulas below.</p>

<div class="formula-block">
  <div class="formula-label">CTR formula</div>
  <div class="formula-main">CTR = (Clicks &divide; Impressions) &times; 100</div>
</div>
<div class="formula-block">
  <div class="formula-label">CPC formula</div>
  <div class="formula-main">CPC = Total Ad Spend &divide; Total Clicks</div>
</div>
<div class="formula-block">
  <div class="formula-label">ROAS formula</div>
  <div class="formula-main">ROAS = Total Revenue &divide; Total Ad Spend</div>
</div>

<p>Enter your own figures into the <a href="/budget-calculator">Marketing Budget Calculator</a> using the custom metrics toggle to turn these generic benchmarks into an accurate channel-specific forecasting model. See the <a href="/guides/how-to-calculate-campaign-budget">how to calculate a marketing campaign budget guide</a> for a step-by-step framework.</p>

""" + AFFILIATES['supermetrics']()

BENCHMARKS_GUIDE_FAQ = [
    ("What is a good ROAS by channel?",
     "Google Paid Search and Bing typically deliver the highest direct ROAS (3.5:1 to 4.5:1) because they capture existing demand from users already looking for your product. Performance Max averages 4.0:1 or higher on well-optimised product feeds. Social channels like Meta and TikTok often show lower immediate click-based ROAS (1.5:1 to 2.5:1) because they introduce products to users who were not actively shopping - their full value requires multi-touch attribution to measure correctly."),
    ("Why is Google Search CPC so much higher than Display?",
     "Google Search ads target active intent. Someone typing a commercial query is highly valuable, causing advertisers to bid aggressively and driving up the CPC. Display Network ads appear passively while users browse, resulting in lower intent, lower conversion rates, and a much lower CPC (around EUR 0.41). The trade-off is that Display CPA is significantly higher despite the lower CPC, because you need many more clicks to get a conversion."),
    ("Why does Meta have such a low CPA for native lead forms?",
     "Meta's native lead forms eliminate website landing page friction. Instead of navigating to an external site, users submit a pre-filled form directly inside the Facebook or Instagram app. This drives conversion rates to 7.5% to 8.5%, dropping the average CPL to EUR 21. The trade-off is lead quality - native form leads sometimes require additional qualification compared to leads who intentionally navigated to your website and completed a form there."),
    ("What is the difference between CPA and CPL in these benchmarks?",
     "CPA (Cost Per Acquisition) refers to a completed transaction or customer conversion, standard in e-commerce. CPL (Cost Per Lead) tracks top-of-funnel actions like sign-ups or form submissions, standard in B2B. When forecasting, always factor in your internal lead-to-customer conversion rate to ensure your pipeline remains profitable against your actual Customer Lifetime Value."),
    ("Should I use TikTok for direct response campaigns?",
     "TikTok can work for direct response with the right creative approach. The platform favours native, creator-style content over polished brand ads. Brands using UGC-style creative see CPA drop to EUR 13 to EUR 20 versus the EUR 30 platform median. TikTok works best for consumer products with a strong visual story and a young-to-mid-age audience. B2B and high-consideration purchases generally see poor results on the platform."),
    ("Are these benchmarks accurate for my industry?",
     "These are cross-industry averages for 2024-2025. Industry-specific benchmarks vary significantly - B2B software has much higher CPCs and CPLs than e-commerce, while industries like insurance and legal services can see Google Search CPCs of EUR 20 to EUR 50+. Use these figures as a starting point for initial planning, then replace them with your own account data once campaigns are live. The Marketing Budget Calculator supports custom metrics for exactly this purpose."),
]
