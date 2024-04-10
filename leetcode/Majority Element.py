from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        for key in m:
            if m[key] > len(nums) // 2:
                return key
        
        return None