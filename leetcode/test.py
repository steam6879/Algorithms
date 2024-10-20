from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyMin = 10000
        profit = 0

        for price in prices:
            buyMin = min(buyMin, price)
            profit = max(profit, price - buyMin)

        return profit
