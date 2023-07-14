let num = 9;

for (let i = 0; i < 100; i++) {
    console.log(num);
    if (num % 2 === 0) {
        num /= 2;
    } else {
        num = num * 3 + 1;
    }
}

console.log(num);
