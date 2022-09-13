#!/usr/bin/node

const fs = require('fs');
const axios = require('axios').default;
const URL = process.argv[2];
const filePath = process.argv[3];

axios.get(URL).then((response) => {
  fs.writeFile(filePath, response.data, 'utf-8', function (err) {
    if (err) {
	    console.log(err);
    }
  });
});
