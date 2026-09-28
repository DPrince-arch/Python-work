def missingNo(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for idx, num in enumerate(nums):
        if num != idx + 1:
            return idx + 1

    return len(nums) + 1


def main():
    nums = [3, 1, 5, 4]
    print("Missing number: " + str(missingNo(nums)))

main()