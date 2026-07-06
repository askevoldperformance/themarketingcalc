from build_helpers import faq, AD_INLINE, AD_SIDEBAR_L, AD_SIDEBAR_R, AFFILIATES

RSA_PREVIEW_TOOL_HTML = '''
<div class="rsa-tool-card" id="rsa-preview-tool">

  <div class="rsa-tool-header">
    <h1>Free RSA Preview Tool</h1>
    <p class="rsa-tool-desc">Enter your headlines and descriptions to see exactly how your Google Responsive Search Ad will look in search results. Randomize combinations, lock positions, and test every variation before going live.</p>
  </div>

  <div class="rsa-tool-body">

    <!-- LEFT: Inputs -->
    <div class="rsa-inputs-col">

      <div class="rsa-section-label">Ad details</div>
      <div class="rsa-field-row">
        <div class="input-group">
          <label>Business name</label>
          <input type="text" id="rsa-brand" placeholder="e.g. Acme Marketing" maxlength="25">
          <span class="rsa-counter" id="count-brand">0/25</span>
        </div>
        <div class="input-group">
          <label>Display URL</label>
          <input type="text" id="rsa-url" placeholder="e.g. acme.com/marketing" maxlength="35">
        </div>
      </div>
      <div class="rsa-field-row">
        <div class="input-group">
          <label>Path 1 <span class="input-hint">optional</span></label>
          <input type="text" id="rsa-path1" placeholder="e.g. services" maxlength="15">
          <span class="rsa-counter" id="count-path1">0/15</span>
        </div>
        <div class="input-group">
          <label>Path 2 <span class="input-hint">optional</span></label>
          <input type="text" id="rsa-path2" placeholder="e.g. free-trial" maxlength="15">
          <span class="rsa-counter" id="count-path2">0/15</span>
        </div>
      </div>

      <div class="rsa-section-label" style="margin-top:20px;">Headlines <span class="rsa-section-hint">up to 15, max 30 chars each</span></div>
      <div id="rsa-headlines-list"></div>
      <button class="rsa-add-btn" onclick="rsaAddHeadline()" id="rsa-add-hl-btn">+ Add headline</button>

      <div class="rsa-section-label" style="margin-top:20px;">Descriptions <span class="rsa-section-hint">up to 4, max 90 chars each</span></div>
      <div id="rsa-descriptions-list"></div>
      <button class="rsa-add-btn" onclick="rsaAddDescription()" id="rsa-add-desc-btn">+ Add description</button>

    </div>

    <!-- RIGHT: Preview -->
    <div class="rsa-preview-col">
      <div class="rsa-section-label">Ad preview</div>
      <div class="rsa-preview-wrapper">
        <div class="rsa-preview-ad" id="rsa-preview">
          <div class="rsa-preview-top">
            <span class="rsa-preview-badge">Sponsored</span>
            <div class="rsa-preview-brand-row">
              <span class="rsa-preview-favicon">&#9632;</span>
              <div>
                <div class="rsa-preview-brand" id="preview-brand">Your Business Name</div>
                <div class="rsa-preview-url" id="preview-url">example.com</div>
              </div>
            </div>
          </div>
          <div class="rsa-preview-headlines" id="preview-headlines">
            <span class="rsa-hl-placeholder">Headline 1</span>
            <span class="rsa-hl-sep"> | </span>
            <span class="rsa-hl-placeholder">Headline 2</span>
            <span class="rsa-hl-sep"> | </span>
            <span class="rsa-hl-placeholder">Headline 3</span>
          </div>
          <div class="rsa-preview-desc" id="preview-desc">
            Your description will appear here. Enter your description text in the fields on the left to see a live preview of your Google Search ad.
          </div>
        </div>
      </div>

      <div class="rsa-combo-controls">
        <button class="calc-btn" onclick="rsaRandomize()">Randomize combination</button>
        <div class="rsa-combo-info" id="rsa-combo-info"></div>
      </div>

      <div class="rsa-lock-info">
        <div class="rsa-section-label" style="margin-top:16px;">Locked positions</div>
        <p style="font-size:0.82rem;color:var(--text-muted);margin:4px 0 12px;">Lock a headline to a specific position (1, 2, or 3) using the pin icon next to each headline input. Locked headlines always appear in that position regardless of randomization.</p>
        <div id="rsa-locked-summary"></div>
      </div>
    </div>

  </div>
</div>
'''

RSA_PREVIEW_EDITORIAL = '''
<h2>What is a Responsive Search Ad preview tool?</h2>
<p>A Responsive Search Ad (RSA) preview tool lets you visualize exactly how your Google Ads will appear in search results before you upload them to your account. Instead of guessing how Google will assemble your headlines and descriptions, you can test combinations, lock specific positions, and see the actual ad layout - including your display URL, paths, and business name - in a realistic Google Search format.</p>

<p>This free RSA preview tool supports up to 15 headlines and 4 descriptions, matching Google Ads' current RSA format limits. Enter your ad copy, randomize combinations to check every variation, and lock any headline to position 1, 2, or 3 before sending copy to a client or uploading to Google Ads.</p>

<h2>How responsive search ads work</h2>
<p>Google Responsive Search Ads automatically test different combinations of your headlines and descriptions to find which combinations perform best for each individual search query and auction. With up to 15 headlines and 4 descriptions, there are theoretically thousands of possible combinations - which is why previewing them before launch matters. A great headline in position 1 may read awkwardly when Google places it in position 3, or two headlines that sound strong individually may contradict each other when paired.</p>

<p>Using a Google Ads RSA preview tool before uploading forces you to read every likely combination systematically rather than assuming Google will always pick sensible pairings. It also helps when getting approval from clients or stakeholders who are not familiar with how RSAs work - a visual mockup communicates far more clearly than a spreadsheet of raw headlines.</p>
''' + AD_INLINE + '''
<h2>Pinning and locking headlines in Google Ads</h2>
<p>Google Ads allows you to pin headlines to specific positions (position 1, 2, or 3) to ensure that certain text always appears in a fixed slot. This is useful for legally required language, brand names that must lead the headline, or calls to action that need to appear in a consistent position for brand compliance. The preview tool above mirrors this pinning behaviour - lock any headline to a position and it will stay fixed while the remaining unpinned headlines rotate through the available slots.</p>

<p>Google's own guidance recommends pinning sparingly. Pinning too many headlines reduces the algorithm's ability to test combinations and typically lowers Ad Strength. A practical approach: pin only one or two headlines per position when there is a genuine compliance or brand reason, and leave the rest to rotate dynamically.</p>

<h2>RSA character limits and format requirements</h2>
<p>Each headline has a 30-character limit. Each description has a 90-character limit. The display URL domain is taken from your final URL. You can add up to two optional path fields (15 characters each) to make the display URL more descriptive - for example, acme.com/free-trial or acme.com/services/marketing. The business name field is displayed above the headlines in the new Google Ads format and can be up to 25 characters. The preview tool enforces all of these limits in real time with a character counter on each field.</p>

<h2>How to use this free Google Ads preview tool</h2>
<p>Enter your business name and display URL in the ad details section. Add your headlines one by one - the live preview on the right updates as you type. Use the pin icon next to each headline to lock it to position 1, 2, or 3 if needed. Add your descriptions in the same way. Once you have filled in your assets, click Randomize to cycle through different combinations and check that every pairing reads naturally. If any combination looks awkward, edit the headline or description before you upload to Google Ads.</p>
''' + AFFILIATES['semrush']()

RSA_PREVIEW_FAQ_ITEMS = [
    ("What is the difference between a responsive search ad and an expanded text ad?",
     "Expanded text ads (ETAs) had fixed positions - you wrote three headlines and two descriptions and they always appeared in that exact order. Google retired ETAs in June 2022. Responsive search ads let you provide up to 15 headlines and 4 descriptions, and Google's algorithm tests different combinations automatically to find which perform best for each query."),
    ("How many combinations does a responsive search ad have?",
     "With 15 headlines and 4 descriptions, the theoretical number of combinations is very large - Google selects 3 headlines and 2 descriptions per ad serving, and the order can vary. In practice the algorithm gravitates toward combinations with strong historical performance, but previewing a representative sample before launch helps catch obvious issues."),
    ("Should I pin headlines in my responsive search ads?",
     "Pin sparingly. Pinning guarantees a headline always appears in a specific position, which is useful for legal disclaimers, brand names, or calls to action that must always be visible. But pinning too many headlines reduces Google's ability to test combinations, which typically lowers your Ad Strength score and limits algorithm optimisation. A good rule: pin one or two headlines max, only when there is a clear compliance or brand reason."),
    ("What is a good Ad Strength for a responsive search ad?",
     "Google rates Ad Strength from Poor to Excellent. Advertisers who improve from Poor to Excellent see 15% more clicks and conversions on average according to Google. To reach Excellent: fill all 15 headline slots, add all 4 descriptions, avoid repeating the same message across multiple headlines, include at least one headline with a keyword, and avoid pinning more than one or two headlines."),
    ("Can I use this RSA preview tool for Microsoft Ads (Bing)?",
     "Yes. Microsoft Ads uses the same responsive search ad format with identical character limits - 30 characters per headline, 90 characters per description, up to 15 headlines and 4 descriptions. The visual format is slightly different in the search results page, but the underlying asset structure and limits are the same, so this preview tool works for planning Microsoft Ads RSAs too."),
    ("What should my display URL paths say?",
     "Display URL paths do not need to match your actual URL structure - they are for readability in the ad only. Use them to signal what the landing page is about. For example, if your final URL is a product page, paths like /free-trial or /get-started communicate the offer clearly. Each path is limited to 15 characters and cannot contain spaces."),
]

RSA_PREVIEW_FAQ = faq(RSA_PREVIEW_FAQ_ITEMS)

RSA_PREVIEW_BODY = f'''
<main>
  <section class="page-hero"><div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="bc-sep">/</span>
      <a href="/marketing-tools">Marketing Tools</a><span class="bc-sep">/</span>
      <span class="bc-current">Free RSA Preview Tool</span>
    </nav>
    <h1>Free <span class="accent">RSA Preview Tool</span></h1>
    <p class="hero-sub">Visualize your Google Responsive Search Ads before you go live. Test combinations, lock positions, and share ad mockups with your team or clients.</p>
  </div></section>

  <section class="calc-content"><div class="container">
    <div class="page-with-sidebar">
      {AD_SIDEBAR_L}
      <div class="main-col">
        {RSA_PREVIEW_TOOL_HTML}
        <div class="prose" style="margin-top:48px;">
          {RSA_PREVIEW_EDITORIAL}
          {RSA_PREVIEW_FAQ}
        </div>
      </div>
      {AD_SIDEBAR_R}
    </div>
  </div></section>
</main>'''
