'''
binary search
time: O(logN)
space: O(1)
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)//2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return left