const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const alphabet = Array.from({length: 26}, (_, i) => String.fromCharCode(97 + i));
const count = {};

// 초기화
alphabet.forEach(char => {
    count[char] = 0;
});

// 문자열 순회하며 카운트 증가
for (let char of input) {
    if (count[char] !== undefined) {
        count[char]++;
    }
}

// 결과 출력
const result = alphabet.map(char => count[char]);
console.log(result.join(' '));
