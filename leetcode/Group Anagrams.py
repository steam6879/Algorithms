from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sCounters = [Counter(sCounter) for sCounter in strs]

        for str in strs:
            sCounters.append(Counter(str))

        