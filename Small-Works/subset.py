def findSubsets(num):
    subsets = []
    subsets.append([])
    
    for current in num:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(current)
            subsets.append(set)

    return subsets

def main():
    print("list of subsets: " + str(findSubsets([1,3,5])))

main()