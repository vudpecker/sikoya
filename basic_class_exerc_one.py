
class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'
 
 
#setattr(Laptop, 'brand', 'Acer')
#setattr(Laptop, 'model', 'Predator')
 
 
print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model: {getattr(Laptop, 'model')}")

class Car:

    def __init__(self, brand, model, price, type_of_car=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'

new_car = Car("opel","Insignia", 115000,"hatch back")
print(new_car.__dict__)
#print(new_car.__class__)

class Laptop:
 
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
 
 
laptop = Laptop('Acer', 'Predator', 5490)
 
 
print(f'brand -> {laptop.brand}')
print(f'model -> {laptop._model}')
print(f'price -> {laptop._Laptop__price}') #TODO why _Laptop?