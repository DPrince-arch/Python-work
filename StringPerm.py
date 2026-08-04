class StringPermutation:
    @staticmethod
    def findPermutation(str, pattern):
        start, matched = 0, 0
        perm = {}

        for chr in pattern:
            if chr not in perm:
                perm[chr] = 0
            perm[chr] += 1

        for end in range(len(str)):
            right = str[end]
            if right in perm:
                perm[right] -= 1
                if perm[right] == 0:
                    matched += 1
            if matched == len(perm):
                return True
            
            if end >= len(pattern) - 1:
                left = str[start]
                start += 1
                if left in perm:
                    if perm[left] == 0:
                        matched -= 1
                    perm[left] += 1

        return False
    
def main():
    print(str(StringPermutation.findPermutation("iodcabf", "abc")))

main()



    
