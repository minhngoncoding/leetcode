class Solution:
    def countNumber1(self, n):
        count = 0
        while n > 0:
            if n % 2 != 0:
                count += 1
            n = n // 2
        return count


    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):
            result.append(self.countNumber1(i))

        return result

