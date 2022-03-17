class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        
        while i < len(pushed) and j < len(popped):
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop(-1)
                j += 1
            
            stack.append(pushed[i])
            i += 1
        
        if stack == popped[j:][::-1]:
            return True
        else:
            return False