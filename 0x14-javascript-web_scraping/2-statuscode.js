#!/usr/bin/node
const axios = require('axios');

const URL = process.argv[2];

axios.get(URL).then((response) => {
  console.log('code: ' + response.status);
})
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
