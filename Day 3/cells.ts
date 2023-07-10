const { columns } = Deno.consoleSize();

let cells: number[] = Array(columns).fill(10);

function iterate(cells: number[]): number[] {
    return cells.map((cell, i) => {
        return cell * 0.8 
            + (i > 0 ? cells[i - 1] * 0.1 : 0)
            + (i < cells.length - 1 ? cells[i + 1] * 0.1 : 0)
    })
}

const blocks = ["█", "▇", "▆", "▅", "▄", "▃", "▂", "▁", " "];
let maxHeight = 0;

function displayCells(cells: number[]) {
    const heightMap = cells.map(cell => {
        const newCell = cell / 10 * (Math.max(Deno.consoleSize().rows - 3, 1));
        const str = blocks[0].repeat(Math.floor(newCell)) + blocks[Math.round(8 - (newCell % 1) * 8)];

        if (str.length > maxHeight) {
            maxHeight = str.length;
        }
        
        return str;
    })

    let consoleStr = "";

    for (let i = maxHeight - 1; i >= 0; i--) {
        consoleStr += heightMap.map(height => {
            return height[i] || " ";
        }).join("") + "\n";
    }

    console.log(consoleStr.trimEnd() == "" ? consoleStr : consoleStr.trimEnd());
}

console.clear();

// we want to iterate forever while keeping track of the iteration number
// deno-lint-ignore for-direction
for (let t = 0; t >= 0 ; t++) {
    console.log("\x1B[0f")
    
    displayCells(cells)
    // Deno.stdout.writeSync(new TextEncoder().encode("-".repeat(10) + `iter ${t}`)) draw in the middle of the line
    Deno.stdout.writeSync(new TextEncoder().encode(" ".repeat(Math.floor((columns - `iter ${t}`.length) / 2)) + `iter ${t}`))
    
    cells = iterate(cells)
}
