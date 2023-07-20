const arr: string[][] = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o']
]

// shuffle every element in the 2d array
function shuffle(arr: readonly string[][]) {
    const flattenedArr = arr.flat();
    const newArr: string[][] = [];
    for (let i = 0; i < arr.length; i++) {
        const subArr = arr[i];
        const newSubArr: string[] = [];
        for (let j = 0; j < subArr.length; j++) {
            const index = Math.floor(Math.random() * flattenedArr.length);
            newSubArr.push(flattenedArr[index]);
            flattenedArr.splice(index, 1);
        }
        newArr.push(newSubArr);
    }

    return newArr;
}

function getPairs(arr: readonly string[][]) {
    const newArr: string[][] = [];
    for (let i = 0; i < arr.length; i++) {
        const subArr = arr[i];
        for (let j = 0; j < subArr.length; j++) {
            for (let k = j + 1; k < subArr.length; k++) {
                newArr.push([subArr[j], subArr[k]]);
            }
        }
    }
    return newArr;
}

let longest = 0;
while (true) {
    let count = 0;
    let length = 0;
    const arrs: string[][][] = [];
    const pairs: Record<string, boolean>[] = [];
    loop: while (true) {
        const shuffled = shuffle(arr);
        const pairsArr = getPairs(shuffled);
        for (const pair of pairsArr) {
            const key = pair.join('');
            if (pairs[key]) {
                count++;

                if (count % 100000 === 0) {
                    break loop;
                }
                continue loop;
            }
            pairs[key] = true;
        }

        length++;

        arrs.push(shuffled);

        if (length > longest) {
            longest = length;
            console.log(arrs);
            console.log(longest);
        }
    }
}