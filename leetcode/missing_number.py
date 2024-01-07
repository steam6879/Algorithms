class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expectedSum = (n * (n + 1)) // 2
        sum = 0
        for i in nums:
            sum += i
        
        return expectedSum - sum

        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if nums[i] != i:
        #         return i
        # else:
        #     return n