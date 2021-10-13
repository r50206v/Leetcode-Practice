class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = collections.Counter(nums1)
        
        result = []
        for k in nums2:
            if nums1Map.get(k) and nums1Map[k] > 0: 
                nums1Map[k] -= 1
                result.append(k)
                
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = j = k = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]