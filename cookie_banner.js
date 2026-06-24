(function () {
  const STORAGE_KEY = 'cookie_consent_v1';

  function getConsent() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)); } catch { return null; }
  }

  function setConsent(stats, marketing) {
    const val = { necessary: true, statistics: stats, marketing: marketing };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(val));
    pushToDataLayer(stats, marketing);
    hideBanner();
  }

  function pushToDataLayer(stats, marketing) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'cookie_consent_update',
      analytics_storage: stats ? 'granted' : 'denied',
      ad_storage: marketing ? 'granted' : 'denied',
      ad_user_data: marketing ? 'granted' : 'denied',
      ad_personalization: marketing ? 'granted' : 'denied'
    });
  }

  function hideBanner() {
    const b = document.getElementById('cookie-banner');
    if (b) b.style.display = 'none';
  }

  function showBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.innerHTML = `
      <div style="position:fixed;bottom:0;left:0;right:0;z-index:99999;background:#1A2640;border-top:1px solid #2d3f5e;padding:16px 20px;font-family:Inter,sans-serif;font-size:13px;color:#cbd5e1;">
        <div style="max-width:900px;margin:0 auto;">
          <p style="margin:0 0 10px 0;">We use cookies to improve your experience and analyse site traffic. <a href="/privacy-policy" style="color:#6366F1;">Privacy Policy</a></p>
          <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px;">
            <label style="display:flex;align-items:center;gap:5px;cursor:default;opacity:0.5;"><input type="checkbox" checked disabled> Necessary</label>
            <label style="display:flex;align-items:center;gap:5px;cursor:pointer;"><input type="checkbox" id="cb-stats"> Statistics</label>
            <label style="display:flex;align-items:center;gap:5px;cursor:pointer;"><input type="checkbox" id="cb-marketing"> Marketing</label>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <button id="cb-accept-all" style="background:#6366F1;color:#fff;border:none;padding:8px 16px;border-radius:6px;cursor:pointer;font-size:13px;">Accept all</button>
            <button id="cb-reject-all" style="background:#1F3550;color:#cbd5e1;border:1px solid #2d3f5e;padding:8px 16px;border-radius:6px;cursor:pointer;font-size:13px;">Reject all</button>
            <button id="cb-save" style="background:#1F3550;color:#cbd5e1;border:1px solid #2d3f5e;padding:8px 16px;border-radius:6px;cursor:pointer;font-size:13px;">Save selection</button>
          </div>
        </div>
      </div>`;
    document.body.appendChild(banner);
    document.getElementById('cb-accept-all').addEventListener('click', () => setConsent(true, true));
    document.getElementById('cb-reject-all').addEventListener('click', () => setConsent(false, false));
    document.getElementById('cb-save').addEventListener('click', () => {
      setConsent(
        document.getElementById('cb-stats').checked,
        document.getElementById('cb-marketing').checked
      );
    });
  }

  const existing = getConsent();
  if (existing) {
    pushToDataLayer(existing.statistics, existing.marketing);
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', showBanner);
    } else {
      showBanner();
    }
  }
})();
