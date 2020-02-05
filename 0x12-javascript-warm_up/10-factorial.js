#!/usr/bin/node

function factorial (a) {
  if (Number(a) === 0) {
    return (1);
  }
  if (Number(a) === 1) {
    return (1);
  }
  return (Number(a) * factorial(Number(a - 1)));
}
if (!process.argv[2]) { console.log(1); } else { console.log(factorial(Number(process.argv[2]))); }
