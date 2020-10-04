# My Answer
'''
Runtime: 48 ms, faster than 32.90% of Python3 online submissions for Implement strStr().
Memory Usage: 13.4 MB, less than 32.00% of Python3 online submissions for Implement strStr().
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for ind in range(len(haystack)):
            if haystack[ind:].startswith(needle):
                return ind
        return -1

    
'''
Runtime: 52 ms, faster than 24.93% of Python3 online submissions for Implement strStr().
Memory Usage: 13.3 MB, less than 67.38% of Python3 online submissions for Implement strStr().
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        needleLength = len(needle)
        for ind in range(len(haystack)):
            if haystack[ind:(ind+needleLength)] == needle:
                return ind
        return -1
            
        
'''
Runtime: 44 ms 
Memory Usage: 13.7 MB
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if needle == haystack: 
            return 0
        
        
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                
                if j == len(needle):
                    return i - j
            
                continue
                
            elif j > 0:
                i = i - j
                j = 0
                
            i += 1
            
        return -1


        
# Solution
'''
Runtime: 32 ms, faster than 95.67% of Python3 online submissions for Implement strStr().
Memory Usage: 13.2 MB, less than 91.25% of Python3 online submissions for Implement strStr().
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        needleLength = len(needle)
        for ind in range(len(haystack) - needleLength + 1):
            if haystack[ind:(ind+needleLength)] == needle:
                return ind
        return -1