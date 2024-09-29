from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for (x, y) in points:
            distance = -(x*x + y*y)

            if len(heap) == K:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))

        return [(x, y) for (distance, x, y) in heap]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for x, y in points:
            distanceance = x ** 2 + y ** 2

            heapq.heappush(heap, (distanceance, [x, y]))

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
