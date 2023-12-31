from typing import List, Sequence

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pl = 0
        pr = len(nums) - 1
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        while True:
            pc = (pl + pr) // 2
            if nums[pc] == target:
                return pc
            elif nums[pc] < target:
                pl = pc + 1
            else:
                pr = pc - 1
                if pr == -1:
                    return 0

            if pl == pr:

                if nums[pl] < target:
                    return pl + 1
                else:
                    return pl
                
if __name__ == '__main__':
    sol = Solution()
    x = [1, 3]
    print(sol.searchInsert(x, 2))
    