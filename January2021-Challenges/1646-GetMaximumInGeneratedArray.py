'''
time: O(N)
space: O(N)
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
            
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        maxNum = 1
        
        for idx in range(1, len(nums)//2):
            if 2 * idx < len(nums) - 1:
                nums[2 * idx] = nums[idx]
                nums[2 * idx + 1] = nums[idx] + nums[idx + 1]
                
                maxNum = max(maxNum, nums[idx] + nums[idx + 1])
        return maxNum