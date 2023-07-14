// This problem can also be represnted as building a sequence using the characters 0 and 1.
// Starting with 0, and in each step, writing the sequence but flipping each digit.
// e.g.:
// 0
// 0 1
// 0 1 1 0
// where each one is the parity of the amount of ones in that n step as related to this problem.
// aka, this file and problem-1.ts are strongly related.]

let lastNum = 0;
for (let j = 0; j <= 200; j++) {
    let str = "";
    for (let i = 0; i <= j; i++) {
        const amountOfOnes = i.toString(2).split('').filter((x) => x === '1').length;
        str += `${amountOfOnes % 2 == 0 ? 0 : 1}`;
    }
    const num = parseInt(str, 2);
    console.log(lastNum + lastNum - num);
    // console.log(num)
    lastNum = num;
}
