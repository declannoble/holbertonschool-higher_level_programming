#!/usr/bin/node
const axios = require('axios').default;
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(URL).then((response) => {
  console.log(response.data.title);
});
