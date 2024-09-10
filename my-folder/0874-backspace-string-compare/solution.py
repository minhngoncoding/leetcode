class Solution:
    def createCharList(self, s):
        lst = []
        if s is not None:
            for char in s:
                if char != "#":
                    lst.append(char)
                else:
                    if lst:
                        lst.pop()
                    else:
                        continue
        return ''.join(lst)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.createCharList(s) == self.createCharList(t)
         
