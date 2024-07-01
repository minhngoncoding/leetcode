class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}
        for char in magazine:
            if char not in dct:
                dct[char] = 1
            else:
                dct[char] += 1

        for char in ransomNote:
            if char not in dct:
                return False
            else:
                if dct[char] > 0:
                    dct[char] -= 1
                else:
                    return False
        return True

