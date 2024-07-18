const fs = require('fs');

// 표준 입력을 읽어와서 문자열로 변환하고 공백으로 분리
const a = fs.readFileSync(0).toString().trim().split('\n');

if ((a % 4 ===0 && a % 100 !== 0) || a % 400 === 0) {
    console.log(1);
} else {
    console.log(0);
}
