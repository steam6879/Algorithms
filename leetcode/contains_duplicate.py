from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = set()
        for i in nums:
            if i in m:
                return True
            else:
                m.add(i)
                       
        return False
    
if __name__ == '__main__':
    nums = [1,2,3,1]
    s = Solution()
    x = s.containsDuplicate(nums)

    print(x)