'''
three pointers
time: O(N)
space: O(N)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [float("inf")] * len(nums)
        
        left = 0
        right = len(nums) - 1
        current_point = len(nums) - 1
        while left <= right: 
            if abs(nums[left]) < abs(nums[right]):
                ans[current_point] = nums[right] ** 2
                right -= 1
            else:
                ans[current_point] = nums[left] ** 2
                left += 1
            current_point -= 1
        return ans