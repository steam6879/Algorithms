from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)  # Handle cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    nums = [1, 2]
    Solution().rotate(nums, k=3)
    print(nums)  # 출력: [2, 1]
