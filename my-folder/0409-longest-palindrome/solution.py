from collections import defaultdict 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        dct = defaultdict(int)
        for char in s:
            dct[char] += 1

        result = 0
        already_odd = False
        value_lst = list(dct.values())
        value_lst.sort(reverse=True)
        
        for value in value_lst:
            if value % 2 == 0:
                result += value
            else:
                if already_odd:
                    result += value-1
                else:
                    result += value
                    already_odd = True

        return result
