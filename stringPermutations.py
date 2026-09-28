from ntpath import join


def findStringPermutations(str):
    subsets = []
    subsets.append(str)
    
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(subsets)
            for j in range(n):
                chs = list(subsets[j])
                chs[i] = chs[i].swapcase()
                subsets.append("".join(chs))

    return subsets

def main():
    print("list of subsets: " + str(findStringPermutations("ad52")))

main()