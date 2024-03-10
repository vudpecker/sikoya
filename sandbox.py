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

#To lower
string = string.lower().replace(" ", "")

# string reverse
string1 = string[::-1]
print(string1)

"""
try:
    factorial(-1)
    assert False  # This line should not be reached
except ValueError:
    pass
"""

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]
#player = input("Rock, Paper, Scissors?")
player = "Rock" #as of now a static value

if player == computer:
    print("Tie!")
print(player)

n = [0, 2, 3, 4, 5, 6]
sum = 0
for i in n:
    if i % 2 == 0:
        sum += i
print (sum)

try:
    if sum - 1 == 0:
        assert False
except SyntaxError:
    pass

assert sum + 1 == 5, 'greater than five'

print(sum - 1)


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))

name = input('what is your name?\n')
print('Hi, %s.' % name)