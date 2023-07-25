import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fixed points In iterative systems")

depth = 3
resolution = 100
x_max = 10
domain = np.linspace(-x_max,x_max,resolution) # list of x values in the 

def function(x): # this is the function in question
    return((4*x) - (4*(x**2))+10)

plt.plot(domain, domain, label="y = x", color="red")
plt.plot(domain, function(domain), label="4x - 4x^2", color="blue")
plt.plot(domain,[0 for x in domain], color="black", label="y=0")

for start in range(-1,1):
    y_value = 0
    for x in range(depth):
        point_list_x = []
        point_list_y = []
        # first getting the from the starting x,y value to the function
        i = 0
        for x in range(resolution):
            point_list_x.append(start)
            point_list_y.append(i*function(start)/resolution)
            i+=1
        plt.plot(point_list_x, point_list_y, label=f"starting value = {start}", color="green")
        
        # going to the line y=x
        point_list_x = []
        point_list_y = []
        y_value = function(start)
        for x in range(resolution):
            point_list_y.append(y_value)

        point_list_x = np.linspace(start, y_value, resolution)
        plt.plot(point_list_x, point_list_y, label=f"starting value = {start}", color="green")

        start = y_value

plt.show()