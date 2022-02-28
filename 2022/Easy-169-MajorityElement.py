import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = collections.Counter()
        thresh = len(nums) // 2 + 1
        
        for n in nums:
            countMap[n] += 1
            if countMap[n] == thresh:
                return n
        
        return None