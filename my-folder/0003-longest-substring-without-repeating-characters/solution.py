class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        unique_lst = []
        result = 0
        for char in  s:
            if char not in unique_lst:
                unique_lst.append(char)
            else:
                #Remove all other char until repeated char\
                temp = unique_lst.copy()
                for c in unique_lst:
                    temp.pop(0)
                    if c == char:
                        break
                unique_lst = temp
                unique_lst.append(char)
            

            result = max(len(unique_lst), result)
                        



        

        return result
