def remove_duplicates(my_list):
    my_set=set(my_list)
    my_newlist=[]
    for i in my_set:
        my_newlist.append(i)
    return my_newlist