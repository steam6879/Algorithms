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

        dfs(0, 0)
        return ans


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return None

            for i in range(start, len(candidates)):
                current = candidates[i]
                if current > remaining:
                    break

                combo.append(current)
                backtrack(remaining - current, combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return result


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         ans = []

#         def findCombination(candidates: List, target: int):
#             if not candidates:
#                 return ans
            
#             target = target - candidates[-1]
#             if target == 0:
#                 ans.append([candidates[-1]])
#                 return ans
            
#             else:
#                 for i in reversed(range(len(candidates))):
#                     if target - candidates[i] >= 0:
#                         ans.append()
#                         return findCombination(candidates[:i + 1], target)