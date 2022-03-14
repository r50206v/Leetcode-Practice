class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increase = nums[-1] >= nums[0]
        
        for i in range(1, len(nums)):
            if increase and nums[i] >= nums[i-1]:
                continue
            elif not increase and nums[i] <= nums[i-1]:
                continue
            else:
                return False
        return True