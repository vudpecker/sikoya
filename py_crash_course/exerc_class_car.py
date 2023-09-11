class CarWithPrice:

    def __init__(self, brand, model, price, type_of_car=None):  # Positional argument
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'

    def read_odometer(self):
        print(f"The car has rum {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back in odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# new_car = Car("opel", "Insignia", 115000, "hatch back")  # will be called in the inherited classes
# print(new_car.__dict__)


# print(new_car.__class__)


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"The car has rum {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back in odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
