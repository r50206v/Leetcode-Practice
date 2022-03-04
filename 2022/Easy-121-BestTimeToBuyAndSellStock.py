'''
dynamic programming
time: O(N)
space: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_date = 0
        profit = 0
        
        for idx in range(1, len(prices)):
            if prices[idx] - prices[buy_date] > profit:
                profit = prices[idx] - prices[buy_date]
            
            if prices[buy_date] > prices[idx]:
                buy_date = idx
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit