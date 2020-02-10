#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocurr = 0;
  for (let cont = 0; cont < list.length; cont++) {
    if (list[cont] === searchElement) {
      ocurr++;
    }
  }
  return ocurr;
};
