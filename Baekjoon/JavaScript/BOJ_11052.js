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
  const arr = input[1].split(" ").map((el) => Number(el));
  const dp = Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
      dp[i] = Math.max(dp[i], dp[i - j] + arr[j - 1]);
    }
  }

  console.log(dp[n]);
};
