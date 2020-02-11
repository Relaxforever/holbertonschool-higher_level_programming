#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf-8' }, function writeData (err) {
  if (err) {
    console.log(err);
  }
});
