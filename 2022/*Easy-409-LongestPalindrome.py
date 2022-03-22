class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        
        ans = 0
        used_single = True
        for k in counter.keys():
            ans += counter[k] // 2 * 2
            counter[k] -= counter[k] // 2 * 2
            
            if used_single and counter[k]:
                ans += 1
                counter[k] -= 1
                used_single = False

        return ans