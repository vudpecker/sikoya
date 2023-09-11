from exerc_class_car import Car


class Battery:
    def __init__(self, battery_size: object = 40) -> object:
        self.battery_size = battery_size

    def desc_battery(self):
        print(f"This cars as a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):

    def __int__(self, make, model, year):
        super(ElectricCar,self).__init__(make, model, year)
        self.battery_size = Battery(65)


my_leaf = ElectricCar("nissan", "leaf", 2022)

#my_leaf.battery.desc_battery() #fixme

my_leaf.battery_size.get_range()
