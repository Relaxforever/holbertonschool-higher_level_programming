#!/usr/bin/node
const arrayNumbers = [];
let cont = process.argv.length;
if (!process.argv[2] || cont === 3) {
  console.log(0);
} else {
  for (let i = 2; i < cont; i++) {
    arrayNumbers.push(Number(process.argv[i]));
  }
  const max = arrayNumbers.reduce(function (a, b) {
    return Math.max(a, b);
  });
  let middle = 0;
  for (cont = 0; cont < arrayNumbers.length; cont++) {
    if (arrayNumbers[cont] < max) {
      if (arrayNumbers[cont] >= middle) {
        middle = arrayNumbers[cont];
      }
    }
  }
  console.log(middle);
}
