import sys

a = 14
b = 25
c = a + b

div = int(input("Enter a divisor"))
d = c % div

print("a" + "b") # Prints as string

print(a + b) 

print(f"Remainder of {c}/{div} is: {d}")

#Split attribute of string
print("Hello:Nick:welcome".split(":")[1])
print('Hello Nick welcome'.split())
#Array or List
print(['Hello', 'Nick', 'welcome'][2])
print(len(['Hello', 'Nick', 'welcome'][2]))

#print python version
print(sys.version.split())
