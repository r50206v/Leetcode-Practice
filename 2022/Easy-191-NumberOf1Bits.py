'''
Bit Manipulation Trick
time: O(1)
space: O(1)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 2
            n = n // 2 
        return ans