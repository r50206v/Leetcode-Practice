# My Answer
'''
Runtime: 60 ms, faster than 5.77% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.3 MB, less than 14.12% of Python3 online submissions for Valid Parentheses.
'''

class Solution:
    def __init__(self):
        self.mapping = {"{": "}", "[": "]", "(": ")"}
    
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        if s[0] in list(self.mapping.values()):
            return False
        
        checkList = []
        for subStr in s:
            if subStr in list(self.mapping.keys()):
                checkList.append(subStr)
            elif subStr == self.mapping[checkList[-1]]:
                checkList = checkList[:-1]
            else:
                return False
        if checkList:
            return False
        else:
            return True


'''
Runtime: 28 ms
Memory Usage: 13.8 MB
09/11/2020
'''       
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'{': '}', '[': ']', '(': ')'}
        
        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False
        if s[0] in list(mapping.values()):
            return False
        
        checkList = []
        for p in s:
            if p in list(mapping.keys()):
                checkList.insert(0, mapping[p])
            elif len(checkList) != 0 and p == checkList[0]:
                checkList.pop(0)
            else: 
                return False
        if len(checkList) == 0:
            return True
        else:
            return False

        
        
        
# Solution
'''
Runtime: 36 ms, faster than 86.60% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.3 MB, less than 24.39% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        stack = []
        dict_br = { ')' : '(', '}' : '{', ']' : '[' }
        
        for char in s:
            if char not in dict_br:
                stack.append(char)
            else:
                if len(stack) > 0 and (stack[-1] == dict_br.get(char)):
                    del stack[-1]
                else:
                    return False
                
        return (len(stack) == 0)