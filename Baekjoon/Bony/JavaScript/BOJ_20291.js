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
//   "8",
//   "sbrus.txt",
//   "spc.spc",
//   "acm.icpc",
//   "korea.icpc",
//   "sample.txt",
//   "hello.world",
//   "sogang.spc",
//   "example.txt",
// ];

const solution = () => {
  const num = parseInt(input[0]);
  const files = input.slice(1).map((el) => el);
  const filesObj = {};
  let answer = "";

  //   filesArr = [];

  files.forEach((file) => {
    let [first, second] = file.split(".");

    if (filesObj[second]) {
      filesObj[second] += 1;
    } else {
      filesObj[second] = 1;
    }
  });

  const filesArr = Object.entries(filesObj).sort();

  //   Object.entries(filesObj).forEach((file) => {
  //     let [key, value] = file;
  //     filesArr.push([key, value]);
  //   });

  //   filesArr.sort();

  filesArr.forEach((file) => {
    let [key, value] = file;

    answer += key + " " + value + "\n";
  });

  console.log(answer);
};

//solution();
