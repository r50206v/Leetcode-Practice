'''
one hashmap
time: O(N)
space: O(N)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        subMap = defaultdict(list)
        
        for idx, n in enumerate(nums):
            subMap[target - n].append(idx)
        
        for n in nums:
            if subMap.get(n):
                if n == target - n:
                    if len(subMap[n]) >= 2:
                        return subMap[n]
                    else:
                        continue
                else:
                    return [subMap[n][0], subMap[target-n][0]]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i