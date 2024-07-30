const fs = require('fs');

// 입력 받기
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trim(), 10);

function primeFactors(n) {
    const factors = [];
    
    // 2로 나누기
    while (n % 2 === 0) {
        factors.push(2);
        n /= 2;
    }
    
    // 3 이상의 홀수로 나누기
    for (let i = 3; i * i <= n; i += 2) {
        while (n % i === 0) {
            factors.push(i);
            n /= i;
        }
    }
    
    // 남은 소수 처리
    if (n > 2) {
        factors.push(n);
    }
    
    return factors;
}

// N이 1인 경우 아무것도 출력하지 않음
if (N !== 1) {
    const factors = primeFactors(N);
    factors.forEach(factor => console.log(factor));
}
