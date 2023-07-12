enum Player {
    P1,
    P2
}

interface Game<Move> {
    readonly numberOfMoves: number;
    readonly size: number;
    clone(): unknown;
    clone<T extends Game<Move>>(): T;
    possibleMoves(): Move[];
    move(move: Move): void;
    gameOver(): boolean;
    isWinningMove(move: Move): boolean;
}

class Chomp implements Game<[row: number, col: number]> {
    state: boolean[][];
    player: Player;
    numberOfMoves = 0;
    readonly size: number;

    constructor(width = 8, height = 5) {
        this.state = Array.from({ length: height }, () => Array.from({ length: width }, () => false));
        this.player = Player.P1;
        this.size = width * height - 1;
    }

    clone<T extends Chomp>() {
        const game = new Chomp();
        game.state = structuredClone(this.state);
        game.player = this.player;
        game.numberOfMoves = this.numberOfMoves;

        return <T> game;
    }

    possibleMoves(): [row: number, col: number][] {
        const result: [number, number][] = [];
        // every single possible move is any square that is false
        // except for the bottom right square
        for (let row = 0; row < this.state.length; row++) {
            for (let col = 0; col < this.state[row].length; col++) {
                if (!this.state[row][col] && !(row === this.state.length - 1 && col === 0)) {
                    result.push([row, col]);
                }
            }
        }

        return result;
    }

    move(move: [row: number, col: number]): void {
        const [row, col] = move;
        for (let i = 0; i <= row; i++) {
            for (let j = col; j < this.state[i].length; j++) {
                this.state[i][j] = true;
            }
        }
        this.numberOfMoves++;
        this.player = this.player === Player.P1 ? Player.P2 : Player.P1;
    }

    gameOver(): boolean {
        return this.possibleMoves().length === 0;
    }

    isWinningMove(move: [row: number, col: number]): boolean {
        const gameCopy = this.clone();
        gameCopy.move(move);
        return gameCopy.gameOver();
    }

    toString(): string {
        return this.state.map(row => row.map(cell => cell ? 'X' : 'O').join(' ')).join('\n');
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
        const gameCopy = game.clone<Chomp>();
        gameCopy.move(move as any);
        const value = -negamax(gameCopy);
        bestValue = Math.max(bestValue, value);
    });

    return bestValue;
}

function bestMove(game: Game<unknown>): null | unknown {
    let bestValue = -Infinity;
    let bestMove: unknown = null;
    game.possibleMoves().forEach(move => {
        const gameCopy = game.clone<Chomp>();
        gameCopy.move(move as any);
        const value = -negamax(gameCopy);
        if (value > bestValue) {
            bestValue = value;
            bestMove = move;
        }
    });

    return bestMove;
}

const moves = Deno.args.map(arg => arg.split('-').map(Number).reverse() as [number, number])

const game = new Chomp(8, 5);
moves.forEach(move => game.move(move));
for (const move of game.possibleMoves()) {
    if (game.isWinningMove(move)) {
        console.log('winning move', move);
    }
}
console.log(game.toString());
console.log(bestMove(game))
console.log(negamax(game))