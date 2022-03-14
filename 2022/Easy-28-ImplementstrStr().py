class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or haystack == needle:
            return 0
        
        for idx in range(len(haystack)):
            if haystack[idx:].startswith(needle):
                return idx
        return -1



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = 0
        n = len(needle)
        while haystack[k:k+n] != needle:
            k += 1
            if k + n > len(haystack):
                return -1
        return k