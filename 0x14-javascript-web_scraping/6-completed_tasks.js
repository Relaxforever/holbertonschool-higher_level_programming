#!/usr/bin/node
const requests = require('request');

requests(process.argv[2], function writestatus (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const datalist = {};
    const jsonbody = JSON.parse(body);
    jsonbody.forEach(element => {
      Object.entries(element).forEach(([key, value]) => {
        if (key === 'completed' && value === true) {
          if (element.userId in datalist) {
            datalist[element.userId] += 1;
          } else {
            datalist[element.userId] = 1;
          }
        }
      });
    });
    console.log(datalist);
  }
});
