#displaying the rules
print("Nim:\n  -The board starts with 3 rows containing some number of sticks\n  -Each player removes any number of sticks from a row\n  -The last player to move wins\n")

#representing the board
done = False
while not done: #getting player input to determine board size
    starting_board = []
    for x in range(3):
        starting_board.append(input(f"Enter the number of sticks for row {x+1}: ").strip())
    for row in starting_board:
        if row.isdigit() and row !="0":
            done = True
            break
        else:
            print("You must enter an integer for all three prompts.")
            break
starting_board = [int(x) for x in starting_board]
board = starting_board[:]

def display_board(board):
    """function that displays the game board in the terminal"""
    output = "\nGame State:\n"
    row = 0
    for pile in board:
        row +=1
        output +=f"Row {row}, {pile} sticks remain: "
        for stick in range(pile):
                output += "1"
        output += "\n"
    print(output)

def is_game_over(board):
    """returns true if there are no sticks left on the game board"""
    sum = 0
    for row in board:
        sum +=row

    if sum == 0:
        return True
    else:
        return False

# main game loop
done = False
while not done:
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

        num_to_eliminate = input("Enter the number of sticks you want to eliminate: ").strip()
        if num_to_eliminate.isdigit() and num_to_eliminate !="0":
            if int(num_to_eliminate) <= board[row-1]:
                num_to_eliminate = int(num_to_eliminate)
                break
            else:
                print(f"Please enter a number less than or equal to the number of sticks left in row {row}")
                continue
        else:
            print("Please enter an integer.")
            continue
    
    # updating the board with the player's move
    board[row-1] = board[row-1] - num_to_eliminate

    if is_game_over(board):
        display_board(board)
        print("The player wins!")
        break

    # making the computer's move, given the new board state

    # making a list of move options
    move_options = []
    row_to_move = 3
    for pair in board[0:2],[board[0],board[-1]],board[1:]:
        move_options.append((row_to_move, pair[0]^pair[1])) #XOR operator finds the third number to make a 3 number losing position in nim
        row_to_move -=1
    
    #deciding which option to move
    for option in move_options:
        num_to_eliminate = board[option[0]-1]-option[1]
        if option[1] <= board[option[0]-1] and num_to_eliminate >0: # if the move is possible to make
            print(f"\nThe computer removes {num_to_eliminate} sticks from row {option[0]}")
            board[option[0]-1] = option[1]
            break
     
    if is_game_over(board):
        display_board(board)
        print("The computer wins!")
        break
