#!/usr/bin/node
const requests = require('request');
const fs = require('fs');

requests(process.argv[2], function writestatus (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, function writeData (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
