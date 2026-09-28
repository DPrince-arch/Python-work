def duplicateNo(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    #return nums

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]



def main():
    nums = [3, 1, 5, 4, 7, 8, 3, 2, 6]
    print("duplicate number: " + str(duplicateNo(nums)))
main()