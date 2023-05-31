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
"""
