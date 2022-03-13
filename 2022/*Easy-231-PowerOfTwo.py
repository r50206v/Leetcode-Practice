'''
brute force
time: O(logN)
space: O(1)
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        
        while n>=2:
            if n%2 == 0:
                n = n/2
            else:
                return False
        return True



'''
bitwise operator
Get the Rightmost 1-bit, and compare the rightmost digit
time: O(1)
space: O(1)
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n