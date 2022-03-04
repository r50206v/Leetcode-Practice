'''
hashmap
time: O(max(N, M))
space: O(max(N, M))
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        ans = []
        for k in counter1.keys():
            if counter2.get(k):
                ans.extend([k] * min(counter1[k], counter2[k]))
        return ans