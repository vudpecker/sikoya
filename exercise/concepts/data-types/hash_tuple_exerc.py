"""
n = int(input())
integer_list = list(map(int, input().split()))

my_tuple = tuple(integer_list[:n])
if n > len(integer_list):
  raise ValueError("Number of elements in the list does not match n")
print(hash(my_tuple))
"""
my_tuple = (1,2)
print(hash(my_tuple))