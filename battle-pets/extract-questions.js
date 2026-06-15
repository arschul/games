// One-time extraction script: pulls MATCH/FILL/MISTAKE/ORDER exercise data
// from each GrammarHub topic page and writes a flat per-topic question bank
// to battle-pets/questions/<slug>.json, plus an index.json manifest.
//
// Re-run manually (node extract-questions.js) whenever topics are added/edited
// in arschul/grammar.

const https = require('https');
const fs = require('fs');
const path = require('path');

const TOPICS = [
  // A1
  {file:'a1/present-continuous.html',        slug:'present-continuous',         name:'Present Continuous',            level:'A1'},
  {file:'a1/simple-past-to-be.html',         slug:'simple-past-to-be',          name:'Simple Past (to be)',           level:'A1'},
  {file:'a1/simple-present-do-does.html',    slug:'simple-present-do-does',     name:'Simple Present (do/does)',      level:'A1'},
  {file:'a1/simple-present-to-be.html',      slug:'simple-present-to-be',       name:'Simple Present (to be)',        level:'A1'},
  // A2
  {file:'a2/past-progressive.html',          slug:'past-progressive',           name:'Past Progressive',              level:'A2'},
  {file:'a2/simple-past-did.html',           slug:'simple-past-did',            name:'Simple Past (did)',             level:'A2'},
  {file:'a2/used-to.html',                   slug:'used-to',                    name:'Used To',                        level:'A2'},
  {file:'a2/zero-conditional.html',          slug:'zero-conditional',           name:'Zero Conditional',              level:'A2'},
  // B1
  {file:'b1/articles.html',                  slug:'articles',                   name:'Articles',                       level:'B1'},
  {file:'b1/defining-relative-clauses.html', slug:'defining-relative-clauses',  name:'Defining Relative Clauses',     level:'B1'},
  {file:'b1/expressing-abilities.html',      slug:'expressing-abilities',       name:'Expressing Abilities',          level:'B1'},
  {file:'b1/first-conditional.html',         slug:'first-conditional',          name:'First Conditional',             level:'B1'},
  {file:'b1/future-forms.html',              slug:'future-forms',               name:'Future Forms',                   level:'B1'},
  {file:'b1/future-possibility-certainty.html', slug:'future-possibility-certainty', name:'Future Possibility & Certainty', level:'B1'},
  {file:'b1/future-time-clauses.html',       slug:'future-time-clauses',        name:'Future Time Clauses',           level:'B1'},
  {file:'b1/gerund-phrases.html',            slug:'gerund-phrases',             name:'Gerund Phrases',                level:'B1'},
  {file:'b1/infinitives-with-to.html',       slug:'infinitives-with-to',        name:'Infinitives with To',           level:'B1'},
  {file:'b1/past-perfect.html',              slug:'past-perfect',               name:'Past Perfect',                  level:'B1'},
  {file:'b1/phrasal-verbs-separable.html',   slug:'phrasal-verbs-separable',    name:'Phrasal Verbs (Separable)',     level:'B1'},
  {file:'b1/present-perfect-progressive.html', slug:'present-perfect-progressive', name:'Present Perfect Progressive', level:'B1'},
  {file:'b1/present-perfect-vs-past.html',   slug:'present-perfect-vs-past',    name:'Present Perfect vs Past',       level:'B1'},
  {file:'b1/present-perfect.html',           slug:'present-perfect',            name:'Present Perfect',               level:'B1'},
  {file:'b1/reflexive-pronouns.html',        slug:'reflexive-pronouns',         name:'Reflexive Pronouns',            level:'B1'},
  {file:'b1/reported-speech.html',           slug:'reported-speech',            name:'Reported Speech',               level:'B1'},
  {file:'b1/second-conditional.html',        slug:'second-conditional',         name:'Second Conditional',            level:'B1'},
  {file:'b1/simple-past-passive.html',       slug:'simple-past-passive',        name:'Simple Past Passive',           level:'B1'},
  {file:'b1/simple-present-passive.html',    slug:'simple-present-passive',     name:'Simple Present Passive',        level:'B1'},
  {file:'b1/so-such.html',                   slug:'so-such',                    name:'So / Such',                      level:'B1'},
  {file:'b1/tag-questions.html',             slug:'tag-questions',              name:'Tag Questions',                  level:'B1'},
  {file:'b1/verb-gerund-infinitive.html',    slug:'verb-gerund-infinitive',     name:'Verb + Gerund/Infinitive',       level:'B1'},
  // B2
  {file:'b2/third-conditional.html',         slug:'third-conditional',          name:'Third Conditional',             level:'B2'},
];

function fetchRaw(file) {
  return new Promise((resolve, reject) => {
    const url = `https://raw.githubusercontent.com/arschul/grammar/main/${file}`;
    https.get(url, res => {
      if (res.statusCode !== 200) return reject(new Error(`${file}: HTTP ${res.statusCode}`));
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

// Extract the array literal that follows `const NAME = `, respecting string
// literals so brackets inside strings don't break the balance count.
function extractArray(src, constName) {
  const marker = `const ${constName} = [`;
  const start = src.indexOf(marker);
  if (start === -1) return [];
  let i = start + marker.length - 1; // position of the opening '['
  let depth = 0;
  let inString = null; // ' or " or `
  let out = '';
  for (; i < src.length; i++) {
    const ch = src[i];
    const prev = src[i - 1];
    out += ch;
    if (inString) {
      if (ch === inString && prev !== '\\') inString = null;
      continue;
    }
    if (ch === "'" || ch === '"' || ch === '`') { inString = ch; continue; }
    if (ch === '[') depth++;
    else if (ch === ']') { depth--; if (depth === 0) break; }
  }
  return new Function('return ' + out)();
}

function stripLeftNum(s) { return s.replace(/^\d+\.\s*/, '').trim(); }
function stripRightLet(s) { return s.replace(/^[a-z]\.\s*/i, '').trim(); }

function convert(topicName, MATCH, FILL, MISTAKE, ORDER) {
  const out = [];
  MATCH.forEach(item => {
    out.push({
      type: 'match',
      prompt: `Complete the sentence: "${stripLeftNum(item.left)} ___"`,
      answer: stripRightLet(item.right),
    });
  });
  FILL.forEach(item => {
    out.push({
      type: 'fill',
      prompt: item.sentence,
      answer: item.explanation ? `${item.answer} — ${item.explanation}` : item.answer,
    });
  });
  MISTAKE.forEach(item => {
    out.push({
      type: 'mistake',
      prompt: `Find the mistake: "${item.sentence}"`,
      answer: item.explanation || (item.options ? item.options[item.correct] : ''),
    });
  });
  ORDER.forEach(item => {
    out.push({
      type: 'order',
      words: item.words,
      answer: item.answer,
    });
  });
  return out;
}

(async () => {
  const outDir = path.join(__dirname, 'questions');
  fs.mkdirSync(outDir, { recursive: true });
  const index = [];

  for (const t of TOPICS) {
    try {
      const html = await fetchRaw(t.file);
      const MATCH = extractArray(html, 'MATCH');
      const FILL = extractArray(html, 'FILL');
      const MISTAKE = extractArray(html, 'MISTAKE');
      const ORDER = extractArray(html, 'ORDER');
      const questions = convert(t.name, MATCH, FILL, MISTAKE, ORDER);
      fs.writeFileSync(
        path.join(outDir, `${t.slug}.json`),
        JSON.stringify({ topic: t.name, level: t.level, questions }, null, 2)
      );
      index.push({ slug: t.slug, name: t.name, level: t.level, count: questions.length });
      console.log(`OK  ${t.slug}: ${questions.length} questions`);
    } catch (e) {
      console.error(`FAIL ${t.slug}: ${e.message}`);
    }
  }

  fs.writeFileSync(path.join(outDir, 'index.json'), JSON.stringify(index, null, 2));
  console.log(`\nWrote index.json with ${index.length} topics`);
})();
