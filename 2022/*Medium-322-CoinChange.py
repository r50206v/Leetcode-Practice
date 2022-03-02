'''
dynamic programming
time: O(S * N)
space: O(S)

S is the amount, n is denomination count
'''
class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            print('-'*20, coin, '-'*20)
            for x in range(coin, amount + 1):
                print(x, dp[x], x-coin, dp[x - coin])
                dp[x] = min(dp[x], dp[x - coin] + 1)
            print('\n')
        return dp[amount] if dp[amount] != float('inf') else -1 