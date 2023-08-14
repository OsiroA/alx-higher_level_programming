#!/usr/bin/node
/* This function executes x times a function */
exports.callMeMoby = function (x, theFunction) {
  let a = 0;
  for (a = 0; a < x; a++) {
    theFunction();
  }
};
