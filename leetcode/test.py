    def nextPermutation(self, nums):
        for i in range(len(nums)-1, 0, -1):
            # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                
                # get the index before the last peak
                j = i - 1
                
                # swap the pre-last peak index with the value just large than it
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()