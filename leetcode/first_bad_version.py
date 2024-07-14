def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
 
# Test cases
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(search(nums1, target1))  # Output: 4
 
target2 = 3
print(search(nums1, target2))  # Output: -1
 
nums3 = [1]
target3 = 0
print(search(nums3, target3))  # Output: -1