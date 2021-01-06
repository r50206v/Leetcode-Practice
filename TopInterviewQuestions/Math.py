# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


# Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        s = [1]*n
        s[0]=s[1]=0
        
        for i in range(2,int(n**0.5)+1):
            if s[i]:
                for j in range(i*i,n,i):
                    s[j] = 0
                    
        return sum(s)


# 326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 1 and abs(n) <= 2**31:
            divThree = 3**19
            if divThree % n == 0:
                return True
        return False


# 231. Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


# 342. Power of Four
# 4**x = n
# log4(n) = x = 1/2 * log2(n) is an integer
# so log2(n) % 2 should be 0
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log2(n) % 2 == 0