from typing import Optional, List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums2[j]:
                    ans[i] = nums2[k]
                    break
            else:
                ans[i] = -1

        return ans