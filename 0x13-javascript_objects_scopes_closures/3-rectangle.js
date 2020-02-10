#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let cont = 0; cont < this.height; cont++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
