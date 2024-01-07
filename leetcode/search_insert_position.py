from typing import List, Sequence

class Solution:

    def bin_search(self, a: Sequence, key: any):
        pl = 0
        pr = len(a) - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                return pc
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl == pr:
                if a[pl] < key:
                    return pl + 1
                else:
                    return pl - 1

    def searchInsert(self, nums: List[int], target: int) -> int:
        pl = 0
        pr = len(nums) - 1

        while True:
            pc = (pl + pr) // 2
            if nums[pc] == target:
                return pc
            elif nums[pc] < target:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl == pr:

                if nums[pl] < target:
                    return pl + 1
                else:
                    return pl - 1