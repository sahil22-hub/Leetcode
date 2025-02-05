class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize the minimum price to infinity
        max_profit = 0  # Initialize the maximum profit to 0
        
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Update the maximum profit
            max_profit = max(max_profit, price - min_price)
        
        return max_profit