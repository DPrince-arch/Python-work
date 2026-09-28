from collections import Counter

def mean(nums=[]):
    return sum(nums) / len(nums)

def median(nums=[]):
    nums.sort()
    i = len(nums)/2
    return nums[i]

def mode(nums):
    n = len(nums)
    data = Counter(nums)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 

    if len(mode) == n: 
        get_mode = "No mode found"
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
        
    return get_mode

def range(nums):
    nums.sort()
    return nums[-1] - nums[1]

