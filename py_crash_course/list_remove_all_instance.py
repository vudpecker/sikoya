

pets = ["dog","parrot","owl","cat","rabbit","cat","dog","goldfish","bunny","cat"]

#pets.append("hamster")

print("\n", pets , "Count of pets are", len(pets) , end="\n")


catchIt = input("You want to remove cat or dog?")
#print((catchIt))


#pets.pop()  ##The oppoposit of append

#while "cat" in pets:

while catchIt in pets:
    pets.remove("cat")

print("\n", pets , "Now the count is", len(pets))
