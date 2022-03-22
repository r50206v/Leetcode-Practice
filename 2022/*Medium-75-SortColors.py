'''
dual-pivot partitioning
time: O(N)
space: O(1) 
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        counter = Counter(nums)
        
        idx_1 = counter[0]
        idx_2 = counter[0] + counter[1]
        
        for idx in range(len(nums)):
            if idx < idx_1:
                nums[idx] = 0
            elif idx_1 <= idx < idx_2:
                nums[idx] = 1
            else:
                nums[idx] = 2