class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        waiting = []
        for char in tokens:
            if char not in ["+", "-", "*", "/"]:
                waiting.append(char)
            else:
                num1 = waiting.pop()
                num2 = waiting.pop()

                waiting.append(str(int(eval(num2 + char + num1))))
        return int(waiting[0])

            
