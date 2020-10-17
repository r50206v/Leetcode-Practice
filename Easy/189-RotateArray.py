'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k > len(nums):
            k = k % len(nums)
        
        nums[:] = nums[-k:] + nums[:-k]
        

# My Answer
'''
Runtime: O(n)
Memory Usage: O(1)
'''
class Solution(object):
    def rotate(self, nums, k):
        if k > len(nums):
            k = k - len(nums)
            
        tmp = nums[-k:]
        del nums[-k:]
        for i in tmp[::-1]:
            nums.insert(0, i)

            
'''
Time Complexity: 
Space Complexity:  
'''


# Solution
'''
Runtime: 44 ms, faster than 89.56% of Python online submissions for Rotate Array.
Memory Usage: 12.1 MB, less than 48.43% of Python online submissions for Rotate Array.

https://leetcode.com/problems/rotate-array/discuss/54353/Straight-forward-python-code-use-slice
'''
class Solution(object):
    def rotate(self, nums, k):
        if k > len(nums):
            k = k - len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        
        
'''
Runtime: 44 ms, faster than 89.56% of Python online submissions for Rotate Array.
Memory Usage: 12 MB, less than 78.70% of Python online submissions for Rotate Array.

https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1