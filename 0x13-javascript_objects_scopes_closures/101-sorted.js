#!/usr/bin/node
/* This script imports a dictionary of occurrences and computes it by user id */
const dict = require('./101-data.js').dict;
const outDict = {};
for (const J in dict) {
  if (outDict[dict[J]] === undefined) {
    outDict[dict[J]] = [];
  }
  outDict[dict[J]].push(J);
}
console.log(outDict);
