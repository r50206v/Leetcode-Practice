### Exponential Search
'''
Runtime: 32 ms
Memory Usage: 13.8 MB
'''
class Solution:
    def divide(self, dividend, divisor):
        #solution1- binary search
        ncount, flag, ans=0, 1, 0
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            flag = -1
            
        divisor, dividend = abs(divisor), abs(dividend)
        if divisor > dividend:return 0
        
        while dividend >= divisor:
            tmp = divisor
            ncount = 1
            while tmp <= dividend:
                dividend -= tmp
                ans += ncount
                tmp += tmp
                ncount += ncount

        if ans * flag < -2147483648: return -2147483648
        elif ans * flag > 2147483647: return 2147483647
        else: return ans * flag
        
        
### Exponential Search with list
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    doubles = []
    powersOfTwo = []

    # Nothing too exciting here, we're just making a list of doubles of 1 and
    # the divisor. This is pretty much the same as Approach 2, except we're
    # actually storing the values this time. */
    powerOfTwo = 1
    while divisor >= dividend:
        doubles.append(divisor)
        powersOfTwo.append(powerOfTwo)
        # Prevent needless overflows from occurring...
        if divisor < HALF_MIN_INT:
            break
        divisor += divisor # Double divisor
        powerOfTwo += powerOfTwo

    # Go from largest double to smallest, checking if the current double fits.
    # into the remainder of the dividend.
    quotient = 0
    for i in reversed(range(len(doubles))):
        if doubles[i] >= dividend:
            # If it does fit, add the current powerOfTwo to the quotient.
            quotient += powersOfTwo[i]
            # Update dividend to take into account the bit we've now removed.
            dividend -= doubles[i]

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return quotient if negatives != 1 else -quotient



### Bitwise Operator
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    # In the first loop, we simply find the largest double of divisor
    # that fits into the dividend.
    # The >= is because we're working in negatives. In essence, that
    # piece of code is checking that we're still nearer to 0 than we
    # are to INT_MIN.
    highest_double = divisor
    highest_power_of_two = -1
    while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
        highest_power_of_two += highest_power_of_two
        highest_double += highest_double

    # In the second loop, we work out which powers of two fit in, by
    # halving highest_double and highest_power_of_two repeatedly.
    # We can do this using bit shifting so that we don't break the
    # rules of the question :-)
    quotient = 0
    while dividend <= divisor:
        if dividend <= highest_double:
            quotient += highest_power_of_two
            dividend -= highest_double
        # We know that these are always even, so no need to worry about the
        # annoying "bit-shift-odd-negative-number" case.
        highest_power_of_two >>= 1
        highest_double >>= 1

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return quotient if negatives == 1 else -quotient