class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model  # protected
        self.__price = price #  private member


laptop = Laptop("Acer", "Predator", 5490)

print(f"brand -> {laptop.brand}")
print(f"model -> {laptop._model}")
print(f"price -> {laptop._Laptop__price}")  #Acessing private member

_Laptop__price = 5700

print(f"Updated price -> {_Laptop__price}")

laptop._Laptop__price = 5650

print(f"price -> {laptop._Laptop__price}")
