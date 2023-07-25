depth = 1000
answers =[]
mods_7 = []
for x in range(depth):
    mods_7.append(7*x+3)

for i in mods_7:
    if i%5 == 2:
        if i%4 ==1:
            answers.append(i)

for x in answers:
    print(x)

""" formula should be y = 140x-123 """