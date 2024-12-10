from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for [start, end] in intervals:
            if merged[-1][1] < start:   # case: 1
                merged.append([start, end])

            else:   #case: 2
                merged[-1][1] = max(merged[-1][1], end)

        return merged
