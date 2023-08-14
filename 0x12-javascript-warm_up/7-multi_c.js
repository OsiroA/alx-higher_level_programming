#!/usr/bin/node
/* This script prints x times "c is fun" where x is an integer on the line */
const arg = parseInt(process.argv[2]);
const string = 'C is fun';
let n = 0;
if (arg) {
  while (n < arg) {
    console.log(string);
    n++;
  }
} else {
  console.log('Missing number of occurrences');
}
