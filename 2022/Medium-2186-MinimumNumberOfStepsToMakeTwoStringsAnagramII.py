'''
count all appearance and sum
time: O(N + M)
space: O(N + M)
'''
from collections import Counter
import string

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount, tCount = Counter(s), Counter(t)
        ans = 0
        for character in string.ascii_lowercase:
            ans += abs(sCount[character] - tCount[character])
        return ans