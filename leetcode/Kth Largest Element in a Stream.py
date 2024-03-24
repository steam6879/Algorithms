from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
if __name__ == "__main__":
    # heap = [4, 5, 8, 2]
    # heapq.heapify(heap)
    # print(heap[-3])
    # Create a KthLargest object with k=3 and initial elements [4, 5, 8, 2].
    obj = KthLargest(3, [4, 5, 8, 2])

    # Add new elements to the stream and find the kth largest element.
    print(obj.add(3))  # Output: 4
    print(obj.add(5))  # Output: 5
    print(obj.add(10)) # Output: 5
    print(obj.add(9))  # Output: 8
    print(obj.add(4))  # Output: 8



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)