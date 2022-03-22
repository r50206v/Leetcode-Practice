class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = []
        for l_idx, r_idx in zip(l, r):
            
            sort_subarray = sorted(nums[l_idx: r_idx+1])
            
            dis = None
            for p, n in zip(sort_subarray[:-1], sort_subarray[1:]):
                if dis is None:
                    dis = p - n
                elif dis != p - n:
                    ans.append(False)
                    break
                    
            if dis != p - n:
                continue
            else:
                ans.append(True)
            
        return ans