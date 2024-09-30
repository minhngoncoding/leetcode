class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        n = len(strs[0])
        result = ""
        for i in range(n):
            char = strs[0][i]

            for word in strs[1:]:
                try:
                    char2 = word[i]
                except:
                    return result
                    
                if char != char2:
                    return result
            
            result += char
        return result
