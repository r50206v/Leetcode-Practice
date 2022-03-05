'''
time: O(N)
space: O(1)
'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap +=1
        
        if swap == 2 or s1 == s2:
            if set(s1) == set(s2):
                return True
        
        return False