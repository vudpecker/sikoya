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

print(album_set)
