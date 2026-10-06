class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_prices = prices[0]
        max_profit = 0
        for stock in range(len(prices)):
            if prices[stock] < low_prices:
                low_prices = prices[stock]
            today_profit = prices[stock] - low_prices
            if today_profit > max_profit:
                max_profit = today_profit
        return max_profit
                
