def threeSum(nums: list[int]) -> list[list[int]]:
    triplets = []

    num = len(nums)
    for i in range(num):
        for j in range(i + 1, num):
            for k in range(j + 1, num):
                #if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in triplets:
                if (
                    nums[i] + nums[j] + nums[k] == 0
                    and sorted([nums[i], nums[j], nums[k]]) not in triplets
                ):
                    triplets.append(sorted([nums[i], nums[j], nums[k]]))

    return triplets

