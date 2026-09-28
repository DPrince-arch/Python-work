def cyclistSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

def main():
    nums = [3, 1, 5, 2, 4]
    print("Sorted array: " + str(cyclistSort(nums)))

main()