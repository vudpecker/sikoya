ch = True
while ch:
    topping = input(("What topping do you want to add? Type 'quit' if enough"))
    if topping != 'quit' and topping != 'Quit':
        print((f"Adding {topping} to your pizza"))
    else:
        ch = False
