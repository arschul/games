#!/usr/bin/env node
/* Validator for question-mark/questions.js. Usage: node question-mark/validate.js
   Exits 1 on any error. */
'use strict';
const path = require('path');
const Q = require(path.join(__dirname, 'questions.js'));
const errors = [], warnings = [];
const err = m => errors.push(m), warn = m => warnings.push(m);
const CEFR = new Set(['A1', 'A2', 'B1', 'B2']);
const words = s => s.trim().split(/\s+/);
const norm = w => w.toLowerCase().replace(/[^a-z0-9']/g, '');

/* Franchise categories must name the franchise in every question, and not always in the same place,
   or students learn to flip that word first. */
const MARKERS = {
  'Harry Potter': /^(harry|harry's|potter|potter's|hogwarts|voldemort|diagon|wizarding)$/,
  'Stranger Things': /^(stranger)$/,
  'Minecraft': /^(minecraft|minecraft's|nether|redstone)$/,
  'Fortnite': /^(fortnite)$/,
  'Roblox': /^(roblox)$/
};

const all = [];
for (const [cat, qs] of Object.entries(Q)) {
  if (!Array.isArray(qs) || qs.length !== 15) { err(`${cat}: needs 15 questions`); continue; }
  const ranks = qs.map(q => q.rank).sort((a, b) => a - b).join(',');
  if (ranks !== Array.from({ length: 15 }, (_, i) => i + 1).join(',')) err(`${cat}: ranks must be 1-15 once each`);
  const seen = new Set();
  const pos = [];
  for (const q of qs) {
    const id = `${cat} #${q.rank}`;
    for (const k of Object.keys(q)) if (!['q', 'a', 'rank', 'cefr', 'alt'].includes(k)) err(`${id}: unknown field ${k}`);
    if (!q.q || !q.a) { err(`${id}: empty question or answer`); continue; }
    if (!CEFR.has(q.cefr)) err(`${id}: bad cefr`);
    const t = words(q.q);
    if (t.length < 5 || t.length > 17) err(`${id}: needs 5-17 words, has ${t.length}`);
    if (/[()[\]_]|\.\.\.|…/.test(q.q)) err(`${id}: brackets, blanks or "..."`);
    if (!/\?$/.test(q.q)) warn(`${id}: does not end with "?"`);
    const qw = new Set(t.map(norm));
    const giveaway = q.a.split(/[\s/,-]+/).map(norm).filter(w => w.length > 3 && qw.has(w) && !['the', 'and'].includes(w));
    if (giveaway.length) warn(`${id}: answer word in question (${giveaway.join(', ')})`);
    const k = q.a.toLowerCase().trim();
    if (seen.has(k)) err(`${id}: answer repeats in category`); seen.add(k);
    if (MARKERS[cat]) {
      const i = t.findIndex(w => MARKERS[cat].test(norm(w)));
      if (i < 0) err(`${id}: doesn't name ${cat} — can't be answered without the category`);
      else pos.push({ i, rel: i / (t.length - 1) });
    }
    all.push({ id, t: t.map(norm) });
  }
  if (MARKERS[cat] && pos.length) {
    const byIndex = {};
    pos.forEach(p => { byIndex[p.i] = (byIndex[p.i] || 0) + 1; });
    const top = Math.max(...Object.values(byIndex));
    if (top / pos.length > 0.4) err(`${cat}: ${top} of ${pos.length} name the franchise at the same word — vary it`);
    const start = pos.filter(p => p.rel < 1 / 3).length, end = pos.filter(p => p.rel > 2 / 3).length, mid = pos.length - start - end;
    if (start < 2 || mid < 2 || end < 2) err(`${cat}: franchise hint needs start/middle/end spread (now ${start}/${mid}/${end})`);
  }
}
let twins = 0;
for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++) {
  const A = all[i].t, B = all[j].t;
  if (A.length === B.length && A.filter((w, k) => w !== B[k]).length <= 1) twins++;
}
const n = Object.values(Q).flat(), easy = n.filter(q => q.rank <= 5).length;
if (easy < 60) err(`Easy pool too small: ${easy}`);
warnings.forEach(w => console.log('warn  ' + w));
errors.forEach(e => console.log('ERROR ' + e));
console.log(`${Object.keys(Q).length} categories, ${n.length} questions (Easy ${easy}); ${twins} near-twin pairs (kept apart in play).`);
console.log(errors.length ? `${errors.length} error(s)` : 'OK');
process.exit(errors.length ? 1 : 0);
