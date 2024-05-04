from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)  # Handle cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    print(Solution.rotate(Solution, nums=[1, 2, 3, 4, 5, 6, 7], k=3))