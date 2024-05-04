from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        m = {}
        for num in prefixSum:
            if num in prefixSum:
                m[num] += 1

            else:
                m[num] = 1

        maxKey = max(m, key = m.get)
        index1 = nums.index(maxKey)
        index2 = nums.index(maxKey)