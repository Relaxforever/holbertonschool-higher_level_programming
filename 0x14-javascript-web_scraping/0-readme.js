#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], { encoding: 'utf-8' }, function readData (err, data) {
  if (err) {
    console.log(data);
  } else {
    console.log(data);
  }
});
