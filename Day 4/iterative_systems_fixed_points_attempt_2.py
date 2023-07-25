import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fixed points In iterative systems")

x_max = 10
domain = [x for x in range(-x_max,x_max)]

def function(domain): # this is the function in question
    output = []
    for x in domain:
        output.append((4*x) - (4*(x**2)))
    return output

plt.plot(domain, domain, label="y = x", color="red") # the y=x function
plt.plot(domain, function(domain), label="4x - 4x^2", color="blue")

for start in domain:
    pass



plt.show()