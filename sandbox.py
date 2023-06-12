#Playground excersices
from random import randint

thisset = {"apple", "banana", "cherry", True, 1, 2} # pylint: disable=duplicate-value

new_set = thisset.copy()
print(new_set)

print(ord("a"))

WIDTH = 2

if not isinstance(WIDTH,int):

    print("It is not a valid input")
else:
    print("It is a valid input")

string = "liril"

#to lower
string = string.lower().replace(" ", "")

"string reverse"
string1 = string[::-1]
print(string1)

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
#player = input("Rock, Paper, Scissors?")
#if player == computer:
#    print("Tie!")
#print(player)

n = [0, 2, 3, 4,5, 6]
for i in n:
    print (i % 2)
