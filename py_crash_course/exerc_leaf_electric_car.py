
from exerc_electric_car import ElectricCar

my_leaf = ElectricCar("nissan", "leaf", "2022")
my_leaf.increment_odometer(23000)

my_leaf.update_odometer(24000)

print(my_leaf.read_odometer())
my_leaf.desc_battery()
