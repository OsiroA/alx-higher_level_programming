#!/usr/bin/node
/* This script prints a message depending on the number of arguments passed */
const argument = process.argv.length;
if (argument <= 2) {
  console.log('No argument');
} else if (argument === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
