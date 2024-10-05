class Solution(object):
    def subsets2(self, nums):
        res = []
        nums.sort()

        for i in range(1 << len(nums)):
            tmp = []

            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])

            res.append(tmp)

        return res
