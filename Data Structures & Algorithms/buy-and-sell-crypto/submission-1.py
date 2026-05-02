class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = prices[0]
        min_profit = prices[0]
        global_profit = 0
        for pr in prices:
            if pr < min_profit:
                global_profit = max(global_profit, max_profit - min_profit)
                min_profit = pr
                max_profit = pr
            
            if pr > max_profit:
                max_profit = pr
            
        return max(global_profit, max_profit - min_profit)
