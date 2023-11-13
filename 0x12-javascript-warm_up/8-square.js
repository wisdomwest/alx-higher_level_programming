#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let k = 0; k < x; k++)
      row += 'X';
    console.log(row);
  }
}
