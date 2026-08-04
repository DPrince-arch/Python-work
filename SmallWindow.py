class SmallWindow:
    def Substring(str, pattern):
        start, matched, subStr = 0, 0, 0
        min = len(str) + 1
        frequency = {}

        for chr in pattern:
            if chr not in frequency:
                frequency[chr] = 0
            frequency[chr] += 1

        for end in range(len(str)):
            right = str[end]
            if right in frequency:
                frequency[right] -= 1
                if frequency[right] == 0:
                    matched += 1

            while matched == len(frequency):
                if min > end - start + 1:
                    min = end - start + 1
                    subStr = start
                left = str[start]
                start += 1
                if left in frequency:
                    if frequency[left] == 0:
                        matched -= 1
                    frequency[left] += 1

        if min > len(str):
            return ""
        return str[subStr:subStr + min]
    
def main():
    print(SmallWindow.Substring("aabdec", "abc"))
    
main()