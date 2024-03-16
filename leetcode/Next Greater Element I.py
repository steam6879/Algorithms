from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            
            stack.append(nums2[i])

        for element in stack:
            mapping[element] = -1

        for num in nums1:
            result.append(mapping[num])
        
        return result


class Solution: #correct ver.
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)  # Initialize ans with -1
        
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums1[i]:  # Compare with nums1[i], not nums2[j]
                    ans[i] = nums2[k]
                    break
        return ans

class Solution: #initially incorrect ver.
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
    

    
if __name__ == '__main__':
    s = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(s.nextGreaterElement(nums1, nums2))