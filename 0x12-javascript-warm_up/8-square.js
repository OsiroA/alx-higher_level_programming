#!/usr/bin/node
/* This script prints a square */
const arg = parseInt(process.argv[2]);
// const character = 'X';
let l = 0;
let b = 0;
// let row = '';
if (!arg) {
  console.log('Missing size');
} else {
  for (l = 0; l < arg; l++) {
    let row = '';
    for (b = 0; b < arg; b++) {
      // console.log(character);
      row += 'X';
    }
    console.log(row);
  }
}
