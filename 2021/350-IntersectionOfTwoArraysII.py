class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = collections.Counter(nums1)
        
        result = []
        for k in nums2:
            if nums1Map.get(k) and nums1Map[k] > 0: 
                nums1Map[k] -= 1
                result.append(k)
                
        return result