# My Answer
'''
Runtime: 64 ms, faster than 94.72% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.3 MB, less than 60.92% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    
'''
Runtime: 52 ms
Memory Usage: 13.8 MB
09/11/2020
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False