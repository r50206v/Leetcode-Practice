'''
time: O(N)
space: O(N)
'''
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = {"1":"1", "6":"9", "8":"8", "9":"6", "0":"0"}
        
        newNum = ""
        for c in num:
            if c not in strobo:
                return False
            else:
                newNum += strobo[c]
        return num == newNum[::-1]