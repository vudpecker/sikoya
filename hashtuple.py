#Enter range as input
num = int(input())
lis = []
for i in range(num):
    lis.append(i+1)
t = tuple(lis)
print(t)
print(hash(t))

"""
Hash of (1,2) is -3550055125485641917
Expected is 3713081631934410656

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    # Create a tuple from the list
    my_tuple = tuple(integer_list[:n])
    print(hash(my_tuple))

"""