#!/usr/bin/node
/* This script prints the first argument passed to it or o argument */
const argP = process.argv[2];
if (!argP) {
  console.log('No argument');
} else {
  console.log(argP);
}
