const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const [A, B, C] = input;
const result = A * B * C;
const resultStr = result.toString();

const digitCount = {};
for (let i = 0; i < 10; i++) {
    digitCount[i] = 0;
}

for (const char of resultStr) {
    digitCount[char]++;
}

// 결과 출력
for (let i = 0; i < 10; i++) {
    console.log(digitCount[i]);
}
