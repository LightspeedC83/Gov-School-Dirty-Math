let str = "0"

for (let i = 0; i < 7; i++) {
    // take the difference between the current entry and the prev entry,
    // e.g. 0 1 1 0 turns into 1 0 -1
    const sequence = str.split("").map((x, i, arr) => {
        if (i === 0) {
            return null;
        }

        return parseInt(x) - parseInt(arr[i - 1]);
    }).slice(1);
    console.log(sequence.join(" "))
    str += str.split('').map((x) => x === '0' ? '1' : '0').join('')
}

