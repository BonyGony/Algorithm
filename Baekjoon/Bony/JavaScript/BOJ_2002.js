// const input = [
//   "4",
//   "ZG431SN",
//   "ZG5080K",
//   "ST123D",
//   "ZG206A",
//   "ZG206A",
//   "ZG431SN",
//   "ZG5080K",
//   "ST123D",
// ];

// const input = [
//   "5",
//   "ZG508OK",
//   "PU305A",
//   "RI604B",
//   "ZG206A",
//   "ZG232ZF",
//   "PU305A",
//   "ZG232ZF",
//   "ZG206A",
//   "ZG508OK",
//   "RI604B",
// ];

// const input = [
//   "5",
//   "ZG206",
//   "PU234",
//   "OS945",
//   "ZG431",
//   "ZG596",
//   "ZG596",
//   "OS945",
//   "ZG206",
//   "PU234",
//   "ZG431",
// ];

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solution();
  process.exit();
});

let input = [];

const solution = () => {
  const n = Number(input[0]);
  const startCars = input.slice(1, 1 + n).map((car) => car);
  const endCars = input.slice(1 + n, 2 * n + 1).map((car) => car);
  const carsMap = new Map();
  let count = 0;

  for (let i = 0; i < n; i++) {
    carsMap.set(startCars[i], i);
  }

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (carsMap.get(endCars[i]) > carsMap.get(endCars[j])) {
        count++;
        break;
      }
    }
  }

  console.log(count);
};

// solution();
