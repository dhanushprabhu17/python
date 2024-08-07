#Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum
def max_subarray(nums):
    if not nums:
        return 0
        
    max_sum=currrent_sum=nums[0]
    for num in nums[1:]:
        currrent_sum=max(num,currrent_sum+num)
        max_sum=max(max_sum,currrent_sum)
    return max_sum
