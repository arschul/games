#!/usr/bin/env node
/* Reveal It! content validator.
 *
 *   node reveal-it/validate.js                      structure, answers, levels, flag rules
 *   node reveal-it/validate.js --twemoji <dir>      also checks every emoji has a Twemoji SVG
 *                                                   (dir = node_modules/@twemoji/svg from `npm i @twemoji/svg@15.0.0`)
 *
 * Reads the CATEGORIES data and the answer matcher straight out of reveal-it.html, so the checks use the
 * same normalisation the game does. Exit code 1 on any error; warnings never fail the run.
 */
'use strict';
const fs = require('fs'), path = require('path'), vm = require('vm');
const args = process.argv.slice(2);
const twIdx = args.indexOf('--twemoji');
const twDir = twIdx >= 0 ? args[twIdx + 1] : null;
const file = path.join(__dirname, 'reveal-it.html');
const src = fs.readFileSync(file, 'utf8');
const grab = (a, b) => { const i = src.indexOf(a), j = src.indexOf(b); if (i < 0 || j < 0) throw new Error('markers missing: ' + a); return src.slice(i, j); };
const ctx = {};
vm.createContext(ctx);
vm.runInContext(grab('/*DATA-START*/', '/*DATA-END*/') + '\n' + grab('/*MATCH-START*/', '/*MATCH-END*/') +
  '\nthis.CATEGORIES = CATEGORIES; this.normalize = normalize; this.forms = forms; this.lev = lev; this.accepted = accepted;', ctx);
const { CATEGORIES, normalize, forms, lev, accepted } = ctx;

const errors = [], warns = [];
const err = m => errors.push(m), warn = m => warns.push(m);
const LEVELS = ['A1', 'A2', 'B1'];
const MIN_ITEMS = 15;
// Not suitable for a teen classroom, or a picture that would need a caption to be safe.
const BLOCKED = ['🍆', '🍑', '🍺', '🍻', '🍷', '🥂', '🍸', '🍹', '🍾', '🥃', '🍶', '🚬', '💊', '💉', '🔫', '💣', '🗡', '🔪', '👙', '🩲', '💩', '🖕'];
// Flags that look (almost) identical to one we keep, or read wrongly on a projector.
const LOOKALIKES = { '🇲🇨': 'Monaco = Indonesia', '🇮🇩': 'Indonesia = Monaco', '🇹🇩': 'Chad ≈ Romania', '🇷🇴': 'Romania ≈ Chad', '🇨🇮': "Côte d'Ivoire = mirrored Ireland", '🇱🇺': 'Luxembourg ≈ Netherlands', '🇻🇪': 'Venezuela ≈ Colombia', '🇪🇨': 'Ecuador ≈ Colombia', '🇸🇰': 'Slovakia ≈ Slovenia/Russia', '🇸🇮': 'Slovenia ≈ Slovakia/Russia' };
const strip = e => e.replace(/️/g, '');
const twFile = e => { let cps = [...e].map(c => c.codePointAt(0).toString(16)); if (!e.includes('‍')) cps = cps.filter(x => x !== 'fe0f'); return cps.join('-') + '.svg'; };

const seenEmoji = new Map(), seenIds = new Set();
let total = 0;
for (const c of CATEGORIES) {
  const where = `[${c.id}]`;
  if (!c.id || !c.label || !c.icon) err(`${where} category needs id, label and icon`);
  if (seenIds.has(c.id)) err(`${where} duplicate category id`); seenIds.add(c.id);
  if (typeof c.rotate !== 'boolean') err(`${where} rotate must be true or false`);
  if (!Array.isArray(c.items) || c.items.length < MIN_ITEMS) err(`${where} needs at least ${MIN_ITEMS} items (has ${c.items ? c.items.length : 0})`);
  const owner = new Map();       // normalised accepted form -> item index
  const counts = { A1: 0, A2: 0, B1: 0 };
  c.items.forEach((it, i) => {
    total++;
    const id = `${where} #${i + 1} ${it.e} "${(it.a || [])[0]}"`;
    if (typeof it.e !== 'string' || !it.e) { err(`${id}: missing emoji`); return; }
    if (BLOCKED.includes(strip(it.e))) err(`${id}: emoji is on the not-for-teens list`);
    if (seenEmoji.has(strip(it.e))) err(`${id}: emoji already used in ${seenEmoji.get(strip(it.e))}`); else seenEmoji.set(strip(it.e), c.id);
    if (!Array.isArray(it.a) || !it.a.length || it.a.some(x => typeof x !== 'string' || !x.trim())) { err(`${id}: a must be a non-empty list of strings`); return; }
    if (it.alt && (!Array.isArray(it.alt) || it.alt.some(x => typeof x !== 'string' || !x.trim()))) err(`${id}: alt must be a list of strings`);
    if (!LEVELS.includes(it.lvl)) err(`${id}: lvl must be one of ${LEVELS.join('/')} (got ${it.lvl})`); else counts[it.lvl]++;
    // answers: no two items in a category may accept the same answer (after the game's own normalisation)
    const mine = new Set();
    accepted(it).forEach(a => {
      const n = normalize(a);
      if (!n) { err(`${id}: answer "${a}" normalises to nothing`); return; }
      if (/[^\x00-\x7F]/.test(a) && n === a.toLowerCase()) warn(`${id}: answer "${a}" has non-ASCII characters`);
      forms(n).forEach(f => {
        if (mine.has(f)) return; mine.add(f);
        if (owner.has(f) && owner.get(f) !== i) err(`${id}: accepts "${a}" but item #${owner.get(f) + 1} ${c.items[owner.get(f)].e} already accepts it`);
        else owner.set(f, i);
      });
    });
    if (it.alt && it.alt.some(x => normalize(x) === normalize(it.a[0]))) warn(`${id}: alt repeats the main answer`);
    if (c.id === 'flags') {
      if (LOOKALIKES[strip(it.e)]) err(`${id}: lookalike flag (${LOOKALIKES[strip(it.e)]})`);
      if (!it.nat || !Array.isArray(it.nat.a) || !it.nat.a.length) err(`${id}: flags need nat.a (nationality answer)`);
      else {
        const nn = new Set(); accepted({ a: it.nat.a, alt: it.nat.alt }).forEach(a => forms(normalize(a)).forEach(f => nn.add(f)));
        c.items.forEach((o, k) => { if (k < i && o.nat) accepted({ a: o.nat.a, alt: o.nat.alt }).forEach(a => { if (nn.has(normalize(a))) err(`${id}: nationality "${a}" already used by #${k + 1} ${o.e}`); }); });
      }
    } else if (it.nat) warn(`${id}: nat is only used for flags`);
    if (twDir && !fs.existsSync(path.join(twDir, twFile(it.e)))) err(`${id}: no Twemoji file ${twFile(it.e)}`);
  });
  // near-miss answers between different items would make "so close" point at the wrong picture
  const keys = [...owner.keys()].filter(k => k.length >= 4);
  for (let x = 0; x < keys.length; x++) for (let y = x + 1; y < keys.length; y++) {
    if (owner.get(keys[x]) !== owner.get(keys[y]) && lev(keys[x], keys[y]) <= 1) warn(`${where} "${keys[x]}" and "${keys[y]}" are one letter apart (${c.items[owner.get(keys[x])].e} vs ${c.items[owner.get(keys[y])].e})`);
  }
  if (c.id === 'flags') {
    if (c.rotate !== false) err(`${where} flags must not rotate (a turned flag is another flag)`);
    if (!c.needsImg) err(`${where} flags need needsImg:true (a Windows PC shows letters, which would give the answer away)`);
  }
  console.log(`${c.icon} ${c.label.padEnd(18)} ${String(c.items.length).padStart(3)} items   A1 ${String(counts.A1).padStart(2)}  A2 ${String(counts.A2).padStart(2)}  B1 ${String(counts.B1).padStart(2)}`);
}
console.log(`\n${total} items in ${CATEGORIES.length} categories.` + (twDir ? ` Twemoji files checked in ${twDir}.` : ' Twemoji files NOT checked (pass --twemoji <dir>).'));
if (warns.length) { console.log(`\n${warns.length} warning(s):`); warns.forEach(w => console.log('  ! ' + w)); }
if (errors.length) { console.log(`\n${errors.length} ERROR(S):`); errors.forEach(e => console.log('  ✗ ' + e)); process.exit(1); }
console.log('\nOK: no errors.');
