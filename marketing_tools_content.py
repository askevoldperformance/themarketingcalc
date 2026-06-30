"""
Marketing Tools hub page and the Free Keyword Tools sub-page.
"""

from build_helpers import AD_SIDEBAR_L, AD_SIDEBAR_R, AD_INLINE, faq, AFFILIATES

# ── HUB PAGE: /marketing-tools ──────────────────────────────────────────────

MARKETING_TOOLS_BODY = '''
<main>
  <section class="page-hero"><div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="bc-sep">/</span><span class="bc-current">Marketing Tools</span>
    </nav>
    <h1>Free <span class="accent">Marketing Tools</span></h1>
    <p class="hero-sub">Beyond calculators - practical free tools for the day-to-day work of running paid media and SEO campaigns. Built for marketers, no sign-up required.</p>
  </div></section>

  <section class="tools-hub-section"><div class="container">
    <p class="tools-hub-intro">Every tool below is free to use directly in your browser. No account, no email gate, no usage limits. If you have a tool you wish existed, we are actively expanding this list - check back regularly or browse our <a href="/">marketing calculators</a> for metric-based planning tools.</p>

    <div class="tool-category-grid">
      <a href="/marketing-tools/free-keyword-tools" class="tool-category-card">
        <span class="tool-category-tag">PPC &amp; SEO</span>
        <h2>Free Keyword Tools</h2>
        <p>Format keyword lists into Google Ads and Microsoft Ads match types, or combine word lists into hundreds of long-tail keyword combinations in seconds.</p>
        <span class="tool-category-link">Open tools &rarr;</span>
      </a>
    </div>
  </div></section>
</main>'''


# ── KEYWORD TOOLS PAGE: /marketing-tools/free-keyword-tools ────────────────

KEYWORD_MATCH_TYPE_TOOL_HTML = '''
<div class="kw-tool-card" id="match-type-tool">
  <div class="kw-tool-header">
    <h2>Keyword Match Type Tool</h2>
    <p class="kw-tool-desc">Paste a list of keywords and instantly format them into Broad, Phrase, and Exact match for Google Ads and Microsoft Ads.</p>
  </div>
  <div class="kw-tool-grid">
    <div class="kw-input-col">
      <label>Your keywords <span class="input-hint">one per line</span></label>
      <textarea id="mt-input" rows="10" placeholder="marketing budget calculator&#10;cpm calculator&#10;roas calculator"></textarea>
      <div class="kw-options-row">
        <label class="kw-check"><input type="checkbox" id="mt-broad" checked> Broad Match</label>
        <label class="kw-check"><input type="checkbox" id="mt-phrase" checked> Phrase Match</label>
        <label class="kw-check"><input type="checkbox" id="mt-exact" checked> Exact Match</label>
      </div>
      <div class="kw-options-row">
        <label class="kw-check"><input type="checkbox" id="mt-lowercase"> Transform to lowercase</label>
        <label class="kw-check"><input type="checkbox" id="mt-dedupe"> Remove duplicates</label>
      </div>
    </div>
    <div class="kw-output-col">
      <label>Result <span id="mt-count" class="kw-count"></span></label>
      <textarea id="mt-output" rows="10" readonly placeholder="Your formatted keywords will appear here"></textarea>
      <button class="btn-secondary kw-copy-btn" onclick="copyKwOutput('mt-output')">Copy to clipboard</button>
    </div>
  </div>
</div>'''

KEYWORD_COMBINER_TOOL_HTML = '''
<div class="kw-tool-card" id="combiner-tool">
  <div class="kw-tool-header">
    <h2>Keyword Combiner Tool</h2>
    <p class="kw-tool-desc">Combine two or three word lists to generate every possible keyword combination. Useful for building long-tail keyword lists for Phrase and Exact match campaigns.</p>
  </div>
  <div class="kw-combiner-lists">
    <div class="kw-list-col">
      <label>List 1</label>
      <textarea id="cb-list1" rows="6" placeholder="cheap&#10;best&#10;free"></textarea>
    </div>
    <div class="kw-list-col">
      <label>List 2</label>
      <textarea id="cb-list2" rows="6" placeholder="marketing&#10;budget&#10;keyword"></textarea>
    </div>
    <div class="kw-list-col">
      <label>List 3 <span class="input-hint">optional</span></label>
      <textarea id="cb-list3" rows="6" placeholder="tool&#10;calculator&#10;software"></textarea>
    </div>
  </div>
  <div class="kw-options-row">
    <label>Separator</label>
    <div class="kw-separator-toggle">
      <button class="sep-btn active" data-sep="space">Space</button>
      <button class="sep-btn" data-sep="none">No separator</button>
      <button class="sep-btn" data-sep="dash">Dash</button>
    </div>
  </div>
  <div class="kw-options-row">
    <label class="kw-check"><input type="checkbox" id="cb-lowercase"> Transform to lowercase</label>
    <label class="kw-check"><input type="checkbox" id="cb-dedupe"> Remove duplicates</label>
  </div>
  <div class="kw-output-col" style="margin-top:4px;">
    <label>Result <span id="cb-count" class="kw-count"></span></label>
    <textarea id="cb-output" rows="10" readonly placeholder="Your combined keywords will appear here"></textarea>
    <button class="btn-secondary kw-copy-btn" onclick="copyKwOutput('cb-output')">Copy to clipboard</button>
  </div>
</div>'''


KEYWORD_TOOLS_EDITORIAL_TOP = '''
<h2>Google Ads and Microsoft Ads match types</h2>
<p><strong>Broad Match</strong> reaches the widest range of related searches and works best with Smart Bidding. <strong>Phrase Match</strong> - wrapped in quotes - matches your phrase plus extra words around it. <strong>Exact Match</strong> - wrapped in brackets - is the most precise and the lowest-waste option. The broad match modifier was retired in 2021 and is no longer a distinct match type on either platform.</p>
'''

KEYWORD_TOOLS_EDITORIAL_MIDDLE = '''
<h2>What the keyword combiner is for</h2>
<p>Cross-multiply two or three word lists into every possible combination - useful for building long-tail keyword lists, ad group structures, or content ideas in seconds instead of typing variations by hand.</p>
'''

KEYWORD_TOOLS_FAQ_ITEMS = [
    ("What is the difference between broad, phrase, and exact match keywords?",
     "Broad match has the widest reach and can trigger ads for related searches and synonyms. Phrase match requires the search to include your exact phrase or a close variation, with extra words allowed around it. Exact match is the most restrictive, matching only the exact term or very close variations like plurals and minor misspellings."),
    ("Is the broad match modifier still supported?",
     "No. Google Ads retired the broad match modifier in 2021, and entering a broad match modifier keyword (with a plus sign) is now treated as Phrase Match by Google and as standard Broad Match by Microsoft Ads. This is why the tool above only offers Broad, Phrase, and Exact - the modifier is no longer a distinct match type on either platform."),
    ("How do I format a large keyword list for Google Ads?",
     "Paste your full list into the Keyword Match Type Tool above, select the match types you need, and click Generate. The tool instantly adds the correct quotation marks or brackets to every keyword in your list, which you can then copy directly into Google Ads Editor or the Google Ads web interface."),
    ("Can I combine multiple keyword lists into one?",
     "Yes - use the Keyword Combiner Tool above. Enter your word lists into two or three separate boxes and the tool generates every possible combination across all of them, which you can format with a space, dash, or no separator between words."),
    ("Which match type should I use for a new campaign with no conversion data?",
     "Phrase Match is generally the safer starting point for new campaigns, since it balances reach with relevance while Smart Bidding builds up conversion data. Once you have 30 or more conversions per month in a campaign, Broad Match paired with Target CPA or Target ROAS often becomes more effective."),
    ("Are these keyword tools free to use?",
     "Yes, both the Keyword Match Type Tool and the Keyword Combiner Tool above are completely free with no sign-up, no usage limits, and no data stored. Paste your keywords, generate your output, and copy the result directly."),
]

KEYWORD_TOOLS_FAQ = faq(KEYWORD_TOOLS_FAQ_ITEMS)

KEYWORD_TOOLS_AFFILIATE = AFFILIATES['ahrefs']()

KEYWORD_TOOLS_BODY = f'''
<main>
  <section class="page-hero"><div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="bc-sep">/</span><a href="/marketing-tools">Marketing Tools</a><span class="bc-sep">/</span><span class="bc-current">Free Keyword Tools</span>
    </nav>
    <h1>Free <span class="accent">Keyword Tools</span></h1>
    <p class="hero-sub">Format keyword match types and generate keyword combinations for Google Ads and Microsoft Ads campaigns - free, instant, no sign-up.</p>
  </div></section>

  <section class="calc-content"><div class="container">
    <div class="page-with-sidebar">
      {AD_SIDEBAR_L}
      <div class="main-col prose">
        {KEYWORD_MATCH_TYPE_TOOL_HTML}
        {KEYWORD_TOOLS_EDITORIAL_TOP}
        {KEYWORD_COMBINER_TOOL_HTML}
        {KEYWORD_TOOLS_EDITORIAL_MIDDLE}
        {KEYWORD_TOOLS_AFFILIATE}
        {KEYWORD_TOOLS_FAQ}
      </div>
      {AD_SIDEBAR_R}
    </div>
  </div></section>
</main>'''
