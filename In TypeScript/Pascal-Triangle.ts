function fact(n: number): number {
    let f = 1;
    for (let i = 1; i <= n; i++) f *= i;
    return f;
}

function ncr(n: number, r: number): number {
    return fact(n) / (fact(r) * fact(n - r));
}

const readline = require("readline-sync");
const n = parseInt(readline.question("Enter number of rows: "));

for (let i = 0; i < n; i++) {
    let row = " ".repeat(n - i);
    for (let j = 0; j <= i; j++) {
        row += ncr(i, j) + " ";
    }
    console.log(row);
}
