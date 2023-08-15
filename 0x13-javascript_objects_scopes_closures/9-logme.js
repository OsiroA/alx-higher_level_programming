#!/usr/bin/node
/* This functionprints the number of argments already printed and the nevalue */
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
