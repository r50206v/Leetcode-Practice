# 1/1
# 266. Palindrome Permutation
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        N = len(s)
        countMap = collections.Counter(s)
        
        if N % 2:
            singleChar = False
            for k, v in countMap.items():
                if v % 2 != 0 and not singleChar:
                    singleChar = True
                elif v % 2 != 0:
                    return False
        else:
            for k, v in countMap.items():
                if v % 2 != 0:
                    return False
                
        return True