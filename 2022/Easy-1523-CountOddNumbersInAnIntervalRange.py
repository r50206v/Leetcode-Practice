class Solution:
    def countOdds(self, low: int, high: int) -> int:
        import math
        return math.ceil(high / 2) - (low // 2)