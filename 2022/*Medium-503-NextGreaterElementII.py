'''
backward looping + stack 
time: O(N)
space: O(N)
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        
        for _ in range(2):
            for i in range(len(nums)-1, -1, -1):
                
                if stack and stack[-1] > nums[i]:
                    result[i] = stack[-1]
                else:
                    while stack and stack[-1] <= nums[i]:
                        stack.pop(-1)
                    if stack:
                        result[i] = stack[-1]

                stack.append(nums[i])
            
        return result
    
        