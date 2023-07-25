board_x = 5
board_y = 5
# creating an empty game board
board = []
for y in range(board_y):
    board.append([0 for x in range(board_x)])

# function to print the game board in the terminal
def print_board_terminal(show_axis=False):
    global board, board_x, board_y
    output = ''
    if show_axis:
        output += "_|_"
        for x in range(board_x):
            output += str(x) + "_"  
    output += "\n"
    i = 0
    for y in board:
        if show_axis:
                output += str(i) + "| "
        i +=1
        for x in y:
            output += str(x) + " "
        output += "\n"
    print(output)

print("this is the empty board:")
print_board_terminal(show_axis=True)

#getting a starting state from the user
starting_points = []
while True:
    coordinate = input("Enter a coordinate in the form 'x,y': ").strip().lower()
    if coordinate in ["exit", "quit", "done", "stop", "no"]:
        break

    try:
        x_start = int(coordinate.split(",")[0])
        y_start = int(coordinate.split(",")[1])
    except:
        print("please enter a coordinate in the form 'x,y'.")
        continue
    
    if x_start < board_x and x_start>=0 and y_start < board_y and y_start>=0:
        starting_points.append((x_start,y_start))
    else:
        print("Please enter a coordinate that is on the plane.")
        continue
    
    board[y_start][x_start] = 1
    print("\nThe new starting board is...")
    print_board_terminal(show_axis=True)

# updating the board state according to the rules for John Conway's game of life
y_pos = 0
for y in board:
    x_pos = 0
    for x in y:
        # for each of the cells, we find the number of neighbors it has which are on

        x_pos += 1
    y_pos += 1

