'''
Sliding Window 
For each right, call opt(right) the smallest left 
so that the product of the subarray 
nums[left] * nums[left + 1] * ... * nums[right] is less than k. 
opt is a monotone increasing function, so we can use a sliding window.
time: O(N)
space: O(N)
'''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans