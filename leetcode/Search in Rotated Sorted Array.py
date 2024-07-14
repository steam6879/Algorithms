class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pl, pr = 0, len(nums) - 1

        while pl <= pr:
            pc = pl + (pr - pl) // 2

            if nums[pc] == target:
                return pc

            if nums[pl] <= nums[pc]:
                if nums[pl] <= target <= nums[pc]:
                    pr = pc - 1
                else:
                    pl = pc + 1

            else:
                if nums[pc] <= target <= nums[pr]:
                    pl = pc + 1
                else:
                    pr = pc - 1

        return -1
