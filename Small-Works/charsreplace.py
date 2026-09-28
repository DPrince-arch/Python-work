class CharacterReplacer:
    def __init__(self, char_map):
        self.char_map = char_map

    def replace_characters(self, input_string):
        result = []
        for char in input_string:
            if char in self.char_map:
                result.append(self.char_map[char])
            else:
                result.append(char)
        return ''.join(result)
    
    