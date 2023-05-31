"""All about list"""

shop_list = ["Apple", "Tamarind", "Orange", "Milk", "Rice", "Egg"]
print(shop_list[1:3])

new_list = [x for x in shop_list if x != ("apple".capitalize)]
print(new_list)
