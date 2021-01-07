# 3. Longest Substring Without Repeating Characters
'''
time: O(N * max(k))
k is the length of between two duplicate characters
space: O(N)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxLength = 0
        seen = []
        for index in range(len(s)):
            if s[index] in seen:
                s_index = seen.index(s[index])
                if s_index == len(seen) - 1:
                    seen = []
                else:
                    seen = seen[s_index + 1:]
            seen.append(s[index])
            maxLength = max(maxLength, len(seen))
        return maxLength


'''
time: O(2N) = O(N) in the worst case, every characters will be visited twice
space: O(N)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_len = 0, 0, 0
        S = set()
        
        while right < len(s):
            current_char = s[right]
            
            if current_char not in S:
                S.add(current_char)
                max_len = max(max_len, len(S))
                right += 1
                
            else:
                S.remove(s[left])
                left += 1

        return max_len