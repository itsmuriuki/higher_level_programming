#!/usr/bin/node
// Computes the number of tasks completed by user id from
// jsonplaceholder.typicode.com API

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let tasks = JSON.parse(body);
  let obj = {};
  for (let task of tasks) {
    if (obj[task.userId] === undefined) {
      obj[task.userId] = 0;
    }
    if (task.completed === true) {
      obj[task.userId]++;
    }
  }
  console.log(obj);
});
