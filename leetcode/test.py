class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = x**2 + y**2 # sqrt does not matter for the size

            # use negative distance for max heap
            # adding new distance, and popping out the largest distance
            if len(heap) < k:
                heapq.heappush(heap, (-distance, x, y))
            else:
                heapq.heappushpop(heap, (-distance, x, y))

        return [[x, y] for _, x, y in heap]
            
            