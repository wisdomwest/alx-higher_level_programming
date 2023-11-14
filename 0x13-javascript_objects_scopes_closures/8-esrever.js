#!/usr/bin/node

exports.esrever = function (list) {
  const rList = [];
  let i = list.length - 1;
  while (i >= 0) {
    rList.push(list[i]);
    i -= 1;
  }

  return rList;
};
