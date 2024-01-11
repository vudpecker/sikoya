# import tempfile



# myfile = tempfile.NamedTemporaryFile(mode='w', delete=False)
# myfile.write("This is the firt line")
# text = myfile.read()
# print(text)

# def read_file(filename):
#     with open(filename, 'r') as f:
#         return f.read()

# if __name__ == "__main__":
#     #new_file = tempfile.NamedTemporaryFile(delete=False)
#     text = read_file(myfile.name)
#     print(text)
#     myfile.close


with open("temp.txt", "w") as f:
    f.write("This is the first line")

with open("temp.txt", "r") as f1:
    print(f1.read())

op = -1

if not isinstance(op, (float, int)):
    print("This is int")

if not op > 0 :
    print("This is int")

