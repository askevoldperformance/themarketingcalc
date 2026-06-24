"""
Page content: editorial text + FAQ per calculator.
Imported by build.py.
"""
from build_helpers import affiliate, faq, AD_INLINE, AFFILIATES

# ── CPM ───────────────────────────────────────────────────────────────────────

CPM_EDITORIAL = '''
<h2>What is CPM?</h2>
<p>CPM (Cost Per Mille) is the price an advertiser pays for 1,000 impressions of an ad. "Mille" is Latin for thousand. It is the standard pricing unit for display advertising, social media reach campaigns, video ads, and programmatic media buying.</p>
<p>CPM is used whenever the primary goal is visibility rather than clicks or conversions. Brand awareness campaigns, video view campaigns, and reach-optimised social campaigns all use CPM as the core efficiency metric.</p>

<h2>The CPM formula</h2>
<p>CPM = (Total Cost / Impressions) x 1,000. If you spend $500 and receive 200,000 impressions, your CPM is $2.50. The formula works in all three directions - given any two values you can calculate the third. Use the calculator above to solve for CPM, total cost, or number of impressions.</p>

<h2>CPM benchmarks by channel (2024-2025)</h2>
<p>CPM varies significantly by platform, audience quality, and creative format. As reference points: Meta Ads typically range from $6 to $14 for feed placements, Google Display from $2 to $5, LinkedIn from $30 to $80 due to the professional audience premium, and TikTok from $8 to $15. Niche B2B audiences and retargeting segments will always command higher CPMs than broad prospecting audiences at the top of the funnel.</p>
<p>These are averages. The only CPM that matters for budget planning is your own historical data. If you are planning a new campaign with no prior data, use the conservative end of the benchmark range to avoid overestimating reach.</p>

<h2>What affects CPM?</h2>
<p>Auction competition is the primary driver. Small, high-value audiences - senior decision-makers, retargeting lists, lookalikes of recent purchasers - attract more advertiser competition and therefore higher CPMs. Seasonal demand spikes in Q4 and peak retail periods push CPMs across all platforms. Creative quality scores on Meta and relevance scores on Google affect how aggressively the algorithm delivers your ads, which in turn affects effective CPM. Placement also matters significantly - Stories, Reels, and in-feed placements all carry different CPM floors.</p>
''' + AD_INLINE + AFFILIATES['semrush']() + '''

<h2>CPM vs eCPM</h2>
<p>CPM is the rate you pay. eCPM (effective CPM) is calculated retroactively from actual spend and impressions regardless of how the media was bought - CPC, CPA, or CPM. eCPM = (Total Cost / Impressions) x 1,000. It is useful for comparing campaign efficiency across different buying models. See our <a href="/guides/cpm-vs-ecpm">CPM vs eCPM guide</a> for a full breakdown.</p>
'''

CPM_FAQ = faq([
    ("How many impressions will I get for my budget?",
     "Impressions = (Budget / CPM) x 1,000. With a $1,000 budget and a $10 CPM, you can expect 100,000 impressions. Use the 'Find Impressions' mode in the calculator above."),
    ("What does it cost to reach 1 million people?",
     "At a $10 CPM: $10,000. At a $5 CPM: $5,000. Cost = (Impressions / 1,000) x CPM. Note that 1 million impressions and 1 million unique people are different - frequency determines how many unique people you actually reach."),
    ("Why is my CPM increasing?",
     "The most common causes are audience saturation (your audience has seen the ad too many times), rising auction competition, seasonal demand spikes, declining creative relevance scores, or reducing your audience size mid-campaign. Refreshing creative and broadening targeting are the first things to try."),
    ("Does a lower CPM always mean a better result?",
     "No. A very low CPM usually means a broad, lower-quality audience. Always evaluate CPM alongside CTR and conversion rate. A $20 CPM with strong CTR can outperform a $4 CPM with negligible engagement if your goal is traffic or sales."),
    ("How do I calculate CPM from a CPC campaign?",
     "eCPM = CPC x CTR x 10. If your CPC is $0.50 and your CTR is 1%, your eCPM is $5. This lets you compare CPC and CPM buys on equal footing."),
    ("What is a good CPM for Facebook ads?",
     "For cold prospecting audiences in most markets, $6 to $14 is typical. Retargeting and high-intent audiences run $15 to $30+. Broad reach campaigns for video views can be lower, around $3 to $8, depending on the market."),
    ("How does audience size affect CPM?",
     "Smaller audiences have higher CPMs because more advertisers compete for fewer impressions. A retargeting list of 10,000 people will almost always cost more per thousand impressions than a broad prospecting audience of 2 million."),
])

# ── CTR ───────────────────────────────────────────────────────────────────────

CTR_EDITORIAL = '''
<h2>What is CTR?</h2>
<p>CTR (Click-Through Rate) is the percentage of people who clicked your ad after seeing it. It is one of the most direct signals of creative and audience relevance - when the right message reaches the right person, they click.</p>
<p>CTR is calculated as: CTR = (Clicks / Impressions) x 100. If 300 people clicked from 20,000 impressions, your CTR is 1.5%. Use the calculator above to solve for CTR, total clicks, or impressions from any two values.</p>

<h2>CTR benchmarks by channel</h2>
<p>CTR varies enormously by channel because the context and user intent is completely different. Google Search sees the highest CTRs of any format - 3% to 6% is typical across industries because ads appear in direct response to an active search query. Google Display drops to 0.1% to 0.3% because display ads interrupt rather than respond. Meta feed ads range from 0.5% to 1.5% for cold audiences, with retargeting often reaching 2% to 4%. LinkedIn typically runs 0.3% to 0.7% due to the professional, task-focused context. TikTok ranges from 0.5% to 1.2% depending on creative format.</p>

<h2>Why CTR matters beyond the click</h2>
<p>On Meta and Google, CTR directly affects your quality score or relevance score. A higher CTR signals that your ad is resonating with its audience, which rewards you with better auction placement and lower CPCs. This means improving creative is not just about more clicks - it makes every click cheaper. CTR is also the bridge between CPM and CPC: CPC = CPM / (CTR x 10). Doubling your CTR at the same CPM halves your effective CPC.</p>
''' + AD_INLINE + AFFILIATES['ahrefs']() + '''

<h2>How to improve CTR</h2>
<p>The single biggest lever for social ads is the first second of video or first frame of an image. On a fast-scroll feed, you have roughly 0.3 seconds to stop someone. Strong contrasts, direct eye contact in creative, motion, and text overlays with immediate value propositions all help. For search ads, headline relevance to the exact query is the primary driver - match your headline as closely as possible to the keyword intent. Negative keywords reduce wasted impressions that would never click, artificially improving CTR.</p>
'''

CTR_FAQ = faq([
    ("How do I calculate how many clicks I will get?",
     "Clicks = (CTR / 100) x Impressions. With 500,000 impressions and a 1% CTR, you get 5,000 clicks. Use the 'Find Clicks' mode in the calculator above."),
    ("What CTR is considered good for Meta ads?",
     "For cold prospecting on Meta, 0.5% to 1.5% is a healthy range. Retargeting typically sees 1.5% to 3%. Below 0.5% on a cold audience suggests a creative or audience relevance issue worth investigating."),
    ("Does a high CTR mean a successful campaign?",
     "Not on its own. CTR measures interest, not outcomes. Always pair it with post-click conversion rate and cost per acquisition. A 5% CTR with a 0.1% conversion rate is often worse than a 0.5% CTR with a 3% conversion rate."),
    ("How does CTR affect my costs on Google and Meta?",
     "Higher CTR improves your quality score (Google) or relevance score (Meta), which reduces the CPM or CPC the platform charges you. It is one of the compounding advantages of strong creative - you pay less for every result."),
    ("What is the relationship between CTR, CPM, and CPC?",
     "CPC = CPM / (CTR x 10). If your CPM is $10 and your CTR is 1%, your CPC is $1. If CTR drops to 0.5%, your effective CPC doubles to $2. This formula shows why creative quality has a direct impact on campaign economics."),
    ("Why is my CTR dropping over time?",
     "Ad fatigue. The same audience has seen the same creative too many times. Refresh your creative assets - new imagery, new first frame, new headline. You do not necessarily need a new audience."),
    ("How do I use CTR to forecast campaign performance?",
     "Impressions x CTR = Clicks. Clicks x Conversion Rate = Conversions. This simple chain is the foundation of any campaign forecast. Start with your budget and expected CPM to get impressions, apply CTR to get clicks, then apply your landing page conversion rate to get conversions."),
])

# ── CPC ───────────────────────────────────────────────────────────────────────

CPC_EDITORIAL = '''
<h2>What is CPC?</h2>
<p>CPC (Cost Per Click) is the amount you pay each time someone clicks your ad. It is the primary efficiency metric for traffic and conversion campaigns where you want to pay only for engaged users rather than for impressions.</p>
<p>CPC = Total Cost / Clicks. If you spend $400 and receive 800 clicks, your CPC is $0.50. The calculator above solves for CPC, total cost, or number of clicks - enter any two values to find the third.</p>

<h2>CPC benchmarks by channel</h2>
<p>Google Search CPC varies more than any other metric because it is driven entirely by keyword competition. Legal, finance, and insurance keywords can exceed $50 per click. E-commerce and retail typically sees $0.50 to $3. B2B software ranges from $3 to $15. Meta Ads delivers lower CPC, typically $0.30 to $1.50 for e-commerce, because the auction includes a wider range of objectives and placements. LinkedIn is significantly higher at $5 to $15 due to the professional audience. TikTok ranges from $0.20 to $0.80.</p>

<h2>What determines your maximum CPC?</h2>
<p>Your maximum sustainable CPC is set by your business economics, not by what the platform charges. The formula is: Max CPC = (Average Order Value x Conversion Rate) / Target ROAS. If your AOV is $100, your site converts at 2%, and you need a 3x ROAS, your max CPC is ($100 x 0.02) / 3 = $0.67. Bidding above this means you are paying more per click than your margin supports - even if the traffic looks good in the platform dashboard.</p>
''' + AD_INLINE + AFFILIATES['supermetrics']() + '''

<h2>CPC and creative quality</h2>
<p>CPC is not only determined by what you bid. On both Meta and Google, your quality or relevance score directly affects the actual CPC charged. A well-performing creative with strong CTR earns better auction positions and lower costs. The formula connecting CPM, CTR, and CPC is: CPC = CPM / (CTR x 10). A creative that doubles your CTR effectively halves your CPC at the same CPM - the most efficient way to reduce spend without reducing results.</p>
'''

CPC_FAQ = faq([
    ("How do I calculate how many clicks I can get from my budget?",
     "Clicks = Budget / CPC. With a $1,000 budget and a $2 CPC, you get 500 clicks. Use the 'Find Clicks' mode in the calculator above."),
    ("What is the maximum CPC I should bid?",
     "Max CPC = (AOV x Conversion Rate) / Target ROAS. Example: AOV $100, conversion rate 2%, target ROAS 3x. Max CPC = ($100 x 0.02) / 3 = $0.67. Bidding above this makes it mathematically impossible to hit your ROAS target."),
    ("Why is my CPC increasing?",
     "Common causes: rising auction competition, declining CTR from creative fatigue (which raises effective CPC even without a bid change), seasonal demand spikes, audience narrowing mid-campaign, or lower quality scores from a stale landing page."),
    ("Should I use CPC or CPM bidding?",
     "CPC makes sense when you want to pay only for clicks and your goal is traffic or conversions. CPM is better for reach and awareness where you want maximum exposure. Most modern platform algorithms handle this automatically when you set your campaign objective - manual CPC vs CPM is less relevant than it was, but understanding both helps you audit performance."),
    ("How do I reduce my CPC?",
     "Four main levers: improve creative CTR (higher CTR = lower effective CPC), broaden targeting to reduce auction competition, improve landing page quality score, and run outside peak demand windows. Testing new creative is usually the fastest win."),
    ("What is the relationship between CPC, CPM, and CTR?",
     "CPC = CPM / (CTR x 10). This means your CPC is directly set by how much you pay per impression and how often people click. Improving CTR is the most efficient way to reduce CPC without cutting bids."),
])

# ── ROAS ──────────────────────────────────────────────────────────────────────

ROAS_EDITORIAL = '''
<h2>What is ROAS?</h2>
<p>ROAS (Return on Ad Spend) measures how much revenue you generate for every dollar spent on advertising. ROAS = Revenue / Ad Spend. Spending $2,000 and generating $10,000 in revenue gives a ROAS of 5x. It is the primary performance benchmark for e-commerce campaigns on Meta, Google Ads, and most paid channels.</p>

<h2>What is POAS - and why it matters more</h2>
<p>POAS (Profit on Ad Spend) uses gross profit instead of revenue: POAS = Gross Profit / Ad Spend. If your $10,000 revenue has a 40% gross margin, gross profit is $4,000. With $2,000 ad spend, POAS is 2x. ROAS shows 5x on the same campaign - which looks far better, but conceals the actual profitability.</p>
<p>The practical difference becomes critical when margins vary across products. A ROAS of 4x on a 20% margin product is losing money. The same ROAS on a 60% margin product is highly profitable. ROAS cannot distinguish between these cases. POAS can, because it bakes margin into the metric.</p>

<h2>What is break-even ROAS?</h2>
<p>Break-even ROAS is the minimum return needed for a campaign to cover its costs - the floor below which you are losing money on every sale. Break-even ROAS = AOV / (AOV - COGS - Other Variable Costs). If your average order value is $100, COGS is $40, and shipping costs $10, your margin is $50 and your break-even ROAS is 100/50 = 2x. Every campaign you run should have this number clearly defined before you set targets.</p>
''' + AD_INLINE + AFFILIATES['triple_whale']() + '''

<h2>Setting ROAS targets in Meta and Google Ads</h2>
<p>Meta calls it Minimum ROAS in Advantage+ setups. Google Ads calls it Target ROAS (tROAS). Both work by instructing the platform algorithm to bid aggressively on users predicted to meet your return target and avoid users predicted to fall below it. Setting the target too high causes under-delivery as the algorithm becomes too selective. Set your target above break-even with enough headroom - typically 20% to 30% - for the algorithm to find volume while staying profitable.</p>

<h2>How to implement POAS in your ad accounts</h2>
<p>Pass gross profit as your conversion value instead of order value. In Google Ads, this is done via a dynamic conversion value in your checkout or through the Enhanced Conversions API. In Meta, use the Conversions API to send a custom revenue value equal to gross profit per order. Once profit is your conversion value, set your target ROAS to 1x - because POAS break-even is always exactly 1, regardless of product or price point. This makes POAS targets universal across your catalogue.</p>
'''

ROAS_FAQ = faq([
    ("What is a good ROAS?",
     "There is no universal answer. The only ROAS that matters is your break-even ROAS, which depends entirely on your gross margin. A 60% margin business can be profitable at ROAS 2x. A 15% margin business needs ROAS 8x just to break even. Use the Break-even ROAS tab in the calculator above to find your specific floor before setting any target."),
    ("What is the difference between ROAS and ROI?",
     "ROAS measures revenue relative to ad spend only. ROI measures profit relative to all costs - COGS, operations, and overhead - not just ad spend. ROAS is useful for comparing campaign efficiency. ROI tells you whether the whole business activity is profitable. POAS bridges the gap by factoring margins into the ad-spend calculation."),
    ("How does iOS affect ROAS reporting?",
     "iOS 14+ privacy changes limited Meta's ability to track conversions from iPhone users. Reported ROAS figures are typically understated by 20% to 40% compared to pre-iOS reality. Data-driven attribution, Conversions API, and aggregated event measurement all help close the gap. This is another reason POAS is gaining adoption - it focuses on actual profit outcomes rather than attributed revenue that may be incomplete."),
    ("Why is my ROAS dropping?",
     "Common causes: audience saturation (CPMs rising, reach shrinking), creative fatigue, increased competition in your auction, seasonal shifts in conversion rate, or attribution gaps from iOS changes. Audit in order: check frequency and CPM trends first, then creative performance, then post-click conversion rate."),
    ("What is break-even POAS?",
     "Break-even POAS is always 1x, regardless of product price or margin. This is the main advantage of POAS over ROAS as a target metric - your target is universal across all products and campaigns. ROAS 3x might be profitable for one SKU and catastrophically unprofitable for another. POAS 1x is always the floor."),
    ("How do I calculate break-even ROAS?",
     "Break-even ROAS = AOV / (AOV - COGS - Variable Costs). Example: AOV $100, COGS $35, shipping $10. Margin = $55. Break-even ROAS = 100/55 = 1.82x. Use the Break-even ROAS tab above to calculate this instantly."),
    ("Should I optimise for ROAS or POAS?",
     "POAS, if you can implement it. ROAS is easier to set up but rewards high-revenue, low-margin products. POAS aligns your ad spend with actual profitability. If all your products have similar margins, ROAS is a reasonable proxy. If margins vary across your catalogue, POAS is more accurate and prevents budget from flowing to unprofitable sales."),
])

# ── CPL ───────────────────────────────────────────────────────────────────────

CPL_EDITORIAL = '''
<h2>What is CPL?</h2>
<p>CPL (Cost Per Lead) is the amount you pay to acquire a single lead - a person who has expressed interest by submitting a form, requesting a callback, signing up for a trial, or taking another qualifying action. CPL = Total Cost / Number of Leads.</p>
<p>CPL is the primary efficiency metric for B2B campaigns, service businesses, and any funnel where the conversion path includes a human sales step before revenue is recognised. Use the calculator above to solve for CPL, total budget, or number of leads.</p>

<h2>What is a good CPL?</h2>
<p>CPL benchmarks are only meaningful relative to the value of a converted customer. Calculate your maximum acceptable CPL as: Max CPL = Average Contract Value x Close Rate x Gross Margin. A B2B SaaS company with a $50,000 ACV and a 20% close rate has a maximum CPL of roughly $2,000 before factoring in margin. A local service business with $500 jobs and a 30% close rate has a maximum of around $50. These numbers should anchor every CPL target you set.</p>
<p>By channel: LinkedIn Lead Gen Forms often see CPL between $50 and $200 for B2B. Meta lead generation runs $5 to $50 depending on industry and form complexity. Google Search lead campaigns range from $20 to $100 for most service categories.</p>

<h2>Lead quantity vs lead quality</h2>
<p>Optimising purely for CPL without tracking lead quality creates a predictable trap: volume goes up, close rates fall, and cost per customer quietly increases. The more complete metric is cost per qualified lead or cost per opportunity. When reporting CPL, always pair it with lead-to-opportunity rate and close rate. A $15 CPL with a 2% close rate is far worse than a $50 CPL with a 15% close rate.</p>
''' + AD_INLINE + AFFILIATES['hubspot']() + '''

<h2>Lead gen forms vs landing pages</h2>
<p>Native lead gen forms - Meta Lead Ads, LinkedIn Lead Gen Forms - produce lower CPL because users never leave the platform. The reduced friction means more submissions at a lower cost. However, lead quality is often lower because the barrier to submit is lower. Landing pages produce fewer but higher-intent leads, because the user actively navigated to a new page and completed a form. The right choice depends on your sales process speed and how quickly you can qualify and follow up on leads.</p>
'''

CPL_FAQ = faq([
    ("How do I calculate how many leads I can get from my budget?",
     "Leads = Budget / CPL. With a $5,000 budget and a target CPL of $40, you can expect approximately 125 leads. Use the 'Find Leads' mode in the calculator above."),
    ("What is the maximum CPL I should target?",
     "Max CPL = Average Contract Value x Close Rate x Gross Margin. If your ACV is $10,000, close rate is 15%, and margin is 60%, your max CPL is $900. This is the ceiling before paid lead generation destroys margin."),
    ("What is the difference between CPL and CPA?",
     "CPL measures cost to acquire a lead - someone who expressed interest. CPA (Cost Per Acquisition) measures cost to acquire a paying customer. CPA = CPL / Close Rate. If your CPL is $40 and you close 20% of leads, your CPA is $200."),
    ("Should I use lead gen forms or landing pages?",
     "Lead gen forms (Meta Lead Ads, LinkedIn) produce lower CPL with lower lead quality. Landing pages produce higher CPL with higher quality. The right answer depends on your close rate and follow-up speed. If your sales team is fast and can qualify quickly, lead gen forms often win on economics. If your qualification is slow, higher-intent landing page leads are usually worth the premium."),
    ("Why is my CPL increasing?",
     "Either CPC is rising (audience competition, creative fatigue, quality score decline) or your landing page conversion rate is dropping (page speed, relevance gap between ad and page, seasonal intent shifts). Diagnose by checking which metric changed first."),
    ("How do I forecast CPL for a new campaign?",
     "Estimate CPL = CPC / Landing Page Conversion Rate. A $2 CPC with a 4% conversion rate gives a $50 CPL. A $2 CPC with a 2% conversion rate gives $100 CPL. Use realistic conversion rate estimates from comparable campaigns."),
])

# ── FREQUENCY ─────────────────────────────────────────────────────────────────

FREQ_EDITORIAL = '''
<h2>What is frequency in advertising?</h2>
<p>Frequency is the average number of times a unique person sees your ad within a given time period. Frequency = Impressions / Reach. A campaign reaching 100,000 unique people with 400,000 impressions has an average frequency of 4.</p>
<p>The calculator above solves for frequency, total impressions, or unique reach - enter any two values to find the third. This is useful both for analysing campaigns in flight and for planning reach targets before launch.</p>

<h2>What is a healthy frequency?</h2>
<p>For cold prospecting on Meta and Instagram, a 7-day frequency of 1.5 to 3 is typically healthy. Above 4 to 5 within a week, ad fatigue begins to manifest as rising CPMs and falling CTR. For retargeting, slightly higher frequency is acceptable - 3 to 6 over a 14-day window - because the audience has prior brand exposure and is closer to a decision. For video awareness campaigns with production-quality creative, 3 to 7 over a 30-day window is manageable before fatigue sets in.</p>

<h2>How reach and frequency trade off</h2>
<p>At a fixed impression volume, reach and frequency move in opposite directions. Broad targeting distributes impressions across many people at low frequency. Narrow targeting concentrates impressions on fewer people at higher frequency. Neither is inherently better - it depends on your objective. Awareness campaigns should maximise reach. Retargeting and consideration campaigns benefit from controlled frequency to reinforce the message without oversaturating.</p>
''' + AD_INLINE + AFFILIATES['whatagraph']() + '''

<h2>Ad fatigue - what it looks like and how to fix it</h2>
<p>Ad fatigue has consistent early warning signs: CPM starts rising while audience size stays flat, CTR declines without changes to targeting, and frequency climbs to 5+ within a 7-day window. The fix is almost always creative refresh rather than audience change. New first frames, new headlines, new formats, or new angles on the same message reset the engagement signal without losing the audience learning the algorithm has built up.</p>
'''

FREQ_FAQ = faq([
    ("How do I calculate total impressions from reach and frequency?",
     "Impressions = Reach x Frequency. To reach 200,000 unique people at a frequency of 5, you need 1,000,000 impressions. Use the 'Find Impressions' mode in the calculator above."),
    ("What is the difference between reach and impressions?",
     "Reach counts unique people. Impressions count total ad views, including multiple views by the same person. A campaign with 500,000 impressions and 200,000 reach has a frequency of 2.5. Reach matters more for awareness campaigns. Impressions matter more for message repetition goals."),
    ("How do I control frequency on Meta?",
     "In Reach and Frequency buying (available to larger accounts), you set a frequency cap directly. In auction buying, you control frequency indirectly through audience size, campaign duration, and budget relative to audience. Longer campaigns with the same budget will naturally produce lower frequency than short burst campaigns."),
    ("What is minimum effective frequency?",
     "Research varies, but 3 to 5 exposures is commonly cited as a baseline for a new brand message to register. For direct response campaigns focused on conversion, even a single high-quality exposure can drive action if the audience-message fit is strong. There is no universal number."),
    ("How does frequency affect CPM?",
     "As frequency rises within a fixed audience, CPM typically increases because the algorithm serves the same people repeatedly rather than finding fresh reach. Rising CPM on a flat audience with rising frequency is the classic saturation pattern."),
    ("Why is my frequency high but reach low?",
     "Your audience is too small relative to your budget and campaign duration. The algorithm has exhausted unique reach and is now recirculating impressions across the same people. Broaden your targeting, increase exclusions to remove converted users, or reduce your daily budget to extend the campaign over a longer period."),
    ("How do I balance reach and frequency for awareness campaigns?",
     "A practical two-stage approach: maximise reach first at frequency 1 to 2 (get the message to as many relevant people as possible), then build frequency selectively with retargeting to reinforce among the most engaged portion of that audience. This is more efficient than trying to achieve both high reach and high frequency in a single campaign structure."),
])
