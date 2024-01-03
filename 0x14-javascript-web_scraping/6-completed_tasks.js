#!/usr/bin/node
const request = require('request');

try {
  request(process.argv[2], (err, response, body) => {
    if (err) {
      console.error(err);
    }

    const todos_data = JSON.parse(body);
    const completed = {};
    todos_data.forEach((todo) => {
      if (todo.completed && !completed[todo.userId]) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });

    console.log(completed);
  });
} catch (err) {
  console.error(err);
}
