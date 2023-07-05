import matplotlib.pyplot as plt

x_list = [0]
y_list_a = [3] #starting values for populations
y_list_b = [1]
max_depth = 500
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

# problem_6(y_list_a[0], y_list_b[0])

def problem_1(a,b):
    """(this one is from day three) returns a list, element 0 is species a, 1 is species b"""
    global max_depth 
    max_depth -= 1
    if max_depth > 0:
        new_a = 1.21*a - 0.25*b
        new_b = 0.25*a + 0.71*b
        #this is a predator prey relationship 
        y_list_a.append(new_a)
        y_list_b.append(new_b)
        global count
        count += 1
        x_list.append(count)
        problem_1(new_a, new_b)
    else:
        print(f"X: {x_list}")
        print(f"A: {y_list_a}")
        print(f"B: {y_list_b}")
        print(f"most recent ratio of a/b: {y_list_a[-1]/y_list_b[-1]}")

        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Day 3 Problem 1")
        
        plt.plot(x_list,y_list_a, label="species A")
        plt.plot(x_list, y_list_b, label="species B")
        leg = plt.legend(loc='upper center')
        plt.show()

# problem_1(y_list_a[0], y_list_b[0])

def problem_2(a,b):
    """(this one is from day three) returns a list, element 0 is species a, 1 is species b"""
    global max_depth 
    max_depth -= 1
    if max_depth > 0:
        new_a = 1.26*a - 0.25*b
        new_b = 0.25*a + 0.76*b
        #this is a predator prey relationship 
        y_list_a.append(new_a)
        y_list_b.append(new_b)
        global count
        count += 1
        x_list.append(count)
        problem_2(new_a, new_b)
    else:
        print(f"X: {x_list}")
        print(f"A: {y_list_a}")
        print(f"B: {y_list_b}")
        print(f"most recent ratio of a/b: {y_list_a[-1]/y_list_b[-1]}")

        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Day 3 Problem 2")
        
        plt.plot(x_list,y_list_a, label="species A")
        plt.plot(x_list, y_list_b, label="species B")
        leg = plt.legend(loc='upper center')
        plt.show()

problem_2(y_list_a[0], y_list_b[0])
