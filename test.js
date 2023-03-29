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

// console.log(sum(1, 2, 3, 4, 4, 8, 9, 5, 11, 21, 32, 332, 23));

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


// ==============================================
// ==============================================

const MONTHS = {
  JAN: 1,
  FEB: 2,
  MAR: 3,
  APR: 4,
  MAY: 5,
  JUN: 6,
  JUL: 7,
  AUG: 8,
  SEP: 9,
  OCT: 10,
  NOV: 11,
  DEC: 12,
};

let events = [
  { event: "dance", month: "MAR" },
  { event: "farmers market", month: "JUN" },
  { event: "parade", month: "JAN" },
];

// sort events by ascending order -> O(NlogN)
function sortByMonth(events) {
  return events.sort((a, b) => MONTHS[a.month] - MONTHS[b.month]);
}
// sortByMonth(events);
// console.log(events);

// ==================================================
// ==================================================



// const user = { name: 'bob' }
// console.log(user && user.name);

// const user2 = undefined;
// console.log(user2.name); // error

// --> to continue execution of thr program and to avoid error like this
// const user2 = undefined;
// console.log(user2 && user2.name); // undefined

/*
The function friendName currently retrieves the name property from the friend.
The problem is, sometimes friend is undefined. When this is the case, let's return undefined without throwing an exception.
*/
// function friendName(friend) {
//   return friend && friend.name;
// }


// ==================================================
// ==================================================

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
