from random import randint

class Die:

    def __init__(selfs, num_of_sides = 6):
        selfs.num_of_sides = num_of_sides

    def roll(self):
        return randint(1, self.num_of_sides)


my_die = Die(12) # Dynamic

results = []

for roll_num in range(25):
    result = my_die.roll()
    results.append(result)

print(results)

your_die = Die(6) #Fixed

results = []

for roll_num in range(45):
    result = your_die.roll()
    results.append(result)

print(results)
