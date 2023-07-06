import matplotlib.pyplot as plt

plt.xlabel("iterations")
plt.ylabel("Y")
plt.title("Day 4, fixed points discussion \nA(n) = 1.5*A(n-1)-4")

lower = -100
upper = 100
depth = 10

x_list = [x for x in range(depth+1)]

for start in range(lower, upper):
    listed = [start] #starting number
    for x in range(depth):
        listed.append(1.5*listed[-1] -4)
    
    plt.plot(x_list,listed)



leg = plt.legend(loc='upper right')
plt.show()