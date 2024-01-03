#!/usr/bin/node
const fs = require('fs');
try {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
} catch (err) {
  console.error(err);
}
