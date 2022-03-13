class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        
        if s[0] in string.ascii_lowercase:
            ans = [s[0], s[0].upper()]
        else:
            ans = [s[0]]
        
        for idx in range(1, len(s)):
            addition = []
            if s[idx] in string.ascii_lowercase:
                addition = [a + s[idx].upper() for a in ans]
            ans = [a + s[idx] for a in ans] + addition
        
        return ans