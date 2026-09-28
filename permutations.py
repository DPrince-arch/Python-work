from collections import deque


def findpermutations(nums):
    length = len(nums)
    subsets = []
    permute = deque()
    permute.append([])
    
    for current in nums:
        n = len(permute)
        for _ in range(n):
            old = permute.popleft()
            for j in range(len(old) + 1):
                new = list(old)
                new.insert(j, current)
                if len(new) == length:
                    subsets.append(new)
                else:
                    permute.append(new)
                    
    return subsets

def main():
    print("list of subsets: " + str(findpermutations([1,3,5])))

main()