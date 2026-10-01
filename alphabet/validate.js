#!/usr/bin/env node
/* Alphabet Grab's word lists moved to ../shared/word-banks.js; the validator moved with them.
   This path is kept so the old command still works:  node alphabet/validate.js [path/to/alphabet.html] */
'use strict';
const path = require('path');
const game = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : null;
if (game) process.argv.splice(2, 1, '--game', game);
require(path.join(__dirname, '..', 'shared', 'validate-word-banks.js'));
