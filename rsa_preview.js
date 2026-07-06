// ── RSA Preview Tool ──────────────────────────────────────────────────────────

var rsaHeadlines = []; // [{text, pin}] pin = 0|1|2|3 (0=free)
var rsaDescriptions = [];
var rsaCurrentCombo = null;

var HL_LIMIT = 15;
var DESC_LIMIT = 4;
var HL_CHARS = 30;
var DESC_CHARS = 90;

function rsaInit() {
  if (!document.getElementById('rsa-headlines-list')) return;
  // Start with 3 headlines, 2 descriptions
  for (var i = 0; i < 3; i++) rsaAddHeadline(true);
  for (var i = 0; i < 2; i++) rsaAddDescription(true);
  rsaUpdatePreview();
  rsaBindDetails();
}

function rsaBindDetails() {
  ['rsa-brand','rsa-url','rsa-path1','rsa-path2'].forEach(function(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('input', function() {
      if (id === 'rsa-brand' || id === 'rsa-url' || id === 'rsa-path1' || id === 'rsa-path2') {
        var countEl = document.getElementById('count-' + id.replace('rsa-',''));
        if (countEl) countEl.textContent = el.value.length + '/' + el.maxLength;
      }
      rsaUpdatePreview();
    });
  });
}

function rsaAddHeadline(silent) {
  if (rsaHeadlines.length >= HL_LIMIT) return;
  var idx = rsaHeadlines.length;
  rsaHeadlines.push({text: '', pin: 0});
  rsaRenderHeadlines();
  if (!silent) rsaUpdatePreview();
}

function rsaAddDescription(silent) {
  if (rsaDescriptions.length >= DESC_LIMIT) return;
  var idx = rsaDescriptions.length;
  rsaDescriptions.push({text: '', pin: 0});
  rsaRenderDescriptions();
  if (!silent) rsaUpdatePreview();
}

function rsaRenderHeadlines() {
  var container = document.getElementById('rsa-headlines-list');
  if (!container) return;
  container.innerHTML = '';
  rsaHeadlines.forEach(function(hl, idx) {
    var row = document.createElement('div');
    row.className = 'rsa-input-row';
    row.innerHTML =
      '<div class="rsa-input-wrap">' +
        '<input type="text" class="rsa-hl-input" maxlength="' + HL_CHARS + '" ' +
          'placeholder="Headline ' + (idx+1) + '" value="' + escHtml(hl.text) + '">' +
        '<span class="rsa-char-count">' + hl.text.length + '/' + HL_CHARS + '</span>' +
      '</div>' +
      '<div class="rsa-pin-wrap">' +
        '<button class="rsa-pin-btn' + (hl.pin ? ' pinned' : '') + '" title="Pin to position">' +
          (hl.pin ? 'Pos ' + hl.pin : 'Pin') +
        '</button>' +
        (hl.pin ? '<button class="rsa-unpin-btn" title="Unpin">&#x2715;</button>' : '') +
      '</div>' +
      (rsaHeadlines.length > 3 ? '<button class="rsa-remove-btn" title="Remove">&#x2715;</button>' : '');

    var input = row.querySelector('.rsa-hl-input');
    input.addEventListener('input', function() {
      rsaHeadlines[idx].text = this.value;
      row.querySelector('.rsa-char-count').textContent = this.value.length + '/' + HL_CHARS;
      rsaUpdatePreview();
    });

    var pinBtn = row.querySelector('.rsa-pin-btn');
    pinBtn.addEventListener('click', function() {
      rsaShowPinMenu(idx, this);
    });

    var unpinBtn = row.querySelector('.rsa-unpin-btn');
    if (unpinBtn) {
      unpinBtn.addEventListener('click', function() {
        rsaHeadlines[idx].pin = 0;
        rsaRenderHeadlines();
        rsaUpdatePreview();
      });
    }

    var removeBtn = row.querySelector('.rsa-remove-btn');
    if (removeBtn) {
      removeBtn.addEventListener('click', function() {
        rsaHeadlines.splice(idx, 1);
        rsaRenderHeadlines();
        rsaUpdatePreview();
      });
    }

    container.appendChild(row);
  });
  var addBtn = document.getElementById('rsa-add-hl-btn');
  if (addBtn) addBtn.style.display = rsaHeadlines.length >= HL_LIMIT ? 'none' : '';
}

function rsaShowPinMenu(idx, btn) {
  // Remove any existing pin menu
  var existing = document.querySelector('.rsa-pin-menu');
  if (existing) existing.remove();

  var menu = document.createElement('div');
  menu.className = 'rsa-pin-menu';
  menu.innerHTML = '<div class="rsa-pin-menu-title">Pin to position</div>' +
    [1,2,3].map(function(pos) {
      return '<button class="rsa-pin-option" data-pos="' + pos + '">Position ' + pos + '</button>';
    }).join('');

  menu.querySelectorAll('.rsa-pin-option').forEach(function(opt) {
    opt.addEventListener('click', function() {
      var pos = parseInt(this.dataset.pos);
      // Remove existing pin at this position
      rsaHeadlines.forEach(function(hl, i) { if (hl.pin === pos && i !== idx) hl.pin = 0; });
      rsaHeadlines[idx].pin = pos;
      menu.remove();
      rsaRenderHeadlines();
      rsaUpdatePreview();
    });
  });

  btn.parentNode.appendChild(menu);
  setTimeout(function() {
    document.addEventListener('click', function closePinMenu(e) {
      if (!e.target.closest('.rsa-pin-menu') && !e.target.closest('.rsa-pin-btn')) {
        menu.remove();
        document.removeEventListener('click', closePinMenu);
      }
    });
  }, 10);
}

function rsaRenderDescriptions() {
  var container = document.getElementById('rsa-descriptions-list');
  if (!container) return;
  container.innerHTML = '';
  rsaDescriptions.forEach(function(desc, idx) {
    var row = document.createElement('div');
    row.className = 'rsa-input-row';
    row.innerHTML =
      '<div class="rsa-input-wrap">' +
        '<textarea class="rsa-desc-input" maxlength="' + DESC_CHARS + '" ' +
          'placeholder="Description ' + (idx+1) + '" rows="2">' + escHtml(desc.text) + '</textarea>' +
        '<span class="rsa-char-count">' + desc.text.length + '/' + DESC_CHARS + '</span>' +
      '</div>' +
      '<div class="rsa-pin-wrap">' +
        '<button class="rsa-pin-btn' + (desc.pin ? ' pinned' : '') + '" title="Pin to position">' +
          (desc.pin ? 'Pos ' + desc.pin : 'Pin') +
        '</button>' +
        (desc.pin ? '<button class="rsa-unpin-btn" title="Unpin">&#x2715;</button>' : '') +
      '</div>' +
      (rsaDescriptions.length > 2 ? '<button class="rsa-remove-btn" title="Remove">&#x2715;</button>' : '');

    var textarea = row.querySelector('.rsa-desc-input');
    textarea.addEventListener('input', function() {
      rsaDescriptions[idx].text = this.value;
      row.querySelector('.rsa-char-count').textContent = this.value.length + '/' + DESC_CHARS;
      rsaUpdatePreview();
    });

    var pinBtn = row.querySelector('.rsa-pin-btn');
    pinBtn.addEventListener('click', function() {
      rsaShowDescPinMenu(idx, this);
    });

    var unpinBtn = row.querySelector('.rsa-unpin-btn');
    if (unpinBtn) {
      unpinBtn.addEventListener('click', function() {
        rsaDescriptions[idx].pin = 0;
        rsaRenderDescriptions();
        rsaUpdatePreview();
      });
    }

    var removeBtn = row.querySelector('.rsa-remove-btn');
    if (removeBtn) {
      removeBtn.addEventListener('click', function() {
        rsaDescriptions.splice(idx, 1);
        rsaRenderDescriptions();
        rsaUpdatePreview();
      });
    }

    container.appendChild(row);
  });
  var addBtn = document.getElementById('rsa-add-desc-btn');
  if (addBtn) addBtn.style.display = rsaDescriptions.length >= DESC_LIMIT ? 'none' : '';
}

function rsaShowDescPinMenu(idx, btn) {
  var existing = document.querySelector('.rsa-pin-menu');
  if (existing) existing.remove();

  var menu = document.createElement('div');
  menu.className = 'rsa-pin-menu';
  menu.innerHTML = '<div class="rsa-pin-menu-title">Pin to position</div>' +
    [1,2].map(function(pos) {
      return '<button class="rsa-pin-option" data-pos="' + pos + '">Position ' + pos + '</button>';
    }).join('');

  menu.querySelectorAll('.rsa-pin-option').forEach(function(opt) {
    opt.addEventListener('click', function() {
      var pos = parseInt(this.dataset.pos);
      rsaDescriptions.forEach(function(d, i) { if (d.pin === pos && i !== idx) d.pin = 0; });
      rsaDescriptions[idx].pin = pos;
      menu.remove();
      rsaRenderDescriptions();
      rsaUpdatePreview();
    });
  });

  btn.parentNode.appendChild(menu);
  setTimeout(function() {
    document.addEventListener('click', function closePinMenu(e) {
      if (!e.target.closest('.rsa-pin-menu') && !e.target.closest('.rsa-pin-btn')) {
        menu.remove();
        document.removeEventListener('click', closePinMenu);
      }
    });
  }, 10);
}

function rsaUpdatePreview() {
  // Brand
  var brand = (document.getElementById('rsa-brand') || {}).value || 'Your Business Name';
  document.getElementById('preview-brand').textContent = brand;

  // URL
  var url = (document.getElementById('rsa-url') || {}).value || 'example.com';
  var path1 = (document.getElementById('rsa-path1') || {}).value;
  var path2 = (document.getElementById('rsa-path2') || {}).value;
  var displayUrl = url + (path1 ? '/' + path1 : '') + (path2 ? '/' + path2 : '');
  document.getElementById('preview-url').textContent = displayUrl;

  // Generate a combination if none
  if (!rsaCurrentCombo) rsaCurrentCombo = rsaBuildCombo();
  rsaShowCombo(rsaCurrentCombo);
  rsaCurrentCombo = null; // reset so next call generates fresh
}

function rsaBuildCombo() {
  // Pinned headlines
  var slots = [null, null, null]; // positions 1,2,3
  var free = [];
  rsaHeadlines.forEach(function(hl) {
    if (!hl.text) return;
    if (hl.pin >= 1 && hl.pin <= 3) {
      slots[hl.pin - 1] = hl.text;
    } else {
      free.push(hl.text);
    }
  });

  // Fill empty slots from free pool
  rsaShuffle(free);
  var fi = 0;
  for (var i = 0; i < 3; i++) {
    if (!slots[i] && fi < free.length) {
      slots[i] = free[fi++];
    }
  }

  // Pick 2 descriptions respecting pins
  var descSlots = [null, null];
  var freeDescs = [];
  rsaDescriptions.forEach(function(d) {
    if (!d.text) return;
    if (d.pin >= 1 && d.pin <= 2) {
      descSlots[d.pin - 1] = d.text;
    } else {
      freeDescs.push(d.text);
    }
  });
  rsaShuffle(freeDescs);
  var dfi = 0;
  for (var i = 0; i < 2; i++) {
    if (!descSlots[i] && dfi < freeDescs.length) descSlots[i] = freeDescs[dfi++];
  }
  var desc1 = descSlots[0] || '';
  var desc2 = descSlots[1] || '';

  return { headlines: slots, desc1: desc1, desc2: desc2 };
}

function rsaShowCombo(combo) {
  var hlEl = document.getElementById('preview-headlines');
  var descEl = document.getElementById('preview-desc');

  var hls = combo.headlines.filter(Boolean);
  if (hls.length === 0) {
    hlEl.innerHTML = '<span class="rsa-hl-placeholder">Headline 1</span><span class="rsa-hl-sep"> | </span><span class="rsa-hl-placeholder">Headline 2</span><span class="rsa-hl-sep"> | </span><span class="rsa-hl-placeholder">Headline 3</span>';
  } else {
    hlEl.innerHTML = hls.map(function(h, i) {
      return (i > 0 ? '<span class="rsa-hl-sep"> | </span>' : '') + '<span class="rsa-hl">' + escHtml(h) + '</span>';
    }).join('');
  }

  var descText = [combo.desc1, combo.desc2].filter(Boolean).join(' ');
  descEl.textContent = descText || 'Your description will appear here. Enter your description text in the fields on the left to see a live preview of your Google Search ad.';

  // Update combo count info
  var freeHls = rsaHeadlines.filter(function(h) { return h.text && !h.pin; }).length;
  var totalFilled = rsaHeadlines.filter(function(h) { return h.text; }).length;
  var infoEl = document.getElementById('rsa-combo-info');
  if (infoEl && totalFilled > 0) {
    infoEl.textContent = totalFilled + ' headline' + (totalFilled !== 1 ? 's' : '') + ', ' +
      rsaDescriptions.filter(function(d) { return d.text; }).length + ' description' +
      (rsaDescriptions.filter(function(d) { return d.text; }).length !== 1 ? 's' : '') + ' entered';
  }

  // Update locked summary
  var lockedEl = document.getElementById('rsa-locked-summary');
  if (lockedEl) {
    var lockedHls = rsaHeadlines.filter(function(h) { return h.pin && h.text; });
    var lockedDescs = rsaDescriptions.filter(function(d) { return d.pin && d.text; });
    var allLocked = lockedHls.length + lockedDescs.length;
    if (allLocked === 0) {
      lockedEl.innerHTML = '<span style="font-size:0.82rem;color:var(--text-muted);">No assets locked. Use the Pin button to fix a headline or description to a specific position.</span>';
    } else {
      var hlHtml = lockedHls.map(function(h) {
        return '<div class="rsa-locked-item"><span class="rsa-locked-type">HL</span><span class="rsa-locked-pos">Pos ' + h.pin + '</span><span class="rsa-locked-text">' + escHtml(h.text) + '</span></div>';
      }).join('');
      var descHtml = lockedDescs.map(function(d) {
        return '<div class="rsa-locked-item"><span class="rsa-locked-type desc">Desc</span><span class="rsa-locked-pos">Pos ' + d.pin + '</span><span class="rsa-locked-text">' + escHtml(d.text) + '</span></div>';
      }).join('');
      lockedEl.innerHTML = hlHtml + descHtml;
    }
  }
}

function rsaRandomize() {
  var combo = rsaBuildCombo();
  rsaShowCombo(combo);
}

function rsaShuffle(arr) {
  for (var i = arr.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
  }
  return arr;
}

function escHtml(str) {
  return (str || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', rsaInit);
} else {
  rsaInit();
}
