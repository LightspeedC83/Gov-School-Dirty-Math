from PIL import Image
import os
import moviepy.editor as me

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

board_width = 1000
depth = 500
# creating an initial game state with one on cell in the middle
game_board = [0 for x in range(board_width)]
game_board[len(game_board)//2] = 1

#clearing the output frames folder
for file in os.listdir("Day 13/cellular_automota/output_frames"):
    file = "Day 13/cellular_automota/output_frames/" + file
    os.remove(file)

board_list = [game_board]
frame_count = 0
for x in range(depth-1):
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

    # creating an image with this up to the most recent board state
    
    pixel_list = []
    for t in board_list:
        for cell in t:
            if cell ==0:
                pixel_list.append((255,255,255))
            else:
                pixel_list.append((0,0,0))
    
    for x in range(board_width*depth-len(pixel_list)):
        pixel_list.append((255,255,255))
    
    frame_output = Image.new(mode="RGB", size=(board_width,depth))
    frame_output.putdata(pixel_list)
    frame_output.save(f"Day 13/cellular_automota/output_frames/{frame_count}.png")
    
    frame_count +=1

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
output.save("Day 13/cellular_automota/cellular_automota_output.png")

frame_output_folder = "Day 13/cellular_automota/output_frames"
# frame_num = len([f for f in os.listdir("Day 13/cellular_automota/output_frames")])
frames = []
for num in range(frame_count-1):
    frames.append(f"Day 13/cellular_automota/output_frames/{num}.png")

output_clip = me.ImageSequenceClip(frames, fps=16)
output_clip.write_videofile("Day 13/cellular_automota/cellular_automota_ouput_animation.mp4", fps=16)