# 
import random

def print_line():
    global line
    for x in line:
        print(x)

def find_new(individual, group, nums_used):    
    group.add(individual)
    for x in nums_used:
        group.add(x)
    
    options = [x for x in range(1,16)]
    for x in group:
        options.remove(x)
    
    random.shuffle(options)
    if len(options) ==0:
        return(None)
    else:
        return(options[0])

while True:
    reset = False
    print("starting from beginning")
    snapshots = []
    line = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    partners = {}
    for x in range(1,16):
        partners[x] = set()
    
    counter = 0
    for x in range(7):
        counter +=1
        print_line()
        print("\n")
        snapshots.append(line)
        #record who's with who
        for row in line:
            for individual in row:
                row_copy = row[:]
                row_copy.remove(individual)
                for x in row_copy:
                    partners[individual].add(x)
        
        #finding next permutation
        row_i = -1
        nums_used = set()
        for row in line:
            row_i += 1
            individual_i = -1
            for individual in row:
                individual_i += 1
                #finding the numbers that individual has been with            
                new_individual = find_new(individual, partners[individual], nums_used)
                if new_individual == None:
                    reset = True
                    break
                else:
                    nums_used.add(new_individual)
                    line[row_i][individual_i] = new_individual
        if reset:
            break
    
    if counter == 7:
        print(snapshots)
        break
                
                


