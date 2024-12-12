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
                ans = max(ans, count)

            elif nums[i + 1] == nums[i]:
                continue

            else:
                ans = max(ans, count)
                count = 1

        return ans


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest