#!/usr/bin/env node
/* Shared word-list validator — shared/word-banks.js (Alphabet Grab + Take a Seat).
   Usage: node shared/validate-word-banks.js [--banks path/to/word-banks.js] [--game path/to/alphabet.html]
   Letters are filed with Alphabet Grab's own headLetter()/wordKey(), read from alphabet.html.
   Exits 1 on any error. Warnings are printed but do not fail. */
'use strict';
const fs = require('fs');
const path = require('path');
const arg = name => { const i = process.argv.indexOf(name); return i > 0 ? process.argv[i + 1] : null; };
const bankFile = path.resolve(arg('--banks') || path.join(__dirname, 'word-banks.js'));
const gameFile = arg('--game') || path.join(__dirname, '..', 'alphabet', 'alphabet.html');
const src = fs.readFileSync(gameFile, 'utf8');
const fn = name => { const m = src.match(new RegExp('function ' + name + '\\([\\s\\S]*?\\n}')); if (!m) throw new Error('missing ' + name); return m[0]; };
const { headLetter, wordKey } = new Function(fn('plain') + '\n' + fn('headLetter') + '\n' + fn('wordKey') + '\nreturn { plain, headLetter, wordKey };')();
const CATS = new Function('module', fs.readFileSync(bankFile, 'utf8') + '\nreturn module.exports;')({ exports: {} });
if (!Array.isArray(CATS)) { console.log('ERROR: ' + bankFile + ' did not export a list'); process.exit(1); }

const LEVELS = ['A1', 'A2', 'B1'];
const GROUPS = ['Vocabulary', 'People and Places', 'Word Types'];
const BLOCK = /\b(beer|wine|vodka|whisky|whiskey|rum|gun|rifle|pistol|kill|killer|drugs?|cigarettes?|sexy|bra|casino|bomb|weapon|knife_fight|blood_bath)\b/i;
const MIN_A2_LETTERS = 16;
const errors = [], warns = [];
const ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

const ids = new Set(), labels = new Set();
const rows = [];
for (const c of CATS) {
  const where = c.id || '(no id)';
  if (!c.id || ids.has(c.id)) errors.push(where + ': missing or repeated id');
  if (!c.label || labels.has(c.label)) errors.push(where + ': missing or repeated label');
  ids.add(c.id); labels.add(c.label);
  if (!c.icon) errors.push(where + ': no icon');
  if (!GROUPS.includes(c.group)) errors.push(where + ': unknown group ' + c.group);
  if (!/^(A|An|Something) [a-z]/.test(c.prompt || '')) errors.push(where + ': prompt must start "A …", "An …" or "Something …"');
  else if (/^An? /.test(c.prompt) && (/^An /.test(c.prompt) !== /^An? [aeiou]/i.test(c.prompt))) errors.push(where + ': "' + c.prompt + '" — a/an does not match the next word');
  if ((c.prompt || '').length > 34) errors.push(where + ': prompt longer than 34 characters');
  for (const k of Object.keys(c)) if (!['id', 'label', 'icon', 'group', 'prompt', ...LEVELS].includes(k)) errors.push(where + ': unknown field ' + k);
  const seen = new Map();
  const byLevel = { A1: {}, A2: {}, B1: {} };
  let count = { A1: 0, A2: 0, B1: 0 };
  for (const lvl of LEVELS) {
    for (const raw of String(c[lvl] || '').split(/\s+/).filter(Boolean)) {
      if (!/^[A-Za-z][A-Za-z'-]*(_[A-Za-z][A-Za-z'-]*)*$/.test(raw)) { errors.push(where + ': odd characters in "' + raw + '"'); continue; }
      const w = raw.replace(/_/g, ' ');
      const L = headLetter(w);
      if (!L) { errors.push(where + ': no first letter for "' + w + '"'); continue; }
      if (/^(a|an|the) /i.test(w)) warns.push(where + ': "' + w + '" starts with an article; it will be filed under ' + L);
      const k = wordKey(w);
      if (seen.has(k)) errors.push(where + ': "' + w + '" (' + lvl + ') repeats "' + seen.get(k) + '"');
      seen.set(k, w + ' ' + lvl);
      if (BLOCK.test(w)) errors.push(where + ': "' + w + '" is on the not-for-teens list');
      byLevel[lvl][L] = (byLevel[lvl][L] || 0) + 1;
      count[lvl]++;
    }
  }
  const letters = max => ABC.filter(L => LEVELS.slice(0, max + 1).some(l => byLevel[l][L])).length;
  const a1 = letters(0), a2 = letters(1), all = letters(2);
  if (a2 < MIN_A2_LETTERS) errors.push(where + ': only ' + a2 + ' playable letters at A2 (need ' + MIN_A2_LETTERS + ')');
  if (count.A1 + count.A2 < 30) errors.push(where + ': only ' + (count.A1 + count.A2) + ' words at A1–A2');
  if (count.A1 < 5) warns.push(where + ': only ' + count.A1 + ' A1 words');
  rows.push([c.label, count.A1, count.A2, count.B1, a1, a2, all]);
}

// Take a Seat: a (list, letter) pair is playable at a level if it has a word at that level or below;
// its tier comes from how many words the WHOLE list has for that letter (5+ easy, 3-4 medium, 1-2 hard).
const POOL_MIN = { A1: { easy: 60, total: 150 }, A2: { easy: 60, total: 250 }, B1: { easy: 60, total: 300 } };
const pools = {};
for (const [i, lvl] of LEVELS.entries()) {
  const t = { easy: 0, medium: 0, hard: 0 };
  for (const c of CATS) {
    const all = {}, at = {};
    for (const [j, l] of LEVELS.entries()) for (const raw of String(c[l] || '').split(/\s+/).filter(Boolean)) {
      const L = headLetter(raw.replace(/_/g, ' ')); if (!L) continue;
      all[L] = (all[L] || 0) + 1; if (j <= i) at[L] = 1;
    }
    for (const L in at) t[all[L] >= 5 ? 'easy' : all[L] >= 3 ? 'medium' : 'hard']++;
  }
  t.total = t.easy + t.medium + t.hard; pools[lvl] = t;
  if (t.easy < POOL_MIN[lvl].easy) errors.push('Take a Seat: only ' + t.easy + ' easy prompts at ' + lvl + ' (need ' + POOL_MIN[lvl].easy + ')');
  if (t.total < POOL_MIN[lvl].total) errors.push('Take a Seat: only ' + t.total + ' prompts at ' + lvl + ' (need ' + POOL_MIN[lvl].total + ')');
}

const pad = (s, n) => String(s).padEnd(n);
console.log(pad('Category', 28) + pad('A1', 5) + pad('A2', 5) + pad('B1', 5) + '| letters A1 / ≤A2 / all');
for (const r of rows) console.log(pad(r[0], 28) + pad(r[1], 5) + pad(r[2], 5) + pad(r[3], 5) + '| ' + r[4] + ' / ' + r[5] + ' / ' + r[6]);
const total = rows.reduce((a, r) => a + r[1] + r[2] + r[3], 0);
console.log(CATS.length + ' categories, ' + total + ' words');
for (const l of LEVELS) console.log('Take a Seat prompts ' + (l === 'A1' ? 'A1   ' : l === 'A2' ? '≤A2  ' : 'all  ') + ': ' + pools[l].easy + ' easy / ' + pools[l].medium + ' medium / ' + pools[l].hard + ' hard = ' + pools[l].total);
for (const w of warns) console.log('warning: ' + w);
for (const e of errors) console.log('ERROR: ' + e);
console.log(errors.length ? errors.length + ' error(s)' : '0 errors');
process.exit(errors.length ? 1 : 0);
