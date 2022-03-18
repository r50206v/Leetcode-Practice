class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        def dfs(sub, string):
            if len(string) == 0:
                return True
            return string.startswith(sub) and dfs(sub, string[len(sub):])
        
        for idx in range(1, len(s)//2+1):
            if dfs(s[:idx], s):
                return True
        return False
