class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)

        return maxSum

class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)

        for i,num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        
        return max(dp)