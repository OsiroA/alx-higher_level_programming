#!/usr/bin/node
/* this script defines a class Square that inherits from Rectangle */
// module.exports = Square;
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
