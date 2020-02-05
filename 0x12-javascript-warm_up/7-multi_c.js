#!/usr/bin/node
if (Number(process.argv[2])) {
  for (let cont = 0; cont < Number(process.argv[2]); cont++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
