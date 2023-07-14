let str = "0"

for (let i = 0; i < 7; i++) {
    console.log(`${str} - ${parseInt(str, 2)}`)
    str += str.split('').map((x) => x === '0' ? '1' : '0').join('')
}

console.log(str)
