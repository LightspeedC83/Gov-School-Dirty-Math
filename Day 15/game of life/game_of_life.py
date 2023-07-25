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

# starting the simulation
while True:
    # updating the board state according to the rules for John Conway's game of life
    next_board = board[:]
    y_pos = 0
    for y in board:
        x_pos = 0
        for cell in y:
            # for each of the cells, we find the number of neighbors it has which are on
            # this is non functional
            try: 
                #finding the neighbors' values
                up_neigbors = board[y_pos-1][x_pos-1:x_pos+2]
                down_neighbors = board[y_pos+1][x_pos-1:x_pos+2]
                side_neighbors = board[x_pos-1:x_pos+2:2]
            except IndexError:
                # if it's on the edge, it just dies
                next_board[y_pos][x_pos] = 0
                continue
            
            #determining how many neighbors are on
            num_on_neighbors = 0
            for n in up_neigbors + down_neighbors + side_neighbors:
                if n == 1:
                    num_on_neighbors +=1
            
            print(x_pos,y_pos, num_on_neighbors)

            # determining the state of the cell in the next iteration based on the number of neighbors that are on
            if cell ==1: # if the cell is alive
                if not (num_on_neighbors ==2 or num_on_neighbors ==3):
                    # if the cell doesn't have 2 or 3 live neighbors, it dies and the cell must be turned off
                    # otherwise, no updates must be made
                    next_board[y_pos][x_pos] = 0
    
            else: # if the cell is dead
                if num_on_neighbors == 3:
                    # if it has 3 neighbors it comes alive! otherwise no updates must be made
                    next_board[y_pos][x_pos] = 1
    
            x_pos += 1
        y_pos += 1
    
    # changing the board state to time+1
    board = next_board[:]
    print_board_terminal()
    # updating the board state according to the rules for John Conway's game of life
    increment = input("Press enter to incrment time, type 'quit' to quit").strip()
    if increment != "":
        break
    