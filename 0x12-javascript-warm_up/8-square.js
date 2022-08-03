#!/usr/bin/node

let size = Number(process.argv[2]);

if (!size) {
  console.log('Missing size');
} else {
  if (size > 0) {
    let square = 'X';
    for (let i = 1; i < size; i++) {
      square += 'X';
    }
    while (size) {
      console.log(square);
      size--;
    }
  }
}
