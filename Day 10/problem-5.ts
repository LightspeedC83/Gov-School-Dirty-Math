type Fraction = [numerator: number, denominator: number];

function sortFractions(fractions: Fraction[]): Fraction[] {
    return fractions.sort((a, b) => a[0] / a[1] - b[0] / b[1]);
}

function filterUniqueFractions(fractions: Fraction[]): Fraction[] {
    const uniqueFractions: Fraction[] = [];
    for (const fraction of fractions) {
        if (!uniqueFractions.some((x) => x[0] / x[1] === fraction[0] / fraction[1])) {
            uniqueFractions.push(fraction);
        }
    }

    return uniqueFractions;
}

function genRow(row: number): Fraction[] {
    if (row == 0) {
        return [[0, 1], [1, 1]];
    }

    const newFractions: Fraction[] = [];
    for (let i = 1; i < row; i++) {
        newFractions.push([i, row]);
    }

    return filterUniqueFractions(sortFractions([
        ...genRow(row - 1),
        ...newFractions,
    ]));
}

// print row 5 like so:
// 0 1
// ---...
// 1 5
// 2 3 5 7 11 13 19 23 29 33 43 47 59 65 73
for (let i = 1; i <= 200; i++) {
    // const row = Deno.args[0] ? parseInt(Deno.args[0]) : 5;
    const row = i;
    const fractions = genRow(row);

    console.log(i + " " + fractions.length)

    // console.log(fractions.map((x) => `${x[0]}`).join("  "));
    // console.log(`${i}-${fractions.length}: ` + fractions.map((x) => `${x[1]}`).join("  "));

    // console.log(fractions.reduce((acc, x) => acc + x[0], 0));
    // console.log(fractions.reduce((acc, x) => acc + x[1], 0));

    // console.log(fractions.reduce((acc, x) => acc + x[0] / x[1], 0));
}