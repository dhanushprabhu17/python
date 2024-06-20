def first_non_repeating_char(string):
    dict1={}
    for i in string:
        dict1[i]=dict1.get(i,0)+1
    
    for i in string:
        if dict1[i]==1:
            return i
    return None