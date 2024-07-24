const fs = require('fs');

// 입력을 읽어옵니다.
const [n, k] = fs.readFileSync(0, 'utf8').trim().split(' ').map(Number);

let a = [];

// 1부터 n까지 순회하여 n의 약수를 찾습니다.
for (let x = 1; x <= n; x++) {
    if (n % x === 0) {
        a.push(x);
    }
}

// 약수의 개수가 k 이상이면 k번째 약수를 출력합니다.
if (a.length >= k) {
    console.log(a[k - 1]);
} else {
    console.log(0);
}
