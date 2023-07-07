import matplotlib.pyplot as plt

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fixed points In iterative systems")

domain = 100

# first plotting the line y = x
line_x = []
line_y = []
for x in range(-domain, domain):
    line_x.append(x)
    line_y.append(x)
plt.plot(line_x,line_y,label="y = x")

# plotting the function in question
function_x = []
function_y = []
for x in range(-domain,domain): 
    function_x.append(x)
    function_y.append(-0.5*x + 12) # this is the defining line for the iterative process A(n) = -0.5A(n-1) + 12, which has a stable fixed point at 8
plt.plot(function_x,function_y,label="y = -0.5x + 12")

# now for the visulaization of the iterative process
starting_value = 25 #starting value
depth = 15
iterative_x_list = []
iterative_y_list = []
for n in range(depth):
    



plt.show()