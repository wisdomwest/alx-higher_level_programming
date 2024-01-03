#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
try {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    console.log(JSON.parse(body).title);
  });
} catch (err) {
  console.error(err);
}
