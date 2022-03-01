class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter = Counter(nums)
        
        for k in counter.keys():
            if counter[k] > 1:
                return True
        return False