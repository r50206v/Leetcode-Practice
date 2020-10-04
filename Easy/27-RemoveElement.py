# My Answer
'''
Runtime: 36 ms, faster than 86.91% of Python3 online submissions for Remove Element.
Memory Usage: 13.2 MB, less than 37.98% of Python3 online submissions for Remove Element.
'''
class Solution:
    def removeElement(self, nums, val) -> int:
        if len(nums) == 0:
            return 0
        
        pointer = 0
        for ind in range(len(nums)):
            if nums[ind] != val:
                nums[pointer] = nums[ind]
                pointer += 1
        return pointer
    
    

'''
Runtime: 32 ms
Memory Usage: 13.7 MB
09/12/2020
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        while ind < len(nums):
            if nums[ind] == val:
                del nums[ind]
            else:
                ind += 1
        return len(nums)