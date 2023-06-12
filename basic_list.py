"""All about list"""

#from sandbox import album_list


shop_list = ["Apple", "Tamarind", "Orange", "Milk", "Rice", "Egg"]
print(shop_list[1:3])

new_list = [x for x in shop_list if x != "apple".capitalize]
print(new_list, end="\n")

album_list = [ 1, "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0, True]
#convert to a set to remove duplicates
album_set = set(album_list)

length = len(album_list)

for i in range(length):
  print(album_list[i])

print(album_set)

squares=['red', 'yellow', 'green', 'purple', 'blue']

#Use of enumerate instead of range
for i, square in enumerate(squares):
    print(i, square)
    
