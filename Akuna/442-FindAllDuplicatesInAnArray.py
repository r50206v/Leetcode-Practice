'''
time: O(N)
space: O(1)
create linked list cycle
and search if there is duplicates
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for idx in range(len(nums)):
            if nums[abs(nums[idx]) - 1] >= 0:
                nums[abs(nums[idx]) - 1] = -1 * nums[abs(nums[idx]) - 1]
            else:
                ans.append(abs(nums[idx]))
        return ans