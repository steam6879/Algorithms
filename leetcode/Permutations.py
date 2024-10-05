from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(picked, unpicked):
            if not unpicked:
                return ans.append(picked)

            for i, num in enumerate(unpicked):
                dfs(picked + [num], unpicked[:i] + unpicked[i + 1:])

        dfs([], nums)

        return ans
