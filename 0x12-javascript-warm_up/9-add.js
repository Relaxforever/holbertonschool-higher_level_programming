#!/usr/bin/node

function add (a, b) {
  console.log(Number(a + b));
}
add(Number(process.argv[2]), Number(process.argv[3]));
