
def linear_Search(name,target):
    for i in range(len(name)):
        if name[i]==target:
            return i
    return -1

L=eval(input("Enter the list : "))
target=eval(input("Enter the item need to be searched : "))
r=linear_Search(L,target)
print(r)