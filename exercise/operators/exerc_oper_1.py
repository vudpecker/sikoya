
n = int(input("Enter a number:"))

"""prints False if n is less than 100, and True if n is 
    greater than or equal to 100"""

#print(n >= 100)
print("TRUE" if n>= 100 else "FALSE")


"""print True if n is even and False otherwise"""

#print(n%2 == 0)

#a is divided by b
input_str = input("Enter two numbers:")
a, b = map(int, input_str.split())

print(a % b == 0)


#length greater than 5
print(len(input_str) > 5)

#positive
print(n > 0 )