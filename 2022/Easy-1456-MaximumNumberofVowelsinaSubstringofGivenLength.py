'''
sliding window
time: O(N)
space: O(1)
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        ans = num_vowels = sum(c in vowels for c in s[:k])

        for i in range(k, len(s)):
            num_vowels += (s[i] in vowels) - (s[i-k] in vowels)
            ans = max(ans, num_vowels)
        return ans