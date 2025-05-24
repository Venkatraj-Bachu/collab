class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        # top-down
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            #base cases
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]

        return dp(len(nums)-1)
        '''

        # bottom-up [or] tabulation

        dp = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return(dp[-1])