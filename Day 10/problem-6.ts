for (let k = 1; k < 10_000_000; k++) {
    let num = k;
    console.log(`--- ${num} ---`)
    for (let i = 0; i < 100; i++) {
        if (num === 1) {
            break;
        }
        if (num % 2 === 0) {
            num /= 2;
        } else {
            num = num * 3 + 1;
        }
    }
}