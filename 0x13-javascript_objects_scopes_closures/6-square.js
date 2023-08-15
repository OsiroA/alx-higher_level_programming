#!/usr/bin/node
/* This class Square defines a Square that inherits a previous script */
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let a = 0;
      for (a = 0; a < this.height; a++) console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
