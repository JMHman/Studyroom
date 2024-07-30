const fs = require('fs');

// 입력 받기
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trim(), 10);

function primeFactors(n) {
    const factors = [];
    let i = 2;
    
    while (i * i <= n) { // i가 n의 제곱근까지 반복
        if (n % i === 0) { // i로 나누어 떨어지면
            while (n % i === 0) { // 계속 나누어떨어질 때까지
                factors.push(i);
                n /= i;
            }
        }
        i++;
    }
    
    if (n > 1) { // n이 1보다 크면, n 자체가 소수
        factors.push(n);
    }
    
    return factors;
}

// N이 1인 경우 아무것도 출력하지 않음
if (N !== 1) {
    const factors = primeFactors(N);
    factors.forEach(factor => console.log(factor));
}
