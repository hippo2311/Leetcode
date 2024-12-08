class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprofit = float('inf')
        for price in prices:
            if price < minprofit:
                minprofit = price
            profit = price- minprofit

            if profit > maxprofit:
                maxprofit = profit
        return maxprofit


# Time: O(N)
# Space: O(1)
        