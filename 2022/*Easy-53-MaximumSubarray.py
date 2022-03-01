'''
dynamic programming
time: O(N)
space: O(1)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = current = nums[0]
        for n in nums[1:]:
            current = max(n, current + n)
            ans = max(ans, current)
        return ans