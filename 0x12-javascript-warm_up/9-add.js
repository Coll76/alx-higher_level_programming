#!/usr/bin/node
// prints the addition of 2 integers
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (!isNaN(a) && !isNaN(b)) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
