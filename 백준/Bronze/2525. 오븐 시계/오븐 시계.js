const input = require('fs').readFileSync(0).toString().trim().split('\n');
const [A,B] = input[0].split(' ').map(Number);
const C = parseInt(input[1]);

let hours = A;
let minutes = B + C;

if (minutes >= 60) {
    hours += Math.floor(minutes / 60);
    minutes = minutes % 60;
}


hours = hours % 24;

console.log(hours, minutes);
