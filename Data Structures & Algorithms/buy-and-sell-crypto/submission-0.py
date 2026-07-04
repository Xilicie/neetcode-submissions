class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        n = len(prices)
        while r < n:
            transaction = prices[r] - prices[l]
            profit = max(transaction, profit)

            if transaction < 0:
                l = r
            r += 1
        return profit
            

