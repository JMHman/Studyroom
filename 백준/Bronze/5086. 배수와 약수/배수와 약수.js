const fs = require('fs');

// 파일에서 입력을 읽어옵니다. (동기 방식)
const input = fs.readFileSync('/dev/stdin', 'utf8');

// 입력된 모든 라인을 저장할 배열로 분리합니다.
const lines = input.trim().split('\n');

// 각 줄을 처리합니다.
for (let i = 0; i < lines.length; i++) {
  // 줄을 공백으로 분리하여 두 숫자를 얻습니다.
  let [a, b] = lines[i].split(' ').map(Number);

  // 종료 조건
  if (a === 0 && b === 0) {
    break;
  }

  // 관계 판단 및 출력
  if (b % a === 0) {
    console.log('factor');
  } else if (a % b === 0) {
    console.log('multiple');
  } else {
    console.log('neither');
  }
}
