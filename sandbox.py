#Playground excersices

thisset = {"apple", "banana", "cherry", True, 1, 2} # pylint: disable=duplicate-value

new_set = thisset.copy()
print(new_set)

string = "liril1"

string = string.lower().replace(" ", "")

if string == string[::-1]:
    print("Palindrome")