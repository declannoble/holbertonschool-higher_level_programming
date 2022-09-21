#!/usr/bin/node
const URL = process.argv[2];
const axios = require('axios');
let wedgeCount = 0;
let allMovies = 0;
axios.get(URL)
  .then(function (response) {
    allMovies = response.data.results;
    for (const movieCount in allMovies) {
      const characters = allMovies[movieCount].characters;
      for (const charCount in characters) {
        if (characters[charCount].includes('18')) {
          wedgeCount = wedgeCount + 1;
        }
      }
    }
    console.log(wedgeCount);
  });
