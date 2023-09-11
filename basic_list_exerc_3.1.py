from random import randint

ch = randint("l", "y")

print(f"Choice :{ch}")

"""
players = ['charles','asif','anwar','karam','vinod','vijay','muru','raja','yash','will','sundar']

for payer in players[2:6]:
    print((payer.title()))

players.sort(reverse=True)
print(f"The first three elements are:{players[:3]}")

length = len(players)
print(length)


#Range
numbers = list[range(1,10)]

#number = numbers[5]   #object does not support item assignment

random = [(2, 2), (3, 4), (1, 1), (4, 1), (1, 3)]

random.sort(reverse=True)



old_player_list = sorted(players,reverse=True)

old_player_list.insert(4,'john')

length = len(old_player_list)
print(f"Number of elements are:{length}\n")

players.append(4)
print(players[-1])

#players.sort()  # Does not work as it have int and str
players.remove(4)
## TOTO Range
numbers = list[range(1,10)]

#number = numbers[5]   #object does not support item assignment

random = [(2, 2), (3, 4), (1, 1), (4, 1), (1, 3)]

random.sort(reverse=True)

new_player_list = sorted(players,reverse=True)

new_player_list.insert(4,'john')

length = len(new_player_list)
print(f"Number of elements are:{length}\n")



#This is a new section
print(new_player_list)

"""