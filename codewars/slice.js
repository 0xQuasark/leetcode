'use strict';

// Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

function removeChar(str){
 //You got this!
  let cutString = '';
  for (let i = 1; i < str.length-1; i++) {
    // cutString.push(str[i]);
    cutString += str[i];
  }
  return cutString;
};

function removeChar(str) {
  return str.slice(1, -1);
}


console.log(removeChar('hello'));