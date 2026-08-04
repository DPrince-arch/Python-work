class WordsConcentanation:
    @staticmethod
    def findConcentanation(str, words):
        if not words or not str:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        window_size = word_len * word_count
        word_freq = {}
        result = []
        
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        for start in range(len(str) - window_size + 1):
            window = str[start:start + window_size]
            seen = {}
            
            for i in range(0, window_size, word_len):
                word = window[i:i + word_len]
                if word not in word_freq:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_freq[word]:
                    break
            else:
                if seen == word_freq:
                    result.append(start)
        
        return result

def main():
    print(WordsConcentanation.findConcentanation("catfoxcat", ["cat", "fox"]))

main()