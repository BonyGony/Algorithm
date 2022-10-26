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

// const input = [
//   "3 8",
//   "20103324",
//   "20133221",
//   "20133221",
//   "20093778",
//   "20140101",
//   "01234567",
//   "20093778",
//   "20103325",
// ];

// const input = [
//   "3 8",
//   "20103324",
//   "20103324",
//   "20103324",
//   "20103324",
//   "20103324",
//   "20103324",
//   "20103324",
//   "20103324",
// ];

const solution = () => {
  const idSet = new Set();
  const [k, l] = input[0].split(" ").map((el) => parseInt(el));
  const studentIds = input.slice(1).map((el) => el);
  let answer = "";

  studentIds.forEach((studentId) => {
    idSet.delete(studentId);
    idSet.add(studentId);
  });

  idArr = [...idSet];

  for (let i = 0; i < k && idArr[i] !== undefined; i++) {
    answer = answer + idArr[i] + "\n";
  }

  console.log(answer);
};

// solution();

// for문 중복조건
// js Set은 순서 가능
// 명칭 명확
// 커밋메세지 콘솔창
