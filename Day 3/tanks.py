import matplotlib.pyplot as plt

class Tank():
    def __init__(self, fluid, salt):
        self.fluid = fluid
        self.salt = salt
        self.concentration = salt / fluid

    def remove_fluid(self, amount_lost):
        #calculates concentration of fluid
        concentration = self.salt / self.fluid
        new_volume = self.fluid - amount_lost
        new_salt = concentration * new_volume
        self.fluid = new_volume
        self.salt = new_salt
        self.calculate_concentration()

    def add_fluid(self, amount_added, concentration):
        self.fluid += amount_added
        self.salt += concentration * amount_added
        self.calculate_concentration()

    def calculate_concentration(self):
        self.concentration = self.salt / self.fluid


tank_1 = Tank(100, 50)
tank_2 = Tank(100, 0)

x_list = []
tank_1_list = []
tank_2_list = []

depth = 75
for x in range(depth):
    tank_2.remove_fluid(10)
    tank_1.remove_fluid(10)
    tank_2.add_fluid(10,tank_1.concentration)
    tank_1.add_fluid(10, 0)

    x_list.append(x)
    tank_1_list.append(tank_1.concentration)
    tank_2_list.append(tank_2.concentration)


plt.xlabel("time")
plt.ylabel("concentration")
plt.title("Day 3 Problem 4 Tanks")

plt.plot(x_list, tank_1_list, label="Tank 1")
plt.plot(x_list, tank_2_list, label="Tank 2")
leg = plt.legend(loc='upper center')
plt.show()

