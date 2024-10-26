class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        # [0,1,2,3,4,5,6,7,8,9,10,11]
        # [0,1,1,2]

        for coin in coins:
            for x in range(coin, amount + 1):
                min_coins[x] = min(min_coins[x], 1 + min_coins[x -coin])


        return min_coins[-1] if min_coins[-1] != (amount + 1) else -1
        
        
