class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        for n in nums1:
            idx = nums2.index(n)
            
            adding = False
            for i in range(idx, len(nums2)):
                if nums2[i] > n:
                    adding = True
                    ans.append(nums2[i])
                    break
            
            if not adding:
                ans.append(-1)
        return ans