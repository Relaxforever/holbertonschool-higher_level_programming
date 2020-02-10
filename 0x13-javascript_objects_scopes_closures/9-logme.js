#!/usr/bin/node
let cont = 0;
exports.logMe = function (item) {
  console.log(cont + ': ' + item);
  cont++;
};
