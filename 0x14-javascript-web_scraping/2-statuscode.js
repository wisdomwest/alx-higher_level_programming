#!/usr/bin/node
const request = require('request');
try {
  request.get(process.argv[2]).on('response', (response, err) => {
    if (err) {
      console.error(err);
    }
    console.log(`code: ${response.statusCode}`);
  });
} catch (err) {
  console.error(err);
}
