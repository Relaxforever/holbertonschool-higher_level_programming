#!/usr/bin/node
const requests = require('request');

requests(process.argv[2], function writestatus (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let cont = 0;
    const mTitle = JSON.parse(body);
    const allValues = Object.values(mTitle.results);
    for (const values of allValues) {
      if (values.characters.includes('https://swapi.co/api/people/18/')) { cont++; }
    }
    console.log(cont);
    return cont;
  }
});
