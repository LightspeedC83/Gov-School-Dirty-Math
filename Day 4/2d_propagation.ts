import * as mod from "https://deno.land/std@0.193.0/fmt/colors.ts";


function I(x: number, y: number, t: number): number {
    if (t == 0) {
        if (x == 2 && y == 3) {
            return 0.1;
        } else {
            return 0;
        }
    }

    return U(x, y, t - 1) * (0.15 * I(x - 1, y, t - 1) + I(x, y - 1, t - 1) + I(x + 1, y, t - 1) + I(x, y + 1, t - 1)) + 0.40 * I(x, y, t - 1);
}

function U(x: number, y: number, t: number): number {
    if (t == 0) {
        if (x == 2 && y == 3) {
            return 0.9;
        } else {
            return 1;
        }
    }

    return U(x, y, t - 1) - I(x, y, t - 1);
}

function R(x: number, y: number, t: number): number {
    if (t == 0) return 0;

    return R(x, y, t - 1) + I(x, y, t - 1);
}

type Position = {
    values: [i: number, u: number, r: number]
}
// const colors = [mod.red, mod.green, mod.blue]; use a mask
const colors: [number, number, number][] = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]
];
const block = "█"

function calc(time: number) {
    // fill a cell grid from x = 0 to x = 6, y = 0 to y = 6
    const grid: Position[][] = Array(7).fill(0).map((_, x) => Array(7).fill(0).map((_, y) => {
        return {
            values: [I(x, y, time), U(x, y, time), R(x, y, time)]
        }
    }));

    // get the length longest number in the grid (toFixed(2))
    const longest = grid.flat().map(cell => cell.values.map(value => value.toFixed(2).length).reduce((a, b) => Math.max(a, b))).reduce((a, b) => Math.max(a, b));

    const longestI = grid.flat().map(cell => cell.values[0]).reduce((a, b) => Math.max(a, b));
    const longestU = grid.flat().map(cell => cell.values[1]).reduce((a, b) => Math.max(a, b));
    const longestR = grid.flat().map(cell => cell.values[2]).reduce((a, b) => Math.max(a, b));

    const smallestI = grid.flat().map(cell => cell.values[0]).reduce((a, b) => Math.min(a, b));
    const smallestU = grid.flat().map(cell => cell.values[1]).reduce((a, b) => Math.min(a, b));
    const smallestR = grid.flat().map(cell => cell.values[2]).reduce((a, b) => Math.min(a, b));

    const longestTypes = [longestI, longestU, longestR];
    const smallestTypes = [smallestI, smallestU, smallestR];

    // print the grid
    console.log(grid.map(row => row.map(cell => {
        const [i, u, r] = cell.values.map(value => value.toFixed(2).padStart(longest, " "));

        return mod.bold(
            mod.red(i) + " " +
            mod.green(u) + " " +
            mod.blue(r)
        )
    }).join(" ")).join("\n"));

    console.log();

    // print each grid individually
    for (const type in [0, 1, 2]) {
        console.log()
        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                const largest = longestTypes[type];
                const smallest = smallestTypes[type];
                const size = largest.toFixed(2).length;

                const toColor = (value: number) => {
                    return Math.round((value - smallest) / (largest - smallest));
                }

                const color = colors[type].map(value => value * toColor(grid[x][y].values[type])).map(value => Math.round(value));
                
                Deno.stdout.writeSync(new TextEncoder().encode(mod.bold(mod.rgb24(block, {
                    r: color[0],
                    g: color[1],
                    b: color[2]
                }))));
            }

            console.log("");
        }
    }
}

const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

for (let t = 0; t < 10; t++) {
    calc(t);
    await sleep(5000);
}
