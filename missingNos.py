def missingNos(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    miss = []
    for idx, num in enumerate(nums):
        if num != idx + 1 and idx + 1 not in miss:
            miss.append(idx + 1)

    return miss

def main():
    nums = [3, 1, 5, 4, 7, 8, 3]
    print("Missing numbers: " + str(missingNos(nums)))
main()