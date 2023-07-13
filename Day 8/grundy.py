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

class State():
    def __init__(self, depth, piles, parent=None, child=None):
        """piles is a list of numbers, each representing a different pile"""
        self.depth = depth
        self.piles = piles
        self.parent = parent
        self.child = child

        # checking to see whether the piles in this state object make a dead state (ie. only 1s or 2s)
        dead_piles = 0
        for pile in self.piles:
            if pile in [1,2]:
                dead_piles +=1
    
        if dead_piles == len(self.piles):
            self.is_dead = True
        else:
            self.is_dead = False
            

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

def check_duplicates(tree_list): #doesn't work yet
    """takes the main_list tree and checks for and 
    removes duplicate states at each level, returning the new list without duplicates."""
    output = []
    depth = 0
    for level in tree_list:
        level_list = [x[1] for x in level]
        no_duplicates = []
        for state in level_list:
            for other in no_duplicates:
                other_other = other[:]
                same_count = 0
                for x in state:
                    if x in other_other:
                        same_count +=1
                        other_other.remove(x)
                if same_count != len(state):
                    no_duplicates.append(state)

        # reformatting the list of states without duplicates
        depth +=1
        to_append = []
        for state in no_duplicates:
            to_append.append([depth,state])
        output.append(to_append)
    return(output)

def print_tree(tree_list):
    """given the game tree list (in this program it is main_list), 
    it prints it to the terminal in a readable fashion"""
    depth = 0
    for level in tree_list:
        print("-"*10 + f"\nDepth = {depth}:\n" + "-"*10)
        output = ""
        for state in level:
            output += f"{state.piles},  "
        print(output)
        depth +=1


depth = 0
starting_value = 10
starting_state = State(depth, piles=[starting_value]) # each state is represented by a list in the form [level (ie. depth), [list of numbers, each representing a pile at said level]]

master_list = [] 
previous_list = [starting_state]

while True:
    current_list = []
    depth +=1
    for state in previous_list:
        # going through each state at the given depth
        pile_num = 0
        for pile in state.piles:
            if pile not in [1,2]:
                for new in break_up_num(pile):
                    list_copy = state.piles[:]
                    del list_copy[pile_num]
                    new_list = list_copy[:pile_num] + new +list_copy[pile_num:]
                    new_object = State(depth,new_list, parent=state)
                    current_list.append(new_object)
                    state.child = new_object

            pile_num +=1

    #updating the master list
    master_list.append(previous_list)

    #condition for exiting loop if all branches are dead
    num_dead = 0
    for state in current_list:
        if state.is_dead:
            num_dead +=1
    if num_dead == len(current_list): # if we are at the end (ie. max possible depth)
        master_list.append(current_list)
        print_tree(master_list)
        break
    else: #resetting and repeating the loop
        previous_list = current_list[:]
        current_list = []



# print(check_duplicates(master_list))