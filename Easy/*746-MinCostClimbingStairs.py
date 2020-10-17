'''
my answer
using DP

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dpList = [float("Inf")] * (len(cost) + 1)
        
        dpList[0] = 0
        dpList[1] = 0
        
        for i in range(2, len(cost) + 1):
            dpList[i] = min(dpList[i-1] + cost[i-1], dpList[i-2] + cost[i-2])
            
        return dpList[-1]
    
    
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)