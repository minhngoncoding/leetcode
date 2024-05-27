class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        matching_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char == '(' or char == '[' or char == "{":
                stack.append(char)
            elif char == "]" or char == "}" or char == ")":
                if stack == []:
                    return False
                current_element = stack.pop()
                if matching_pairs.get(current_element) != char:
                    return False

        return False if stack else True
        
