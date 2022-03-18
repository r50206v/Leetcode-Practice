'''
queue
time: O(N)
space: O(N)
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for idx in range(len(digits)-1, -1, -1):
            tmp = digits[idx] + carry
            carry = tmp // 10
            digits[idx] = tmp % 10
        
        if carry:
            digits.insert(0, carry)
        
        return digits