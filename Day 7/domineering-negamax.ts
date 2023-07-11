enum Player {
    P1,
    P2
}

interface Game<Move> {
    readonly numberOfMoves: number;
    readonly size: number;
    clone(): Game<Move>;
    possibleMoves(): Move[];
    move(move: Move): void;
    gameOver(): boolean;
    isWinningMove(move: Move): boolean;
}

class Domineering implements Game<[row: number, col: number]> {
    private state: boolean[][];
    player: Player;
    numberOfMoves = 0;
    readonly size: number;

    constructor(width = 4, height = 4) {
        this.state = Array.from({ length: height }, () => Array.from({ length: width }, () => false));
        this.player = Player.P1;
        this.size = width * height;
    }

    clone(): Game<[row: number, col: number]> {
        const game = new Domineering();
        game.state = [...this.state];
        game.player = this.player;
        game.numberOfMoves = this.numberOfMoves;

        return game;
    }

    possibleMoves(): [row: number, amount: number][] {
        const result: [number, number][] = [];

        if (this.player === Player.P1) {
            for (let row = 0; row < this.state.length - 1; row++) {
                for (let col = 0; col < this.state[row].length; col++) {
                    if (!this.state[row][col] && !this.state[row + 1][col]) {
                        result.push([row, col]);
                    }
                }
            }
        } else {
            for (let row = 0; row < this.state.length; row++) {
                for (let col = 0; col < this.state[row].length - 1; col++) {
                    if (!this.state[row][col] && !this.state[row][col + 1]) {
                        result.push([row, col]);
                    }
                }
            }
        }

        return result;
    }

    move(move: [row: number, col: number]): void {
        const [row, col] = move;
        this.state[row][col] = true;
        if (this.player === Player.P1) {
            this.state[row + 1][col] = true;
        } else {
            this.state[row][col + 1] = true;
        }
        this.player = this.player === Player.P1 ? Player.P2 : Player.P1;
        this.numberOfMoves++;
    }

    gameOver(): boolean {
        return this.possibleMoves().length === 0;
    }

    isWinningMove(move: [row: number, amount: number]): boolean {
        const gameCopy = this.clone();
        gameCopy.move(move);
        return gameCopy.gameOver();
    }
}

function negamax(game: Game<unknown>): number {
    for (const move of game.possibleMoves()) {
        if (game.isWinningMove(move)) {
            return game.size - game.numberOfMoves;
        }
    }

    let bestValue = -Infinity;
    game.possibleMoves().forEach(move => {
        const gameCopy = game.clone();
        gameCopy.move(move);
        const value = -negamax(gameCopy);
        bestValue = Math.max(bestValue, value);
    });

    return bestValue;
}

const size = Deno.args[0] ? parseInt(Deno.args[0]) : 4;

const game = new Domineering(size, size);
console.log(game.possibleMoves())
const value = negamax(game);
console.log(value);