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
  let cnt = 0;
  const dp = Array(1000001).fill(0);

  dp[1] = 999;
  dp[2] = 1;
  dp[3] = 999;
  dp[4] = 2;
  dp[5] = 1;

  for (let i = 6; i <= n; i++) {
    dp[i] = Math.min(dp[i - 2] + 1, dp[i - 5] + 1);
  }

  console.log(dp[n] === 999 ? -1 : dp[n]);
};

// solution();
