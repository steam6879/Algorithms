class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i] = False
            else:
                m[i] = True

        for key in m:
            if m[key] == True:
                return int(key)