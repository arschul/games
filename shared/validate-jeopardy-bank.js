#!/usr/bin/env node
/* Validator for shared/jeopardy-bank.js (Jeopardy + Question Mark).
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
    for (const kk of Object.keys(q)) if (!['q', 'a', 'rank', 'cefr', 'alt', 'reveal'].includes(kk)) err(`${id}: unknown field ${kk}`);
    if (q.reveal !== undefined && (typeof q.reveal !== 'string' || !q.reveal.trim())) err(`${id}: empty reveal`);
  });
}
for (const f of bank.frame || []) if (!cats[f]) err(`frame: unknown category ${f}`);
for (const g of Object.keys(bank.groups || {})) if (!cats[g]) err(`groups: unknown category ${g}`);

/* Question Mark pool: not Grammar, not a fixed frame. Each question is shown one word per tile. */
const pool = names.filter(c => bank.groups[c] !== 'Grammar' && !(bank.frame || []).includes(c));
const words = s => s.trim().split(/\s+/);
const norm = w => w.toLowerCase().replace(/[^a-z0-9']/g, '');
const all = [];
for (const c of pool) for (const q of cats[c]) {
  const id = `${c} #${q.rank}`, text = q.reveal || q.q, t = words(text);
  if (t.length < 5 || t.length > 17) err(`${id}: Question Mark needs 5-17 words, has ${t.length} — add a reveal wording`);
  if (/[()[\]_]|\.\.\.|…/.test(text)) err(`${id}: brackets, blanks or "..." don't work as hidden words — add a reveal wording`);
  if (t.some(w => !norm(w))) warn(`${id}: a word is only punctuation ("${t.find(w => !norm(w))}")`);
  all.push({ id, cat: c, rank: q.rank, t: t.map(norm) });
}
/* near-twins: same length, one word different — the game never draws both in one game, so just report */
let twins = 0;
for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++) {
  const A = all[i].t, B = all[j].t;
  if (A.length === B.length && A.filter((w, k) => w !== B[k]).length <= 1) twins++;
}
const count = n => all.filter(q => q.rank <= n).length;
if (count(5) < 60) err(`Question Mark Easy pool too small: ${count(5)}`);

warnings.forEach(w => console.log('warn  ' + w));
errors.forEach(e => console.log('ERROR ' + e));
console.log(`${names.length} categories, ${names.length * 15} questions. Question Mark pool: ${pool.length} categories, ` +
  `Easy ${count(5)} / Medium ${count(10)} / All ${count(15)}; ${twins} near-twin pairs (kept apart in play).`);
console.log(errors.length ? `${errors.length} error(s)` : 'OK');
process.exit(errors.length ? 1 : 0);
