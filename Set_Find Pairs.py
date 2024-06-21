def find_pairs(arr1,arr2,target):
    set1=set(arr1)
    pairs=[]
    for num in arr2:
        complement=target-num
        if complement in set1:
            pairs.append((complement,num))
    return pairs