# My Answer
'''
Runtime: 32 ms, faster than 97.38% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.4 MB, less than 10.11% of Python3 online submissions for Longest Common Prefix.
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        
        shortestStr = min(strs, key=len)
        for ind in range(len(shortestStr), 0, -1):
            prefix = shortestStr[:ind]
            if all([s.startswith(prefix) for s in strs]):
                return prefix
        return ''
    
    
'''
Runtime: 28 ms
Memory Usage: 13.7 MB
09/11/2020
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        shortest = min(strs, key=len)
        ans = ""
        for i in shortest:
            if all(x.startswith(ans + i) for x in strs):
                ans += i
            else:
                break
        return ans
        

    
    
# Solution
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)