'''
two pointer
time: O(N)
space: O(N)
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                left += 1
                right += 1
        return nums


class Solution(object):
    def moveZeroes(self, nums):
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[ptr] = nums[ptr],nums[i]
                ptr += 1