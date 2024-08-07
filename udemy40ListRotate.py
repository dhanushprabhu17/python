#Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.
def rotate(nums,k):
     k=k%len(nums)
     nums[:]=nums[-k:]+nums[:-k]
