"""Multiple assignment"""
bob, sera, mike = 19,21,20
print("Bob's age is " + str(bob))
print("Mike's age is " + str(mike))


stud_name = "Jake" # pylint: disable=C0103

message = "%s is 16 yrs old" # pylint: disable=C0103
print(message%stud_name)
message="%s is %d yrs old" # pylint: disable=C0103
print(message%("Phil",14))

print("Person's name is %s, and age is %d"%("Sam",21))


num1 = int(input("Enter first number "))
NUM1 = int(input("Enter second number "))

print("%d and %d"%(num1,NUM1))