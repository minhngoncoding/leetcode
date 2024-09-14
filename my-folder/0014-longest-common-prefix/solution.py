class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        try:
            n = len(strs[0])

            for i in range(n):
                char = strs[0][i]
                for j in range(1, len(strs)):
                    if char != strs[j][i]:
                        return result
                result += char
        except: 
            return result

        return result
