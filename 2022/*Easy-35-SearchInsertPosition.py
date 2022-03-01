'''
binary search 
time: O(logN)
space: O(1)
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left