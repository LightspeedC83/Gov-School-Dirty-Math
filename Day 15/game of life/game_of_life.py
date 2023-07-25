board_x = 5
board_y = 5
# creating an empty game board
board = []
for y in range(board_y):
    board.append([0 for x in range(board_x)])

# function to print the game board in the terminal
def print_board_terminal():
    global board, board_x, board_y
    output = ''
    for y in board:
        for x in y:
            output += str(x) + " "
        output += "\n"
    print(output)

print("this is the empty board:")
print_board_terminal()

#getting a starting state from the user
while True:
    coordinate = input("enter a coordinate")