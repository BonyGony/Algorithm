// const input = ["5"]; 9655 돌 게임
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

const input = [];

const solution = () => {
  const n = Number(input[0]);

  console.log(n % 2 === 0 ? "CY" : "SK");
};

// solution();
