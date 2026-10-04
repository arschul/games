#!/usr/bin/env node
/* Validator for shared/jeopardy-bank.js (Jeopardy). Question Mark has its own: question-mark/validate.js.
   Usage: node shared/validate-jeopardy-bank.js [path/to/jeopardy-bank.js]
   Exits 1 on any error. Warnings are printed but don't fail. */
'use strict';
const path = require('path');
const file = path.resolve(process.argv[2] || path.join(__dirname, 'jeopardy-bank.js'));
delete require.cache[file];
const bank = require(file);
const errors = [], warnings = [];
const err = m => errors.push(m), warn = m => warnings.push(m);
const CEFR = new Set(['A1', 'A2', 'B1', 'B2']);
const cats = bank.categories || {};
const names = Object.keys(cats);

if (names.length < 1) err('no categories');
for (const c of names) {
  if (!bank.groups || !bank.groups[c]) err(`${c}: no group`);
  const qs = cats[c];
  if (!Array.isArray(qs) || qs.length !== 15) { err(`${c}: needs 15 questions, has ${qs && qs.length}`); continue; }
  const ranks = qs.map(q => q.rank).sort((a, b) => a - b).join(',');
  if (ranks !== Array.from({ length: 15 }, (_, i) => i + 1).join(',')) err(`${c}: ranks must be 1-15 once each`);
  const seen = new Map();
  qs.forEach(q => {
    const id = `${c} #${q.rank}`;
    if (typeof q.q !== 'string' || !q.q.trim()) err(`${id}: empty question`);
    if (typeof q.a !== 'string' || !q.a.trim()) err(`${id}: empty answer`);
    if (!CEFR.has(q.cefr)) err(`${id}: bad cefr ${q.cefr}`);
    if (q.a && q.a.length > 60) err(`${id}: answer over 60 characters`);
    if (q.alt !== undefined && (!Array.isArray(q.alt) || q.alt.some(x => typeof x !== 'string' || !x.trim()))) err(`${id}: bad alt`);
    const k = String(q.a).toLowerCase().trim();
    if (seen.has(k)) err(`${id}: answer repeats #${seen.get(k)}`); else seen.set(k, q.rank);
    for (const kk of Object.keys(q)) if (!['q', 'a', 'rank', 'cefr', 'alt'].includes(kk)) err(`${id}: unknown field ${kk}`);
  });
}
for (const g of Object.keys(bank.groups || {})) if (!cats[g]) err(`groups: unknown category ${g}`);

warnings.forEach(w => console.log('warn  ' + w));
errors.forEach(e => console.log('ERROR ' + e));
console.log(`${names.length} categories, ${names.length * 15} questions.`);
console.log(errors.length ? `${errors.length} error(s)` : 'OK');
process.exit(errors.length ? 1 : 0);
