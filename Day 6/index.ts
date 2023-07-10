/* return an array of numbers inclusively between a and b */
function listNumbers(a: number, b: number): number[] {
    let result: number[] = [];
    for (let i = a; i <= b; i++) {
        result.push(i);
    }

    return result;
}

enum Player {
    P1,
    P2
}

class Game {
    state: [number, number, number];
    player: Player;
    numberOfMoves = 0;

    constructor(state: [number, number, number] = [3, 5, 7]) {
        this.state = state;
        this.player = Player.P1;
    }

    clone(): Game {
        const game = new Game();
        game.state = [...this.state];
        game.player = this.player;
        game.numberOfMoves = this.numberOfMoves;

        return game;
    }

    possibleMoves(): [row: number, amount: number][] {
        const result: [number, number][] = [];
        this.state.forEach((_, index) => {
            const possibleMoves = listNumbers(1, this.state[index]);
            possibleMoves.forEach(move => {
                result.push([index, move]);
            });
        });

        return result;
    }

    move(row: number, amount: number): void {
        this.state[row] -= amount;
        this.player = this.player === Player.P1 ? Player.P2 : Player.P1;
        this.numberOfMoves++;
    }

    gameOver(): boolean {
        return this.state.every(row => row === 0);
    }

    isWinningMove(move: [row: number, amount: number]): boolean {
        const gameCopy = this.clone();
        gameCopy.move(...move);
        return gameCopy.gameOver();
    }
}

function negamax(game: Game): number {
    for (const move of game.possibleMoves()) {
        if (game.isWinningMove(move)) {
            return (3 + 5 + 7) - game.numberOfMoves;
        }
    }

    let bestValue = -Infinity;
    game.possibleMoves().forEach(move => {
        const gameCopy = game.clone();
        gameCopy.move(...move);
        const value = -negamax(gameCopy);
        bestValue = Math.max(bestValue, value);
    });

    return bestValue;
}

const args = Deno.args.length > 0;

if (args) {
    const pos = Deno.args[0].split("-").map(Number);
    console.assert(pos.length === 3, "Invalid input - expected 3 numbers");
    const game = new Game(pos as [number, number, number]);
    console.log(negamax(game));
}

if (!args) {

    // get every config and negamax it
    const configs = [];
    for (let a = 0; a <= 7; a++) {
        for (let b = 0; b <= 5; b++) {
            for (let c = 0; c <= 3; c++) {
                configs.push([a, b, c]);
            }
        }
    }

    for (const config of configs) {
        const game = new Game(config as [number, number, number]);
        const value = negamax(game);
        console.log(config, value);
    }
}