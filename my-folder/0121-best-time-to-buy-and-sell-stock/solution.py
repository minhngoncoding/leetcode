class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        profit = 0
        current_min_buy = 1000000000000
        for index, buy_value in enumerate(prices):
            if buy_value >= current_min_buy:
                continue
            else:
                current_min_buy = buy_value
                
            for sell_value in prices[index+1:]:
                if buy_value >= sell_value:
                    continue
                else:
                    if sell_value - buy_value > profit:
                        profit = sell_value - buy_value
        return profit
