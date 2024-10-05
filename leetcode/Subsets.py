from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(start, visited):
            ans.append(visited)

            for i in range(start, len(nums)):
                dfs(i + 1, visited + [nums[i]])

        dfs(0, [])

        return ans


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ans += [[num] + item for item in ans]

        return ans
