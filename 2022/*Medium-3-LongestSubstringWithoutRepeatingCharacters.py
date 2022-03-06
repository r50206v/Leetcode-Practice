'''
time: O(N)
space: O(min(m,n)). 
We need O(k)O(k) space for the sliding window, 
where kk is the size of the Set. 
The size of the Set is upper bounded by 
the size of the string nn and the size of the charset/alphabet mm.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        left = right = 0
        result = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        
        return result