import matplotlib.pyplot as plt
count = 0
max_depth = 25
x_list = [0]
y_list = [35_000]

def problem_5(p):
    """aaa"""
    global max_depth 
    max_depth -= 1
    if max_depth > 0:
        new_p = 2.5*p -0.00005*p**2
        y_list.append(new_p)
        global count
        count += 1
        x_list.append(count)
        problem_5(new_p)
    else:
        print(f"X: {x_list}")
        print(f"Y: {y_list}")
        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Day 3 Problem 5")
        
        plt.plot(x_list,y_list, label="squirrel population")
        leg = plt.legend(loc='upper right')
        plt.show()

problem_5(y_list[0])
