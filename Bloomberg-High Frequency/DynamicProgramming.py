import collections

def LongestPalidromeSubstring(strs):

    ans = ""
    dp = [[0] * len(strs) for _ in len(strs)]
    for i in range(len(strs)):
        dp[i][i] = 1

    for i in range(len(strs) - 1, -1, -1):
        for j in range(i + 1, len(strs)):

            if s[i] == s[j]:
                if j-i == 1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    if len(ans) < j - i + 1:
                        ans = s[i: j+1]
    return ans


def MaximumSubarray(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i]])
    return max(dp)


def WordBreak(s, wordDict):
    visited = {}

    def word_break_recursion(s, wordDict, visited):
        if s == "":
            return True
        if s in wordDict:
            return True
        if s in visited:
            return visited[s]

        for i in range(1, len(s) + 1):
            if s[:i] in wordDict and self.word_break_recursion(s[i:], wordDict, visited):
                visited[s] = True
                return visited[s]
        visited[s] = False
        return visited[s]

    return self.word_break_recursion(s, wordDict, visited)


# 204 count prime
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        s = [1]*n
        s[0]=s[1]=0
        
        for i in range(2,int(n**0.5)+1):
            if s[i]:
                for j in range(i*i,n,i):
                    s[j] = 0
        return sum(s)