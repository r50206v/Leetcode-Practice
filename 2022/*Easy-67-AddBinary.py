'''
time: O(max(N, M))
space: O(max(N, M))
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        if len(a) < len(b):
            a, b = b, a
        
        carry = 0
        ans = [0] * len(a)
        for idx in range(len(a)):
            if idx < len(b):
                total = int(a[idx]) + int(b[idx]) + carry
                ans[idx] = total % 2
                carry = total // 2
            else:
                total = int(a[idx]) + carry
                ans[idx] = total % 2
                carry = total // 2
        
        ans = "".join([str(i) for i in ans[::-1]])
        if carry:
                ans = str(carry) + ans
        return ans