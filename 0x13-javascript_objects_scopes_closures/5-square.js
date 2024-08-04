#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
module.exports = Square;
