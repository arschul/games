// Validates the Sentence Auction paragraph bank.
// Usage: node shared/validate-sentence-auction.js [path to sentence-auction.html or a .js file that defines PARAGRAPHS]
const fs = require('fs'), path = require('path');
const file = process.argv[2] || path.join(__dirname, '..', 'sentence-auction', 'sentence-auction.html');
let src = fs.readFileSync(file, 'utf8');
if (file.endsWith('.html')) { const m = src.match(/<script id="data">([\s\S]*?)<\/script>/); if (!m) { console.error('No <script id="data"> block'); process.exit(1); } src = m[1]; }
const PARAGRAPHS = new Function(src + '\nreturn PARAGRAPHS;')();
const RULES = { A1: { n: [3, 4], sent: 50, para: 190 }, A2: { n: [3, 4], sent: 60, para: 230 }, B1: { n: [4, 5], sent: 85, para: 400 }, B2: { n: [4, 5], sent: 85, para: 400 } };
const PER_LEVEL = 16;
const errs = []; let checks = 0;
const ok = (c, msg) => { checks++; if (!c) errs.push(msg); };
const words = s => s.toLowerCase().replace(/[.,!?]/g, '').split(/\s+/);
function wordDiff(a, b) { // tokens that are not shared, counting repeats
  const A = words(a), B = words(b), cnt = {}; A.forEach(w => cnt[w] = (cnt[w] || 0) + 1);
  let common = 0; B.forEach(w => { if (cnt[w] > 0) { cnt[w]--; common++; } });
  return (A.length - common) + (B.length - common);
}
ok(Object.keys(PARAGRAPHS).join() === 'A1,A2,B1,B2', 'levels must be A1,A2,B1,B2');
for (const [L, list] of Object.entries(PARAGRAPHS)) {
  const R = RULES[L]; ok(list.length === PER_LEVEL, `${L}: ${list.length} paragraphs, expected ${PER_LEVEL}`);
  ok(new Set(list.map(p => p.topic)).size === list.length, `${L}: duplicate topic`);
  const oks = new Set(list.flatMap(p => p.s.map(s => s.ok)));
  ok(oks.size === list.reduce((n, p) => n + p.s.length, 0), `${L}: the same correct sentence appears twice`);
  list.forEach(p => {
    const id = `${L} "${p.topic}"`;
    ok(p.topic && p.topic.length <= 28, `${id}: topic missing or too long`);
    ok(p.s.length >= R.n[0] && p.s.length <= R.n[1], `${id}: ${p.s.length} sentences, expected ${R.n.join('–')}`);
    ok(p.s.reduce((n, s) => n + Math.max(s.ok.length, ...s.bad.map(b => b.text.length)) + 1, 0) <= R.para, `${id}: paragraph too long for the card`);
    p.s.forEach((s, i) => {
      const sid = `${id} s${i + 1}`;
      ok(/^[A-ZÀ-Ý].*[.?!]$/.test(s.ok), `${sid}: correct sentence needs a capital and end punctuation`);
      ok(s.ok.length <= R.sent, `${sid}: correct sentence too long (${s.ok.length})`);
      ok(Array.isArray(s.bad) && s.bad.length >= 1 && s.bad.length <= 2, `${sid}: needs 1–2 wrong versions`);
      (s.bad || []).forEach(b => {
        ok(b.text && b.text !== s.ok, `${sid}: wrong version equals the correct one`);
        ok(!oks.has(b.text), `${sid}: wrong version is a correct sentence elsewhere`);
        ok(b.tag && b.tag.length <= 32, `${sid}: tag missing or too long`);
        ok(/^[A-ZÀ-Ý].*[.?!]$/.test(b.text) && b.text.slice(-1) === s.ok.slice(-1), `${sid}: wrong version punctuation differs`);
        ok(Math.abs(b.text.length - s.ok.length) <= 10, `${sid}: length tell (${b.text.length} vs ${s.ok.length})`);
        const d = wordDiff(s.ok, b.text); ok(d <= 5, `${sid}: wrong version differs by ${d} words (want one small change; 0 = word order only)`);
        ok(b.text.length <= R.sent, `${sid}: wrong version too long (${b.text.length})`);
      });
      ok(new Set(s.bad.map(b => b.text)).size === s.bad.length, `${sid}: duplicate wrong versions`);
    });
  });
}
if (errs.length) { console.error(errs.join('\n')); console.error(`\n${errs.length} problem(s) in ${checks} checks`); process.exit(1); }
const total = Object.values(PARAGRAPHS).reduce((n, l) => n + l.length, 0), sents = Object.values(PARAGRAPHS).reduce((n, l) => n + l.reduce((m, p) => m + p.s.length, 0), 0);
console.log(`OK: ${total} paragraphs, ${sents} sentences, ${checks} checks passed`);
