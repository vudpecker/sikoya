import sys

a = 14
b = 25
c = a + b

div = int(input("Enter a divisor"))
d = c % div

print("a" + "b") # Prints as string

print(a + b) 

print(f"Remainder of {c}/{div} is: {d}")

#print python version
print(sys.version.split())
