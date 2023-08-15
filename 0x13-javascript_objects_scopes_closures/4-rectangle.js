#!/usr/bin/node
/* This class defines a Rectangle with a constructor */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      // if (w <= 0 || h <= 0) {
      // this.width = undefined;
      // this.height = undefined;
      // this.emptyObj = {};
      // {};
    }
  }

  print () {
    for (let wi = 0; wi < this.height; wi++) {
      let row = '';
      for (let he = 0; he < this.width; he++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    let temp = 0;
    // this.width = temp;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
