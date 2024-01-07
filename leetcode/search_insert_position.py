from typing import List, Sequence

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        pl = 0
        pr = len(nums) - 1

        while pl <= pr:
            pc = (pl + pr) // 2
            if nums[pc] == target:
                return pc
            elif nums[pc] < target:
                pl = pc + 1
            else:
                pr = pc - 1

        return pl