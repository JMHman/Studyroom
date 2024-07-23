const fs = require('fs');

let [A, B] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

if (B >= 45) {
    B = B - 45
} else {
    if (A != 0) {
        A = A - 1
    } else {
        A = 23
    }
    B = B + 15
}

console.log(A,B)