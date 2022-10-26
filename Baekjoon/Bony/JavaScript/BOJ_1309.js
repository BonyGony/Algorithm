// 1309 동물원

// const input = ["4"];
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
  const dp = Array(n + 1).fill(0);

  dp[1] = 3;
  dp[2] = 7;

  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901;
  }

  console.log(dp[n]);
};

// solution();
