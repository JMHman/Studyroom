const fs = require('fs');

// 소수 판별 함수 (효율적인 방법)
function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

// 입력을 읽어옵니다.
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = parseInt(input[0]);
const numbers = input[1].split(' ').map(Number);

// 소수의 개수를 셉니다.
let primeCount = 0;
for (let i = 0; i < N; i++) {
    if (isPrime(numbers[i])) {
        primeCount++;
    }
}

// 소수의 개수를 출력합니다.
console.log(primeCount);