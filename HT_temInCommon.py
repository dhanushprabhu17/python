def item_in_common(list1,list2):
    dict1=[]
    for i in list1:
        dict1.append(i)
    for j in list2:
        if j in dict1:
            return True
    return False