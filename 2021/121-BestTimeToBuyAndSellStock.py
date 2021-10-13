class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxReturn = 0
        
        for p in prices:
            if p < minPrice:
                minPrice = p
            
            maxReturn = max(maxReturn, p - minPrice)
        return maxReturn