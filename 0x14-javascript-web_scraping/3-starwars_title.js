#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movId = process.argv[2];
if (!movId) {
  process.exit();
}
request(url + movId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log((JSON.parse(body)).title);
  }
});
