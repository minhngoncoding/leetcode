class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] = char_count[char] + 1
        
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            else:
                char_count[char] -= 1
                if char_count[char] == 0:
                    char_count.pop(char)

        return False if char_count else True

        



