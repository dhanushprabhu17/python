#This code defines a function called find_max_min, wh
# ich takes a single argument, myList. The function is designed to find the maximum and minimum values in the given list and return them as a tuple (maximum, minimum). Here's an explanation of the code
def find_max_min(mylist):
    max_val=min_val=mylist[0]
    for i in (mylist):
        if i>max_val:
            max_val=i
        if i<min_val:
            min_val=i
    return (max_val,min_val)