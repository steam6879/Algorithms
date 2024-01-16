from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        for key in m:
            if m[key] > n // 2:
                return key
            pass