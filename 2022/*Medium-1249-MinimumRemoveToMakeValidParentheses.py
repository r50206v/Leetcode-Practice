'''
stack 
time: O(N)
space: O(N)
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for idx in range(len(s)):
            if s[idx] in "(":
                stack.append(idx)
            elif stack and s[stack[-1]] == "(" and s[idx] == ")":
                stack.pop(-1)
            elif s[idx] in ["(", ")"]:
                stack.append(idx)
        
        sList = list(s)
        for idx in stack[::-1]:
            sList.pop(idx)
        return "".join(sList)