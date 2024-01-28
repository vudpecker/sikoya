
num1 = input("Enter first number :")
num2 = input("Enter second number :")
num3 = input("Enter third number :")

largest_num = num1

#if num2 > largest_num : largest_num = num2
#if num3 > largest_num : largest_num = num3

largest_num = max(num1,num2,num3)

print("Largest num is :", largest_num)