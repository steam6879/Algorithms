from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def findCombination(candidates: List, target: int):
            if not candidates:
                return ans
            
            target = target - candidates[-1]
            if target == 0:
                return ans
            else:
                for candidate in reversed(candidates):
                    