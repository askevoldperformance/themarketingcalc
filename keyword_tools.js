// ── Keyword Match Type Tool ──────────────────────────────────────────────────
function generateMatchTypes() {
  const input = document.getElementById('mt-input');
  const output = document.getElementById('mt-output');
  if (!input || !output) return;

  let lines = input.value.split('\n').map(l => l.trim()).filter(l => l.length > 0);

  if (document.getElementById('mt-lowercase').checked) {
    lines = lines.map(l => l.toLowerCase());
  }
  if (document.getElementById('mt-dedupe').checked) {
    lines = [...new Set(lines)];
  }

  const doBroad = document.getElementById('mt-broad').checked;
  const doPhrase = document.getElementById('mt-phrase').checked;
  const doExact = document.getElementById('mt-exact').checked;

  let result = [];
  lines.forEach(kw => {
    if (doBroad) result.push(kw);
    if (doPhrase) result.push(`"${kw}"`);
    if (doExact) result.push(`[${kw}]`);
  });

  output.value = result.join('\n');
  const countEl = document.getElementById('mt-count');
  if (countEl) countEl.textContent = `(${result.length} keywords)`;
}

// ── Keyword Combiner Tool ────────────────────────────────────────────────────
let combinerSeparator = ' ';

document.addEventListener('click', e => {
  const btn = e.target.closest('.sep-btn');
  if (!btn) return;
  document.querySelectorAll('.sep-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  combinerSeparator = btn.dataset.sep === 'space' ? ' ' : btn.dataset.sep === 'dash' ? '-' : '';
});

function generateCombinations() {
  const list1 = document.getElementById('cb-list1');
  const list2 = document.getElementById('cb-list2');
  const list3 = document.getElementById('cb-list3');
  const output = document.getElementById('cb-output');
  if (!list1 || !list2 || !output) return;

  const parseLines = (el) => el.value.split('\n').map(l => l.trim()).filter(l => l.length > 0);

  const l1 = parseLines(list1);
  const l2 = parseLines(list2);
  const l3 = parseLines(list3);

  if (l1.length === 0 || l2.length === 0) {
    output.value = 'Please enter at least two lists.';
    return;
  }

  let combos = [];
  l1.forEach(a => {
    l2.forEach(b => {
      if (l3.length > 0) {
        l3.forEach(c => combos.push([a, b, c].join(combinerSeparator)));
      } else {
        combos.push([a, b].join(combinerSeparator));
      }
    });
  });

  if (document.getElementById('cb-lowercase').checked) {
    combos = combos.map(c => c.toLowerCase());
  }
  if (document.getElementById('cb-dedupe').checked) {
    combos = [...new Set(combos)];
  }

  output.value = combos.join('\n');
  const countEl = document.getElementById('cb-count');
  if (countEl) countEl.textContent = `(${combos.length} keywords)`;
}

// ── Shared: copy to clipboard ─────────────────────────────────────────────────
function copyKwOutput(id) {
  const el = document.getElementById(id);
  if (!el || !el.value) return;
  navigator.clipboard.writeText(el.value).then(() => {
    const btn = event.target;
    const original = btn.textContent;
    btn.textContent = 'Copied!';
    setTimeout(() => { btn.textContent = original; }, 1500);
  });
}
