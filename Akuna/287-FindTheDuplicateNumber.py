'''
time: O(N)
space: O(N)
'''
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

'''
time: O(N)
space: O(1)
create linked list cycle
and search if there is duplicates
'''
class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
        
            if nums[abs(nums[i])] >= 0:
                nums[abs(nums[i])] = nums[abs(nums[i])] * -1
            else:
                return abs(nums[i])


'''
time: O(N)
space: O(1)
Approach 3: Floyd's Tortoise and Hare (Cycle Detection)
create linked list cycle
and search if there is duplicates
'''
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare