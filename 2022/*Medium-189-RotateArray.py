'''
time: O(1)
space: O(N)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) <= 1 or k == 0:
            return nums
        
        end = nums[-k:]
        start = nums[:(len(nums) - k)]
        nums[:] = end + start


'''
time: O(N)
space: O(N)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a