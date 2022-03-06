from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
			# Using sliding window, with a window length of the length of s1
            if Counter(s2[i: i+len(s1)]) == s1_counter: 
                return True
        return False