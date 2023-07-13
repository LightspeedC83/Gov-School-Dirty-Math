const letters = ["a", "b", "c"]

// string is ok when there are not two adjacent identical letter blocks
function isStringOk(string: string) {
    for (let i = 0; i < string.length; i++) {
        for (let j = i + 1; j <= string.length; j++) {
            const str = string.slice(i, j);

            const nextIndex = string.indexOf(str, string.indexOf(str, i) + 1);
            if (nextIndex === -1) {
                break;
            }

            if (nextIndex - string.indexOf(str, i) === str.length) {
                return false;
            }
        }
    }

    return true;
}

const go = false;

if (go) {
    console.log(isStringOk("abab")) // false

    console.log(isStringOk("abcab")) // true

    console.log(isStringOk("aba")) // true

    console.log(isStringOk("abaa")) // false

    console.log(isStringOk("abaab")) // false

    console.log(isStringOk("abaaba")) // false

    console.log(isStringOk("abacabcbacab")) // true

    console.log(isStringOk("abcabacabcacabcacabcacabacabcacacabca")) // false

} else {
    const random = (min: number, max: number) => Math.floor(Math.random() * (max - min + 1)) + min;
    
    let len = 0;
    let string = ""
    let i = 0;
    while (true) {
        string += letters[i]

        if (isStringOk(string)) {
            if (string.length > len) {
                len = string.length
                console.log(string)
            }
        } else {
            string = ""
        }

        i = random(0, letters.length - 1)
    }
}