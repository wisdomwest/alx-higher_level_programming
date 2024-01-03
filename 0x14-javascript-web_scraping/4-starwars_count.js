#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
try {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, film) => {
      if (film.characters.find((character) => character.endsWith('/18/'))) {
        return count + 1;
      } else {
        return count;
      }
    }, 0));
  });
} catch (err) {
  console.error(err);
}
