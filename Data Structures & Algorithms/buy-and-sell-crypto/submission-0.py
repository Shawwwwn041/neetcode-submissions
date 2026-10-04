class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for i in prices:
            if lowest > i:
                lowest = i
            today = i - lowest
            if today > profit:
                profit = today
        return profit