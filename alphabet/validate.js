#!/usr/bin/env node
/* Alphabet Grab — word bank validator.
   Usage: node alphabet/validate.js [path/to/alphabet.html]
   Exits 1 on any error. Warnings are printed but do not fail. */
'use strict';
const fs = require('fs');
const path = require('path');
const file = process.argv[2] || path.join(__dirname, 'alphabet.html');
const src = fs.readFileSync(file, 'utf8');

const bank = src.slice(src.indexOf('/*BANK-START*/') + 14, src.indexOf('/*BANK-END*/'));
const fn = name => { const m = src.match(new RegExp('function ' + name + '\\([\\s\\S]*?\\n}')); if (!m) throw new Error('missing ' + name); return m[0]; };
const sandbox = new Function(fn('plain') + '\n' + fn('headLetter') + '\n' + fn('wordKey') + '\n' + bank + '\nreturn { CATS, plain, headLetter, wordKey };')();
const { CATS, headLetter, wordKey } = sandbox;

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
  for (const k of Object.keys(c)) if (!['id', 'label', 'icon', 'group', ...LEVELS].includes(k)) errors.push(where + ': unknown field ' + k);
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

const pad = (s, n) => String(s).padEnd(n);
console.log(pad('Category', 28) + pad('A1', 5) + pad('A2', 5) + pad('B1', 5) + '| letters A1 / ≤A2 / all');
for (const r of rows) console.log(pad(r[0], 28) + pad(r[1], 5) + pad(r[2], 5) + pad(r[3], 5) + '| ' + r[4] + ' / ' + r[5] + ' / ' + r[6]);
const total = rows.reduce((a, r) => a + r[1] + r[2] + r[3], 0);
console.log(CATS.length + ' categories, ' + total + ' words');
for (const w of warns) console.log('warning: ' + w);
for (const e of errors) console.log('ERROR: ' + e);
console.log(errors.length ? errors.length + ' error(s)' : '0 errors');
process.exit(errors.length ? 1 : 0);
