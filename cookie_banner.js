(function () {
  var STORAGE_KEY = 'cookie_consent_v1';

  function getConsent() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)); } catch (e) { return null; }
  }

  function setConsent(stats, marketing) {
    var val = { necessary: true, statistics: stats, marketing: marketing };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(val));
    pushToDataLayer(stats, marketing);
    removeBanner();
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

  function removeBanner() {
    var overlay = document.getElementById('consent-overlay');
    var banner  = document.getElementById('consent-banner');
    if (overlay) overlay.remove();
    if (banner)  banner.remove();
  }

  function buildToggle(id, label, description) {
    return '<div style="margin-bottom:20px;">'
      + '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">'
      + '<strong style="font-size:15px;color:#f1f5f9;">' + label + '</strong>'
      + (id === 'necessary'
          ? '<span style="background:#6366F1;color:#fff;font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px;">Always on</span>'
          : '<label style="position:relative;display:inline-block;width:44px;height:24px;cursor:pointer;">'
            + '<input type="checkbox" id="cb-' + id + '" style="opacity:0;width:0;height:0;position:absolute;">'
            + '<span id="track-' + id + '" style="position:absolute;inset:0;background:#334155;border-radius:12px;transition:background 0.2s;"></span>'
            + '<span id="thumb-' + id + '" style="position:absolute;left:2px;top:2px;width:20px;height:20px;background:#fff;border-radius:50%;transition:transform 0.2s;"></span>'
            + '</label>')
      + '</div>'
      + '<p style="font-size:13px;color:#94a3b8;margin:0;line-height:1.5;">' + description + '</p>'
      + (id === 'necessary' ? '' : '</div>');
  }

  function showBanner() {
    // Overlay
    var overlay = document.createElement('div');
    overlay.id = 'consent-overlay';
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:99998;backdrop-filter:blur(2px);';
    document.body.appendChild(overlay);

    // Banner
    var banner = document.createElement('div');
    banner.id = 'consent-banner';
    banner.style.cssText = [
      'position:fixed;bottom:0;left:50%;transform:translateX(-50%);',
      'width:100%;max-width:520px;z-index:99999;',
      'background:#1A2640;border:1px solid #2d3f5e;border-bottom:none;',
      'border-radius:16px 16px 0 0;padding:28px 28px 24px;',
      'font-family:Inter,sans-serif;box-shadow:0 -8px 40px rgba(0,0,0,0.5);'
    ].join('');

    banner.innerHTML = ''
      + '<h2 style="font-size:18px;font-weight:700;color:#f1f5f9;margin:0 0 8px;font-family:\'Space Grotesk\',Inter,sans-serif;">We use cookies</h2>'
      + '<p style="font-size:13px;color:#94a3b8;margin:0 0 24px;line-height:1.6;">We use cookies to improve your experience, analyse traffic, and show relevant ads. You choose what you accept.</p>'
      + buildToggle('necessary', 'Necessary', 'Required for the site to function. Cannot be disabled.')
      + buildToggle('statistics', 'Statistics', 'Helps us understand how visitors use the site (Google Analytics). No personal data is shared with third parties.')
      + buildToggle('marketing', 'Marketing', 'Used to show relevant ads via Google AdSense. Data may be shared with advertising partners.')
      + '<div style="display:flex;gap:8px;margin-top:24px;flex-wrap:wrap;">'
      + '<button id="cb-accept-all" style="flex:1;background:#6366F1;color:#fff;border:none;padding:12px 16px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:600;font-family:Inter,sans-serif;">Accept all</button>'
      + '<button id="cb-reject-all" style="flex:1;background:#1F3550;color:#cbd5e1;border:1px solid #2d3f5e;padding:12px 16px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:600;font-family:Inter,sans-serif;">Reject all</button>'
      + '<button id="cb-save" style="width:100%;background:#1F3550;color:#cbd5e1;border:1px solid #2d3f5e;padding:12px 16px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:600;font-family:Inter,sans-serif;margin-top:0;">Save selection</button>'
      + '</div>'
      + '<p style="text-align:center;margin:14px 0 0;"><a href="/privacy-policy" style="font-size:12px;color:#64748b;text-decoration:underline;">Privacy Policy</a></p>';

    document.body.appendChild(banner);

    // Toggle interactivity
    ['statistics', 'marketing'].forEach(function(id) {
      var cb    = document.getElementById('cb-' + id);
      var track = document.getElementById('track-' + id);
      var thumb = document.getElementById('thumb-' + id);
      if (!cb || !track || !thumb) return;
      cb.addEventListener('change', function() {
        track.style.background = cb.checked ? '#6366F1' : '#334155';
        thumb.style.transform  = cb.checked ? 'translateX(20px)' : 'translateX(0)';
      });
    });

    document.getElementById('cb-accept-all').addEventListener('click', function() { setConsent(true, true); });
    document.getElementById('cb-reject-all').addEventListener('click', function() { setConsent(false, false); });
    document.getElementById('cb-save').addEventListener('click', function() {
      var stats    = document.getElementById('cb-statistics');
      var mkt      = document.getElementById('cb-marketing');
      setConsent(stats ? stats.checked : false, mkt ? mkt.checked : false);
    });
  }

  // Default denied state for Google Consent Mode v2 before user chooses
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: 'cookie_consent_update',
    analytics_storage: 'denied',
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied'
  });

  var existing = getConsent();
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
