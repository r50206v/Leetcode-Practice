'''
binary search
time: O(logN)
space: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or nums[-1] < target:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1