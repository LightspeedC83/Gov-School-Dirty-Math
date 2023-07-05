import matplotlib.pyplot as plt

x_list = [0]
y_list_a = [2] #starting values for populations
y_list_b = [2]
max_depth = 250
count = 0

def problem_5(a,b):
    """returns a list, element 0 is species a, 1 is species b"""
    global max_depth 
    max_depth -= 1
    if max_depth > 0:
        new_a = 1.3*a - 0.4*b
        new_b = 0.6*a + 0.2*b
        #this is a predator prey relationship 
        y_list_a.append(new_a)
        y_list_b.append(new_b)
        global count
        count += 1
        x_list.append(count)
        problem_5(new_a, new_b)
    else:
        print(f"most recent ratio of a/b: {y_list_a[-1]/y_list_b[-1]}")

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Day 2 Problem 5")
        
        plt.plot(x_list,y_list_a, label="species A")
        plt.plot(x_list, y_list_b, label="species B")
        leg = plt.legend(loc='upper center')
        plt.show()

# problem_5(y_list_a[0], y_list_b[0])


def problem_6(a,b):
    """returns a list, element 0 is species a, 1 is species b"""
    global max_depth 
    max_depth -= 1
    if max_depth > 0:
        new_a = 0.96*a + b
        new_b = 0.96*b
        y_list_a.append(new_a)
        y_list_b.append(new_b)
        global count
        count += 1
        x_list.append(count)
        problem_6(new_a, new_b)
    else:

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Day 2 Problem 6")
        
        plt.plot(x_list,y_list_a, label="species A")
        plt.plot(x_list, y_list_b, label="species B")
        leg = plt.legend(loc='upper center')
        plt.show()

problem_6(y_list_a[0], y_list_b[0])

