# does NOT work, see the .ts simulation
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("start")
    x_start = 2
    y_start = 3
    depth = 5

    # getting the starting conditions
    if x_start == 2 and y_start == 3:
        I_list = [0.1]
        U_list = [0.9]
    else:
        I_list = [0]
        U_list = [1]
    R_list = [0]

    t_list = [x for x in range(depth)]

    # defining our functions
    I_count, U_count, R_count = 0,0,0
    def I(x,y,t):
        global t_list
        global I_count
        I_count +=1
        if t==0:
            return(I_list[0])
        elif I_count <= depth:
            return (U(x,y,t_list[t-1]) * (0.15*(I(x-1,y,t_list[t-1]) + I(x,y-1,t_list[t-1]) + I(x+1,y,t_list[t-1]) + I(x,y+1,t_list[t-1])) + 0.4*I(x,y,t_list[t-1])))
    
    def U(x,y,t):
        global t_list
        global U_count
        U_count +=1
        if t==0:
            return(U_list[0])
        elif I_count <= depth:
            return (U(x,y,t_list[t-1]) - I(x,y,t_list[t-1]))
    
    def R(x,y,t):
        global t_list
        global R_count
        R_count +=1
        if t==0:
            return(R_list[0])
        elif I_count <= depth:
            return (R(x,y,t_list[t-1]) + I(x,y,t_list[t-1]))
    

    for t in t_list[1:]:
        print(t)
        I_list.append(I(x_start,y_start,t))
        U_list.append(U(x_start,y_start,t))
        R_list.append(R(x_start,y_start,t))
    
    # generating the graph
    plt.xlabel("t")
    plt.ylabel("output_value")
    plt.title(f"Day 4, Problem 1 /nx={x_start}, y={y_start}")
    
    print(t_list)
    print(I_list)
    print(U_list)
    print(R_list)

    plt.plot(t_list, I_list, label="I")
    plt.plot(t_list, U_list, label="U")
    plt.plot(t_list, R_list, label="R")

    leg = plt.legend(loc='upper center')
    plt.show()
    
    