def findSubsets(num):
    list.sort(num)
    subsets = []
    subsets.append([])
    start, end = 0, 0

    for i in range(len(num)):
        if i > 0 and num[i] == num[i - 1]:
            start = end + 1
        end = len(subsets) - 1
    
        for j in range(start, end+1):
            set = list(subsets[j])
            set.append(num[i])
            subsets.append(set)

    return subsets

def main():
    print("list of subsets: " + str(findSubsets([1, 3, 3, 5])))

main()