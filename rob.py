class Solution:
    def rob(self, nums: List[int]) -> int:
        num_of_houses = len(nums) + 2
        dp = [-1] * num_of_houses
        dp[0] = 0
        dp[1] = 0

        for i in range(2, num_of_houses):
            dp[i] = max(nums[i - 2] + dp[i - 2], dp[i - 1])

        return dp[num_of_houses - 1]
