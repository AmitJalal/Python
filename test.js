function sum(a, b, ...args) {
  let sum = 0;
  for (const ele of [...args]) sum += ele;
  //   console.log(...args);
  //   console.log(Array(...args));
  //   console.log(new Array(...args));
  //   console.log([...args].length);
  //   console.log(sum);
  return a + b + sum;
}

console.log(sum(1, 2, 3, 4, 4, 8, 9, 5, 11, 21, 32, 332, 23));

// let a4 = 13;

// function scope() {
//   a4 = 12;
//   console.log(a4);
// }

// console.log(a4);
// scope();
// console.log(a4);

// const li = [1, 2, 3, 4, 5];
// const li2 = li;
// console.log(li === li2);

// const li = [1, 2, 3, 4, 5];
// let li2 = li;
// li2 = [1, 2, 3, 4, 5, 6];

// const li = [1, 2, 3, 4, 5];
// let li2 = li;
// li2[1] = [1, 2, 3, 4, 5, 6];

// console.log(li === li2);
// console.log(li, li2)
