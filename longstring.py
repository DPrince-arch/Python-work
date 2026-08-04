class LongString:
    def __init__(self, string):
        self.string = string

    def get_longest_substring(self):
        max_length = 0
        start = 0
        char_index_map = {}

        for end in range(len(self.string)):
            right_char = self.string[end]
            if right_char in char_index_map:
                start = max(start, char_index_map[right_char] + 1)
            char_index_map[right_char] = end
            max_length = max(max_length, end - start + 1)

        return max_length  
    
def main():
    string = "abcabcbb"
    long_string = LongString(string)
    result = long_string.get_longest_substring()
    print("The length of the longest substring without repeating characters is:", result)

if __name__ == "__main__":
    main()