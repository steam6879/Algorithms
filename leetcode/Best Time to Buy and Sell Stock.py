from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10000
        profit = 0

        for price in prices:
            minPrice = min(price, minPrice)
            profit = max(profit, price - minPrice)

        return profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         decendingPrices = sorted(prices)[::-1]
#         ans = 0
#         maxPrice = 0

#         while decendingPrices:
#             i = prices.index(decendingPrices.pop())
#             minPrice = prices[i]
#             maxPrice = max(maxPrice, max(prices[i:]))
#             ans = max(ans, maxPrice - minPrice)

#         return ans





# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 1, len(prices) - 2
#         minPrice, maxPrice = prices[0], prices[-1]

#         while left <= right:
#             minPrice = min(prices[left], minPrice)
#             left += 1
            
#             maxPrice = max(prices[right], maxPrice)
#             right -= 1

#         if minPrice > maxPrice:
#             return 0
#         else:
#             return maxPrice - minPrice
        
if __name__ == '__main__':
    print(Solution.maxProfit(Solution, prices=[3, 2, 6, 5, 0, 3]))