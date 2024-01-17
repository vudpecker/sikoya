first_name = "Murugaraja"
last_name  = "Sabanayagam"

#Formated print
print(f'My oficial mail id is {first_name.lower()}'
      f'.{last_name.lower()}@mail.com')


snack = "poori"
choice = "tea"

#result = f"The choice is {snack.lower()}" if choice.lower() == "sweet" else "WATER".upper()
print(f"The choice is {snack.lower()}" if choice.lower() == "sweet" else "WATER".upper())
#print(result)