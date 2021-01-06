# 1539. Kth Missing Positive Number
'''
brute force solution
time: O(N)
space: O(N)
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # all possible integers
        numsList = range(1, len(arr) + k + 1)
        
        for n in numsList:
            if k == 0 and arr:
                return n-1
            elif k == 0 and len(arr) == 0:
                return n
            
            if arr and arr[0] == n:
                arr.pop(0)
            else:
                k -= 1
        return n


'''
binary search
time: O(lgN)
space: O(1)
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (right - left)//2 + left
            missingInt = arr[mid] - mid - 1
            
            if missingInt < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return k + left