# two-pass hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {target - k: idx for idx, k in enumerate(nums)}
        
        for idx, n in enumerate(nums):
            if mapping.get(n):
                if mapping[n] != idx:
                    return [idx, mapping.get(n)]



# one-pass hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i