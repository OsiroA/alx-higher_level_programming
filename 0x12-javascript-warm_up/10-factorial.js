#!/usr/bin/node
/* This script computes and prints a factorial */
const a = parseInt(process.argv[2]);
function fact (number) {
  if (number === 1 || !number) {
    return 1;
  } else {
    return number * fact(number - 1);
  }
}
console.log(fact(a));
