# Shared helpers: ad placements, affiliate boxes, FAQ builder

AD_LEADERBOARD = '<div class="ad-leaderboard" aria-hidden="true"></div>'
AD_INLINE      = '<div class="ad-inline" aria-hidden="true"></div>'
AD_SIDEBAR_L   = '<div class="sidebar-left"><div class="ad-sidebar" aria-hidden="true"></div></div>'
AD_SIDEBAR_R   = '<div class="sidebar-right"><div class="ad-sidebar" aria-hidden="true"></div></div>'


def affiliate(icon, label, title, desc, cta_text, cta_url):
    return f'''
<div class="affiliate-box">
  <div class="aff-icon">{icon}</div>
  <div class="aff-body">
    <div class="aff-label">{label}</div>
    <div class="aff-title">{title}</div>
    <p class="aff-desc">{desc}</p>
    <a href="{cta_url}" class="aff-cta" rel="noopener sponsored" target="_blank">{cta_text}</a>
    <p class="affiliate-disclaimer">Affiliate link - we may earn a commission at no extra cost to you.</p>
  </div>
</div>'''


def faq(items):
    html = '<div class="faq-section"><h2>Frequently asked questions</h2>'
    for q, a in items:
        html += f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a">{a}</div></div>'
    html += '</div>'
    return html


AFFILIATES = {
    'semrush': lambda: affiliate(
        '📊', 'Sponsored tool',
        'Track your rankings with SEMrush',
        'The industry standard for SEO and PPC research. See exactly what your competitors are spending and which keywords drive their traffic.',
        'Try SEMrush free', 'https://www.semrush.com'
    ),
    'ahrefs': lambda: affiliate(
        '🔍', 'Sponsored tool',
        'Keyword research with Ahrefs',
        'Find the search terms your audience uses before they click an ad. Ahrefs gives you search volume, difficulty, and click data across every channel.',
        'Try Ahrefs', 'https://www.ahrefs.com'
    ),
    'triple_whale': lambda: affiliate(
        '🐋', 'Sponsored tool',
        'Fix your ROAS attribution with Triple Whale',
        'iOS privacy changes broke last-click attribution. Triple Whale rebuilds your true ROAS picture using first-party pixel data and MMM modeling.',
        'Try Triple Whale', 'https://www.triplewhale.com'
    ),
    'supermetrics': lambda: affiliate(
        '📈', 'Sponsored tool',
        'Pull all your ad data into one place with Supermetrics',
        'Connect Meta, Google Ads, LinkedIn and more to Google Sheets, Looker Studio, or BigQuery. Stop copying numbers manually.',
        'Try Supermetrics free', 'https://www.supermetrics.com'
    ),
    'hubspot': lambda: affiliate(
        '🧲', 'Sponsored tool',
        'Turn leads into customers with HubSpot',
        'Free CRM with built-in lead tracking, email sequences, and pipeline management. The natural next step after calculating your CPL target.',
        'Try HubSpot free', 'https://www.hubspot.com'
    ),
    'whatagraph': lambda: affiliate(
        '📋', 'Sponsored tool',
        'Client reporting made easy with Whatagraph',
        'Build automated marketing reports that pull from all your ad channels. Stop spending Mondays in spreadsheets.',
        'Try Whatagraph', 'https://www.whatagraph.com'
    ),
}
