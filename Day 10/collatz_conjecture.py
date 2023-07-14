# (relevant) https://www.youtube.com/watch?v=094y1Z2wpJg

import matplotlib.pyplot as plt

plt.xlabel("iterations")
plt.ylabel("Y")
plt.title("Day 10, problem 6 (Collatz Conjecture)")

def function(x):
    if x%2==0:
        return(x/2)
    else:
        return(x*3 +1)


starting_range = 10000
for starting_number in range(1,starting_range):
    x_list = [0]
    y_list = [starting_number] # starting number

    while True:
        x_list.append(x_list[-1]+1)
        next_number = function(y_list[-1])
        y_list.append(next_number)
        if next_number == 1: #once you get to one, it's done
            break


    plt.plot(x_list,y_list)

plt.show()