# My Answer
'''
Runtime: 4004 ms
Memory Usage: 12.8 MB
'''
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for i_index, i in enumerate(nums):
            for j_index in range(i_index + 1, len(nums)):
                j = nums[j_index]
                if i + j == target:
                    return sorted([i_index, j_index])
                
                
'''
09/11/2020
Runtime: 56ms
Memory Usage: 16.1 MB
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        org = {target - val: ind for ind, val in enumerate(nums)}
        for ind, val in enumerate(nums):
            if org.get(val) is not None:
                if ind != org.get(val):
                    return [ind, org[val]]
        return []
    
    
                
                
# Solution
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dictionary = {v: ind for ind, v in enumerate(nums)}
        for ind, value in enumerate(nums):
            targetNum = target - value
            if targetNum in list(dictionary.keys()) and dictionary[targetNum] != ind:
                return [ind, dictionary[targetNum]]