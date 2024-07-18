const fs = require('fs');

// 표준 입력을 읽어와서 문자열로 변환하고 공백으로 분리
const input = fs.readFileSync(0).toString().trim().split('\n');

// 입력 데이터 확인
const x = parseInt(input[0]);
const y = parseInt(input[1]);

// 사분면 판별
if (x > 0) {
    if (y > 0) {
        console.log("1");  // 제1사분면
    } else {
        console.log("4");  // 제4사분면
    }
} else {
    if (y > 0) {
        console.log("2");  // 제2사분면
    } else {
        console.log("3");  // 제3사분면
    }
}
