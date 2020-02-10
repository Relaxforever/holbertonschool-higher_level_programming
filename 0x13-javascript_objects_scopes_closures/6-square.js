#!/usr/bin/node

const SquareFirst = require('./5-square.js');
class Square extends SquareFirst {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let cont = 0; cont < this.height; cont++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
