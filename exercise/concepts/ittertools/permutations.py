from itertools import permutations 

#*my_list, key = input("Enter the list and iterator").split()

list_string, key = input("Enter the list and iterator").split()
my_list = list(map(int, list_string.split()))  # Convert list string to list of integers



print(my_list, key)