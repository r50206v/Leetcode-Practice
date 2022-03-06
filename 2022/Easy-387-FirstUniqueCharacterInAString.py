class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        countMap = Counter(s)
        
        for idx in range(len(s)):
            if countMap[s[idx]] == 1:
                return idx
        return -1