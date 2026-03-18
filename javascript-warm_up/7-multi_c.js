#!/usr/bin/node

const x = Number(process.argv[2]);

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x * 3; i++) {
    console.log('C is fun');
  }
}
