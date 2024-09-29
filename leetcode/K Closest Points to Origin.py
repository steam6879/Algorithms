from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for x, y in points:
            distance = x ** 2 + y ** 2

            heapq.heappush(heap, (distance, [x, y]))

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
