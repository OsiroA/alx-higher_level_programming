#!/usr/bin/node
/* This script prints two arguments passed to it concatenating themwith 'is' */
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const printOut = arg1 + ' ' + 'is' + ' ' + arg2;
console.log(printOut);
