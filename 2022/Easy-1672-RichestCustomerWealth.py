class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = float("-inf")
        for l in accounts:
            ans = max(ans, sum(l))
        return ans