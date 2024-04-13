#!/usr/bin/node
// empty class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      return {};
    }
  }
}
module.exports = Rectangle;
