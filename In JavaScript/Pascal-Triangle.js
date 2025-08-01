function fact(n) {
    let f = 1;
    for (let i = 1; i <= n; i++) f *= i;
    return f;
}

function ncr(n, r) {
    return fact(n) / (fact(r) * fact(n - r));
}

const prompt = require('prompt-sync')();
let n = parseInt(prompt("Enter number of rows: "));

for (let i = 0; i < n; i++) {
    let row = " ".repeat(n - i);
    for (let j = 0; j <= i; j++) {
        row += ncr(i, j) + " ";
    }
    console.log(row);
}
