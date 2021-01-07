'''
time: O(N)
space: O(1) no extra space needed 
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 1
        oddPos = True
        while index < len(nums):
            if oddPos:
                if nums[index] < nums[index - 1]:
                    nums[index], nums[index - 1] = nums[index - 1], nums[index]
            else:
                if nums[index] > nums[index - 1]:
                    nums[index], nums[index - 1] = nums[index - 1], nums[index]
            
            oddPos = not oddPos
            index += 1
        return nums