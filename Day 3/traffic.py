class Car():
    def __init__(self, speed, position):
        self.speed = speed
        self.position = position


highway = [30 for x in range(20)] # each element in the list is the number of cars, ie. car density

for strech in highway:
    speed = 75 - strech/2
    if speed > 60:
        speed = 60
    cars_to_leave = (speed/60)* strech

initial_cars = 20
for x in range(initial_cars):
    pass

time = 0
depth = 60
for x in range(depth):
    pass