players = ['charles','asif','anwar','karam','vinod','vijay','muru','raja','yash','will','sundar']

for payer in players[2:6]:
    print((payer.title()))

players.sort(reverse=True)
print(f"The first three elements are:{players[:3]}")

length = len(players)
print(length)

players[4] = 'kalai'

print(players)
#Range
numbers = list[range(1,10)]

#number = numbers[5]   #object does not support item assignment

random = [(2, 2), (3, 4), (1, 1), (4, 1), (1, 3)]

random.sort(reverse=True)

#random[2] = 3
random[2] = [3,]

print(random)
sorted(players,reverse=True)

players.insert(4,'john')

length = len(players)
print(f"Number of elements are:{length}\n")

players.append(4)
print(players[-1])

#players.sort()  # Does not work as it have int and str