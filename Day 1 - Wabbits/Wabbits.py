"""this project got me saying wabbit so much I feel like Elmer Fudd"""

import matplotlib.pyplot as plt

class Wabbit_Pair(): # creating a rabbit class
    def __init__(self, reproductive_strength, years_til_fertility):
        self.reproductive_strength = reproductive_strength
        self.years_til_fertility = years_til_fertility
        self.age = 0
        print()
    


def problem_1(depth):
    """"In year zero, we begin with a single pair of newborn rabbits, one male and one female. 
    A pair of rabits gives birrth to one pair of rabits, one mail and one female every year,
    beggining at one year of age"""

    #setting up the plot
    plt.xlabel("year")
    plt.ylabel("number of rabbit pairs")
    plt.title("Wabbits - problem 1")

    #setting up the simulation
    wabbits_list = []
    wabbits_list.append(Wabbit_Pair(reproductive_strength=1, years_til_fertility=0))

    x_points_list = []
    y_points_list = []
    #starting the simulation
    for year in range(depth+1):
        x_points_list.append(year)
        y_points_list.append(len(wabbits_list))
        for x in range(len(wabbits_list)):
            wabbits_list.append(Wabbit_Pair(reproductive_strength=1, years_til_fertility=0))
        
    #making the plot 
    plt.plot(x_points_list, y_points_list)
    plt.show()
    
# problem_1(10)

def problem_2(depth):
    """repeat problem 1 except a pair of rabbits gives birth
    to one pair of baby rabbits every year bgeggining at age two years"""
    
    #setting up the plot
    plt.xlabel("year")
    plt.ylabel("number of rabbit pairs")
    plt.title("Wabbits - problem 1")

    #setting up the simulation
    wabbits_list = []
    wabbits_list.append(Wabbit_Pair(reproductive_strength=1, years_til_fertility=2))

    x_points_list = []
    y_points_list = []
    #starting the simulation
    for year in range(depth+1):
        x_points_list.append(year)
        y_points_list.append(len(wabbits_list))

        new_wabbits = []
        for wabbit in wabbits_list:
            if wabbit.age >= wabbit.years_til_fertility-1:
                new_wabbits.append(Wabbit_Pair(reproductive_strength=1, years_til_fertility=0))
            
            ### i know this is the problem area, we should be getting fibonacci sequence but no
        wabbits_list = wabbits_list + new_wabbits
        for wabbit in wabbits_list:
            wabbit.age +=1

    print(x_points_list)
    print(y_points_list)
    #making the plot 
    plt.plot(x_points_list, y_points_list)
    plt.show()

problem_2(5)