import matplotlib.pyplot as plt

def find_new(x):
    return(4*x - 4*x**2)

depth = 100
n_list = [0]
outputs = [0.732] #starting value

for n in range(1,depth):
    outputs.append(find_new(outputs[-1]))
    n_list.append(n)

# print(n_list)
# print(outputs)

plt.xlabel("iterations")
plt.ylabel("output_value")
plt.title("Day 4, Problem 5\nA(n) = 4A(n-1) - 4A(n-1)^2")

plt.plot(n_list, outputs)
plt.show()