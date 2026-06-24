# GTM Setup - TheMarketingCalc.com
## Container: GTM-WFL4M8ND

---

## How the consent system works

The cookie banner fires on page load if no prior consent is stored. It pushes a `cookie_consent_update` event to `dataLayer` in two scenarios:

1. **On page load (default denied)** - before the user has made a choice, the banner pushes all storage types as `denied`. This is the Google Consent Mode v2 default state.
2. **On user action** - when the user clicks Accept all, Reject all, or Save selection, a second `cookie_consent_update` is pushed with the actual choices.

On return visits, the stored choice is read from `localStorage` (key: `cookie_consent_v1`) and pushed immediately on load without showing the banner.

### dataLayer event structure

```json
{
  "event": "cookie_consent_update",
  "analytics_storage": "granted | denied",
  "ad_storage": "granted | denied",
  "ad_user_data": "granted | denied",
  "ad_personalization": "granted | denied"
}
```

- `analytics_storage` - controls GA4 tracking
- `ad_storage` - controls AdSense and Google Ads cookies
- `ad_user_data` - controls sending user data to Google for ads
- `ad_personalization` - controls personalised ad targeting

---

## GTM Variables to create

### 1. DLV - analytics_storage
- Type: Data Layer Variable
- Data Layer Variable Name: `analytics_storage`
- Default Value: `denied`

### 2. DLV - ad_storage
- Type: Data Layer Variable
- Data Layer Variable Name: `ad_storage`
- Default Value: `denied`

### 3. DLV - ad_user_data
- Type: Data Layer Variable
- Data Layer Variable Name: `ad_user_data`
- Default Value: `denied`

### 4. DLV - ad_personalization
- Type: Data Layer Variable
- Data Layer Variable Name: `ad_personalization`
- Default Value: `denied`

---

## GTM Triggers to create

### Trigger 1: Consent Update - All Pages
- Type: Custom Event
- Event Name: `cookie_consent_update`
- This fires: All Custom Events
- Use this trigger to update Google Consent Mode signals.

### Trigger 2: Consent Granted - Statistics
- Type: Custom Event
- Event Name: `cookie_consent_update`
- This fires: Some Custom Events
- Condition: `DLV - analytics_storage` equals `granted`
- Use this trigger to fire GA4 only when statistics consent is given.

### Trigger 3: Consent Granted - Marketing
- Type: Custom Event
- Event Name: `cookie_consent_update`
- This fires: Some Custom Events
- Condition: `DLV - ad_storage` equals `granted`
- Use this trigger to fire AdSense / Google Ads tags only when marketing consent is given.

---

## GTM Tags to create

### Tag 1: Google Consent Mode - Default + Update
- Type: Custom HTML
- Trigger: All Pages (Page View) AND Consent Update - All Pages
- HTML:
```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  // Default denied state (fires on All Pages before consent)
  gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'wait_for_update': 2000
  });

  // Update on consent event
  gtag('consent', 'update', {
    'analytics_storage': {{DLV - analytics_storage}},
    'ad_storage': {{DLV - ad_storage}},
    'ad_user_data': {{DLV - ad_user_data}},
    'ad_personalization': {{DLV - ad_personalization}}
  });
</script>
```
- **Important**: this tag must fire BEFORE GA4 and AdSense tags. Set tag firing priority to 10 (higher number = fires first). Set GA4 and AdSense to priority 0.

### Tag 2: GA4 Configuration
- Type: Google Analytics: GA4 Configuration
- Measurement ID: (your GA4 ID, e.g. G-XXXXXXXXXX)
- Trigger: Consent Granted - Statistics
- Tag firing priority: 0

### Tag 3: AdSense Auto Ads
- Type: Custom HTML
- Trigger: Consent Granted - Marketing
- HTML:
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4789906927045850" crossorigin="anonymous"></script>
```
- Tag firing priority: 0

---

## Consent Mode v2 - summary

Google Consent Mode v2 requires four signals: `analytics_storage`, `ad_storage`, `ad_user_data`, and `ad_personalization`. The setup above covers all four. When a user denies consent, Google uses modelled conversions to fill attribution gaps - so you still get data, just anonymised. When a user grants consent, full tracking resumes.

---

## localStorage reference

Key: `cookie_consent_v1`

Stored value example (JSON):
```json
{
  "necessary": true,
  "statistics": true,
  "marketing": false
}
```

To reset consent during testing: open browser DevTools, go to Application > Local Storage, delete the `cookie_consent_v1` key, and reload the page.
