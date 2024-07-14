class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pl, pr = 0, len(nums) - 1

        while pl <= pr:
            pc = (pl + pr) // 2
            if nums[pc] == target:
                return pc

            elif nums[pc] < target:
                pl = pc + 1

            else:
                pr = pc - 1

        return -1
