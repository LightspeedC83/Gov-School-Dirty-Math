// This problem can also be represnted as building a sequence using the characters 0 and 1.
// Starting with 0, and in each step, writing the sequence but flipping each digit.
// e.g.:
// 0
// 0 1
// 0 1 1 0
// where each one is the parity of the amount of ones in that n step as related to this problem.
// aka, this file and problem-1.ts are strongly related.]

for (let i = 0; i <= 200; i++) {
    const amountOfOnes = i.toString(2).split('').filter((x) => x === '1').length;
    // console.log(`${i} - ${amountOfOnes % 2 == 0 ? 0 : 1} (${i.toString(2)})`);
    // console.log(amountOfOnes % 2 == 0 ? 0 : 1)
    Deno.stdout.writeSync(new TextEncoder().encode(`${amountOfOnes % 2 == 0 ? 0 : 1}`));
}

console.log()
