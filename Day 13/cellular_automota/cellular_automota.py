from PIL import Image
import os
import moviepy.editor as me
from progress.bar import Bar

background_color = (97, 167, 242)

# getting the rule to use
while True:
    rule = input("Enter a number from 0 to 255 for the propagation rule: ").strip()
    if rule.isdigit():
        rule = int(rule)
        rule_int = rule
        if 0 <= rule and rule <= 255:
            break
    print("Please enter an integer between 0 and 255")

#checking to see if the user wants to make it pretty
gradient = False
want_gradient = input("Do you want a gradient? (Y/N): ").strip().lower()
if want_gradient in ["y", ""]:
    gradient = True

states = [
    "000",
    "001",
    "010",
    "011",
    "100",
    "101",
    "110",
    "111"
]

mapping = {}
rule = str(bin(rule))[2:]
if len(rule) < len(states):
    rule = "0"*(len(states)-len(rule)) + rule

print(f"The binary key for rule {rule} is:")
i = 0
for state in states[::-1]:
    print(state, rule[i])
    mapping[state] = int(rule[i])
    i += 1

def find_next(left, cell, right):
    """returns the next cell's value given the three cells above it (left, center, and right)"""
    state = str(left) + str(cell) + str(right)
    global mapping
    return mapping[state]

depth = 500
board_width = depth*2

# creating an initial game state with one on cell in the middle
game_board = [0 for x in range(board_width)]
game_board[len(game_board)//2] = 1

#clearing the output frames folder
for file in os.listdir("Day 13/cellular_automota/output_frames"):
    file = "Day 13/cellular_automota/output_frames/" + file
    os.remove(file)

#starting the image generation process
with Bar("\nRunning the simulations...") as bar:
    current_fg = (0,0,0)
    if gradient:
        current_bg = background_color
    else:
        current_bg = (255,255,255)

    board_list = [game_board]
    frame_count = 0
    previous_percent = 0 #flag for progress bar 
    for x in range(depth-1):            
        new_board = []
        i = 0
        for cell in game_board:
            # getting the arraingement of the 3 cells on whcih the next cell will depend
            if mapping["000"] == 0: # if all off parents goes to off, it does this (it pretends that its off at the edges)
                if i ==0: # if it's the first cell (it pretends there's white space next to it going off the image)
                    left = 0
                    right = game_board[i+1]
                if i == len(game_board)-1: # if it's the last cell
                    left = game_board[i-1]
                    right = 0
                else: #if a cell in between 
                    left = game_board[i-1]
                    right = game_board[i+1]
            else: # if the off goes to on, it pretends that it's on on the edges
                ### IMPORTANT: THE SIMULATION WILL START MESSING UP WHEN THE CONFIGURATION REACHES THE EDGES OF THE SCREEN
                if i ==0: # if it's the first cell (it pretends there's a space the color of itself next to it)
                    left = game_board[i]
                    right = game_board[i+1]
                if i == len(game_board)-1: # if it's the last cell
                    left = game_board[i-1]
                    right = game_board[i]
                else: #if a cell in between 
                    left = game_board[i-1]
                    right = game_board[i+1]

            i+=1
            new_board.append(find_next(left, cell, right))

        board_list.append(new_board)
        game_board = new_board[:]

        # creating an image with this up to the most recent board state
        pixel_list = []
        i = -1
        for t in board_list:
            i += 1
            #updating the gradient
            if gradient:
                gradient_percent = int((255 * i/depth)//1)
                current_fg = (gradient_percent,0,0)

            for cell in t:
                if cell == 0:
                    pixel_list.append(current_bg)
                else:
                    pixel_list.append(current_fg)
        
        for i in range(board_width*depth-len(pixel_list)):
            pixel_list.append(current_bg)
        
        frame_output = Image.new(mode="RGB", size=(board_width,depth))
        frame_output.putdata(pixel_list)
        frame_output.save(f"Day 13/cellular_automota/output_frames/{frame_count}.png")
        
        if 100*(x/depth)//1 > previous_percent:
            bar.next()
        previous_percent = 100*(x/depth)//1

        frame_count +=1
        
        

# saving the image
current_fg = (0,0,0)

i = -1
pixel_list = []
for t in board_list:
    i +=1
    if gradient:
        gradient_percent = int((255 * (i/depth))//1)
        current_fg = (gradient_percent,0,0)
    for cell in t:
        if cell ==0:
            pixel_list.append(current_bg)
        else:
            pixel_list.append(current_fg)

output = Image.new(mode="RGB", size=(board_width,depth))
output.putdata(pixel_list)

marker = ""
if gradient:
    marker = "_gradient"

output.save(f"Day 13/cellular_automota/cellular_automota_output_rule_{rule_int}{marker}.png")

frame_output_folder = "Day 13/cellular_automota/output_frames"
# frame_num = len([f for f in os.listdir("Day 13/cellular_automota/output_frames")])
frames = []
for num in range(frame_count-1):
    frames.append(f"Day 13/cellular_automota/output_frames/{num}.png")

output_clip = me.ImageSequenceClip(frames, fps=20)
output_clip.write_videofile(f"Day 13/cellular_automota/cellular_automota_ouput_animation_{rule_int}{marker}.mp4", fps=20)