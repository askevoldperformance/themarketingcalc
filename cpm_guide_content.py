from build_helpers import faq, AD_INLINE, AFFILIATES

CPM_GUIDE_CONTENT = """
<p style="font-size:1.05rem;color:var(--text-muted);margin-bottom:32px;line-height:1.7;">Whether you are launching a digital marketing campaign, buying TV spots, or running an email newsletter, mastering CPM is essential for keeping your ad spend under control. Here is everything you need to know about what CPM means, how to calculate it, and how to use it to benchmark your campaigns.</p>

<h2>What is CPM? Meaning and definition</h2>
<p>CPM stands for Cost Per Mille, where "mille" is the Latin and French word for one thousand. In advertising, CPM represents the cost an advertiser pays for every 1,000 views or impressions of an advertisement.</p>
<p>Every time your ad is displayed 1,000 times on a screen, billboard, or print page, you incur the baseline CPM cost.</p>

<h2>Why use "per thousand"?</h2>
<p>Because single digital ad impressions are incredibly cheap - often fractions of a cent - the industry scales the metric up to 1,000 impressions to make budgeting, pricing, and forecasting much easier to manage. Saying a campaign costs EUR 12.50 CPM is far more practical than saying it costs EUR 0.0125 per impression.</p>

<h2>How to calculate CPM</h2>
<p>To find your cost per thousand impressions, you need two numbers: the total cost of the campaign and the total number of impressions generated.</p>

<div class="formula-block">
  <div class="formula-label">CPM formula</div>
  <div class="formula-main">CPM = (Total Cost &divide; Total Impressions) &times; 1,000</div>
</div>

<h3>Step-by-step calculation example</h3>
<p>Say you invest EUR 5,000 into a campaign and your ad is served 400,000 times.</p>

<div class="calc-example">
  <div class="calc-example-step">
    <span class="calc-step-num">1</span>
    <div>
      <div class="calc-step-label">Divide total cost by total impressions</div>
      <div class="calc-step-formula">EUR 5,000 &divide; 400,000 = <strong>0.0125</strong></div>
    </div>
  </div>
  <div class="calc-example-step">
    <span class="calc-step-num">2</span>
    <div>
      <div class="calc-step-label">Multiply by 1,000 to get cost per thousand</div>
      <div class="calc-step-formula">0.0125 &times; 1,000 = <strong>EUR 12.50</strong></div>
    </div>
  </div>
  <div class="calc-example-result">
    Your CPM is <strong>EUR 12.50</strong> - meaning it costs EUR 12.50 for every 1,000 times your ad is seen.
  </div>
</div>

<p>Use the <a href="/cpm-calculator">free CPM calculator</a> above to run this calculation instantly for your own numbers.</p>

""" + AD_INLINE + """

<h2>Why is CPM so important in marketing?</h2>
<p>CPM is a universal benchmarking tool. Because it standardises cost based on volume, it allows you to compare the efficiency of entirely different media channels on equal terms. With CPM, you can directly compare:</p>
<ul>
  <li>A high-traffic digital banner ad campaign</li>
  <li>A prime-time television commercial - the Super Bowl has a massive upfront cost but a highly competitive CPM due to millions of concurrent viewers</li>
  <li>An email marketing campaign where the ESP charges a CPM rate to cover server bandwidth and deliverability</li>
</ul>
<p>Without CPM as a common unit, comparing a EUR 10,000 TV spot reaching 2 million viewers against a EUR 500 display campaign reaching 80,000 people would be nearly impossible. CPM reduces both to a single comparable number.</p>

<h2>Advanced variations: vCPM vs eCPM</h2>
<p>As advertising technology has evolved, two important variations of CPM have emerged to provide deeper insight into ad exposure and publisher revenue.</p>

<h3>Viewable CPM (vCPM)</h3>
<p>Standard CPM counts an impression the moment an ad loads, even if it sits below the fold and the user never scrolls to see it. vCPM solves this by ensuring you only pay when 1,000 impressions are officially clocked as viewable - typically defined as at least 50% of the ad being on screen for a minimum of one continuous second.</p>
<p>vCPM is increasingly the default in programmatic buying and is generally a more accurate reflection of actual ad exposure than raw CPM.</p>

<h3>Effective CPM (eCPM)</h3>
<p>Publishers often sell inventory across different pricing models - CPC, CPA, or flat rates - and need a way to compare how much revenue each placement generates per thousand views. eCPM translates all those different earnings back into a CPM format for apples-to-apples comparison.</p>

<div class="formula-block">
  <div class="formula-label">eCPM formula</div>
  <div class="formula-main">eCPM = (Total Earnings &divide; Total Impressions) &times; 1,000</div>
</div>

<div class="calc-example">
  <div class="calc-example-step">
    <span class="calc-step-num">&#9432;</span>
    <div>
      <div class="calc-step-label">Publisher example</div>
      <div class="calc-step-formula">A banner ad generates 100,000 impressions and earns EUR 500 through user clicks.</div>
    </div>
  </div>
  <div class="calc-example-result">
    eCPM = (EUR 500 &divide; 100,000) &times; 1,000 = <strong>EUR 5.00</strong>
  </div>
</div>

<p>For a full breakdown of the differences, see our <a href="/guides/cpm-vs-ecpm">CPM vs eCPM guide</a>.</p>

<h2>CPM compared to other key advertising metrics</h2>
<p>CPM measures exposure. To understand the full picture of campaign performance, it helps to know how it compares to the other core metrics in digital advertising.</p>

<div style="overflow-x:auto;margin:24px 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.875rem;">
  <thead>
    <tr style="border-bottom:2px solid var(--border);">
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Metric</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Full name</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Focus area</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Best used for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:700;color:var(--accent);">CPM</td>
      <td style="padding:10px 12px;color:var(--text);">Cost Per Mille</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Brand awareness and reach</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Measuring exposure and ad delivery volume</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:700;color:var(--text);"><a href="/cpc-calculator" style="color:var(--text);">CPC</a></td>
      <td style="padding:10px 12px;color:var(--text);">Cost Per Click</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Traffic and engagement</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Driving users to a specific landing page</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;font-weight:700;color:var(--text);">CPA</td>
      <td style="padding:10px 12px;color:var(--text);">Cost Per Action</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Conversions and sales</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Direct response campaigns</td>
    </tr>
    <tr>
      <td style="padding:10px 12px;font-weight:700;color:var(--text);"><a href="/ctr-calculator" style="color:var(--text);">CTR</a></td>
      <td style="padding:10px 12px;color:var(--text);">Click-Through Rate</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Ad relevancy</td>
      <td style="padding:10px 12px;color:var(--text-muted);">Evaluating how engaging your ad creative is</td>
    </tr>
  </tbody>
</table>
</div>

<p>See also: <a href="/cpc-calculator">CPC Calculator</a> - <a href="/ctr-calculator">CTR Calculator</a> - <a href="/cpl-calculator">CPL Calculator</a> - <a href="/roas-calculator">ROAS Calculator</a></p>

""" + AFFILIATES['semrush']()

CPM_GUIDE_FAQ = [
    ("What is a good CPM in digital advertising?",
     "A good CPM varies significantly by channel, audience, and market. As a rough benchmark: display advertising typically ranges from EUR 0.50 to EUR 5, social media (Meta, LinkedIn) from EUR 5 to EUR 25, and premium video placements on YouTube or connected TV from EUR 15 to EUR 50 or more. LinkedIn tends to have the highest CPMs due to its professional audience targeting. The right CPM for your campaign depends on your objective and what a conversion is worth to you."),
    ("What is the difference between CPM and CPC?",
     "CPM charges per 1,000 impressions regardless of whether anyone clicks. CPC charges only when someone clicks. CPM is better suited to brand awareness campaigns where the goal is reach and visibility. CPC is better for direct response campaigns where the goal is to drive traffic or conversions. Most platforms let you choose which model to use, and some optimise between the two automatically."),
    ("What does CPM mean on YouTube?",
     "On YouTube, CPM refers to the cost advertisers pay per 1,000 ad impressions shown to viewers. YouTube also shows creators a related metric called RPM (Revenue Per Mille), which represents earnings per 1,000 video views after YouTube takes its share. CPM on YouTube varies by content category, viewer location, and time of year - Q4 typically has the highest CPMs due to holiday advertiser spend."),
    ("What is the difference between CPM and vCPM?",
     "Standard CPM counts an impression as soon as the ad loads, even if it is never visible on screen. vCPM (viewable CPM) only counts an impression when at least 50% of the ad has been on screen for at least one continuous second. vCPM gives a more accurate picture of actual ad exposure and is generally the preferred metric for brand awareness campaigns."),
    ("What is eCPM and how is it different from CPM?",
     "CPM is what an advertiser pays per 1,000 impressions. eCPM (effective CPM) is what a publisher earns per 1,000 impressions, calculated by dividing total earnings by total impressions and multiplying by 1,000. Publishers use eCPM to compare the revenue efficiency of different ad placements and pricing models regardless of whether they were sold on a CPM, CPC, or CPA basis."),
    ("How do I reduce my CPM?",
     "The most effective ways to reduce CPM are: broadening your target audience (narrower audiences typically cost more to reach), improving your ad quality score (platforms reward high-quality ads with better auction prices), testing different ad formats and placements, reducing campaign frequency (high frequency inflates CPM as you exhaust the audience), and shifting spend toward off-peak periods where competition is lower."),
]
