from build_helpers import faq, AD_INLINE, AFFILIATES

CPM_VS_ECPM_CONTENT = """
<p style="font-size:1.05rem;color:var(--text-muted);margin-bottom:32px;line-height:1.7;">CPM and eCPM look almost identical and use the same maths, but they represent two completely different sides of the advertising equation. One tracks what you spend, the other tracks what you earn. Here is a definitive breakdown of the difference, how to calculate both, and why it matters for your campaigns or your ad inventory.</p>

<h2>The core difference: advertiser vs publisher</h2>
<p>The easiest way to understand the difference is to consider who is using each metric:</p>

<div class="calc-example">
  <div class="calc-example-step">
    <span class="calc-step-num">&#9432;</span>
    <div>
      <div class="calc-step-label">CPM - Cost Per Mille (advertiser metric)</div>
      <div class="calc-step-formula">What an advertiser pays for every 1,000 times their ad is served. Used to manage budgets and measure brand awareness reach.</div>
    </div>
  </div>
  <div class="calc-example-step">
    <span class="calc-step-num">&#9432;</span>
    <div>
      <div class="calc-step-label">eCPM - Effective Cost Per Mille (publisher metric)</div>
      <div class="calc-step-formula">What a publisher earns per 1,000 ad impressions, regardless of the pricing model used to buy the space - CPM, CPC, or CPA.</div>
    </div>
  </div>
  <div class="calc-example-result">
    <strong>The golden rule:</strong> CPM tells the advertiser what it cost to buy exposure. eCPM tells the publisher how effectively their inventory turned impressions into revenue.
  </div>
</div>

<h2>What is CPM?</h2>
<p>CPM stands for Cost Per Mille, where mille is Latin for one thousand. It is the standard rate an advertiser pays for 1,000 ad impressions. For a full breakdown of the metric, see our <a href="/guides/what-is-cpm">CPM guide</a>.</p>

<div class="formula-block">
  <div class="formula-label">CPM formula</div>
  <div class="formula-main">CPM = (Total Advertising Cost &divide; Total Impressions) &times; 1,000</div>
</div>

<p>Display banner ads typically range from EUR 1 to EUR 4 CPM, while premium video placements and hyper-targeted search inventory command significantly higher rates due to user intent and engagement. Use the <a href="/cpm-calculator">CPM calculator</a> to calculate your cost, impressions, or CPM from any two values.</p>

<h2>What is eCPM?</h2>
<p>eCPM stands for Effective Cost Per Mille. For publishers - website owners, app developers, newsletter operators - it is the primary metric for understanding how well their ad inventory is monetising. Publishers often run hybrid ad models where some placements are sold on a CPC basis (pay per click), others on a CPA basis (pay per action), and others at a flat CPM rate. eCPM normalises all of those different revenue streams into a single number: how much did we earn for every 1,000 ads we served?</p>

<div class="formula-block">
  <div class="formula-label">eCPM formula</div>
  <div class="formula-main">eCPM = (Total Ad Revenue &divide; Total Impressions) &times; 1,000</div>
</div>

<h3>Step-by-step eCPM calculation example</h3>
<p>A mobile app publisher runs a mix of native ads and rewarded video ads over a weekend.</p>

<div class="calc-example">
  <div class="calc-example-step">
    <span class="calc-step-num">1</span>
    <div>
      <div class="calc-step-label">Total impressions served</div>
      <div class="calc-step-formula">500,000 impressions across all ad formats</div>
    </div>
  </div>
  <div class="calc-example-step">
    <span class="calc-step-num">2</span>
    <div>
      <div class="calc-step-label">Total revenue earned</div>
      <div class="calc-step-formula">EUR 2,500 across all clicks and video completions</div>
    </div>
  </div>
  <div class="calc-example-step">
    <span class="calc-step-num">3</span>
    <div>
      <div class="calc-step-label">Apply the eCPM formula</div>
      <div class="calc-step-formula">(EUR 2,500 &divide; 500,000) &times; 1,000 = <strong>EUR 5.00</strong></div>
    </div>
  </div>
  <div class="calc-example-result">
    The publisher's eCPM is <strong>EUR 5.00</strong> - regardless of how the individual ads were priced, the inventory yielded an effective rate of EUR 5.00 per thousand impressions.
  </div>
</div>

""" + AD_INLINE + """

<h2>eCPM vs CPM: direct comparison</h2>

<div style="overflow-x:auto;margin:24px 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.875rem;">
  <thead>
    <tr style="border-bottom:2px solid var(--border);">
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">Feature</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">CPM</th>
      <th style="text-align:left;padding:10px 12px;color:var(--text-muted);font-weight:600;">eCPM</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;color:var(--text-muted);font-weight:600;">Primary user</td>
      <td style="padding:10px 12px;color:var(--text);">Advertisers and media buyers</td>
      <td style="padding:10px 12px;color:var(--text);">Publishers, app developers, webmasters</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;color:var(--text-muted);font-weight:600;">Core objective</td>
      <td style="padding:10px 12px;color:var(--text);">Track and reduce campaign spend</td>
      <td style="padding:10px 12px;color:var(--text);">Measure and maximise ad inventory yield</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(45,63,94,0.5);">
      <td style="padding:10px 12px;color:var(--text-muted);font-weight:600;">Value</td>
      <td style="padding:10px 12px;color:var(--text);">Fixed by contract or auction bid</td>
      <td style="padding:10px 12px;color:var(--text);">Fluctuates based on user engagement and ad type</td>
    </tr>
    <tr>
      <td style="padding:10px 12px;color:var(--text-muted);font-weight:600;">Optimisation goal</td>
      <td style="padding:10px 12px;color:var(--accent);font-weight:600;">Lower is better</td>
      <td style="padding:10px 12px;color:var(--accent);font-weight:600;">Higher is better</td>
    </tr>
  </tbody>
</table>
</div>

<h2>How to optimise both sides</h2>
<p>Because high revenue for a publisher equals high cost for an advertiser, both parties need to optimise their setups independently to reach a profitable middle ground.</p>

<h3>For advertisers: how to lower your CPM</h3>
<p><strong>Refine audience targeting.</strong> Narrower audiences reduce wasted impressions, but very narrow targeting also increases CPM because you are competing with more advertisers for the same inventory. Find the balance between relevance and reach that keeps your <a href="/ctr-calculator">CTR</a> high without driving CPM up.</p>
<p><strong>Improve ad creative quality.</strong> Platforms like Google and Meta reward highly engaging ads with better auction positions and lower baseline CPM rates. Higher <a href="/ctr-calculator">CTR</a> signals relevance, which reduces the bid required to win impressions.</p>
<p><strong>Test ad formats.</strong> Social media feed placements and display networks typically offer more competitive CPMs than standalone video placements. Run format tests to find which placement type delivers the best cost-to-reach ratio for your objective.</p>

<h3>For publishers: how to increase your eCPM</h3>
<p><strong>Use high-value ad formats.</strong> Programmatic video ads and mobile rewarded video typically deliver eCPMs of EUR 10 to EUR 50 or more, compared to EUR 1 to EUR 4 for standard display banners. Shifting inventory mix toward video or native formats is the fastest way to increase eCPM.</p>
<p><strong>Set eCPM floors.</strong> Use an ad server like Google Ad Manager to set minimum pricing tiers that prevent ad networks from buying premium placements at remnant rates. A well-calibrated floor price ensures your highest-value inventory is not undersold.</p>
<p><strong>Improve page performance.</strong> Faster page load speeds and non-intrusive ad placements increase viewability and user engagement, which raises <a href="/ctr-calculator">CTR</a> on performance-priced placements and lifts overall eCPM across the board.</p>

""" + AFFILIATES['supermetrics']()

CPM_VS_ECPM_FAQ = [
    ("What is the difference between CPM and eCPM?",
     "CPM is what an advertiser pays per 1,000 impressions - it is the buying cost. eCPM is what a publisher earns per 1,000 impressions - it is the yield metric. Both use the same calculation (cost or revenue divided by impressions, multiplied by 1,000), but they measure opposite sides of the same transaction."),
    ("Does a high CPM automatically mean a high eCPM?",
     "Not necessarily. A premium ad placement might cost an advertiser a high CPM, but if user engagement on the publisher's page is low and performance-priced ads are not generating clicks or actions, the publisher's total revenue will be lower than expected, resulting in a lower eCPM. eCPM depends on both the rate paid and the engagement generated."),
    ("Why should publishers track eCPM instead of just total revenue?",
     "Total revenue only tells you how much money you made - not how efficiently your inventory generated it. eCPM allows publishers to compare ad networks, placements, and formats on equal footing regardless of traffic volume. A placement generating EUR 200 from 50,000 impressions (EUR 4.00 eCPM) outperforms one generating EUR 300 from 200,000 impressions (EUR 1.50 eCPM) on a per-impression basis."),
    ("Can audience targeting influence eCPM?",
     "Yes, significantly. When publishers attract a niche, high-intent audience - such as a blog focused entirely on enterprise software or B2B finance - advertisers bid more to reach those users, which drives eCPM upward. Audience quality is one of the most powerful levers for increasing publisher eCPM."),
    ("How is eCPM different from RPM?",
     "eCPM and RPM (Revenue Per Mille) are often used interchangeably, but there is a subtle difference. eCPM is calculated based on ad impressions - it measures revenue per 1,000 ad views. RPM in platforms like Google AdSense is typically calculated based on page views or sessions, not ad impressions. On a page with multiple ad units, RPM will be lower than eCPM because RPM divides by total page views, not by individual ad impressions."),
    ("What is a good eCPM for a website?",
     "A good eCPM depends heavily on niche, geography, and ad format. Display banner eCPMs typically range from EUR 1 to EUR 5 for general content. Technology, finance, and B2B niches often command EUR 8 to EUR 20. Video and native formats range from EUR 10 to EUR 50 or more. Tier-1 markets like the US, UK, and Australia typically deliver 3 to 5 times higher eCPMs than Tier-3 markets for the same content."),
]
