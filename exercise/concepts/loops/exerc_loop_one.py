"""Using tuple and while loop"""

#n = int(input("Enter number of elements :"))
i = 0
nums = [2,3,6,1,9,7,5]

while i <= len(nums):
    if nums[i] > nums[i+1]:
        temp = nums[i+1]
        nums[i+1] = nums[i]
        nums[i+1] = temp
    i+=1

#print(n)