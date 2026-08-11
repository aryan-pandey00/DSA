class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for i in prices:
            # lowest buying price
            if i < min_price:
                min_price = i

            # Calculate profit
            profit = i - min_price

            # Update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit