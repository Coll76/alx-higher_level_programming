#!/usr/bin/node
// prints the first argument passed to it:
const numArgs = process.argv[2];
if (numArgs === undefined) {
  console.log('No argument');
} else {
  console.log(numArgs);
}
