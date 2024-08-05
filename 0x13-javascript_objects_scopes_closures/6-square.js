#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (ch) {
    if (ch === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(ch);
        }
        process.stdout.write('\n');
      }
    }
  }
}
const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');
module.exports = Square;
