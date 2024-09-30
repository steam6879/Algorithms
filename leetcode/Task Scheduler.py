from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap = Counter(tasks)
        maxCounts = max(countMap.values())
        idleSum = (maxCounts - 1) * n

        for count in countMap.values():
            idleSum -= min(maxCounts - 1, count)

        idleSum += maxCounts - 1

        return len(tasks) + max(0, idleSum)
