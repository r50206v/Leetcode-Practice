'''
using hashmap
time: O(N)
space: O(N)
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        
        ans = 0
        for n in nums:
            if n == k / 2:
                ans += counter[n] // 2
                del counter[n]
            elif counter[k - n] > 0:
                min_pairs = min(counter[n], counter[k - n])
                ans += min_pairs
                counter[n] -= min_pairs
                counter[k - n] -= min_pairs
            
        return ans