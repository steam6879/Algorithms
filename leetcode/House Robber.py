class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


class Solution2:
    def rob(self, nums: list[int]) -> int:
        prev2, prev, curr = 0, 0, 0
        for num in nums:
            curr = max(prev, prev2 + num)
            prev2 = prev
            prev = curr
        return curr
