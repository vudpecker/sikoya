#attributes

class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'
 
 
setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')
 
 
print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model: {getattr(Laptop, 'model')}")


class Laptop:
 
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model # protected
        self.__price = price
 
 
laptop = Laptop('Acer', 'Predator', 5490)
 
 
print(f'brand -> {laptop.brand}')
print(f'model -> {laptop._model}')
print(f'price -> {laptop._Laptop__price}') #TODO why _Laptop?