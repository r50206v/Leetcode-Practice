# My Answer
'''
Runtime: 60 ms, faster than 88.01% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.1 MB, less than 94.31% of Python3 online submissions for Roman to Integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        smallerThanNext = False
        tmp = 1001
        acc = 0
        for i in s:
            i = self.mapping(i)
            smallerThanNext = (tmp < i)
            if smallerThanNext:
                acc += i - tmp*2
            else:
                acc += i

            tmp = i
        return acc
        
    def mapping(self, r: str) -> int:
        return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[r]
    

'''
Runtime: 48 ms
Memory Usage: 14.1 MB
09/11/2020
'''    
class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
        }
        ans = 0
        the_last = ''
        for i in s[::-1]:
            
            if len(the_last) == 0 or maps[the_last] <= maps[i]:
                ans += maps[i]
            else:
                ans -= maps[i]
                
            the_last = i
            
        return ans