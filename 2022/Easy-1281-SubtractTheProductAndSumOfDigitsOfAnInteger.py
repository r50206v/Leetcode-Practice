'''
time: O(N)
space: O(N)
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numList = [int(s) for s in str(n)]
        prod = 1
        summation = 0
        for n in numList:
            prod *= n
            summation += n
        
        return prod - summation