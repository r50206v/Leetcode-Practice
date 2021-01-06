# 526. Beautiful Arrangement
class Solution:
    def __init__(self):
        self.output = 0
    
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        
        def backtrack(nums, first):    
            if first == len(nums):
                self.output += 1
                return 
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                if nums[first] % (first + 1) == 0 or (first + 1) % nums[first] == 0:
                    backtrack(nums, first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack(nums, 0)
        return self.output