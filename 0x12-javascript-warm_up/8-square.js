#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let cont = 0; cont < Number(process.argv[2]); cont++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else { console.log('Missing size'); }
