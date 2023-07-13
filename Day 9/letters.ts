const letters = ["a", "b"]

// string is ok when there are not two adjacent identical letter blocks
function isStringOk(string: string) {
    for (let i = 0; i < string.length; i++) {
        for (let j = i + 1; j <= string.length; j++) {
            const str = string.slice(i, j);
            if (string.indexOf(str, string.indexOf(str) + 1) === -1) {
                break;
            }
            if (Math.abs(string.indexOf(str) - string.indexOf(str, string.indexOf(str) + 1)) === str.length) {
                return false;
            }
        }
    }

    return true;
}

console.log(isStringOk("abab")) // false

console.log(isStringOk("abcab")) // true

console.log(isStringOk("aba")) // true

console.log(isStringOk("abaa")) // true

let string = ""
let finalStrings = new Set<string>();
// loop: while (true) {
//     // try to continiously add to the array and backtrack when it doesn't work

//     for (let i = 0; i < letters.length; i++) {
//         string += letters[i];
//         console.log(string)
//         if (!isStringOk(string)) {
//             string = string.slice(0, -1);
//             if (finalStrings.has(string)) {
//                 break loop;
//             }
//             finalStrings.add(string);
//             console.log(string)
//             break;
//         }
//     }
// }