class CompareStrings:
    def compare_strings(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        for i in range(len(str1) - 1):
            if str1[i] == "#":
                str1 = str1.replace(str1[i-1], "")
                str1 = str1.replace(str1[i], "")
                
        for i in range(len(str2) - 1):
            if str2[i] == "#":
                str2 = str2.replace(str2[i-1], "")
                str2 = str2.replace(str2[i], "")

        return str1 == str2
    
def main():
    str1 = "ab#c"
    str2 = "ad#c"
    result = CompareStrings().compare_strings(str1, str2)
    print("The strings are " + ("equal" if result else "not equal"))

main()