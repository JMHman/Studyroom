const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const M = input[0];
const N = input[1];

function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

let primeList = [];
for (let i = M; i <= N; i++) {
    if (isPrime(i)) {
        primeList.push(i);
    }
}

if (primeList.length > 0) {
    const primeSum = primeList.reduce((sum, val) => sum + val, 0);
    const primeMin = Math.min(...primeList);
    console.log(primeSum);
    console.log(primeMin);
} else {
    console.log(-1);
}
