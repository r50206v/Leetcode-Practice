'''
dynamic programming
time: O(N**2)
space: O(N**2)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_length = 0
        for j in range(n):
            for i in range(0, j+1):
                dp[i][j] = ((s[i] == s[j]) and ((j - i <= 2) or dp[i+1][j-1]))
                if dp[i][j]:
                    if (j-i+1) > max_length:
                        max_length = j-i+1
                        res = s[i:j+1]
        return res