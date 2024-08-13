class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or char != pairs[stack.pop()]:
                return False
            
        return len(stack) == 0

        
