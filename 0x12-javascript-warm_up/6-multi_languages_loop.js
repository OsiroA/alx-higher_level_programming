#!/usr/bin/node
/* This script prints 3 lines but uses an array of strings and a loop */
const newArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let index = 0;
while (index < newArray.length) {
  console.log(newArray[index]);
  index++;
}
