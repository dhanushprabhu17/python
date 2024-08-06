#Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.
#
#Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any additional data structures to solve this problem. The original list should be modified in-place
def remove_duplicates(nums):
    if not nums:
        return 0
    
    w_pointer=1
    for r_p in range(1,len(nums)):
        if nums[r_p]!=nums[r_p-1]:
            nums[w_pointer]=nums[r_p]
            w_pointer+=1
            
    return w_pointer