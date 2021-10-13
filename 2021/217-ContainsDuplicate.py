# Hash table solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for n in nums:
            if n in mapping:
                return True
            else:
                mapping[n] = 1
        return False

# Using Python Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# Sorting solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for idx in range(len(n) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False