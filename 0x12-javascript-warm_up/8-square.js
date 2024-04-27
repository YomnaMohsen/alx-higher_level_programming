#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
  process.exit(1);
}
let square;
for (let i = 0; i < size; i++) {
  square = '';
  for (let j = 0; j < size; j++) {
    square += 'X';
  }
  console.log(square);
}
