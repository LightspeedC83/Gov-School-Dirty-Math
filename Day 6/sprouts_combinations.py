# not functional, should grow by 3n-1

class Spot():
    def __init__(self, connections):
        self.connections = connections

starting_number = 3 #starting number of spots
spots = []
for x in range(starting_number): # initializing the spot list with x spots each with 0 connections
    spots.append(Spot(0))

def print_state():
    global spots
    output = []
    for spot in spots:
        output.append(spot.connections)
    print(output)

depth = 10
done = False
for x in range(depth):
    print(x)
    print_state()
    if done:
        break
    for spot in spots:
        if spot.connections == 3:
            spots.remove(spot)
        elif spot.connections < 2:
            spot.connections += 2
            spots.append(Spot(2)) #creates a new spot with one connection left
        elif spot.connections == 2:
            if spots.index(spot) == len(spots)-1 and spot.connections > 1:
                print('done')
                done = True
                print(f"number of dots able to to be made after starting with {starting_number} dots: {x+1}") # needs to be x+1 because index starts at 0
                break
            else:
                next_spot = spots[spots.index(spot)+1]
                spot.connections +=1
                next_spot.connections +=1
                spots.append(Spot(2)) # creates a new spot with one connection left
                
