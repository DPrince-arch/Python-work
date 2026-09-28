class StringAnagrams:
    @staticmethod
    def findAnagram(str, pattern):
        start, matched = 0, 0
        index = {}

        for chr in pattern:
            if chr not in index:
                index[chr] = 0
            index[chr] += 1

        for end in range(len(str)):
            right = str[end]
            if right in index:
                index[right] -= 1
                if index[right] == 0:
                    matched += 1
            if matched == len(index):
                return start
            if end >= len(pattern) - 1:
                left = str[start]
                start += 1
                if left in index:
                    if index[left] == 0:
                        matched -= 1
                    index[left] += 1
        return -1
    
def main():
    print(str(StringAnagrams.findAnagram("iodcabf", "abc")))
    
main()