#representing the board
board = [3,5,7]

def display_board(board):
    """function that displays the game board in the terminal"""
    output = "\nGame State:\n    "
    #first row
    for stick in board[0]:
        output += str(stick)
    output += "\n   "
    #second row
    for stick in board[1]:
        output += str(stick)
    output += "\n  "
    #third row
    for stick in board[2]:
        output += str(stick)
    print(output)

def update_board(board, row, num_to_eliminate):
    """function that updates game board by taking away num_to_eliminate sticks from the row row"""
    new_board = board
    start_index = len([x for x in board[row-1] if x == 0])
    for x in range(start_index, start_index + num_to_eliminate):
        new_board[row-1][x] = 0 

    return(new_board)

# main game loop
done = False
while done == False:
    # the player will make the first move
    # getting the player's move as a row and a number of sticks to eliminate on said row
    display_board(board)
    while True:
        row = input("Enter the row you would like to move on (1, 2, or 3): ").strip()
        if row.isdigit():
            if not(1<= int(row) and int(row) <= 3):
                print("Please enter the integer 1, 2, or 3.")
                continue
        else:
            print("Please enter the integer 1, 2, or 3.")
            continue
        
        row = int(row)

        num_to_eliminate = input("Enter the number of sticks you want to eliminate:").strip()
        if num_to_eliminate.isdigit():
            count = len([x for x in board[row-1] if x == 1])
            if int(num_to_eliminate) <= count:
                num_to_eliminate = int(num_to_eliminate)
                break
            else:
                print(f"Please enter a number less than or equal to the number of sticks left in row {row}")
                continue
        else:
            print("Please enter an integer.")
            continue
    
    update_board(board, row, num_to_eliminate)
