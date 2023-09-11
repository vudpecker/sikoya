
# take second element for sort
def takeSecond(elem):
    return elem[1]

def takeFirst(elem):
    return elem[0]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)
#random.sort(key=takeFirst)

# print list
print('Sorted list:', random)