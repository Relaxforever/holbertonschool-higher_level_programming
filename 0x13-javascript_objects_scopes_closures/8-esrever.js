#!/usr/bin/node

exports.esrever = function (list) {
  let revert = list.length - 1;
  const listR = [];
  for (let cont = 0; cont < list.length; cont++, revert--) {
    listR[cont] = list[revert];
  }
  return listR;
};
