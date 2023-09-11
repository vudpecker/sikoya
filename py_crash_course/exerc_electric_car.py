from exerc_class_car import Car

# Inheritance
class ElectricCar(Car):

    def __int__(self, make, model, year):
        super().__init__(make, model, year)
        #self.battery_size = 40 #fixme

    def desc_battery(self):
        print(f"This cars as a {self.battery_size}-kwh battery.")


my_leaf = ElectricCar("nissan", "leaf", "2022") #fixme
# my_leaf.increment_odometer(23000)
# my_leaf.update_odometer(24000)
# print(my_leaf.read_odometer())
my_leaf.desc_battery()


