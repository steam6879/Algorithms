from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = heapq.heapify(score)
        m = {}
        if len(heap) == 1:
            m[heapq.heappop(heap)] = 'Gold Medal'
        elif len(heap) == 2:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
        elif len(heap) == 3:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
            m[heapq.heappop(heap)] = 'Bronze Medal'

        elif len(heap) > 3:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
            m[heapq.heappop(heap)] = 'Bronze Medal'

            for i in range(4, len(heap)):
                m[heapq.heappop(heap)] = i

        for i, key in len(score):
            
