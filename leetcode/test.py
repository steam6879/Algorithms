def maxSubArray(nums):
    max_sum = nums[0]  # Initialize the maximum sum with the first element
    current_sum = nums[0]  # Initialize the current sum with the first element
    
    for num in nums[1:]:
        # Update the current sum by either adding the current element or starting a new subarray
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum