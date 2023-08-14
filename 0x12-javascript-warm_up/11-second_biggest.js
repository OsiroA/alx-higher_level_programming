#!/usr/bin/node
/* this script prints the second largest of integers */
const argments = process.argv.slice(2);
// This process excludesthe first twocmds
// convert the argument to numbers
const integers = argments.map(argument => parseInt(argument));
// Then add the condition if there is no- or just one number
if (integers.length <= 1) {
  console.log('0');
} else {
  // You then sort the numbers in descending order
  integers.sort((a, b) => b - a);
  // The second largest number will then be at index 1
  const secondLargestNumber = integers[1];
  console.log(secondLargestNumber);
}
