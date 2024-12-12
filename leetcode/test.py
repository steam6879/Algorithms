from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans, count = 1, 1
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                count += 1

            elif nums[i + 1] == nums[i]:
                continue

            else:
                ans = max(ans, count)
                count = 1

        return max(ans, count)
