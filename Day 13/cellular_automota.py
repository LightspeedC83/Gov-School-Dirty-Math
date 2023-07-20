from PIL import Image

# this mapping is set for rule 90, which should make the serpinski triangle
mapping = {
    "000": 0,
    "001": 1,
    "010": 0,
    "011": 1,
    "100": 1,
    "101": 0,
    "110": 1,
    "111": 0,
}

def find_next(left, cell, right):
    """returns the next cell's value given the three cells above it (left, center, and right)"""
    state = str(left) + str(cell) + str(right)
    global mapping
    return mapping[state]

board_width = 2000
depth = 1000
# creating an initial game state with one on cell in the middle
game_board = [0 for x in range(board_width)]
game_board[len(game_board)//2] = 1

board_list = [game_board]

for x in range(depth):
    # print(game_board)
    new_board = []
    i = 0
    for cell in game_board:
        # getting the arraingement of 3 cells
        if i ==0: # if it's the first cell
            left = 0
            right = game_board[i+1]
        if i == len(game_board)-1: # if it's the last cell
            left = game_board[i-1]
            right = 0
        else: #if a cell in between 
            left = game_board[i-1]
            right = game_board[i+1]
        i+=1
        new_board.append(find_next(left, cell, right))

    board_list.append(new_board)
    game_board = new_board[:]


# saving the image
pixel_list = []

for t in board_list:
    for cell in t:
        if cell ==0:
            pixel_list.append((255,255,255))
        else:
            pixel_list.append((0,0,0))

output = Image.new(mode="RGB", size=(board_width,depth+1))

output.putdata(pixel_list)

output.save("Day 13/cellular_automota_output.png")