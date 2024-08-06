#Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list
def remove_element(nums,val):
    i=0
    while i<len(nums):
        if nums[i]==val:
            nums.pop(i)
        else:
            i+=1
    return len(nums)