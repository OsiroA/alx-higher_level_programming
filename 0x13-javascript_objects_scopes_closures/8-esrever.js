#!/usr/bin/node
/* this script returns the reversed version of a list */
exports.esrever = function (list) {
  const reversedList = [];
  while (list.length > 0) {
    reversedList.push(list.pop());
  }
  return reversedList;
};
