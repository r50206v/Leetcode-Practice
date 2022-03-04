'''
dynamic programming
time: O(N)
space: O(N)
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        total = 0
        
        for idx in range(2, len(nums), 1):
            if nums[idx] - nums[idx-1] == nums[idx-1] - nums[idx-2]:
                dp[idx] = dp[idx - 1] + 1
                total += dp[idx]
        return total