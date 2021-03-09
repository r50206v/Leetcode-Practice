'''
Brute Force Using Backtracking
time: O(N**5)
space: O(N)
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:        
        def count(n, vowels):
            if n == 0:
                return 1
            result = 0
            for idx in range(vowels, 6, 1):
                result += count(n - 1, idx)
            return result
        
        return count(n, 1)

'''
decoding the pattern using recursion
time: O(N**5)
space: O(N)
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count(n, vowels):
            if n == 1:
                return vowels
            if vowels == 1:
                return 1
            return count(n - 1, vowels) + count(n, vowels - 1)
        return count(n, 5)


'''
Bottom Up Dynamic Programming, Tabulation
time: O(N)
space: O(N)
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5] * n
        
        for idx in range(5):
            dp[0][idx] = idx + 1
        
        for idx in range(1, n, 1):
            dp[idx][0] = 1
            for v in range(1, 5, 1):
                dp[idx][v] = dp[idx][v - 1] + dp[idx - 1][v]
        
        return dp[n - 1][4]


'''
math
time: O(1)
space: O(1)
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int((n + 4)*(n + 3)*(n + 2)*(n + 1) / 24)
            
        