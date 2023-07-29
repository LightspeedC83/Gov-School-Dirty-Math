# (relevant) https://www.youtube.com/watch?v=094y1Z2wpJg

import matplotlib.pyplot as plt

plt.xlabel("iterations")
plt.ylabel("Y")
plt.title("Collatz Conjecture")

def function(x):
    if x%2==0:
        return(x/2)
    else:
        return(x*3 +1)

depth = 150
starting_range = 100

for starting_number in range(starting_range):
    x_list = [0]
    y_list = [starting_number] # starting number

    for x in range(depth):
        x_list.append(x_list[-1]+1)
        next_number = function(y_list[-1])
        y_list.append(next_number)

    plt.plot(x_list,y_list)

plt.show()