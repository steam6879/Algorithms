from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for item in stones:
            heapq.heappush(heap, (-item, item))

        while len(heap) > 2:
            x, y = heapq.heappop(heap)[1], heapq.heappop(heap)[1]
            d = x - y
            heapq.heappush(heap, (-d, d))

        if len(heap) == 2:
            return heapq.heappop(heap)[1] - heapq.heappop(heap)[1]
        elif len(heap) == 1:
            return heapq.heappop(heap)[1]
        else:
            return 0