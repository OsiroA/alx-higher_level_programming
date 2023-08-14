#!/usr/bin/node
/* This script prints a given string and converts string to integer */
const arg = parseInt(process.argv[2]);
if (arg) {
  console.log('My number:', arg);
} else {
  console.log('Not a number');
}
