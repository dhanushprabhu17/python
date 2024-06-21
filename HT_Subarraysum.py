def subarray_sum(nums,target):
    sum_index = {0:-1}
    current_sum=0
    for i, num in enumerate(nums):
        current_sum+= num
        if current_sum-target in sum_index:
            return [sum_index[current_sum-target]+1,i]
        sum_index[current_sum]=i
    return []