from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counters = Counter(nums)

        for value in counters.values():
            if value >= 2:
                return True
            
        else:
            return False