'''
time: O(NlogN)
space: O(1)
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        gap = arr[1] - arr[0]
        
        for idx in range(2, len(arr)):
            if arr[idx] - arr[idx - 1] != gap:
                return False
        return True