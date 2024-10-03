from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        ans = []

        for i, value in enumerate(arr):
            diff = abs(x - value)
            heapq.heappush(heap, (diff, i))

        for _ in range(k):
            (diff, i) = heapq.heappop(heap)
            ans.append(arr[i])

        ans.sort()

        return ans


