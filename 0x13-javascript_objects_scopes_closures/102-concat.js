#!/usr/bin/node
// This script concats 2 files named on the command line
// The file they'd be concatenated in is also the next argument on the cmd line
const argument = process.argv.slice(2);
const fs = require('fs');
const firstFile = fs.readFileSync('./' + argument[0]);
const secondFile = fs.readFileSync('./' + argument[1]);
fs.writeFileSync('./' + argument[2], firstFile + secondFile);
