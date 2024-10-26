from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, nums = [], []

        def dfs(start, total):
            if total > target:
                return None

            elif total == target:
                ans.append(nums[:])

            else:
                for i in range(start, len(candidates)):
                    num = candidates[i]
                    nums.append(num)
                    dfs(i, total + num)
                    nums.pop()