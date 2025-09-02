class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            elif i == 0:
                return 0
            elif i <= 2:
                return 1
            memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]

        return dp(n)