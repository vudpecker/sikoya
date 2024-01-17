from functools import reduce


def ret_large(ex):
    return max(ex)

ex = [1,2,3,4]

print(ret_large(ex))


new_map = map(lambda z : z*z, ex)

odd_map = filter(lambda z : z%2 != 0, ex)

sum = reduce(lambda x,y : x+y, ex)

print(list(new_map))

print(list(odd_map))

print(sum)

#max_map = map(lambda x : max(x) , ex)

#print(int(lambda ex : max(ex)))
#print(list(max_map))

