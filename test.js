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



// ================= Alchemy University BlockChain --> Module JS =====================

function countElements(elements) {
  const count = new Map();
  for (const ele of elements) count.set(ele, count.get(ele) + 1 || 1);
  return Object.fromEntries(count);
}
// const elements = ["e", "k", "e", "z", "i", "z"];
// console.log(countElements(elements));

function playerHandScore(hand) {
  const scores = { K: 4, Q: 3, J: 2 };
  let score = 0;
  for (letter of hand) score += scores[letter];
  return score;
}

// console.log(playerHandScore("KQQ"));







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


