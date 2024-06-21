def has_unique_chars(string):
    my_set=set()
    my_list=[]
    for i in string:
        if i in my_set:
            return False
        my_set.add(i)
    return True