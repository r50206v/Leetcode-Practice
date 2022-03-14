'''
hashtable
time: O(N)
space: O(N)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        
        for k in count.keys():
            if count[k] == 1:
                return k
        return 


'''
math 
2*(a+b+c) - (a+a+b+b+c) = c
time: O(N)
space: O(N)
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


'''
bit manipulation
using XOR
a XOR 0 = a
a XOR a = 0
a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b

time: O(N)
space: O(1)
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a