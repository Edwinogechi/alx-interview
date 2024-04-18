#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Initiates an API request to retrieve film information
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Extracts the list of character URLs from the response body
  const charURLList = JSON.parse(body).characters;

  // Iterates through each character URL to fetch character information
  // Makes a request to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parses the character information and prints the character's name
        // Resolves the promise to indicate completion
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
