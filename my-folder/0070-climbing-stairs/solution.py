class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            result = memo[i-1] + memo[i-2]
            memo[i] = result

        return memo[n]

