"""
Rules for Grundy's game:
    -begin with x number of counters/sticks/tiles
    -on a  move a player breaks a pile of counters into two uneven piles
    -the winner is the last player to make a move

The tree will be represented in a list, each element in the list is another list, 
whose index is the depth in the tree (ie. index 0 is at depth 0). Each element inside the lists at 
a given depth is a list of a possible game state that could be reached at said depth. 
Game states are represented by a list whose first element is its depth and whose second element
is a list of numbers each representing a different sized pile in said state.
"""

def print_tree(tree_list):
    """given the game tree list (in this program it is main_list), 
    it prints it to the terminal in a readable fashion"""
    depth = 0
    for level in tree_list:
        print("-"*10 + f"\nDepth = {depth}:\n" + "-"*10)
        output = ""
        for state in level:
            output += f"{state[1]},  "
        print(output)
        depth +=1

def check_is_dead(state):
    """function that checks whether or not a given state has no possible moves left to make
    (ie. the only remaining piles are of size 1 or 2)"""
    dead_piles = 0
    for pile in state[1]:
        if pile in [1,2]:
            dead_piles +=1
    
    if dead_piles == len(state[1]):
        return True

def break_up_num(num):
    """function that returns a list of the ways to break up an inputted number into two other uneven nubmers"""
    output = []
    if num not in [1,2]:
        for x in range(1,num):
            if x != num-x:
                output.append([x,num-x])
            else:
                break
    return(output)


depth = 0
starting_value = 5
starting_state = [depth, [starting_value]] # each state is represented by a list in the form [level (ie. depth), [list of numbers, each representing a pile at said level]]

master_list = [] 
previous_list = [starting_state]

while True:
    current_list = []
    depth +=1
    for state in previous_list:
        # going through each state at the given depth
        pile_num = 0
        for pile in state[1]:
            if pile not in [1,2]:
                for new in break_up_num(pile):
                    list_copy = state[1][:]
                    del list_copy[pile_num]
                    new_list = list_copy[:pile_num] + new +list_copy[pile_num:]
                    current_list.append([depth, new_list])

            pile_num +=1

    #updating the master list
    master_list.append(previous_list)

    #condition for exiting loop if all branches are dead
    num_dead = 0
    for state in current_list:
        if check_is_dead(state):
            num_dead +=1
    if num_dead == len(current_list): # if we are at the end (ie. max possible depth)
        master_list.append(current_list)
        print_tree(master_list)
        break
    else: #resetting and repeating the loop
        previous_list = current_list[:]
        current_list = []