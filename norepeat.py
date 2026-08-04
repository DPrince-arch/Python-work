class NoRepeat:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        window_start = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_index_map:
                window_start = max(window_start, char_index_map[right_char] + 1)
            char_index_map[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length   
    
def main():
    string = "abcabcbb"
    no_repeat = NoRepeat()
    result = no_repeat.lengthOfLongestSubstring(string)
    print("The length of the longest substring without repeating characters is:", result)

if __name__ == "__main__":
    main()