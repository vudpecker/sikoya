#Playground excersices

thisset = {"apple", "banana", "cherry", True, 1, 2} # pylint: disable=duplicate-value

new_set = thisset.copy()
print(new_set)

print(ord("a"))

WIDTH = 2

if not isinstance(WIDTH,int):
    print("It is not a valid input")
else:
    print("It is a valid input")

print(type(WIDTH))



string = "liril"

#to lower
string = string.lower().replace(" ", "")

"string reverse"
string1 = string[::-1]
print(string1)