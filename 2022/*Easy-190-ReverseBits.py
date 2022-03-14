class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = bin(n)[:1:-1]
        if len(reverse) < 32:
            reverse += "0" * (32 - len(reverse))
        return int(reverse, base=2)
    
    
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret